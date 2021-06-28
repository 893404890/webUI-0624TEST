import time

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


def w_cookies():

    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
    driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
    cookies = driver.get_cookies()
    with open('./datas/wechcookies.yaml', "w", encoding='UTF-8') as f:
        yaml.dump(cookies, f)

# @pytest.fixture(autouse=True)
def login():
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 获取企业微信cookies
        with open('../datas/wechcookies.yaml', encoding='UTF-8') as f:
            yaml_date = yaml.safe_load(f)
        for cookie in yaml_date:
            driver.add_cookie(cookie)
        print(yaml_date)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.maximize_window()
        driver.find_element(By.ID, 'menu_contacts').click()
        yield
        driver.quit()
def getUserInfoData():
    with open('./datas/adduser.yaml',encoding='UTF-8') as f:
        data=yaml.safe_load(f)
    return data
#将数据保存于变量，以免频繁读取yaml文件
data=getUserInfoData()
# 返回用户信息
@pytest.fixture(params=data)
def getuserinfo(request):

    return request.param
