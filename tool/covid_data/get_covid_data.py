import sys

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
import tempfile
import urllib.request
from datetime import datetime as dt
import json
import os
import setting


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
        if line_str.find('cid') != -1:
            print(line_str)
        line_list = line_str.split(':')
        self.no = line_list[0]
        self.revealed_dt = self.check_date(line_list[1])
        self.old = self.check_old(line_list[2])
        self.sex = self.check_sex(line_list[3])
        self.job = self.parse_job(line_list[4], line_str)
        self.symptom = self.parse_symptom(line_str)
        self.appearance_dt = self.parse_appearance_dt(line_list[6],line_str)
        self.status_id = self.get_status_id(self.box_list[-1].x0)

    def cid_to_jp(self, text:str) -> str:
        ret_str=text
        #print(ret_str)
        ret_str = ret_str.replace('(cid:7053)', '未')
        ret_str = ret_str.replace('(cid:8246)', '満')
        ret_str = ret_str.replace('(cid:3510)', '公')
        ret_str = ret_str.replace('(cid:3771)', '務')
        ret_str = ret_str.replace('(cid:7197)', '査')
        ret_str = ret_str.replace('(cid:2928)', '中')
        ret_str = ret_str.replace('(cid:4256)', '営')
        ret_str = ret_str.replace('(cid:3851)', '医')
        ret_str = ret_str.replace('(cid:5777)', '従')
        ret_str = ret_str.replace('(cid:2982)', '事')
        ret_str = ret_str.replace('(cid:2903)', '下')
        ret_str = ret_str.replace('(cid:9321)', '痢')
        ret_str = ret_str.replace('(cid:7890)', '汁')
        ret_str = ret_str.replace('(cid:14069)', '関')
        ret_str = ret_str.replace('(cid:10247)', '節')
        ret_str = ret_str.replace('(cid:10173)', '筋')
        ret_str = ret_str.replace('(cid:10967)', '肉')
        ret_str = ret_str.replace('(cid:14050)', '閉')
        ret_str = ret_str.replace('(cid:9329)', '痰')
        ret_str = ret_str.replace('(cid:4071)', '呼')
        ret_str = ret_str.replace('(cid:4030)', '吸')
        ret_str = ret_str.replace('(cid:4436)', '困')
        ret_str = ret_str.replace('(cid:14260)', '難')
        ret_str = ret_str.replace('(cid:6245)', '扁')
        ret_str = ret_str.replace('(cid:7240)', '桃')
        ret_str = ret_str.replace('(cid:8534)', '炎')
        ret_str = ret_str.replace('(cid:13596)', '重')
        ret_str = ret_str.replace('(cid:4748)', '声')
        ret_str = ret_str.replace('(cid:18140)', 'が')
        ret_str = ret_str.replace('(cid:18139)', 'か')
        ret_str = ret_str.replace('(cid:18153)', 'す')
        ret_str = ret_str.replace('(cid:18204)', 'れ')
        ret_str = ret_str.replace('(cid:18203)', 'る')
        ret_str = ret_str.replace('(cid:11034)', '胸')
        ret_str = ret_str.replace('(cid:11100)', '腰')
        ret_str = ret_str.replace('(cid:18191)', 'み')
        ret_str = ret_str.replace('(cid:4302)', '嘔')
        ret_str = ret_str.replace('(cid:4004)', '吐')
        ret_str = ret_str.replace('(cid:5967)', '悪')
        ret_str = ret_str.replace('(cid:5166)', '寒')
        ret_str = ret_str.replace('(cid:14551)', '食')
        ret_str = ret_str.replace('(cid:7719)', '欲')
        ret_str = ret_str.replace('(cid:8182)', '減')
        ret_str = ret_str.replace('(cid:13285)', '退')
        ret_str = ret_str.replace('(cid:18169)', 'ど')
        ret_str = ret_str.replace('(cid:13354)', '違')
        ret_str = ret_str.replace('(cid:4084)', '和')
        ret_str = ret_str.replace('(cid:3506)', '全')
        ret_str = ret_str.replace('(cid:13087)', '身')
        ret_str = ret_str.replace('(cid:16089)', '－')
        ret_str = ret_str.replace('(cid:7868)', '気')
        ret_str = ret_str.replace('(cid:11004)', '背')
        ret_str = ret_str.replace('(cid:13450)', '部')
        ret_str = ret_str.replace('(cid:3048)', '以')
        ret_str = ret_str.replace('(cid:10997)', '肺')
        ret_str = ret_str.replace('(cid:4260)', '嗄')
        ret_str = ret_str.replace('(cid:11105)', '腹')
        ret_str = ret_str.replace('(cid:16887)', '－')
        ret_str = ret_str.replace('(cid:5776)', '徒')
        ret_str = ret_str.replace('(cid:18313)', '・')
        ret_str = ret_str.replace('(cid:5083)', '学')
        ret_str = ret_str.replace('(cid:9173)', '生')
        ret_str = ret_str.replace('(cid:18445)', '１')
        ret_str = ret_str.replace('(cid:18446)', '２')
        ret_str = ret_str.replace('(cid:18447)', '３')
        ret_str = ret_str.replace('(cid:18448)', '４')
        ret_str = ret_str.replace('(cid:18449)', '５')
        ret_str = ret_str.replace('(cid:18450)', '６')
        ret_str = ret_str.replace('(cid:18451)', '７')
        ret_str = ret_str.replace('(cid:18452)', '８')
        ret_str = ret_str.replace('(cid:18453)', '９')
        ret_str = ret_str.replace('(cid:7763)', '歳')
        ret_str = ret_str.replace('(cid:4065)', '味')
        ret_str = ret_str.replace('(cid:12396)', '覚')
        ret_str = ret_str.replace('(cid:14208)', '障')
        ret_str = ret_str.replace('(cid:5142)', '害')
        ret_str = ret_str.replace('(cid:4261)', '嗅')
        ret_str = ret_str.replace('(cid:12396)', '覚')
        ret_str = ret_str.replace('(cid:15407)', '鼻')
        ret_str = ret_str.replace('(cid:14476)', '頭')
        ret_str = ret_str.replace('(cid:4119)', '咽')
        ret_str = ret_str.replace('(cid:18141)', 'き')
        ret_str = ret_str.replace('(cid:11358)', '苦')
        ret_str = ret_str.replace('(cid:3392)', '像')
        ret_str = ret_str.replace('(cid:5925)', '息')
        ret_str = ret_str.replace('(cid:18149)', 'さ')
        ret_str = ret_str.replace('(cid:13307)', '通')
        ret_str = ret_str.replace('(cid:18550)', 'コ')
        ret_str = ret_str.replace('(cid:18583)', 'ロ')
        ret_str = ret_str.replace('(cid:18561)', 'ナ')
        ret_str = ret_str.replace('(cid:4773)', '外')
        ret_str = ret_str.replace('(cid:18314)', '－')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        #ret_str = ret_str.replace('(cid:)', '')
        return ret_str
    def check_date(self, text) -> dt:
        if text.find('－') != -1 or text.find('ー') != -1 or text.find('-') != -1:
            return ''

        if text.find('11/') != -1 or text.find('12/') != -1:
            year = '2020'
        else:
            year = '2021'
        return dt.strptime(f'{year}/{text}', '%Y/%m/%d')

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
            if line_str[i].isdecimal() is True or line_str[i].find('－') != -1 or line_str[i].find('ー') != -1  or line_str[i].find('-') != -1:
                break
        if line_str[i-1] == ':':
            symptom_end_index = i-1
        else:
            symptom_end_index = i
        return line_str[symptom_start_index:symptom_end_index]

    def parse_appearance_dt(self, line_list_6, line_str):
        # 例外処理
        '''
        if self.no in ['2933', '2921', '3066', '3062', '3032', '3023', '3087', '3089']:
            ret_str = None
            return ret_str
        '''
        
        # 綺麗な形の場合
        ret_str = ''
        try:
            if line_list_6.find('－') != -1 or line_list_6.find('ー') != -1 or line_list_6.find('-') != -1:
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
            if line_str[i-1] == ':':
                appearance_dt_start_index = i
            else:
                appearance_dt_start_index = i

            # 発症日のおしり出し
            if line_str[appearance_dt_start_index].find('－') != -1 or line_str[appearance_dt_start_index].find('ー') != -1  or line_str[appearance_dt_start_index].find('-') != -1:
                ret_str =  None

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
        if 190 <= coordinate and coordinate <= 415:
            return 1
        elif 420 <= coordinate and coordinate <= 435:
            return 2
        elif 450 <= coordinate and coordinate <= 460:
            return 3
        elif 475 <= coordinate and coordinate <= 485:
            return 4
        elif 500 <= coordinate and coordinate <= 510:
            return 5
        elif 520 <= coordinate and coordinate <= 535:
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
    # pdf data
    patient_datas_pdf = []
    patient_datas_old = []
    ret_data = []
    '''
    リスト取得
    '''
    befor_tb_avg = 10000  # (top + bottom)/2

    # pdf格納用のテンプディレクトリを作成
    with tempfile.TemporaryDirectory() as dname:
        # 分割されたPDFを1つずつ読み込み・処理
        box_list = []
        for pdf_url in setting.pdf_urls:
            # pdf取得
            pdf_path = dname + '/covid_data.pdf'
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
                            else:
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
    old_no_range = list(range(1, 1301)) + list(range(1601, 1801))
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
