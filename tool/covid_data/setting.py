import os
import json


class setting():

    def __init__(self):
        self.setting_file = os.path.dirname(os.path.abspath(__file__)) + "/setting.json"
        self.init_setting()
        self.notify_token = self.setting_json['notify_token']
        self.db_path = os.path.dirname(os.path.abspath(__file__)) + '/covid_data.db'

    def init_setting(self):
        if os.path.isfile(self.setting_file) is False:
            self.setting_json = {}
        else:
            with open(self.setting_file) as f:
                try:
                    self.setting_json = json.load(f)
                    if 'notify_token' not in self.setting_json.keys():
                        line_notify_token = input("LINE notifyのTokenを入力(使わない場合そのままEnter)>>")
                        self.setting_json['notify_token']['line'] = line_notify_token
                        '''
                        discord_notify_token = input("Discord notifyのTokenを入力(使わない場合そのままEnter)>>")
                        self.setting_json['notify_token']['discord'] = discord_notify_token
                        slack_notify_token = input("Slack notifyのTokenを入力(使わない場合そのままEnter)>>")
                        self.setting_json['notify_token']['slack'] = slack_notify_token
                        '''
                except json.JSONDecodeError:
                    self.setting_json = {}

        if self.setting_json == {}:
            line_notify_token = input("LINE notifyのTokenを入力(使わない場合そのままEnter)>>")
            '''
            discord_notify_token = input("Discord notifyのTokenを入力(使わない場合そのままEnter)>>")
            slack_notify_token = input("Slack notifyのTokenを入力(使わない場合そのままEnter)>>")
            '''

        self.dump_setting()

    def dump_setting(self):
        with open(self.setting_file, "w") as f:
            json.dump(self.setting_json, f, indent=4)

    def __str__(self):
        return json.dumps(self.setting_json, indent=2)