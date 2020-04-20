import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import datetime
import re
from . import City


class temp_city_name(City.City):

    def __init__(self, setting):
        super().__init__(city_code='temp_city_code', setting=setting)

    def watch(self):
        print("*INFO: 調査->{}".format(self.city_url))
        '''
        更新を確認するためのコード
        '''

    def update_data(self):
        pass
