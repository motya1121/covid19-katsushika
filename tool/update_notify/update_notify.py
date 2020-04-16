#!/usr/bin/env python3
# coding: utf-8

import os
import argparse
import json
import pprint
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re
import datetime
import requests


class update_notify():

    def __init__(self):
        self.web_data_file = os.path.dirname(os.path.abspath(__file__)) + "/web_data.json"
        self.web_data = self.init_web_data()
        self.setting_file = os.path.dirname(os.path.abspath(__file__)) + "/setting.json"
        self.setting = self.init_setting()
        self.dump_setting()

    def init_web_data(self):
        if os.path.isfile(self.web_data_file) is False:
            df = {}
        else:
            with open(self.web_data_file) as f:
                try:
                    df = json.load(f)
                    if 'survey_datetime' not in df.keys():
                        df['survey_datetime'] = '1970-01-01 00:00:00'
                    if 'update_datetime' not in df.keys():
                        df['update_datetime'] = '1970-01-01 00:00:00'
                except json.JSONDecodeError:
                    df = {}

        if df == {}:
            df = {"survey_datetime": '1970-01-01 00:00:00', "update_datetime": '1970-01-01 00:00:00'}

        return df

    def init_setting(self):
        if os.path.isfile(self.setting_file) is False:
            df = {}
        else:
            with open(self.setting_file) as f:
                try:
                    df = json.load(f)
                    if 'line_notify_token' not in df.keys():
                        line_notify_token = input("LINE notifyのTokenを入力>>")
                        df['line_notify_token'] = line_notify_token
                    if 'watch_url' not in df.keys():
                        watch_url = input("監視対象サイトのURLを入力>>")
                        df['watch_url'] = watch_url
                except json.JSONDecodeError:
                    df = {}

        if df == {}:
            line_notify_token = input("LINE notifyのTokenを入力>>")
            watch_url = input("監視対象サイトのURLを入力>>")
            df = {"line_notify_token": line_notify_token, "watch_url": watch_url}

        return df

    def dump_setting(self):
        with open(self.setting_file, "w") as f:
            json.dump(self.setting, f, indent=4)

    def dump_web_data(self):
        with open(self.web_data_file, "w") as f:
            json.dump(self.web_data, f, indent=4)

    def print_list(self):
        pprint.pprint(self.web_data, width=40)
        pass

    def watch(self):
        print("*INFO: 調査->{}".format(self.setting['watch_url']))

        # 更新の確認
        soup = BeautifulSoup(urllib.request.urlopen(self.setting['watch_url']), 'html.parser')
        printed_price = soup.find(text="区内の新型コロナウイルス感染者数")
        update_text = printed_price.next_element.next_element.text

        m = re.match(r'(\d+)月(\d+)日発表', update_text)
        if m is None:
            return -1

        get_update_datetime = datetime.datetime.strptime('2020-{0[0]}-{0[1]}'.format(m.groups()), '%Y-%m-%d')
        update_datetime = datetime.datetime.strptime(self.web_data['update_datetime'], '%Y-%m-%d %H:%M:%S')
        if update_datetime < get_update_datetime:
            self.alart_notify()
            self.web_data['update_datetime'] = get_update_datetime.strftime('%Y-%m-%d %H:%M:%S')

        self.web_data['survey_datetime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.dump_web_data()

    def alart_notify(self):
        url = "https://notify-api.line.me/api/notify"
        access_token = self.setting['line_notify_token']
        headers = {'Authorization': 'Bearer ' + access_token}
        message = '({})葛飾区の感染者情報が更新されました．'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        payload = {'message': message}
        requests.post(
            url,
            headers=headers,
            params=payload,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='更新確認を行う')
    parser.add_argument('-w', '--watch_price', action='store_true', help='監視')

    args = parser.parse_args()
    un = update_notify()

    if args.watch_price is True:
        un.watch()
