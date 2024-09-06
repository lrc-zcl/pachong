import os
import requests
from lxml import etree
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import pandas as pd
"""
爬取教育部官网高等职业学校专业教学标准
"""
#url = "http://www.moe.gov.cn/s78/A07/zcs_ztzl/2017_zt06/17zt06_bznr/bznr_gzjxbz/"
url = "http://www.moe.gov.cn/s78/A07/zcs_ztzl/2017_zt06/17zt06_bznr/bznr_zdzyxxzyml/"
=======
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc

"""
爬取教育部官网高等职业学校专业教学标准
"""
url = "http://www.moe.gov.cn/s78/A07/zcs_ztzl/2017_zt06/17zt06_bznr/bznr_gzjxbz/"
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}


def send_requsts(url):
    """
    获取请求
    "http://www.moe.gov.cn/s78/A07/zcs_ztzl/2017_zt06/17zt06_bznr/bznr_gzjxbz/"
    :param url:
    :return:
    """

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=header)

    response.encoding = "utf-8"
    result = response.text
    etreesignal = etree.HTML(result)
    return etreesignal


def get_first(url):
    yiji_url = []
    yiji_name = []
    etreesignal = send_requsts(url=url)
    yiji_el = etreesignal.xpath("//div[@class='moe-list']")  # 一级目录名称
    for data in yiji_el:
        data_1 = data.xpath("./div[1]/h2/a/@href")[0].replace(".", "")
        yiji_url.append(data_1)
        fir_name = data.xpath("./div[1]/h2//text()")[0].replace(">", "")
        yiji_name.append(data.xpath("./div[1]/h2//text()")[0].replace(">", ""))  # 一级目录
    return yiji_url, yiji_name


def get_second(url):
    yiji_url = get_first(url)
    erji_all_url = []
    erji_all_name = []
    for data in yiji_url[0]:
        etreesignal = send_requsts(url=url + data)
        erji_el = etreesignal.xpath("//div[@class='moe-list']/div")
        erji_url = []
        erji_name = []
        for data_2 in erji_el:
            data = data_2.xpath("./h2/a/@href")[0].replace(".", "")
            erji_url.append(data)
            # erji_name = data_2.xpath("./h2//text()")[0].replace(">", "")
            erji_name.append(data_2.xpath("./h2//text()")[0].replace(">", ""))
        erji_all_url.append(erji_url)
        erji_all_name.append(erji_name)
    return erji_all_url, erji_all_name


def get_paper(url):
    yijidata = get_first(url=url)
    erjidata = get_second(url=url)
    for index_1, yiji in enumerate(yijidata[0]):
        for index_2, erji in enumerate(erjidata[0][index_1]):
            etreesignal = send_requsts(url=url + yiji + erji)
            paper_el = etreesignal.xpath("//ul[@id='list']/li")
            for final in paper_el:
                paperul = str(final.xpath("./a/@href")[0]).replace("./", "")
                papername = final.xpath("./a//text()")[0]
                print(papername)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                path = f"C:/Users/36974/Desktop/data/{yijidata[1][index_1].strip()}/{erjidata[1][index_1][index_2].strip()}"
=======
                path = f"C:/Users/36974/Desktop/2324/{yijidata[1][index_1].strip()}/{erjidata[1][index_1][index_2].strip()}"
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
                path = f"C:/Users/36974/Desktop/2324/{yijidata[1][index_1].strip()}/{erjidata[1][index_1][index_2].strip()}"
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
                path = f"C:/Users/36974/Desktop/2324/{yijidata[1][index_1].strip()}/{erjidata[1][index_1][index_2].strip()}"
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
                if not os.path.exists(path):
                    os.makedirs(path)
                    print("创建文件夹成功!")

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                signal_paper_url = f"http://www.moe.gov.cn/s78/A07/zcs_ztzl/2017_zt06/17zt06_bznr/bznr_zdzyxxzyml/{yiji}{erji}" + paperul
=======
                signal_paper_url = f"http://www.moe.gov.cn/s78/A07/zcs_ztzl/2017_zt06/17zt06_bznr/bznr_gzjxbz{yiji}{erji}" + paperul
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
                signal_paper_url = f"http://www.moe.gov.cn/s78/A07/zcs_ztzl/2017_zt06/17zt06_bznr/bznr_gzjxbz{yiji}{erji}" + paperul
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
                signal_paper_url = f"http://www.moe.gov.cn/s78/A07/zcs_ztzl/2017_zt06/17zt06_bznr/bznr_gzjxbz{yiji}{erji}" + paperul
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
                result = requests.get(signal_paper_url, headers=header)
                result.encoding = "utf-8"
                savefile = os.path.join(path, papername) + ".pdf"
                with open(savefile, 'wb') as file:
                    file.write(result.content)
                print(f'PDF downloaded successfully: {savefile}')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                xpath = "C:/Users/36974/Desktop/data/type-info.xlsx"
                if not os.path.exists(xpath):
                    df = pd.DataFrame(columns=['yiji', 'erji', 'wenzhang'])
                    df.to_excel(xpath, index=False)
                df = pd.read_excel(xpath)
                new_data = {'yiji':yijidata[1][index_1], 'erji': erjidata[1][index_1][index_2], 'wenzhang': papername}
                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                df.to_excel(xpath, index=False)
=======
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
                # xpath = "./xuexiao.xlsx"
                # if not os.path.exists(xpath):
                #     df = pd.DataFrame(columns=['yiji', 'erji', 'wenzhang'])
                #     df.to_excel(xpath, index=False)
                # df = pd.read_excel(xpath)
                # new_data = {'yiji':fir_name, 'erji': sec_name, 'wenzhang': wenzhangming}
                # df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                # df.to_excel(xpath, index=False)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
=======
>>>>>>> ba96a5eb739f85ef566c5417785ef6ab26d688bc
    print("over!!!")


if __name__ == "__main__":
    get_paper(url=url)
