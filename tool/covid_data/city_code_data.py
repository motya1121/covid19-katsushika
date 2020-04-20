import csv
import sqlite3
from pykakasi import kakasi
import jaconv
import os


def init_city_code():
    '''
    都市コードをデータベースに格納する
    '''
    sql = 'CREATE TABLE city_codes( city_code TEXT PRIMARY KEY, city_name TEXT, ken TEXT, shi TEXT, ku TEXT, ken_kana TEXT, shi_kana TEXT, ku_kana TEXT);'
    execute_sql(sql)

    city_datas = []
    shi_names = []
    with open('./data/000618153.csv', 'r') as csvfile:
        city_datas = csv.DictReader(csvfile)
        for city_data in city_datas:
            t_city_code = "'" + city_data['city_code'] + "'"
            t_ken = "'" + city_data['ken'] + "'"
            t_shi = "'" + city_data['shi'] + "'" if city_data['shi'] != '' else "NULL"
            t_ku = "'" + city_data['ku'] + "'" if city_data['ku'] != '' else "NULL"
            t_ken_kana = "'" + city_data['ken_kana'] + "'" if city_data['ken_kana'] != '' else "NULL"
            t_shi_kana = "'" + city_data['shi_kana'] + "'" if city_data['shi_kana'] != '' else "NULL"
            t_ku_kana = "'" + city_data['ku_kana'] + "'" if city_data['ku_kana'] != '' else "NULL"
            shi_names.append(city_data['shi'])

            t_city_name = "'" + jp2roma(jaconv.h2z(city_data['ken_kana']))
            if t_shi != "NULL":
                t_city_name += "_" + jp2roma(jaconv.h2z(city_data['shi_kana']))
                if t_ku != "NULL":
                    t_city_name += "_" + jp2roma(jaconv.h2z(city_data['ku_kana']))
            t_city_name += "'"

            sql = "INSERT INTO city_codes VALUES"
            sql += "({t_city_code},{t_city_name},{t_ken},{t_shi},{t_ku},{t_ken_kana},{t_shi_kana},{t_ku_kana})".format(
                t_city_code=t_city_code,
                t_city_name=t_city_name,
                t_ken=t_ken,
                t_shi=t_shi,
                t_ku=t_ku,
                t_ken_kana=t_ken_kana,
                t_shi_kana=t_shi_kana,
                t_ku_kana=t_ku_kana)
            execute_sql(sql)
    '''
    区の情報を追加
    '''
    with open('./data/000618153_2.csv', 'r') as csvfile:
        city_datas = csv.DictReader(csvfile)
        for city_data in city_datas:
            if city_data['shiku'] in shi_names:
                t_shi = city_data['shiku']
                sql = "SELECT * FROM city_codes WHERE city_code = '{}'".format(city_data['city_code'])
                results = execute_sql(sql)
                for result in results:
                    t_ken = result[2]
                    t_ken_kana = result[5]
                    t_shi_kana = result[6]

                continue

            t_city_code = "'" + city_data['city_code'] + "'"
            t_ku = city_data['shiku'].replace(t_shi, '')
            t_ku_kana = jaconv.hira2hkata(city_data['shiku_kana']).replace(t_shi_kana, '')

            t_city_name = "'" + jp2roma(jaconv.h2z(t_ken_kana))
            if t_shi != "NULL":
                t_city_name += "_" + jp2roma(jaconv.h2z(t_shi_kana))
                if t_ku != "NULL":
                    t_city_name += "_" + jp2roma(jaconv.h2z(t_ku_kana))
            t_city_name += "'"

            sql = "INSERT INTO city_codes VALUES"
            sql += "({t_city_code},{t_city_name},{t_ken},{t_shi},{t_ku},{t_ken_kana},{t_shi_kana},{t_ku_kana})".format(
                t_city_code=t_city_code,
                t_city_name=t_city_name,
                t_ken="'" + t_ken + "'",
                t_shi="'" + t_shi + "'",
                t_ku="'" + t_ku + "'",
                t_ken_kana="'" + t_ken_kana + "'",
                t_shi_kana="'" + t_shi_kana + "'",
                t_ku_kana="'" + t_ku_kana + "'")
            execute_sql(sql)


def city_code():
    pass


def kenshiku():
    pass


def city_name():
    pass


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


def jp2roma(jp_str: str):
    Kakasi = kakasi()  # Generate kakasi instance
    Kakasi.setMode("H", "a")  # Hiragana to ascii
    Kakasi.setMode("K", "a")  # Katakana to ascii
    Kakasi.setMode("J", "a")  # Japanese(kanji) to ascii
    Kakasi.setMode("r", "Hepburn")  # Use Hepburn romanization

    conv = Kakasi.getConverter()
    result = conv.do(jp_str).replace("'", "")
    return (result)


if __name__ == "__main__":
    init_city_code()