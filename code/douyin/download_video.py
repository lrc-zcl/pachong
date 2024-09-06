import requests
from lxml import etree
from selenium import webdriver
import time
import aiohttp
from selenium.webdriver.common.by import By
import asyncio

'''
根据下载链接  进行异步编程 下载图片
'''
bro = webdriver.Chrome(executable_path=r"D:\code\wechat-app\chromedriver\chromedriver-win64\chromedriver.exe")
# data = ['https://www.douyin.com/video/7273472752261123386', 'https://www.douyin.com/video/7255641057038290213',
#         'https://www.douyin.com/video/7269800024463232313', 'https://www.douyin.com/video/7410755470492814644',
#         'https://www.douyin.com/video/7410379084368284962', 'https://www.douyin.com/video/7410009151071325474',
#         'https://www.douyin.com/video/7409632772022652212', 'https://www.douyin.com/video/7409265186655178024',
#         'https://www.douyin.com/video/7408892498879302912', 'https://www.douyin.com/video/7408514148990012687',
#         'https://www.douyin.com/video/7408136395820125449', 'https://www.douyin.com/video/7407781494791490843',
#         'https://www.douyin.com/video/7407411185684991270', 'https://www.douyin.com/video/7407044762781420826',
#         'https://www.douyin.com/video/7406658906044239130', 'https://www.douyin.com/video/7406296178217733403',
#         'https://www.douyin.com/video/7405901048096853298', 'https://www.douyin.com/video/7405537484571987238',
#         'https://www.douyin.com/video/7404814183776128282', 'https://www.douyin.com/note/7405378179377958170', ]

data = ['https://www.douyin.com/video/7273472752261123386', 'https://www.douyin.com/video/7255641057038290213',
        'https://www.douyin.com/video/7269800024463232313', 'https://www.douyin.com/video/7410755470492814644',
        'https://www.douyin.com/video/7410379084368284962', 'https://www.douyin.com/video/7410009151071325474']

all_final_url = []
for index, i in enumerate(data):
    bro.get(i)
    bro.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(6)
    bro.execute_script("window.scrollTo(0, 0);")

    new_cha = bro.find_element(by=By.XPATH, value='//*[@id="login-pannel"]/div/div/div[2]')
    new_cha.click()

    bro.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    bro.execute_script("window.scrollTo(0, 0);")

    final = bro.find_element(by=By.XPATH,
                             value='//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[3]')
    final_data = final.get_attribute('src')
    print("获取了一次")

    all_final_url.append(final_data)
    print(final_data)


async def send_requests(index, url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url) as response:
            result = await response.read()
            with open(f'D:/data/douyin/{index}.mp4', "wb") as f:
                f.write(result)
                print(index)


async def main(all_final_url):
    task_list = []
    for index, data in enumerate(all_final_url):
        task_list.append(asyncio.create_task(send_requests(index=index, url=data)))

    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done)


asyncio.run(main(all_final_url=all_final_url))
