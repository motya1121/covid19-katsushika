import datetime
import requests


def notify(setting):
    if 'line' in setting.notify_token.keys():
        url = "https://notify-api.line.me/api/notify"
        access_token = setting.notify_token['line']
        headers = {'Authorization': 'Bearer ' + access_token}
        message = '({0})感染者情報が更新されました．\n{1}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), setting.city_url)
        payload = {'message': message}
        requests.post(
            url,
            headers=headers,
            params=payload,
        )
    if 'discord' in setting.notify_token.keys():
        pass
    if 'slack' in setting.notify_token.keys():
        pass
