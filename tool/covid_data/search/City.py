import datetime
import requests
import sqlite3
import os
import random


class City(object):

    def __init__(self, city_code, setting):
        self.city_code = city_code
        self.setting = setting

        sql = "SELECT city_name FROM city_codes WHERE city_code='{}'".format(self.city_code)
        results = self.execute_sql(sql)
        for result in results:
            self.city_name = result[0]

        sql = "SELECT * FROM city_setting WHERE city_code='{}'".format(self.city_code)
        results = self.execute_sql(sql)
        for result in results:
            self.city_url = result[1]
            self.survey_datetime = result[2]
            self.update_datetime = result[3]

    def alart_notify(self):
        if 'line' in self.setting.notify_token.keys():
            url = "https://notify-api.line.me/api/notify"
            access_token = self.setting.notify_token['line']
            headers = {'Authorization': 'Bearer ' + access_token}
            message = '({0}){1}の感染者情報が更新されました．'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                       self.city_name)
            payload = {'message': message}
            requests.post(
                url,
                headers=headers,
                params=payload,
            )
        if 'discord' in self.setting.notify_token.keys():
            pass
        if 'slack' in self.setting.notify_token.keys():
            pass

    def execute_sql(self, sql: str, ret_type: str = 'default', placeholder: tuple = ()):
        conn = sqlite3.connect(self.setting.db_path)
        if ret_type == 'dict':
            conn.row_factory = self.dict_factory
        c = conn.cursor()
        result = []
        try:
            c.execute(sql, placeholder)
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

    def make_id(self, strings: str = '1234567890abcdef', length: int = 8):
        print_string = ""
        for i in range(0, length):
            print_string += strings[random.randint(0, len(strings) - 1)]
        return print_string
