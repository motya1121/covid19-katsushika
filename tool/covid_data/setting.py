import os
import json


class setting():
    json_template = {
        "notify_token": {
            "line": ""
        },
        "city_setting": {
            "city_url": "",
            "survey_datetime": "1970-01-01 00:00:00",
            "update_datetime": "1970-01-01 00:00:00",
            "public_datetime": "1970-01-01 00:00:00"
        }
    }
    error_flag = False

    def __init__(self):
        self.setting_file = os.path.dirname(os.path.abspath(__file__)) + "/setting.json"
        self.notify_token = {}
        self.city_url = ''
        self.pdf_base_url = ''
        self.survey_datetime = ''
        self.update_datetime = ''
        self.public_datetime = ''

        self.init_setting()
        if self.error_flag is False:
            self.get_setting()

    def init_setting(self):
        if os.path.isfile(self.setting_file) is False:  # 設定ファイルが存在しない場合
            self.setting_json = self.json_template
            self.dump_setting()
            print("設定ファイルが見つかりませんでした．")
            print('"{}"に設定内容を記述してください'.format(os.path.dirname(os.path.abspath(__file__)) + "/setting.json"))
            self.error_flag = True
        else:
            # ファイルの内容を確認
            with open(self.setting_file) as f:
                try:
                    self.setting_json = json.load(f)
                    # notify_tokenが設定されているかの確認
                    if 'notify_token' not in self.setting_json.keys():
                        print("設定ファイルの形式が異なっています．(notify_tokenが存在しません)")
                        print("現在の設定ファイルを削除し，もう一度このプログラムを実行すると，正常なテンプレートが作成されます．")
                        self.error_flag = True

                    # city_settingが設定されているかの確認
                    elif 'city_setting' not in self.setting_json.keys():
                        print("設定ファイルの形式が異なっています．(city_settingが存在しません)")
                        print("現在の設定ファイルを削除し，もう一度このプログラムを実行すると，正常なテンプレートが作成されます．")
                        self.error_flag = True

                    # city_setting内が設定されているかの確認
                    elif 'city_url' not in self.setting_json['city_setting'].keys():
                        print("設定ファイルの形式が異なっています．(city_setting内にcity_urlが存在しません)")
                        print("現在の設定ファイルを削除し，もう一度このプログラムを実行すると，正常なテンプレートが作成されます．")
                        self.error_flag = True
                    elif 'pdf_base_url' not in self.setting_json['city_setting'].keys():
                        print("設定ファイルの形式が異なっています．(city_setting内にpdf_base_urlが存在しません)")
                        print("現在の設定ファイルを削除し，もう一度このプログラムを実行すると，正常なテンプレートが作成されます．")
                        self.error_flag = True
                    elif 'survey_datetime' not in self.setting_json['city_setting'].keys():
                        print("設定ファイルの形式が異なっています．(city_setting内にsurvey_datetimeが存在しません)")
                        print("現在の設定ファイルを削除し，もう一度このプログラムを実行すると，正常なテンプレートが作成されます．")
                        self.error_flag = True
                    elif 'update_datetime' not in self.setting_json['city_setting'].keys():
                        print("設定ファイルの形式が異なっています．(city_setting内にupdate_datetimeが存在しません)")
                        print("現在の設定ファイルを削除し，もう一度このプログラムを実行すると，正常なテンプレートが作成されます．")
                        self.error_flag = True
                    elif 'public_datetime' not in self.setting_json['city_setting'].keys():
                        print("設定ファイルの形式が異なっています．(city_setting内にpublic_datetimeが存在しません)")
                        print("現在の設定ファイルを削除し，もう一度このプログラムを実行すると，正常なテンプレートが作成されます．")
                        self.error_flag = True
                except json.JSONDecodeError:
                    print('jsonファイルの形式が壊れています．')
                    print('正常なテンプレートに置き換えました．')
                    self.setting_json = self.json_template
                    self.error_flag = True

        if self.setting_json == {}:
            print('jsonファイル空です．')
            print('正常なテンプレートに置き換えました．')
            self.setting_json = self.json_template
            self.error_flag = True

        self.dump_setting()

    def get_setting(self):
        '''jsonのデータを配列に格納する
        '''
        # TODO: データの形式を確認
        self.city_url = self.setting_json['city_setting']['city_url']
        self.city_url = self.setting_json['city_setting']['pdf_base_url']
        self.notify_token = self.setting_json['notify_token']
        self.survey_datetime = self.setting_json['city_setting']['survey_datetime']
        self.update_datetime = self.setting_json['city_setting']['update_datetime']
        self.public_datetime = self.setting_json['city_setting']['public_datetime']

    def dump_setting(self):
        '''jsonファイルに書き出す．クラス内の変数に値が入っている場合はそちらを書き込む
        '''
        if self.survey_datetime != '':
            self.setting_json['city_setting']['survey_datetime'] = self.survey_datetime
        if self.update_datetime != '':
            self.setting_json['city_setting']['update_datetime'] = self.update_datetime
        if self.public_datetime != '':
            self.setting_json['city_setting']['public_datetime'] = self.public_datetime

        with open(self.setting_file, "w") as f:
            json.dump(self.setting_json, f, indent=4)

    def __str__(self):
        ret_string = ''
        ret_string += '- city_url:' + self.city_url + '\n'
        ret_string += '- pdf_base_url:' + self.pdf_base_url + '\n'
        ret_string += '- notify_token:' + json.dumps(self.notify_token) + '\n'
        ret_string += '- survey_datetime:' + self.survey_datetime + '\n'
        ret_string += '- update_datetime:' + self.update_datetime + '\n'
        ret_string += '- public_datetime:' + self.public_datetime + '\n'

        return ret_string
