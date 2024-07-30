import pandas as pd
import re

"""
将x人 提取出放置某一列
"""
# 读取Excel文件
file_path = r"E:\pythonWorkSpace\python_learn\22222.xlsx"  # 替换为你的文件路径
df = pd.read_excel(file_path)

# 遍历每一行
for index, row in df.iterrows():
    signalzhuanyenumber = row['signalzhuanyenumber']

    # 判断signalzhuanyenumber列是否有内容
    if pd.notna(signalzhuanyenumber):
        continue  # 如果有内容，跳过本次循环

    # 使用正则表达式在zhuanyename列中查找匹配
    zhuanyename = row['zhuanyename']
    match = re.search(r'\d+人', zhuanyename)  # 替换为你要匹配的模式

    if match:
        # 如果找到匹配项，将匹配内容添加到signalzhuanyenumber列
        df.at[index, 'signalzhuanyenumber'] = match.group()  # 将匹配内容添加到signalzhuanyenumber列
        print()
    else:
        continue

# 保存修改后的数据到新的Excel文件
output_file_path = r"E:\pythonWorkSpace\python_learn\new_data.xlsx"  # 替换为你希望保存的文件路径
df.to_excel(output_file_path, index=False)
