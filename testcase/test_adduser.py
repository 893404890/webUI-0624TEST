import logging
import time
import allure
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.feature('企业微信web自动化测试')
class Test_add:

    @allure.story('企业微信添加用户')
    @allure.title('添加{getuserinfo}')
    @pytest.mark.adduser
    def setup(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            # 获取企业微信cookies
            with open('./datas/wechcookies.yaml', encoding='UTF-8') as f:
                    yaml_date = yaml.safe_load(f)
            for cookie in yaml_date:
                    self.driver.add_cookie(cookie)
            print(yaml_date)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            self.driver.maximize_window()
            self.driver.find_element(By.ID, 'menu_contacts').click()

    def teardown(self):
        self.driver.quit()
    def test_adduser01(self,getuserinfo):
        data=getuserinfo

        with allure.step('点击添加用户'):

            self.driver.implicitly_wait(10)
            self.driver.find_elements_by_link_text("添加成员")[0].click()
            time.sleep(2)
        with allure.step('输入用户名字'):

            self.driver.find_element(By.ID,'username').send_keys(data[0])
        with allure.step('输入用户别名'):

            self.driver.find_element(By.ID,'memberAdd_english_name').send_keys(data[1])
        with allure.step('输入账号'):
            self.driver.find_element(By.ID,'memberAdd_acctid').send_keys(data[2])
        with allure.step('输入职务'):
            self.driver.find_element(By.ID,'memberAdd_title').send_keys(data[3])
        with allure.step('输入邮箱'):
            self.driver.find_element(By.ID,'memberAdd_mail').send_keys(data[4])
        with allure.step('保存并添加用户'):
            logging.info("保存添加并保存用户")
            self.driver.execute_script("document.documentElement.scrollTop=10000")
            time.sleep(2)
            self.driver.find_element(By.XPATH,'//div[@class="member_colRight_operationBar ww_operationBar"][2]/a[2]').click()
            time.sleep(2)
        with allure.step('判断是否添加成功'):
            a=self.driver.find_elements_by_link_text("添加成员")[0].text
            assert a=='添加成员'