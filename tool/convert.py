#!/usr/bin/env python3

import csv
import datetime


header = []
data = []
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
                'sex': row[3],
                'job': row[4],
                'status': {
                    '入院調整中': True if row[6] == '1' else False,
                    '入院': True if row[7] == '1' else False,
                    '自宅療養中': True if row[8] == '1' else False,
                    '退院': True if row[9] == '1' else False
                },
                'symptoms': {
                    '発熱': True if row[10] == '1' else False,
                    '咳': True if row[11] == '1' else False,
                    '咽頭痛': True if row[12] == '1' else False,
                    '味覚障害': True if row[13] == '1' else False,
                    '嗅覚障害': True if row[14] == '1' else False,
                    '倦怠感': True if row[15] == '1' else False,
                    '下痢': True if row[16] == '1' else False,
                    '頭痛': True if row[17] == '1' else False,
                    '鼻汁': True if row[18] == '1' else False,
                    '関節痛': True if row[19] == '1' else False,
                    '鼻閉': True if row[20] == '1' else False,
                    '痰': True if row[21] == '1' else False
                }
            }
            data.append(temp_data)
        i += 1
