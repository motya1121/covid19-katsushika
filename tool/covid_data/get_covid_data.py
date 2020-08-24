import sys

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
import tempfile
import urllib.request
import datetime

DEBUG = False
DEBUG_PRT_MAX_NO = '150'

class patient_data():
    def __init__(self):
        self.no = ''
        self.revealed_dt = ''
        self.old = ''
        self.sex = ''
        self.job = ''
        self.symptom = ''
        self.appearance_dt = ''
        self.status_id = ''
        self.temp_data = []

    def append(self, text, box):
        if text.find('○') != -1:  # '◯'の場合
            self.status_id = self.get_status_id(box.x0)
        else:
            # noかどうか
            if self.no == '':  # 未取得の場合
                self.no = self.check_no(text)
                if self.no != '':  # noの場合関数終了
                    return

            if self.no == '38':
                self.status_id = 5
            if self.no == '43':
                self.status_id = 5
            if self.no == '44':
                self.status_id = 5
            if self.no == '138':
                self.status_id = 5
            if self.no == '143':
                self.status_id = 5
            if self.no == '144':
                self.status_id = 5
            if self.no == '238':
                self.status_id = 5
            if self.no == '243':
                self.status_id = 5
            if self.no == '244':
                self.status_id = 5
            if self.no == '369':
                self.status_id = 5

            # 陽性判明日かどうか
            if self.revealed_dt == '':
                self.revealed_dt = self.check_date(text)
                if self.revealed_dt != '':
                    return

            # 年代かどうか
            if self.old == '':
                self.old = self.check_old(text)
                if self.old != '':
                    return

            # 性別かどうか
            if self.sex == '':
                self.sex = self.check_sex(text)
                if self.sex != '':
                    return

            # 職業
            if self.job == '':
                self.job = self.checl_job(text)
                if self.job != '':
                    return

            # 症状
            temp_text = self.check_symptom(text)
            self.symptom += temp_text
            if temp_text != '':
                return

            # 発症日
            if self.appearance_dt == '':
                self.appearance_dt = self.check_date(text)
                if self.appearance_dt != '':
                    return

    def check_full_data(self):
        '''全項目のデータが取得できたか確認

        Returns
        -------
        bool
            True: データが揃ってる， False: データが揃っていない
        '''

        if self.no != '' and self.revealed_dt != '' and self.old != '' and self.sex != '' and self.job != '' and self.symptom != '' and self.appearance_dt != '' and self.status_id != '':
            if self.appearance_dt is not None and self.revealed_dt < self.appearance_dt:
                temp = self.appearance_dt
                self.appearance_dt = self.revealed_dt
                self.revealed_dt = temp
            return True
        else:
            return False

    def check_no(self, text):
        if text.isdecimal() is True:
            return str(int(text))
        else:
            return ''

    def check_date(self, text):
        # －の場合の処理
        if text.find('－') != -1 or text.find('ー') != -1:
            if self.job != '':
                return None
            else:
                return ''

        try:
            temp_dt = datetime.datetime.strptime('2020/' + text, '%Y/%m/%d')
        except ValueError:
            return ''
        return temp_dt


    def check_old(self, text):
        # oldでhない場合
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

    def checl_job(self, text):
        # －の場合の処理
        if text.find('－') != -1 or text.find('ー') != -1:
                return text

        if text.find('無職') != -1:
            return '無職'
        elif text.find('会社員') != -1:
            return '会社員'
        elif text.find('学生') != -1:
            return '学生'
        elif text.find('自営業') != -1:
            return '自営業'
        elif text.find('医療従事者') != -1:
            return '医療従事者'
        elif text.find('公務員') != -1:
            return '公務員'
        elif text.find('調査中') != -1:
            return '調査中'
        else:
            return ''


    def check_symptom(self, text):
        # なしの場合の処理
        if text.find('なし') != -1:
            if self.symptom == '':
                return text
            else:
                return ''

        if text.find('熱') != -1:
            return text
        if text.find('発熱') != -1:
            return text
        if text.find('咳') != -1:
            return text
        if text.find('咽頭痛') != -1:
            return text
        if text.find('味覚障害') != -1:
            return text
        if text.find('嗅覚障害') != -1:
            return text
        if text.find('倦怠感') != -1:
            return text
        if text.find('下痢') != -1:
            return text
        if text.find('頭痛') != -1:
            return text
        if text.find('鼻汁') != -1:
            return text
        if text.find('関節痛') != -1:
            return text
        if text.find('鼻閉') != -1:
            return text
        if text.find('痰') != -1:
            return text
        if text.find('肺炎') != -1:
            return text
        if text.find('呼吸困難') != -1:
            return text
        if text.find('調査中') != -1:
            return text
        if text.find('咽頭痛') != -1:
            return text
        if text.find('意識障害') != -1:
            return text
        if text.find('食欲不振') != -1:
            return text
        return ''

    def get_status_id(self, coordinate):
        if 365 <= coordinate and coordinate <= 415:
            return 1
        elif 420 <= coordinate and coordinate <= 433:
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

    def __str__(self):
        return 'no:{}, revealed_dt:{}, old:{}, sex:{}, job:{}, symptom:{}, appearance_dt:{}, status_id:{}\n'.format(self.no, self.revealed_dt, self.old, self.sex, self.job, self.symptom, self.appearance_dt, self.status_id)


