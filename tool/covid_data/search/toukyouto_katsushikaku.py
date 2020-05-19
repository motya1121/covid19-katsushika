import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import datetime
import re
from . import City
import json


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
        status_id = {'1': '入院調整中', '2': '入院中', '3': '宿泊療養中', '4': '自宅療養中', '5': '死亡', '6': '退院'}
        # 患者データを引っ張ってくる Noの順番
        sql = "SELECT * FROM patients_{} ORDER BY No".format(self.city_code)
        patients = self.execute_sql(sql, ret_type='dict')
        new_patients = []
        delete_patient_ids = []
        i = 1

        for patient in patients:
            '''
            if i == 1:
                new_patients.append(patient)
                sql = "UPDATE patients_131229 SET"
                sql += " No=NULL WHERE id = '{}'".format(patient['id'])
                self.execute_sql(sql)
                continue
            '''
            temp_patient = patient
            # データの確認(削除？->delete_listに追加, 挿入？->insert_patient())
            while True:
                print('\n[{0}] {1[old]}代{2}({1[job]}) 判明日:{3} 発症日:{4} 状態:{5}'.format(
                    i, patient, '男性' if patient['sex'] == 1 else '女性', patient['revealed_dt'][:-9],
                    patient['appearance_dt'][:-9], status_id[patient['status_id']]))
                result = input("削除[D], 挿入[I], 変更なし[Enter]>>")
                if result in ['D', '']:
                    break
                elif result == 'I':
                    new_patients.append(self.insert_patient())
                    i += 1
            if result == 'D':
                delete_patient_ids.append(patient['id'])
                continue
            elif result == '':
                pass

            # statusの確認
            while True:
                result = input("ステータスを変更, 入院調整中->1, 入院中->2, 宿泊療養中->3, 自宅療養中->4, 死亡->5, 退院->6, 変更なし->[Enter]>>")
                if result in ['1', '2', '3', '4', '5', '6', '']:
                    break
            if result in ['1', '2', '3', '4', '5', '6']:
                temp_patient['status_id'] = result

            # TODO: 病状の確認

            new_patients.append(temp_patient)
            # DB のNoを初期化
            sql = "UPDATE patients_131229 SET"
            sql += " No=NULL WHERE id = '{}'".format(temp_patient['id'])
            self.execute_sql(sql)
            i += 1

        # 新規登録
        while True:
            result = input("[{}]新規登録はありますが？[Y/n]]>>".format(i))
            if result in ['N', 'n']:
                break
            elif result in ['Y', 'y']:
                new_patients.append(self.insert_patient())
                i += 1

        # delete
        for patient_id in delete_patient_ids:
            sql = "DELETE FROM patients_{} WHERE id='{}'".format(self.city_code, patient_id)
            self.execute_sql(sql)

        # update number and status
        i = 1
        for new_patient in new_patients:
            sql = "UPDATE patients_131229 SET"
            sql += " No=?, status_id=? WHERE id = '{}'".format(new_patient['id'])
            # print(sql, i, new_patient['status_id'])
            self.execute_sql(sql, placeholder=(i, new_patient['status_id']))
            i += 1

    def insert_patient(self):
        while True:
            result = input("陽性判明日(YYYY-MM-DD)>>")
            try:
                revealed_dt = datetime.datetime.strptime(result, '%Y-%m-%d')
            except ValueError as e:
                print(e)
            else:
                break
        revealed_dt = revealed_dt.strftime('%Y-%m-%d %H:%M:%S')

        while True:
            result = input("年代(10歳未満は0, 不明は[Enter])>>")
            if result in ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100', '']:
                break
        old = result

        while True:
            result = input("性別(1:男性, 2:女性, NULL: 不明)>>")
            if result in ['1', '2', '']:
                break
        sex = result

        result = input("職業>>")
        job = result

        while True:
            result = input("発症日(YYYY-MM-DD)>>")
            try:
                appearance_dt = datetime.datetime.strptime(result, '%Y-%m-%d')
            except ValueError as e:
                print(e)
            else:
                break
        appearance_dt = appearance_dt.strftime('%Y-%m-%d %H:%M:%S')

        while True:
            result = input("ステータス, 入院調整中->1, 入院中->2, 宿泊療養中->3, 自宅療養中->4, 死亡->5, 退院->6>>")
            if result in ['1', '2', '3', '4', '5', '6', '']:
                break
        if result in ['1', '2', '3', '4', '5', '6']:
            status_id = result

        while True:
            print('\n{0}代{1}({2}) 判明日:{3} 発症日:{4} 状態:{5}'.format(old, '男性' if sex == 1 else '女性', job, revealed_dt,
                                                                 appearance_dt, status_id))
            result = input("このデータで合っていますか？[Y/n]>>")
            if result in ['Y', 'y,' 'N', 'n']:
                break
        if result in ['N', 'n']:
            input_data = self.insert_patient()
        else:
            input_data = []
            patients_id = self.make_id()
            sql = "INSERT INTO patients_{} VALUES(?, NULL, ?, ?, ?, NULL, ?, ?, ?, NULL, ?);".format(self.city_code)
            placeholder = (patients_id, self.city_code, revealed_dt, appearance_dt, old, sex, job, status_id)
            self.execute_sql(sql, placeholder=placeholder)
            sql = "SELECT * FROM patients_{} WHERE id='{}'".format(self.city_code, patients_id)
            result = self.execute_sql(sql, ret_type='dict')
            for r in result:
                input_data = r
        return input_data

    def print_list(self):
        status_id = {'1': '入院調整中', '2': '入院中　　', '3': '宿泊療養中', '4': '自宅療養中', '5': '死亡　　　', '6': '退院　　　'}
        sql = "SELECT * FROM patients_{} ORDER BY No".format(self.city_code)
        patients = self.execute_sql(sql, ret_type='dict')
        for patient in patients:
            print('[{0[No]}]\t 判明日:{2}\t 発症日:{3}\t 状態:{4}\t {0[old]}代{1}({0[job]})'.format(
                patient, '男性' if patient['sex'] == 1 else '女性', patient['revealed_dt'][:-9],
                patient['appearance_dt'][:-9], status_id[patient['status_id']]))

    def export_data(self):
        #updated_datetime = datetime.datetime.now()
        # TODO: 日付を変える
        updated_datetime = datetime.datetime.strptime('2020-05-19 23:59', '%Y-%m-%d %H:%M')
        sql = "SELECT * FROM patients_{} ORDER BY No".format(self.city_code)
        db_patients = self.execute_sql(sql, ret_type='dict')

        # patients
        patients = {'date': updated_datetime.strftime('%Y/%m/%d %H:%M'), 'data': []}
        status_id = {'1': '入院調整中', '2': '入院中', '3': '宿泊療養中', '4': '自宅療養中', '5': '死亡', '6': '退院'}

        for db_patient in db_patients:
            temp_patient = {
                'リリース日':
                    datetime.datetime.strptime(db_patient['revealed_dt'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d') +
                    'T08:00:00.000Z',
                '居住地':
                    '調査中',
                '年代':
                    str(db_patient['old']) + '代' if db_patient['old'] != 0 else '10歳未満',
                '性別':
                    '男性' if db_patient['sex'] == 1 else '女性',
                '退院':
                    '〇' if db_patient['status_id'] in ['5', '6'] else None,
                '状態':
                    status_id[db_patient['status_id']],
                'date':
                    datetime.datetime.strptime(db_patient['revealed_dt'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
            }
            patients['data'].append(temp_patient)

        # patients_by_age
        patients_by_age = {'date': updated_datetime.strftime('%Y/%m/%d %H:%M'), 'data': []}
        temp_patient = {}
        for db_patient in db_patients:
            if db_patient['old'] not in temp_patient.keys():
                temp_patient[db_patient['old']] = 1
            else:
                temp_patient[db_patient['old']] += 1

        age = 0
        while True:
            if max(temp_patient.keys()) < age:
                break
            if age not in temp_patient.keys():
                patients_by_age['data'].append({'age': str(age) + '代' if age != 0 else '10歳未満', 'number': 0})
            else:
                patients_by_age['data'].append({
                    'age': str(age) + '代' if age != 0 else '10歳未満',
                    'number': temp_patient[age]
                })
            age += 10

        # patients_summary

        temp_per_day = {}

        for db_patient in db_patients:
            temp_revealed_dt = datetime.datetime.strptime(db_patient['revealed_dt'],
                                                          '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
            if temp_revealed_dt not in temp_per_day.keys():
                temp_per_day[temp_revealed_dt] = 0
            temp_per_day[temp_revealed_dt] += 1

        patients_summary = {'date': updated_datetime.strftime('%Y/%m/%d %H:%M'), 'data': []}
        start_date = datetime.datetime.strptime('2020-02-16', '%Y-%m-%d')
        end_date = updated_datetime

        date = start_date
        while True:
            if end_date < date:
                break
            patients_summary['data'].append({
                '日付': date.strftime('%Y-%m-%d'),
                '小計': temp_per_day[date.strftime('%Y-%m-%d')] if date.strftime('%Y-%m-%d') in temp_per_day.keys() else 0
            })
            date += datetime.timedelta(days=1)

        # main_summary
        status_sumary = {'入院調整中': 0, '入院中': 0, '宿泊療養中': 0, '自宅療養中': 0, '死亡': 0, '退院': 0}

        for db_patient in db_patients:
            if db_patient['status_id'] == '1':
                status_sumary['入院調整中'] += 1
            if db_patient['status_id'] == '2':
                status_sumary['入院中'] += 1
            if db_patient['status_id'] == '3':
                status_sumary['宿泊療養中'] += 1
            if db_patient['status_id'] == '4':
                status_sumary['自宅療養中'] += 1
            if db_patient['status_id'] == '5':
                status_sumary['死亡'] += 1
            if db_patient['status_id'] == '6':
                status_sumary['退院'] += 1

        main_summary = {
            "attr":
                "検査実施人数",
            "value":
                0,
            'children': [{
                'attr':
                    '感染者数',
                'value':
                    len(db_patients),
                'children': [{
                    'attr': '入院調整中',
                    'value': status_sumary['入院調整中']
                }, {
                    'attr': '入院中',
                    'value': status_sumary['入院中']
                }, {
                    'attr': '宿泊療養中',
                    'value': status_sumary['宿泊療養中']
                }, {
                    'attr': '自宅療養中',
                    'value': status_sumary['自宅療養中']
                }, {
                    'attr': '死亡',
                    'value': status_sumary['死亡']
                }, {
                    'attr': '退院',
                    'value': status_sumary['退院']
                }]
            }]
        }
        export_data = {
            'lastUpdate': datetime.datetime.now().strftime('%Y/%m/%d %H:%M'),
            'patients': patients,
            'patients_summary': patients_summary,
            'patients_by_age': patients_by_age,
            'main_summary': main_summary
        }

        with open('../../data/data.json', 'w') as f:
            json.dump(export_data, f, indent=4, ensure_ascii=False)
