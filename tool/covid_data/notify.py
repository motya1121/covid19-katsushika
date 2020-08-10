import datetime
import requests
import os
import json
import urllib


def notify(setting):
    setting_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "secret/slack.json")
    ichiran = setting.pdf_url
    syukei = setting.pdf_url.replace('itiran', 'jokyo')
    with open(setting_file) as f:
        setting_json = json.load(f)
        headers = {'Content-Type': 'application/json'}
        message = '感染者情報が更新されました．\n<{0}|葛飾区内の新型コロナウイルス感染者発生状況>\n<{1}|感染者一覧>\n<{2}|感染者属性別集計表>'.format(
            setting.city_url, ichiran, syukei)

        post_data = {'blocks': [{'type': 'section', 'text': {'type': 'mrkdwn', 'text': message}}]}
        req = urllib.request.Request(setting_json['slack_url'],
                                     data=json.dumps(post_data).encode('utf-8'),
                                     headers=headers,
                                     method='POST')
        urllib.request.urlopen(req)