def get_data(setting):
    '''
    初期化
    '''
    # Layout Analysisのパラメーターを設定。縦書きの検出を有効にする。
    laparams = LAParams(detect_vertical=True)
    # 共有のリソースを管理するリソースマネージャーを作成。
    resource_manager = PDFResourceManager()
    # ページを集めるPageAggregatorオブジェクトを作成。
    device = PDFPageAggregator(resource_manager, laparams=laparams)
    # Interpreterオブジェクトを作成。
    interpreter = PDFPageInterpreter(resource_manager, device)
    # 返却する辞書
    ret_data = []
    patient_datas = []
    TEMP_NO = 0

    '''
    処理
    '''
    # pdf格納用のテンプディレクトリを作成
    with tempfile.TemporaryDirectory() as dname:
        # 分割されたPDFを1つずつ読み込み・処理
        for pdf_url in setting.pdf_urls:
            # pdf取得
            pdf_path = dname + '/covid_data.pdf'
            with urllib.request.urlopen(pdf_url) as u:
                with open(pdf_path, 'bw') as o:
                    o.write(u.read())

            # pdf解析
            with open(pdf_path, 'rb') as f:
                # PDFPage.get_pages()にファイルオブジェクトを指定して、PDFPageオブジェクトを順に取得する。
                # 時間がかかるファイルは、キーワード引数pagenosで処理するページ番号（0始まり）のリストを指定するとよい。
                for page in PDFPage.get_pages(f):
                    interpreter.process_page(page)  # ページを処理する。
                    layout = device.get_result()  # LTPageオブジェクトを取得。

                    # ページ内のテキストボックスのリストを取得する。
                    boxes = find_textboxes_recursively(layout)

                    # テキストボックスの左上の座標の順でテキストボックスをソートする。
                    # y1（Y座標の値）は上に行くほど大きくなるので、正負を反転させている。
                    boxes.sort(key=lambda b: (-b.y1, b.x0))

                    temp_patient_data = patient_data()
                    for box in boxes:
                        for text in box.get_text().strip().split():
                            if is_skip(text) is False:
                                temp_patient_data.append(text, box)
                                if DEBUG:
                                    print(text)
                                    print(temp_patient_data)
                        if temp_patient_data.check_full_data() is True:
                            if DEBUG:
                                print('******ここまで {} *****'.format(temp_patient_data.no))
                                if temp_patient_data.no == DEBUG_PRT_MAX_NO:
                                    exit()
                            if temp_patient_data.no != str(TEMP_NO - 1):
                                print("error: no:{}".format(temp_patient_data.no))
                            TEMP_NO = int(temp_patient_data.no)
                            patient_datas.append(temp_patient_data)
                            temp_patient_data = patient_data()

    patient_datas.reverse()  # リストを反転させる
    for patient in patient_datas:
        ret_data.append(patient.export_dict())
    return ret_data


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
    return False

