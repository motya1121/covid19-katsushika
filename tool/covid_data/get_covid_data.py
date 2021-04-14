from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
import urllib.request
from datetime import datetime as dt
import json
import os
import shutil


class patient_data():

    def __init__(self, box_list=''):
        self.no = ''
        self.revealed_dt = ''
        self.old = ''
        self.sex = ''
        self.job = ''
        self.symptom = ''
        self.appearance_dt = ''
        self.status_id = ''
        self.box_list = box_list
        self.is_error = False

    def parse_line(self):
        line_str = ''
        for box in self.box_list:
            line_str += '{}:'.format(self.cid_to_jp(box.get_text()).replace('\n', '').replace(' ', ':'))

        # check remain cid
        if line_str.find('cid') != -1:
            print(line_str)
            exit()

        line_list = line_str.split(':')
        # 例外処理
        if line_list[0] == '3842':
            line_list = ['3842', '2/12', '７０代', '男', '無職', '咳以外の呼吸器症状', '2/12', '○', '']
        self.no = line_list[0]
        self.revealed_dt = self.check_date(line_list[1])
        self.old = self.check_old(line_list[2])
        self.sex = self.check_sex(line_list[3])
        self.job = self.parse_job(line_list[4], line_str)
        self.symptom = self.parse_symptom(line_str)
        self.appearance_dt = self.parse_appearance_dt(line_list[6], line_str)
        self.status_id = self.get_status_id(self.box_list[-1].x0)
        if self.status_id == 0:
            print(line_list[0], self.box_list[-1].x0, self.status_id)

    def cid_to_jp(self, text: str) -> str:
        with open(os.path.dirname(os.path.abspath(__file__)) + "/cid_jp_map.json", "r") as f:
            cid_jp_map = json.load(f)

        ret_str = text
        if ret_str.find('cid') != -1:
            for cid, jp in cid_jp_map.items():
                ret_str = ret_str.replace(f'(cid:{cid})', jp)

        return ret_str

    def check_date(self, text) -> dt:
        if text.find('－') != -1 or text.find('ー') != -1 or text.find('-') != -1:
            return ''

        text = text.replace('月', '/')
        text = text.replace('日', '')

        if text.find('11/') != -1 or text.find('12/') != -1:
            year = '2020'
        else:
            year = '2021'

        try:
            ret_dt = dt.strptime(f'{year}/{text}', '%Y/%m/%d')
        except ValueError:
            print(f'no:{self.no}, text:{text}')
            exit()
        return ret_dt

    def check_old(self, text) -> int:
        # oldではない場合
        if text.find('代') == -1 and text.find('未満') == -1 and text.find('以上') == -1:
            return ''

        # oldの場合
        if text.find('未満') != -1:
            return 0
        if text.find('１０') != -1:
            return 10
        elif text.find('２０') != -1:
            return 20
        elif text.find('３０') != -1:
            return 30
        elif text.find('４０') != -1:
            return 40
        elif text.find('５０') != -1:
            return 50
        elif text.find('６０') != -1:
            return 60
        elif text.find('７０') != -1 or text.find('70') != -1:
            return 70
        elif text.find('８０') != -1:
            return 80
        elif text.find('９０') != -1:
            return 90
        return 100

    def check_sex(self, text):
        if text.find('男') != -1:
            return 1
        elif text.find('女') != -1:
            return 2
        else:
            return ''

    def parse_job(self, line_list_4, line_str):
        # －の場合の処理
        if line_list_4.find('－') != -1 or line_list_4.find('ー') != -1 or line_list_4.find('-') != -1:
            return '－'
        if line_str.find('無職') != -1:
            return '無職'
        elif line_str.find('会社員') != -1:
            return '会社員'
        elif line_str.find('学生') != -1:
            return '学生'
        elif line_str.find('生徒') != -1:
            return '生徒'
        elif line_str.find('自営業') != -1:
            return '自営業'
        elif line_str.find('医療従事者') != -1:
            return '医療従事者'
        elif line_str.find('公務員') != -1:
            return '公務員'
        elif line_str.find('調査中') != -1:
            return '調査中'
        else:
            return ''

    def parse_symptom(self, line_str):
        symptom_start_index = line_str.find(self.job) + len(self.job)
        if line_str[symptom_start_index] == ':':
            symptom_start_index += 1
        for i in range(symptom_start_index, len(line_str)):
            if line_str[i].isdecimal() is True or line_str[i].find('－') != -1 or line_str[i].find(
                    'ー') != -1 or line_str[i].find('-') != -1:
                break
        if line_str[i - 1] == ':':
            symptom_end_index = i - 1
        else:
            symptom_end_index = i
        return line_str[symptom_start_index:symptom_end_index]

    def parse_appearance_dt(self, line_list_6, line_str):
        # 綺麗な形の場合
        ret_str = ''
        try:
            if line_list_6.find('－') != -1 or line_list_6.find('ー') != -1 or line_list_6.find(
                    '-') != -1 or line_list_6.find('―') != -1:
                ret_str = None
            elif line_list_6 == '1/0':
                ret_str = None
            else:
                if line_list_6.find('11/') != -1 or line_list_6.find('12/') != -1:
                    year = '2020'
                else:
                    year = '2021'
                ret_str = dt.strptime(f'{year}/{line_list_6}', '%Y/%m/%d')
        except ValueError:
            # 症状の頭出し
            symptom_start_index = line_str.find(self.job) + len(self.job)
            if line_str[symptom_start_index] == ':':
                symptom_start_index += 1
            # 発症日の頭出し
            for i in range(symptom_start_index, len(line_str)):
                if line_str[i].isdecimal() is True or line_str[i].find('－') != -1 or line_str[i].find('ー') != -1:
                    break
            if line_str[i - 1] == ':':
                appearance_dt_start_index = i
            else:
                appearance_dt_start_index = i

            # 発症日のおしり出し
            if line_str[appearance_dt_start_index].find('－') != -1 or line_str[appearance_dt_start_index].find(
                    'ー') != -1 or line_str[appearance_dt_start_index].find('-') != -1:
                ret_str = None

            for i in range(appearance_dt_start_index, len(line_str)):
                if line_str[i].isdecimal() is True or line_str[i] == '/':
                    continue
                else:
                    appearance_dt_end_index = i
                    break
            ret_str = dt.strptime(f'{year}/{line_str[appearance_dt_start_index:appearance_dt_end_index]}', '%Y/%m/%d')

        return ret_str

    def get_status_id(self, coordinate):
        # DEBUG
        if 186 <= coordinate and coordinate <= 386:
            return 1
        elif 409 <= coordinate and coordinate <= 424:
            return 2
        elif 435 <= coordinate and coordinate <= 450:
            return 3
        elif 460 <= coordinate and coordinate <= 480:
            return 4
        elif 485 <= coordinate and coordinate <= 504:
            return 5
        elif 506 <= coordinate and coordinate <= 535:
            return 6
        else:
            return 0

    def export_dict(self):
        temp_dict = {}
        temp_dict['No'] = self.no
        temp_dict['revealed_dt'] = self.revealed_dt
        temp_dict['old'] = self.old
        temp_dict['sex'] = self.sex
        temp_dict['job'] = self.job
        temp_dict['symptom'] = self.symptom
        temp_dict['appearance_dt'] = self.appearance_dt
        temp_dict['status_id'] = self.status_id
        return temp_dict

    def __str__(self) -> str:
        return f'{self.no}, {self.revealed_dt}, {self.old}, {self.sex}, {self.job}, {self.symptom}, {self.appearance_dt}, {self.status_id}'


