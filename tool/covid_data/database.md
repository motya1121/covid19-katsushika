# database

## city_setting Table

情報が発表されている都市のリスト
ここに記載がある場合はテーブルが存在していることになる

| カラム名        | 型   | キー                          | 概要                                                                             |
| --------------- | ---- | ----------------------------- | -------------------------------------------------------------------------------- |
| city_code       | TEXT | PRIMARY KEY                   | 感染が確認されたところの全国地方公共団体コード(都道府県コード及び市区町村コード) |
| city_url        | TEXT |                               | URL                                                                              |
| survey_datetime | TEXT | DEFAULT '1970-01-01 00:00:00' | 直近で操作した時刻                                                               |
| update_datetime | TEXT | DEFAULT '1970-01-01 00:00:00' | 最終更新日時                                                                     |


```
CREATE TABLE city_setting(
    city_code TEXT PRIMARY KEY,
    city_url TEXT,
    survey_datetime TEXT DEFAULT '1970-01-01 00:00:00' ,
    update_datetime TEXT DEFAULT '1970-01-01 00:00:00'
);
```


## patients-<city_code> Table template

患者テーブル

| カラム名           | 型      | キー        | 概要                                                                             |
| ------------------ | ------- | ----------- | -------------------------------------------------------------------------------- |
| id                 | TEXT    | PRYMARY KEY | 患者のID(こっちで勝手に振ったもの)                                               |
| No                 | INTEGER | UNIQUE      | 患者ナンバー(区などが発表している値)                                             |
| revealed_city_code | TEXT    | NOT NULL    | 感染が確認されたところの全国地方公共団体コード(都道府県コード及び市区町村コード) |
| revealed_dt        | TEXT    |             | 判明した日時                                                                     |
| appearance_dt      | TEXT    |             | 発症した日時                                                                     |
| live_city_code     | TEXT    |             | 居住地の全国地方公共団体コード(都道府県コード及び市区町村コード)                 |
| old                | INTEGER |             | 年代(NULL: 不明, 0: 10歳未満, 10: 10代・・・)                                    |
| sex                | INTEGER |             | 性別(1:男性, 2:女性, NULL: 不明)                                                 |
| job                | TEXT    |             |                                                                                  |
| travel_history     | INTEGER |             | 渡航歴(0:なし, 1:あり, NULL:不明)                                                |
| status_id          | TEXT    |             | 患者の状態                                                                       |


[全国地方公共団体コード(都道府県コード及び市区町村コード)](https://www.soumu.go.jp/denshijiti/code.html)


```
CREATE TABLE patients-<city_code>(
    id TEXT PRYMARY KEY,
    No INTEGER UNIQUE,
    revealed_city_code TEXT NOT NULL,
    revealed_dt TEXT,
    appearance_dt TEXT,
    live_city_code TEXT,
    old INTEGER,
    sex INTEGER,
    job TEXT,
    travel_history INTEGER,
    status_id TEXT
);
```

## patients_timetable Table

患者のstatusの移り変わり


| カラム名  | 型      | キー        | 概要                               |
| --------- | ------- | ----------- | ---------------------------------- |
| id        | TEXT    | PRYMARY KEY | 患者のID(こっちで勝手に振ったもの) |
| status_id | INTEGER |             | 患者の状態                         |
| datetime  | TEXT    | NOT NULL    | 登録した時間                       |



```
CREATE TABLE patients_timetable(
    id TEXT PRYMARY KEY,
    status_id INTEGER,
    datetime TEXT NOT NULL
);
```

## statuses Table

入院状況に関するテーブル

| カラム名  | 型   | キー        | 概要         |
| --------- | ---- | ----------- | ------------ |
| status_id | TEXT | PRYMARY KEY | 患者の状態ID |
| status    | TEXT | UNIQUE      | 患者の状態   |

1. 入院調整中
2. 入院中
3. 宿泊療養
4. 自宅療養中
5. 死亡
6. 退院

```
CREATE TABLE statuses(
    status_id INTEGER PRYMARY KEY,
    status TEXT UNIQUE
);
```

```
INSERT INTO statuses VALUES ('1', '入院調整中'), ('2', '入院中'), ('3', '宿泊療養'), ('4', '自宅療養中'), ('5', '退院'), ('6', '死亡');
```

## symptoms_map Table

患者の病状
症状が改善した場合でも消さずに残しておく


| カラム名    | 型      | キー        | 概要                               |
| ----------- | ------- | ----------- | ---------------------------------- |
| id          | TEXT    | PRYMARY KEY | 患者のID(こっちで勝手に振ったもの) |
| symptoms_id | INTEGER |             | 患者の病状                         |
| datetime    | TEXT    | NOT NULL    | 登録した時間                       |

```
CREATE TABLE symptoms_map(
    id TEXT PRYMARY KEY,
    symptoms_id INTEGER,
    datetime TEXT NOT NULL
);
```

## symptoms Table

患者の病状

| カラム名    | 型   | キー        | 概要   |
| ----------- | ---- | ----------- | ------ |
| symptoms_id | TEXT | PRYMARY KEY | 病状ID |
| symptoms    | TEXT | UNIQUE      | 病状   |

```
CREATE TABLE symptoms(
    symptoms_id TEXT PRYMARY KEY,
    symptoms TEXT UNIQUE
);
```

```
INSERT INTO symptoms VALUES ('3a335cbf', '発熱'), ('50608b3c', '咳'), ('ad25dbf5', '咽頭痛'), ('ba37a6a6', '味覚障害'), ('d85230a0', '嗅覚障害'), ('2c062671', '倦怠感'), ('8fbd4b35', '下痢'), ('bcccd4be', '頭痛'), ('5a3888d5', '鼻汁'), ('9c47dac3', '関節痛'), ('a1a05b1f', '鼻閉'), ('d9a6c0a1', '痰'), ('3a61a964', '肺炎'), ('a5d30b3f', '呼吸困難');
```


## city_codes Table

| カラム名  | 型   | キー        | 概要           |
| --------- | ---- | ----------- | -------------- |
| city_code | TEXT | PRIMARY KEY | 都市コード     |
| city_name | TEXT |             | 都市の名前     |
| ken       | TEXT |             | 県             |
| shi       | TEXT |             | 市(特別区含む) |
| ku        | TEXT |             | 区             |
| ken_kana  | TEXT |             | 県（振り仮名)  |
| shi_kana  | TEXT |             | 市（振り仮名)  |
| ku_kana   | TEXT |             | 区（振り仮名)  |


```
CREATE TABLE city_codes(
    city_code TEXT PRIMARY KEY,
    city_name TEXT,
    ken TEXT,
    shi TEXT,
    ku TEXT,
    ken_kana TEXT,
    shi_kana TEXT,
    ku_kana TEXT
);
```