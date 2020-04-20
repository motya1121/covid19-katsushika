import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import datetime
import re
from . import City


class toukyouto_katsushikaku(City.City):

    def __init__(self, setting):
        super().__init__(city_code='131229', setting=setting)

    def watch(self):
        print("*INFO: 調査->{}".format(self.city_url))

        # 更新の確認
        soup = BeautifulSoup(urllib.request.urlopen(self.city_url), 'html.parser')
        printed_price = soup.find(text="区内の新型コロナウイルス感染者数")
        update_text = printed_price.next_element.next_element.text

        m = re.match(r'(\d+)月(\d+)日発表', update_text)
        if m is None:
            return -1

        get_update_datetime = datetime.datetime.strptime('2020-{0[0]}-{0[1]}'.format(m.groups()), '%Y-%m-%d')
        update_datetime = datetime.datetime.strptime(self.update_datetime, '%Y-%m-%d %H:%M:%S')
        if update_datetime < get_update_datetime:
            self.alart_notify()
            update_datetime = get_update_datetime.strftime('%Y-%m-%d %H:%M:%S')
        survey_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        sql = "UPDATE city_setting SET update_datetime='{}', survey_datetime='{}' WHERE city_code='{}'".format(
            update_datetime, survey_datetime, self.city_code)
        self.execute_sql(sql)

    def update_data(self):
        pass
