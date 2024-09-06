import requests
import pandas as pd
import os
from lxml import etree

"""
安居客爬取信阳二手房
"""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
location = ['abcdefghijklm','pingqiaob','yangshanxinqu']
#location = ['huaibin']
=======
# location = ['abcdefghijklm','pingqiaob','yangshanxinqu']
location = ['huaibin']
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
# location = ['abcdefghijklm','pingqiaob','yangshanxinqu']
location = ['huaibin']
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
# location = ['abcdefghijklm','pingqiaob','yangshanxinqu']
location = ['huaibin']
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc

for locationdata in location:
    for pagedata in range(1, 20):
        urldata = f"https://xinyang.anjuke.com/sale/{locationdata}/p{pagedata}/"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        response = requests.get(urldata, headers=header)
        response.encoding = "utf-8"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        print("状态码:",response.status_code)
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
        result = response.text
        # print(result)
        headerdata = ['title', 'vaules']
        etreesignal = etree.HTML(result)
        hotol_list = etreesignal.xpath("//section[@class='list']/div")
        xlsxpath = f"../xinyang-{locationdata}.xlsx"
        if not os.path.exists(xlsxpath):
            df = pd.DataFrame(columns=['Title', 'Location', 'Size-Floor-Years', 'Values'])
            df.to_excel(xlsxpath, index=False)

        for signal_hotol in hotol_list:
            signal_title_data = signal_hotol.xpath("./a/div[2]/div[1]/div[1]//text()")  # 标题
            signal_location_data = signal_hotol.xpath("./a/div[2]/div[1]/section/div[2]//text()")  # 位置
            signal_size_data = signal_hotol.xpath("./a/div[2]/div[1]/section/div[1]//text()")  # 面积 方位 楼层 年份
            signal_value_data = signal_hotol.xpath("./a/div[2]/div[2]//text()")  # 价格

            final_title_data = signal_title_data[1].strip().replace("  ", " ")
            final_location_data = "-".join(signal_location_data[2:]).strip().replace("  ", " ")
            final_size_data = "".join(signal_size_data).strip().replace("\n", "-").replace(" ", "")
            final_value_data = "".join(signal_value_data).strip().replace("\n", "-").replace(" ", "")
            print(final_title_data, final_location_data, final_size_data, final_value_data)
            df = pd.read_excel(xlsxpath)
            new_data = {'Title': final_title_data, 'Location': final_location_data, 'Size-Floor-Years': final_size_data,
                        'Values': final_value_data}
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_excel(xlsxpath, index=False)
        print(f"{locationdata}:{pagedata} over!!!")