def find_textboxes_recursively(layout_obj):
    """
    再帰的にテキストボックス（LTTextBox）を探して、テキストボックスのリストを取得する。
    """
    # LTTextBoxを継承するオブジェクトの場合は1要素のリストを返す。
    if isinstance(layout_obj, LTTextBox):
        return [layout_obj]

    # LTContainerを継承するオブジェクトは子要素を含むので、再帰的に探す。
    if isinstance(layout_obj, LTContainer):
        boxes = []
        for child in layout_obj:
            boxes.extend(find_textboxes_recursively(child))

        return boxes

    return []  # その他の場合は空リストを返す。


def is_skip(text):
    if text.find('葛飾区内の') != -1:
        return True
    if text.find('一覧') != -1:
        return True
    elif text.find('備考') != -1:
        return True
    elif text.find('№') != -1:
        return True
    elif text.find('陽性') != -1:
        return True
    elif text.find('判明日') != -1:
        return True
    elif text.find('No') != -1:
        return True
    elif text.find('年代') != -1:
        return True
    elif text.find('性別') != -1:
        return True
    elif text.find('職業') != -1:
        return True
    elif text.find('症状') != -1:
        return True
    elif text.find('発症日') != -1:
        return True
    elif text.find('入院') != -1:
        return True
    elif text.find('調整') != -1:
        return True
    elif text.find('宿泊') != -1:
        return True
    elif text.find('自宅') != -1:
        return True
    elif text.find('療養') != -1:
        return True
    elif text.find('回復') != -1:
        return True
    elif text.find('死亡') != -1:
        return True
    elif text.find('通学') != -1:
        return True
    elif text.find('ｺﾛﾅ以外') != -1:
        return True
    elif text.find('#N/A') != -1:
        return True
    return False


def setup_pdf_archive_dir() -> str:
    this_py_path = os.path.dirname(os.path.abspath(__file__))
    pdf_archive_dir = os.path.join(this_py_path, 'pdf_archive')
    shutil.rmtree(pdf_archive_dir)
    os.mkdir(pdf_archive_dir)

    return pdf_archive_dir


