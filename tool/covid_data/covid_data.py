#!/usr/bin/env python3
# coding: utf-8

import search
import setting
import argparse
import shutil
import sqlite3
import city_code_data
import os


def add_city():
    city_code = input("都市のコード(参考: https://www.soumu.go.jp/main_content/000632830.pdf)>>")
    city_url = input("都市のデータのURL(空白可)>>")

    if city_code is None:
        print("都市コードを入力してください．")
        return -1
    city_url = "'" + city_url + "'" if city_url is not None else 'NULL'

    # 存在する都市か
    sql = "SELECT * FROM city_codes WHERE city_code='{}'".format(city_code)
    results = execute_sql(sql)
    count = 0
    for result in results:
        count += 1
        city_name_ja = result[2]
        city_name_ja += result[3] if result[3] is not None else ''
        city_name_ja += result[4] if result[4] is not None else ''
        city_name = result[1]

    # すでに登録されていないか
    sql = "SELECT * FROM city_setting WHERE city_code ='{}'".format(city_code)
    results = execute_sql(sql)
    count = 0
    for result in results:
        count += 1
    if count != 0:
        print("{0}はすでに登録されています．".format(city_name_ja))
        return 0

    # city_name.py
    shutil.copyfile("./search/city_template.py", "./search/" + city_name + ".py")
    with open("./search/" + city_name + ".py", "r", newline='') as city_py:
        rows = city_py.readlines()
    write_pg = []
    for row in rows:
        if row.find('temp_city_code') != -1:
            write_pg.append(row.replace('temp_city_code', city_code))
        elif row.find('temp_city_name') != -1:
            write_pg.append(row.replace('temp_city_name', city_name))
        else:
            write_pg.append(row)
    with open("./search/" + city_name + ".py", "w") as city_py:
        city_py.writelines(write_pg)

    # __init__.py
    with open("./search/__init__.py", "r", newline='') as init_py:
        rows = init_py.readlines()
    rows.append('from . import {}'.format(city_name))
    with open("./search/__init__.py", "w") as city_py:
        city_py.writelines(rows)

    sql = "INSERT INTO city_setting (city_code, city_url) VALUES('{}', {})".format(city_code, city_url)
    execute_sql(sql)
    sql = "CREATE TABLE patients_{}( id TEXT PRYMARY KEY, No INTEGER UNIQUE, revealed_city_code TEXT NOT NULL, revealed_dt TEXT, appearance_dt TEXT, live_city_code TEXT, old INTEGER, sex INTEGER, travel_history INTEGER, status_id TEXT);".format(
        city_code)
    execute_sql(sql)


def database_init():
    # make table
    sql = "CREATE TABLE city_setting( city_code TEXT PRIMARY KEY, city_url TEXT, survey_datetime TEXT DEFAULT '1970-01-01 00:00:00' , update_datetime TEXT DEFAULT '1970-01-01 00:00:00');"
    execute_sql(sql)
    sql = "CREATE TABLE patients_timetable(id TEXT PRYMARY KEY, status_id INTEGER, datetime TEXT NOT NULL);"
    execute_sql(sql)
    sql = "CREATE TABLE statuses( status_id INTEGER PRYMARY KEY, status TEXT UNIQUE);"
    execute_sql(sql)
    sql = "CREATE TABLE symptoms_map( id TEXT PRYMARY KEY, symptoms_id INTEGER, datetime TEXT NOT NULL);"
    execute_sql(sql)
    sql = "CREATE TABLE symptoms( symptoms_id TEXT PRYMARY KEY, symptoms TEXT UNIQUE);"
    execute_sql(sql)


def print_list():
    sql = "SELECT city_setting.city_code, ken, shi, ku FROM city_setting"
    sql += " INNER JOIN city_codes ON city_setting.city_code = city_codes.city_code"
    results = execute_sql(sql)
    for result in results:
        city_name_ja = result[1]
        city_name_ja += result[2] if result[2] is not None else ''
        city_name_ja += result[3] if result[3] is not None else ''
        print('{}: {}'.format(result[0], city_name_ja))


def execute_sql(sql: str):
    conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '/covid_data.db')
    c = conn.cursor()
    result = ""
    try:
        c.execute(sql)
        result = c.fetchall()
    except sqlite3.OperationalError as e:
        print(e)
    except sqlite3.IntegrityError as e:
        print(e)
    conn.commit()
    conn.close()

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='更新確認を行う')
    parser.add_argument('-w', '--watch_price', action='store_true', help='更新されているサイトの確認')
    parser.add_argument('-a', '--add_city', action='store_true', help='都市を追加')
    parser.add_argument('-di', '--database_init', action='store_true', help='データベースを初期化')
    parser.add_argument('-l', '--list', action='store_true', help='登録されている都市を表示')

    args = parser.parse_args()
    setting = setting.setting()

    if args.database_init is True:
        while True:
            result = input("本当に初期化しますか？[Y/n]>>")
            if result in ['Y', 'N', 'n']:
                break
        if result == 'Y':
            os.remove(setting.db_path)
            city_code_data.init_city_code()
            database_init()
    elif args.add_city is True:
        add_city()
    elif args.watch_price is True:
        tk = search.toukyouto_katsushikaku.toukyouto_katsushikaku(setting)
        tk.watch()
    elif args.list is True:
        print_list()
