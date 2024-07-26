import requests
import pandas as pd
import os
from lxml import etree

"""
爬取软科民办高职信息
"""
for pagedata in range(1, 10):
    urldata = f"https://www.shanghairanking.cn/rankings/bcvcr/2024633"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    response = requests.get(urldata, headers=header)
    response.encoding = "utf-8"
    result = response.text
    # print(result)
    etreesignal = etree.HTML(result)
    hotol_list = etreesignal.xpath("//table[@class='rk-table']/tbody/tr")
    xlsxpath = "../data/all.xlsx"
    if not os.path.exists(xlsxpath):
        df = pd.DataFrame(columns=['Name', 'Location', 'Educational level', 'Type'])
        df.to_excel(xlsxpath, index=False)

    for signal_hotol in hotol_list:
        Name_data = signal_hotol.xpath("./td[2]/div/div[2]/div[1]//text()")  # 标题
        English_name_data = signal_hotol.xpath("./td[2]/div/div[2]/div[2]//text()")
        Location_data = signal_hotol.xpath("./td[3]//text()")  # 位置
        # Education_data = signal_hotol.xpath("./td[2]/div/div[2]/p/text()")  # 面积 方位 楼层 年份
        # Type_data = signal_hotol.xpath("./td[4]//text()")  # 价格

        name_data = Name_data[0].replace(" ", '').replace("\n", "")
        english_name_data = English_name_data[0].lower().strip().replace(" ", "-")
        location_data = Location_data[0].replace(" ", "").replace("\n", "")
        # education_data = Education_data[0].replace(" ", "").replace("\n", "")
        # type_data = Type_data[0].replace(" ", "").replace("\n", "")
        print(name_data, location_data)
        df = pd.read_excel(xlsxpath)
        new_data = {'Name': name_data, 'Location': location_data}
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_excel(xlsxpath, index=False)
    print("write over!!!")
