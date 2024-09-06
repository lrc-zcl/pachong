import os
import docx
import pandas as pd

"""
处理文档 self
"""


def extract_first_bracket_content(input_str):
    # 使用正则表达式匹配第一个括号内的内容
    # 总人数 + 文理
    match = re.search(r'\((.*?)\)', input_str)
    if match:
        return match.group(1)  # 返回括号内的内容
    else:
        return None  # 如果没有匹配到括号，则返回None


import re

xuexiao_name = ""
xuexiao_code = ""
zhuanye_name = ""
zhuanye_code = ""
signal_zhuanye_number = ""
beizhu_information = ""


def extract_text_between_brackets(input_str):
    """
    提取）（ 单独专业人数
    :param input_str:
    :return:
    """
    pattern = r'\((.*?)\)'  # 匹配括号内的任意内容，非贪婪模式
    match = re.search(pattern, input_str)
    if match:
        return match.group(1).strip()  # 返回括号内的内容，并去除首尾空格
    else:
        return None  # 如果没有匹配到括号，则返回None


def read_docx(file_path):
    global xuexiao_name
    global xuexiao_code
    global zhuanye_name
    global zhuanye_code
    global signal_zhuanye_number
    global beizhu_information
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
        # a = '\n'.join(full_text)
    for signal_data_i in full_text:
        signal_data = signal_data_i.replace(" ", "")
        if len(signal_data) >= 5 and signal_data[:5].isdigit():
            xuexiao_code = signal_data[:5]  # 学校代码 str
            xuexiao_name_list = []
            count = 0
            # a = signal_data[5:]
            for indata in signal_data[5:]:
                if not indata.isdigit():
                    xuexiao_name_list.append(indata)
                    # xuexiao_name = "".join(xuexiao_name_list) # 学校名称
                    count = count + 1
                else:
                    for i in range(len(signal_data)):
                        if signal_data[i] == "(":
                            renshu_index = i - 1
                            renshu_number = signal_data[count + 5:renshu_index]  # 招生人数

                    xuexiao_name = "".join(xuexiao_name_list)  # 学校名称

                    people_number = str(renshu_number) + str(
                        extract_first_bracket_content(signal_data))  # 招生人数 + 文理  (作废)
                    break
        if len(signal_data) >= 5 and signal_data[:3].isdigit() and not signal_data[:5].isdigit():  # 提取专业信息
            zhuanye_code = signal_data[:3]  # 专业代码
            for i in range(len(signal_data)):
                if signal_data[i] == "(":
                    zhuanye_name = signal_data[3:i]  # 专业名称
            signal_zhuanye = re.search(r'\b(\d+\s*人)\b', signal_data)
            if signal_zhuanye:
                signal_zhuanye_number = signal_zhuanye.group(1)
            else:
                print("未找到专业代码人数匹配的内容")
            beizhu = re.findall(r'\((.*?)\)', signal_data)
            beizhu_information = " ".join(beizhu)

        else:
            print("不做记录的信息！")
            continue
        print(xuexiao_name, xuexiao_code, zhuanye_name, zhuanye_code, signal_zhuanye_number, beizhu_information)
        if not os.path.exists(excel_path):
            df = pd.DataFrame(
                columns=['xuexiaoname', 'xuexiaocode', 'zhuanyecode', 'zhuanyename', 'signalzhuanyenumber',
                         'beizhuinfomation'])
            df.to_excel(excel_path, index=False)
        df = pd.read_excel(excel_path)
        new_data = {'xuexiaoname': xuexiao_name, 'xuexiaocode': xuexiao_code, 'zhuanyename': zhuanye_name,
                    'zhuanyecode': zhuanye_code, 'signalzhuanyenumber': signal_zhuanye_number,
                    'beizhuinfomation': beizhu_information}
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_excel(excel_path, index=False)
    # return xuexiao_name,xuexiao_code,zhuanye_name,zhuanye_code,signal_zhuanye_number,beizhu_information


if __name__ == "__main__":
    # 替换为你的 Word 文档路径
    word_file = r"C:\Users\86186\Desktop\2023gxzsjh_Password_Removed_2.docx"
    excel_path = "./dataresult.xlsx"
    result = read_docx(word_file)
    print("over!")