def get_data(setting) -> list:
    '''
    初期化
    '''
    # Layout Analysisのパラメーターを設定。縦書きの検出を有効にする。
    laparams = LAParams()
    # 共有のリソースを管理するリソースマネージャーを作成。
    resource_manager = PDFResourceManager()
    # ページを集めるPageAggregatorオブジェクトを作成。
    device = PDFPageAggregator(resource_manager, laparams=laparams)
    # Interpreterオブジェクトを作成。
    interpreter = PDFPageInterpreter(resource_manager, device)
    pdf_archive_dir = setup_pdf_archive_dir()

    # pdf data
    patient_datas_pdf = []
    patient_datas_old = []
    ret_data = []
    '''
    リスト取得
    '''
    befor_tb_avg = 10000  # (top + bottom)/2

    # 分割されたPDFを1つずつ読み込み・処理
    box_list = []
    for pdf_url in setting.pdf_urls:
        # pdf取得
        pdf_path = os.path.join(pdf_archive_dir, pdf_url.split('/')[-1])
        print(pdf_url)
        with urllib.request.urlopen(pdf_url) as u:
            with open(pdf_path, 'bw') as o:
                o.write(u.read())

        with open(pdf_path, 'rb') as f:
            for page in PDFPage.get_pages(f):
                interpreter.process_page(page)
                layout = device.get_result()

                # ページ内のテキストボックスのリストを取得する。
                boxes = find_textboxes_recursively(layout)

                # テキストボックスの左上の座標の順でテキストボックスをソートする。
                # y1（Y座標の値）は上に行くほど大きくなるので、正負を反転させている。
                boxes.sort(key=lambda b: (-b.y1, b.x0))

                for box in boxes:
                    if is_skip(box.get_text()) is True:
                        if box.get_text().find('#N/A') != -1:
                            box_list = []
                        continue
                    temp_tb_avg = (box.y1 + box.y0) / 2

                    if 10 < befor_tb_avg - temp_tb_avg or befor_tb_avg - temp_tb_avg < -10:
                        box_list.sort(key=lambda b: (b.x0))
                        if len(box_list) == 0:
                            befor_tb_avg = temp_tb_avg
                            box_list = []
                        elif box_list[0].get_text().find('-1') != -1 or box_list[0].get_text().find(
                                '○') != -1 or box_list[0].get_text().find('(cid:16089)1') != -1:
                            befor_tb_avg = temp_tb_avg
                            box_list = []
                        else:
                            #print(box_list[0].get_text())
                            temp_pd = patient_data(box_list)
                            temp_pd.parse_line()
                            if temp_pd.is_error is False:
                                patient_datas_pdf.append(temp_pd)
                                befor_tb_avg = temp_tb_avg
                                box_list = []
                            else:
                                print('error')
                                print(box_list)
                                befor_tb_avg = temp_tb_avg
                                box_list = []

                    box_list.append(box)

        # 前のPDFファイルで残されたデータの処理
        temp_pd = patient_data(box_list)
        temp_pd.parse_line()
        if temp_pd.is_error is False:
            patient_datas_pdf.append(temp_pd)
            befor_tb_avg = temp_tb_avg
            box_list = []
        else:
            print('error')
            print(box_list)
            befor_tb_avg = temp_tb_avg
            box_list = []

    # 最後でデータを処理
    if len(box_list) == 0:
        befor_tb_avg = temp_tb_avg
        box_list = []
    else:
        temp_pd = patient_data(box_list)
        temp_pd.parse_line()
        if temp_pd.is_error is False:
            print(temp_pd.no)
            patient_datas_pdf.append(temp_pd)
            befor_tb_avg = temp_tb_avg
            box_list = []
        else:
            print('error')
            print(box_list)
            befor_tb_avg = temp_tb_avg
            box_list = []
    patient_datas_pdf.reverse()

    # 閲覧不可になったデータの処理
    # 4501~4510が削除されたため例外対応
    old_no_range = list(range(1, 3401)) + list(range(3501, 3701)) + list(range(4501, 4511)) 
    row_datas = []
    patient_datas_old = []
    with open(os.path.dirname(os.path.abspath(__file__)) + "/data/row_data.json", "r") as f:
        row_datas = json.load(f)
    for row_data in row_datas:
        if int(row_data['No']) not in old_no_range:
            continue
        temp_patient_data = patient_data()
        temp_patient_data.no = row_data['No']
        temp_patient_data.revealed_dt = dt.strptime(row_data['revealed_dt'], '%Y-%m-%d')
        temp_patient_data.old = row_data['old']
        temp_patient_data.sex = row_data['sex']
        temp_patient_data.job = row_data['job']
        temp_patient_data.symptom = row_data['symptom']
        if row_data['appearance_dt'] == '':
            temp_patient_data.appearance_dt = None
        else:
            temp_patient_data.appearance_dt = dt.strptime(row_data['appearance_dt'], '%Y-%m-%d')
        temp_patient_data.status_id = row_data['status_id']
        patient_datas_old.append(temp_patient_data)

    patient_datas = patient_datas_old + patient_datas_pdf
    patient_datas_sorted = sorted(patient_datas, key=lambda x: int(x.no))

    for patient in patient_datas_sorted:
        ret_data.append(patient.export_dict())
    return ret_data
