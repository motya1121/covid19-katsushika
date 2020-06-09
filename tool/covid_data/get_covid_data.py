import sys

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
import tempfile
import urllib.request
import datetime


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

    '''
    処理
    '''
    # pdf格納用のテンプディレクトリを作成
    with tempfile.TemporaryDirectory() as dname:
        # pdf取得
        pdf_path = dname + '/covid_data.pdf'
        with urllib.request.urlopen(setting.pdf_url) as u:
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

                count = 0
                symptom_flag = False
                next_i = False
                temp_data = {}
                for box in boxes:
                    next_i = False
                    text = []
                    if is_skip(box.get_text().strip()) is True:
                        continue
                    if count == 0:
                        if check_symptom(box.get_text().strip()) is True:
                            temp_data['Symptom'] = box.get_text().strip()
                            symptom_flag = True
                            count -= 1
                        else:
                            temp_data['No'] = box.get_text().strip()
                    if count == 1:
                        if next_i is not False and next_i != 0:
                            temp_data['revealed_dt'] = datetime.datetime.strptime('2020/' + text[next_i], '%Y/%m/%d')
                            next_i += 1
                            if next_i < len(text):
                                count += 1
                            else:
                                next_i = 0
                        else:
                            text = box.get_text().strip()
                            text = text.split(' ')
                            if 1 < len(text):
                                next_i += 1
                                count += 1
                            temp_data['revealed_dt'] = datetime.datetime.strptime('2020/' + text[0], '%Y/%m/%d')  # 要請判明日
                    if count == 2:
                        if next_i != 0:
                            temp_data['old'] = cal_old(text[next_i])
                            next_i += 1
                            if next_i < len(text):
                                count += 1
                            else:
                                next_i = 0
                        else:
                            text = box.get_text().strip()
                            text = text.split(' ')
                            if 1 < len(text):
                                next_i += 1
                                count += 1
                            temp_data['old'] = cal_old(text[0])
                    if count == 3:
                        if next_i != 0:
                            temp_data['sex'] = 1 if text[next_i].find('男') != -1 else 2
                            next_i += 1
                            if next_i < len(text):
                                count += 1
                            else:
                                next_i = 0
                        else:
                            text = box.get_text().strip()
                            text = text.split(' ')
                            if 1 < len(text):
                                next_i += 1
                                count += 1
                            temp_data['sex'] = 1 if text[0].find('男') != -1 else 2
                    if count == 4:
                        if next_i != 0:
                            temp_data['job'] = text[next_i]
                            next_i += 1
                            if next_i < len(text):
                                count += 1
                            else:
                                next_i = 0
                        else:
                            text = box.get_text().strip()
                            text = text.split(' ')
                            if 1 < len(text):
                                next_i += 1
                                count += 1
                                temp_data['job'] = text[0]
                            else:
                                temp_data['job'] = box.get_text().strip()
                    if count == 5:
                        if symptom_flag is True:
                            count += 1
                        elif next_i != 0:
                            temp_data['symptom'] = text[next_i]
                            next_i += 1
                            if next_i < len(text):
                                count += 1
                            else:
                                next_i = 0
                        else:
                            text = box.get_text().strip()
                            text = text.split(' ')
                            if 1 < len(text):
                                next_i += 1
                                count += 1
                                temp_data['symptom'] = text[0]
                            else:
                                temp_data['symptom'] = box.get_text().strip()
                    if count == 6:
                        if next_i != 0:
                            if text[next_i].find('なし') != -1:
                                temp_data['appearance_dt'] = None
                            else:
                                temp_data['appearance_dt'] = datetime.datetime.strptime('2020/' + text[next_i], '%Y/%m/%d')  # 発症日text[next_i]
                            next_i += 1
                            if next_i < len(text):
                                count += 1
                            else:
                                next_i = 0
                        else:
                            text = box.get_text().strip()
                            text = text.split(' ')
                            if 1 < len(text):
                                next_i += 1
                                count += 1
                                if box.get_text().strip().find('なし') != -1:
                                    temp_data['appearance_dt'] = None
                                else:
                                    temp_data['appearance_dt'] = datetime.datetime.strptime('2020/' + text[0], '%Y/%m/%d')  # 発症日
                            else:
                                if box.get_text().strip().find('なし') != -1:
                                    temp_data['appearance_dt'] = None
                                else:
                                    temp_data['appearance_dt'] = datetime.datetime.strptime('2020/' + box.get_text().strip(), '%Y/%m/%d')  # 発症日
                    if count == 7:
                        temp_data['status_id'] = get_status_id(box.x0)
                        count = -1
                        symptom_flag = False
                        ret_data.append(temp_data)
                        temp_data = {}
                    count += 1

    ret_data.reverse()  # リストを反転させる
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


def cal_old(text):
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
    elif text.find('７０') != -1:
        return 70
    elif text.find('８０') != -1:
        return 80
    elif text.find('９０') != -1:
        return 90
    return 100


def get_status_id(coordinate):
    if 400 <= coordinate and coordinate <= 415:
        return 1
    elif 420 <= coordinate and coordinate <= 433:
        return 2
    elif 450 <= coordinate and coordinate <= 460:
        return 3
    elif 475 <= coordinate and coordinate <= 485:
        return 4
    elif 500 <= coordinate and coordinate <= 510:
        return 5
    elif 525 <= coordinate and coordinate <= 535:
        return 6
    else:
        return 0


def is_skip(text):
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
    return False


def check_symptom(text):
    if text.find('発熱') != -1:
        return True
    if text.find('咳') != -1:
        return True
    if text.find('咽頭痛') != -1:
        return True
    if text.find('味覚障害') != -1:
        return True
    if text.find('嗅覚障害') != -1:
        return True
    if text.find('倦怠感') != -1:
        return True
    if text.find('下痢') != -1:
        return True
    if text.find('頭痛') != -1:
        return True
    if text.find('鼻汁') != -1:
        return True
    if text.find('関節痛') != -1:
        return True
    if text.find('鼻閉') != -1:
        return True
    if text.find('痰') != -1:
        return True
    if text.find('肺炎') != -1:
        return True
    if text.find('呼吸困難') != -1:
        return True
    return False
