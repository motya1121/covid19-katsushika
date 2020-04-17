#!/usr/bin/env python3

import csv
import datetime
import json

# 手動で日時を設定
updated_datetime = datetime.datetime.strptime('2020-04-17', '%Y-%m-%d')
# 現在の時刻を採用
# updated_datetime = datetime.datetime.now()

header = []
row_datas = []
with open('../data/row_data.csv', 'r') as row_data_f:
    reader = csv.reader(row_data_f)
    i = 0
    for row in reader:
        if i == 0:
            header = row
        else:
            temp_data = {
                'No': row[0],
                'revealed_date': datetime.datetime.strptime(row[1], '%Y-%m-%d') if row[1] != '' else None,
                'appearance_date': datetime.datetime.strptime(row[5], '%Y-%m-%d') if row[5] != '' else None,
                'age': row[2],
                'sex': '男性' if row[3] is '1' else '女性' if row[3] is '2' else '不明',
                'job': row[4],
                'status': {
                    '入院調整中': True if row[6] == '1' else False,
                    '入院中': True if row[7] == '1' else False,
                    '自宅療養中': True if row[8] == '1' else False,
                    '死亡': True if row[9] == '1' else False,
                    '退院': True if row[10] == '1' else False
                },
                'symptoms': {
                    '発熱': True if row[11] == '1' else False,
                    '咳': True if row[12] == '1' else False,
                    '咽頭痛': True if row[13] == '1' else False,
                    '味覚障害': True if row[14] == '1' else False,
                    '嗅覚障害': True if row[15] == '1' else False,
                    '倦怠感': True if row[16] == '1' else False,
                    '下痢': True if row[17] == '1' else False,
                    '頭痛': True if row[18] == '1' else False,
                    '鼻汁': True if row[19] == '1' else False,
                    '関節痛': True if row[20] == '1' else False,
                    '鼻閉': True if row[21] == '1' else False,
                    '痰': True if row[22] == '1' else False
                }
            }
            row_datas.append(temp_data)
        i += 1

# patients
'''
リリース日				String			"2020-01-24T08:00:00.000Z"	表中の「公表日」の列に対応．
居住地					String			"湖北省武漢市"	表中の「居住地」の列に対応．値が存在しない場合は「調査中」と表示．
年代					String			"40代"	表中の「年代」の列に対応．値が存在しない場合は「不明」と表示．値は component 内で変換して表示．
性別					String			"男性"	表中の「性別」の列に対応．値が存在しない場合は「不明」と表示．値が存在する場合は「男性」または「女性」と表示．
退院					String | null			"〇"	表中の「公表日」の列に対応．値は「○」または null．
date					String			"2020-01-24"	不使用
'''
patients = {'date': updated_datetime.strftime('%Y/%m/%d %H:%M'), 'data': []}

for row_data in row_datas:
    temp_patient = {
        'リリース日': row_data['revealed_date'].strftime('%Y-%m-%d') + 'T08:00:00.000Z',
        '居住地': '調査中',
        '年代': row_data['age'],
        '性別': row_data['sex'],
        '退院': '〇' if row_data['status']['退院'] is True else None,
        'date': row_data['revealed_date'].strftime('%Y-%m-%d')
    }
    patients['data'].append(temp_patient)


# patients_summary
'''
date					String				"2020/04/12 20:15"
data					Array <Object>
	日付					String			"2020-01-24T08:00:00.000Z"
	小計					Integer			1
'''

temp_per_day = {}
for row_data in row_datas:
    if row_data['revealed_date'] not in temp_per_day.keys():
        temp_per_day[row_data['revealed_date']] = 0
    temp_per_day[row_data['revealed_date']] += 1

patients_summary = {'date': updated_datetime.strftime('%Y/%m/%d %H:%M'), 'data': []}
start_date = datetime.datetime.strptime('2020-02-16', '%Y-%m-%d')
end_date = updated_datetime

date = start_date
while True:
    if end_date < date:
        break
    patients_summary['data'].append(
        {
            '日付': date.strftime('%Y-%m-%d') + 'T08:00:00.000Z',
            '小計': temp_per_day[date] if date in temp_per_day.keys() else 0
        }
    )
    date += datetime.timedelta(days=1)

# main_summary

status_sumary = {'入院調整中': 0, '入院中': 0, '自宅療養中': 0, '死亡': 0, '退院': 0}
for row_data in row_datas:
    if row_data['status']['入院調整中'] is True:
        status_sumary['入院調整中'] += 1
    if row_data['status']['入院中'] is True:
        status_sumary['入院中'] += 1
    if row_data['status']['自宅療養中'] is True:
        status_sumary['自宅療養中'] += 1
    if row_data['status']['死亡'] is True:
        status_sumary['死亡'] += 1
    if row_data['status']['退院'] is True:
        status_sumary['退院'] += 1

main_summary = {
    "attr": "検査実施人数",
    "value": 0,
    'children': [{
        'attr': '感染者数',
        'value': len(row_datas),
        'children': [{
            'attr': '入院調整中',
            'value': status_sumary['入院調整中']
        }, {
            'attr': '入院中',
            'value': status_sumary['入院中']
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
    'lastUpdate': updated_datetime.strftime('%Y/%m/%d %H:%M'),
    'patients': patients,
    'patients_summary': patients_summary,
    'main_summary': main_summary
}
with open('../data/data.json', 'w') as f:
    json.dump(export_data, f, indent=4, ensure_ascii=False)