import docx
import pandas as pd
import os
import re

"""
处理文档，将院校招生信息提取出来。
"""


def extract_first_bracket_content(input_str):
    # Extracts content within the first pair of brackets
    match = re.search(r'\((.*?)\)', input_str)
    if match:
        return match.group(1).strip()  # Strip whitespace from extracted content
    else:
        return None


def read_docx(file_path):
    doc = docx.Document(file_path)
    data_rows = []

    xuexiao_name = ''
    xuexiao_code = ''

    for para in doc.paragraphs:
        signal_data = para.text.strip().replace(" ", "")

        if signal_data:
            # Extracting school information
            if signal_data[:5].isdigit() and not signal_data[:6].isdigit():
                xuexiao_code = signal_data[:5]
                xuexiao_name = ''.join([c for c in signal_data[5:] if not c.isdigit()]).strip()
                renshu_index = signal_data.find('(')
                renshu_number = signal_data[5:renshu_index].strip() if renshu_index != -1 else ''
                xuexiao_name = xuexiao_name.rstrip('(').strip()
                people_number = str(renshu_number) + ' ' + str(
                    extract_first_bracket_content(signal_data)) if renshu_number else None

            # Extracting major information
            elif signal_data[:3].isdigit() and not signal_data[:5].isdigit():
                zhuanye_code = signal_data[:3]
                zhuanye_name = signal_data[3:signal_data.find('(')].strip()
                signal_zhuanye = re.search(r'\b(\d+\s*人)\b', signal_data)
                signal_zhuanye_number = signal_zhuanye.group(1) if signal_zhuanye else ''
                beizhu_information = ' '.join(re.findall(r'\((.*?)\)', signal_data))

                data_rows.append({
                    'xuexiaoname': xuexiao_name,
                    'xuexiaocode': xuexiao_code,
                    'zhuanyename': zhuanye_name,
                    'zhuanyecode': zhuanye_code,
                    'signalzhuanyenumber': signal_zhuanye_number,
                    'beizhuinfomation': beizhu_information
                })

    df = pd.DataFrame(data_rows)

    excel_path = "./lrc.xlsx"
    if not os.path.exists(excel_path):
        df.to_excel(excel_path, index=False)
    else:
        existing_df = pd.read_excel(excel_path)
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        updated_df.to_excel(excel_path, index=False)


if __name__ == "__main__":
    word_file = r"C:\Users\86186\Desktop\2023gxzsjh_Password_Removed_2.docx"
    read_docx(word_file)
    print("Process complete.")
