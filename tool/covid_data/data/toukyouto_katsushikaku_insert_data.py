import csv
import random
import sqlite3
import datetime
import os


def make_string(strings: str = '1234567890abcdef', length: int = 8):
    print_string = ""
    for i in range(0, length):
        print_string += strings[random.randint(0, len(strings) - 1)]
    return print_string


def execute_sql(sql: str, ret_type: str = 'default'):
    conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '/../covid_data.db')
    if ret_type == 'dict':
        conn.row_factory = dict_factory
    c = conn.cursor()
    result = []
    try:
        c.execute(sql)
        if ret_type == 'dict':
            while True:
                res = c.fetchone()
                if res is None:
                    break
                else:
                    result.append(res)
        else:
            result = c.fetchall()
    except sqlite3.OperationalError as e:
        print(e)
    except sqlite3.IntegrityError as e:
        print(e)
    conn.commit()
    conn.close()

    return result


def dict_factory(self, cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


datas = []
with open('./data/tokyo_katsushika.csv', 'r') as data_f:
    reader = csv.DictReader(data_f)
    for row in reader:
        datas.append(dict(row))
        # print(dict(row))

for data in datas:
    print(data)
    t_id = make_string()
    t_No = int(data['No'])
    t_revealed_city_code = '131229'
    t_revealed_dt = datetime.datetime.strptime(data['陽性判明日'], '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')
    t_appearance_dt = "'" + datetime.datetime.strptime(
        data['発症日'], '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S') + "'" if data['発症日'] != '' else "'NULL'"
    if data['年代'] == '10歳未満':
        t_old = 0
    elif data['年代'] == '':
        t_old = 'NULL'
    else:
        t_old = int(data['年代'].replace('代', ''))
    t_sex = int(data['性別'])
    t_job = "'" + data['職業'] + "'" if data['職業'] != '' else 'NULL'
    t_travel_history = 'NULL'
    if data['入院調整中'] == '1':
        t_status_id = '1'
    elif data['入院'] == '1':
        t_status_id = '2'
    elif data['宿泊療養'] == '1':
        t_status_id = '3'
    elif data['自宅療養中'] == '1':
        t_status_id = '4'
    elif data['死亡'] == '1':
        t_status_id = '5'
    elif data['退院'] == '1':
        t_status_id = '6'
    sql = "INSERT INTO patients_131229 VALUES"
    sql += "('{id}',{No},'{revealed_city_code}','{revealed_dt}',{appearance_dt},NULL,{old},{sex},{job},{travel_history},'{status_id}')".format(
        id=t_id,
        No=t_No,
        revealed_city_code=t_revealed_city_code,
        revealed_dt=t_revealed_dt,
        appearance_dt=t_appearance_dt,
        old=t_old,
        sex=t_sex,
        job=t_job,
        travel_history=t_travel_history,
        status_id=t_status_id)
    print(sql)

    execute_sql(sql)
'''
| カラム名           | 型      | キー        | 概要                                                                             |
| ------------------ | ------- | ----------- | -------------------------------------------------------------------------------- |
| id                 | TEXT    | PRYMARY KEY | 患者のID(こっちで勝手に振ったもの)                                               |
| No                 | INTEGER | UNIQUE      | 患者ナンバー(区などが発表している値)                                             |
| revealed_city_code | TEXT    | NOT NULL    | 感染が確認されたところの全国地方公共団体コード(都道府県コード及び市区町村コード) |
| revealed_dt        | TEXT    |             | 判明した日時                                                                     |
| appearance_dt      | TEXT    |             | 発症した日時                                                                     |
| live_city_code     | TEXT    |             | 居住地の全国地方公共団体コード(都道府県コード及び市区町村コード)                 |
| old                | INTEGER |             | 年代(NULL: 不明, 0: 10歳未満, 10: 10代・・・)                                    |
| sex                | INTEGER |             | 性別(1:男性, 2:女性, NULL: 不明)                                                 |
| travel_history     | INTEGER |             | 渡航歴(0:なし, 1:あり, NULL:不明)                                                |
| status_id          | TEXT    |             | 患者の状態                                                                       |
'''