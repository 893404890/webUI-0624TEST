#新建部分页面
import logging
from time import sleep

import allure
from selenium.webdriver.common.by import By

from po.basepage import BasePage




class New_Department(BasePage):
    #创建部门

    _DENAME=(By.NAME,'name')
    _CHO=(By.CSS_SELECTOR,'.js_toggle_party_list')
    _CONFIM=(By.CSS_SELECTOR,'.ww_dialog_foot a:nth-child(1)')
    _CANCLE=(By.CSS_SELECTOR,'.ww_dialog_foot a:nth-child(2)')
    _FATHER=(By.XPATH,'//div[@class="qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container"]/div/ul/li/a/i')
    #部门信息
    def fill_info(self,name):

        with allure.step('输入部门名称'):
            self.sendkeys(self._DENAME,name)
        with allure.step('选择部门上级'):
            self.find_click(self._CHO)
            self.find_click(self._FATHER)


    #取消操作
    def cancel_sava(self,name):
        from po.contact_page import ContactPage
        with allure.step('点击取消'):
            self.fill_info(name)
            self.find_click(self._CANCLE)
            self.wait(2)
        return ContactPage(self.driver)

    #保存部分信息
    def sava_info(self,name):
        from po.contact_page import ContactPage
        logging.info(f'添加部门{name}')

        with allure.step('点击保存'):
            self.fill_info(name)
            self.find_click(self._CONFIM)
            sleep(2)
        return ContactPage(self.driver)