import requests
import pandas as pd
import os
from lxml import etree
import asyncio
import aiohttp

"""
安居客爬取信阳二手房
"""
location = ['abcdefghijklm', 'pingqiaob', 'yangshanxinqu']
# location = ['huaibin']
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
xlsxpath = r"C:\Users\36974\Desktop\wechat-app\data\alldata.xlsx"


def data_check(hotol_list, xlsxpath):
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
        print(f"一个房源写入完成{new_data}")


async def send_response(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url, headers=header) as response:
            html_result = await response.text()
            etreesignal = etree.HTML(html_result)
            hotol_list = etreesignal.xpath("//section[@class='list']/div")
            data_check(hotol_list=hotol_list,xlsxpath=xlsxpath)  # 解析数据
    # return hotol_list




async def main():
    task = []
    for locationdata in location:
        for pagedata in range(1, 20):
            urldata = f"https://xinyang.anjuke.com/sale/{locationdata}/p{pagedata}"
            task.append(asyncio.create_task(send_response(url=urldata)))
    result = await asyncio.wait(task)
    print("全部完成！！")

if __name__ == "__main__":
    asyncio.run(main())
