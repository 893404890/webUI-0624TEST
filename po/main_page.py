import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


from po.basepage import BasePage
#通讯录页面
class MainPage(BasePage):
    #迪点击通讯录
    _contact=(By.XPATH,'//a[@id="menu_contacts"]/span')
    def goto_contact(self):
        from po.contact_page import ContactPage
        with allure.step('点击通讯录'):
            self.find_click(self._contact)
            time.sleep(2)
            return ContactPage(self.driver)