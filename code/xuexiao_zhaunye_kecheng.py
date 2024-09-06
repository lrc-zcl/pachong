import time
from selenium import webdriver
import requests
from lxml import etree
from selenium.webdriver.common.by import By


# bro = webdriver.Chrome(executable_path="../chromedriver/chromedriver-win64/chromedriver.exe")
# bro.get("https://www.gaokao.cn/")


class xuexiao():
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path="../chromedriver/chromedriver-win64/chromedriver.exe")
        self.bro.get("https://www.gaokao.cn/")
        self.page_result = self.bro.page_source
        self.tree = etree.HTML(self.page_result)
        print("初始化完成！！")

    def ele_data(self, path):
        data = self.tree.xpath(path)
        return data

    def find_click(self, xpath_data):
        self.find = self.bro.find_element(by=By.XPATH, value=xpath_data)
        self.find.click()

    def find_send_data(self, path_data, senddata):
        self.find_send = self.bro.find_element(by=By.XPATH, value=path_data)
        self.find_send.send_keys(senddata)

    def denglu(self):
        self.find_click('//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[3]/span')  # 点击登录
        self.find_click(
            '//*[@id="dialog_package"]/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]')  # 点击密码登录

    def zhanghao_mima(self):
        self.find_send_data(
            '//*[@id="dialog_package"]/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/input', "13137741301")
        self.find_send_data(
            '//*[@id="dialog_package"]/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/input', "Lrc130530")

    def final_denglu(self):
        self.find_click(
            '//*[@id="dialog_package"]/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[5]/div[1]/label/span[1]/input')
        self.find_click('//*[@id="dialog_package"]/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[4]')

    def chadaxue_diqu_zhuanke(self):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        chadauxe = WebDriverWait(self.bro, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/div/div[1]/div[6]/div/div[3]/div'))
        )
        chadauxe.click()

        # time.sleep(5)
        # self.find_click('//*[@id="root"]/div/div[1]/div/div/div[2]/div/div[1]/div[6]/div/div[3]/div')
        self.find_click(
            '//*[@id="root"]/div/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/div/div[4]/div[2]/span[2]')
        self.find_click(
            '//*[@id="root"]/div/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/div/div[6]/div[2]/span[3]')

    def signalxuexiao(self):
        self.find_click(
            '//*[@id="root"]/div/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/h3/em')
        self.find_click('//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[3]/div/div[4]/div/div[2]/div[4]')
        self.find_click('//*[@id="setUpMajorEle"]/div[2]/div/table/tbody/tr[1]/td[7]/span')

        self.zhuanyeinfo = self.ele_data(
            '//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[3]/div/div[4]/div/div[3]/div[1]/div/div/div[1]//text()')
        return self.zhuanyeinfo

    def funmain(self):
        self.denglu()
        self.zhanghao_mima()
        self.final_denglu()
        self.chadaxue_diqu_zhuanke()

        return self.signalxuexiao()


if __name__ == "__main__":
    xuexiao_1 = xuexiao()
    data = xuexiao_1.funmain()
    print(data)
