import setting
import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import datetime
import re
from notify import notify
from get_covid_data import get_data
import os
import json


def check():
    '''区の情報が更新されているか確認する

    Returns
    -------
    str
        最新の感染者一覧のPDFのURL
    '''
    # 更新の確認
    soup = BeautifulSoup(urllib.request.urlopen(setting.city_url), 'html.parser')
    update_text = soup.find(text=re.compile("※令和"))

    #m = re.match(r'.*(\d+)月(\d+)日発表', update_text)
    m = re.match(r'.*(\d+)月(\d+)', update_text)
    if m is None:
        return -1

    get_update_datetime = datetime.datetime.strptime('2020-{0[0]}-{0[1]}'.format(m.groups()), '%Y-%m-%d')
    update_datetime = datetime.datetime.strptime(setting.update_datetime, '%Y-%m-%d %H:%M:%S')
    update_flag = False
    if update_datetime < get_update_datetime:
        setting.update_datetime = get_update_datetime.strftime('%Y-%m-%d %H:%M:%S')
        setting.public_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_flag = True
    setting.survey_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # PDFのURL取得
    setting.pdf_urls = []
    relative_pdf_links = soup.find(class_="objectlink").find_all('a')
    for link in relative_pdf_links:
        if link.get('href').find('itiran') != -1 or link.get('href').find('ituran') != -1 or link.get('href').find('a.pdf') != -1 or link.get('href').find('b.pdf') != -1:
            setting.pdf_urls.append(urllib.parse.urljoin(setting.city_url, link.get('href')))
        if link.get('href').find('zokusei') != -1 or link.get('href').find('zolusei') != -1:
            setting.pdf_joukyou_url = urllib.parse.urljoin(setting.city_url, link.get('href'))

    # 時刻のログを表示
    print('survey_datetime={}\nupdate_datetime={}\npublic_datetime={}\n'.format(setting.survey_datetime,
                                                                                setting.update_datetime,
                                                                                setting.public_datetime))

    setting.dump_setting()

    if update_flag is True:
        notify(setting)


def update():
    '''PDFから感染者の情報を取得し，利用可能なjsonを書き出す
    '''

    # odfの情報取得
    pdf_data = get_data(setting)

    # サイトで使う用のデータを書き出す
    export_data(pdf_data)

    # pdfの全データをjsonとして書き出し
    row_data = []
    for data in pdf_data:
        temp_data = data
        if temp_data['revealed_dt'] is None:
            temp_data['revealed_dt'] = ''
        else:
            temp_data['revealed_dt'] = temp_data['revealed_dt'].strftime('%Y-%m-%d')
        if temp_data['appearance_dt'] is None:
            temp_data['appearance_dt'] = ''
        else:
            temp_data['appearance_dt'] = temp_data['appearance_dt'].strftime('%Y-%m-%d')
        row_data.append(temp_data)
    with open(os.path.dirname(os.path.abspath(__file__)) + "/data/row_data.json", "w") as f:
        json.dump(row_data, f, indent=4, ensure_ascii=False)


def export_data(pdf_datas):
    set_up_dt = datetime.datetime.strptime(setting.update_datetime, '%Y-%m-%d %H:%M:%S')
    set_pub_dt = datetime.datetime.strptime(setting.public_datetime, '%Y-%m-%d %H:%M:%S')
    if set_up_dt < set_pub_dt:
        updated_datetime = datetime.datetime.strptime(setting.update_datetime[:-8] + '23:59:00', '%Y-%m-%d %H:%M:%S')
    else:
        updated_datetime = setting.public_datetime

    # patients
    patients = {'date': updated_datetime.strftime('%Y/%m/%d %H:%M'), 'data': []}
    status_id = {1: '入院調整中', 2: '入院中', 3: '宿泊療養中', 4: '自宅療養中', 6: '死亡', 5: '回復'}

    for pdf_data in pdf_datas:
        temp_patient = {
            'リリース日': pdf_data['revealed_dt'].strftime('%Y-%m-%d') + 'T08:00:00.000Z',
            '症状': pdf_data['symptom'],
            '年代': str(pdf_data['old']) + '代' if pdf_data['old'] != 0 else '10歳未満',
            '性別': '男性' if pdf_data['sex'] == 1 else '女性',
            '回復': '〇' if pdf_data['status_id'] in [5, 6] else None,
            '状態': status_id[pdf_data['status_id']],
            'date': pdf_data['revealed_dt'].strftime('%Y-%m-%d')
        }
        patients['data'].append(temp_patient)

    # patients_by_age
    patients_by_age = {'date': updated_datetime.strftime('%Y/%m/%d %H:%M'), 'data': []}
    temp_patient = {}
    for pdf_data in pdf_datas:
        if pdf_data['old'] not in temp_patient.keys():
            temp_patient[pdf_data['old']] = 1
        else:
            temp_patient[pdf_data['old']] += 1

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
    for pdf_data in pdf_datas:
        temp_revealed_dt = pdf_data['revealed_dt'].strftime('%Y-%m-%d')
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
    status_sumary = {'入院調整中': 0, '入院中': 0, '宿泊療養中': 0, '自宅療養中': 0, '死亡': 0, '回復': 0}
    for pdf_data in pdf_datas:
        if pdf_data['status_id'] == 1:
            status_sumary['入院調整中'] += 1
        if pdf_data['status_id'] == 2:
            status_sumary['入院中'] += 1
        if pdf_data['status_id'] == 3:
            status_sumary['宿泊療養中'] += 1
        if pdf_data['status_id'] == 4:
            status_sumary['自宅療養中'] += 1
        if pdf_data['status_id'] == 6:
            status_sumary['死亡'] += 1
        if pdf_data['status_id'] == 5:
            status_sumary['回復'] += 1

    main_summary = {
        "attr":
            "検査実施人数",
        "value":
            0,
        'children': [{
            'attr':
                '感染者数',
            'value':
                len(pdf_datas),
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
                'attr': '回復',
                'value': status_sumary['回復']
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

    with open(os.path.dirname(os.path.abspath(__file__)) + '/../../data/data.json', 'w') as f:
        json.dump(export_data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    setting = setting.setting()
    update_flag = False
    flesh = True
    check()
    if update_flag is True or flesh is True:
        update()
