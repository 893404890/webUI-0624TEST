import os
import time

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    #初始化driver
    def __init__(self,driver_base:WebDriver = None):
        if driver_base==None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            # 获取企业微信cookies
            with open('./datas/wechcookies.yaml', encoding='UTF-8') as f:
                yaml_date = yaml.safe_load(f)
            for cookie in yaml_date:
                self.driver.add_cookie(cookie)
            # print(yaml_date)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            self.driver.maximize_window()
        else:
            self.driver=driver_base
    #查找元素
    def find(self,loc):
        self.driver.find_element(*loc)
    #查找元素并输入值
    def sendkeys(self,loc,v):
        self.driver.find_element(*loc).send_keys(v)
    #查找元素并点击
    def find_click(self,loc):
        self.driver.find_element(*loc).click()
    #显示等待
    def wait(self,_time):
        self.driver.implicitly_wait(_time)

    #关闭浏览器
    def close_driver(self):
        self.driver.close()

    #遍历查找
    def finds(self,loc):
        return  self.driver.find_elements(*loc)

    #截图
    def screenshot(self):
        filedir = "./screenshot/test.png"

        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        return screen_name

