import requests
from selenium import webdriver
import asyncio
from selenium.webdriver.common.by import By
from lxml import etree
import time
import cv2
from selenium.webdriver import ActionChains
import random
import aiohttp

'''
访问抖音链接  破解滑动验证 获取下载链接
'''


def get_imag_pos(image_data, name, max_area=10000, max_zhouchang=400, min_area=8100, min_zhouchang=360):
    image = cv2.imread(image_data)
    blurred = cv2.GaussianBlur(image, (5, 5), 0, 0)
    canny = cv2.Canny(blurred, 0, 100)
    contours, hierachy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for signal_contour in contours:
        x, y, w, h = cv2.boundingRect(signal_contour)
        if min_area < w * h < max_area and min_zhouchang < 2 * (w + h) < max_zhouchang:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imwrite(name, image)
            print("xiaode", (x, y, w, h))
            return (w + 10) * (h + 10), 2 * (w + h + 20), (w - 10) * (h - 10), ((w - 10) + (h - 10)) * 2, x


url = "https://www.douyin.com/user/MS4wLjABAAAA6Ua9Cme28iLRyZeYHXJT1Z6T-qXu_A7NI6MElmPAWgI?from_tab_name=main"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

bro = webdriver.Chrome(executable_path=r"D:\code\wechat-app\chromedriver\chromedriver-win64\chromedriver.exe")
bro.get(url=url)
page = bro.page_source
new = etree.HTML(page)

bro.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
bro.execute_script("window.scrollTo(0, 0);")

iframe = bro.find_element(by=By.TAG_NAME, value='iframe')
bro.switch_to.frame(iframe)
later = etree.HTML(bro.page_source)
# 获取验证码背景图 340x211   552x344
beijingtu = later.xpath('//*[@id="captcha_verify_image"]/@src')
xiaohuakuai = later.xpath('//*[@id="captcha-verify_img_slide"]/@src')
# 获取大图片和小图片
with open('./beijing.jpeg', "wb") as f:
    f.write(requests.get(beijingtu[0]).content)
with open("./xiaohuakuai.png", "wb") as f:
    f.write(requests.get(xiaohuakuai[0]).content)

# 获取小图片的面积和周长
max_mianji, max_zhouchang, min_mianji, min_zhouchang, min_x = get_imag_pos("./xiaohuakuai.png",
                                                                           "./xiaohuakuai_huaguo.png")
# 通过 小图片面积范围判断滑动缺口位置
data = get_imag_pos('./beijing.jpeg', "./beijing_guaguo.jpeg", max_area=max_mianji, max_zhouchang=max_zhouchang,
                    min_area=min_mianji, min_zhouchang=min_zhouchang)
pos = data[-1]

bro.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
bro.execute_script("window.scrollTo(0, 0);")
anniu = bro.find_element(by=By.XPATH, value='//*[@id="vc_captcha_box"]/div/div/div[3]/div/div[2]/div[2]/div')

xiaojuli = anniu.location['x']
fignal = (pos / 552) * 340 - xiaojuli
print('fignal pos', fignal)

action = ActionChains(bro)
action.click_and_hold(anniu).perform()
move = 0
while move < fignal + 15:  # 还得多移动10
    x = random.randint(3, 10)
    move = move + x
    action.move_by_offset(x, 0).perform()
    time.sleep(0.5)
print('move', move)
action.release().perform()
# 滑动完成
bro.switch_to.default_content()

bro.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(20)
bro.execute_script("window.scrollTo(0, 0);")
cha = bro.find_element(by=By.XPATH, value='//*[@id="login-pannel"]/div/div/div[2]')
cha.click()

time.sleep(6)
bro.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
bro.execute_script("window.scrollTo(0, 0);")

result = bro.page_source
new_2 = etree.HTML(result)
base_ele = new_2.xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/ul/li')

all_href_data = []
for data in base_ele:
    href_data = data.xpath('./div/a/@href')
    all_href_data.append('https://www.douyin.com' + href_data[0])
bro.close()
bro = webdriver.Chrome(executable_path=r"D:\code\wechat-app\chromedriver\chromedriver-win64\chromedriver.exe")
# 再去单独请求这些
with open("./data_list.txt", "w", encoding="utf-8") as f:
    f.write(all_href_data)
