import logging
import time

import allure
from selenium.webdriver.common.by import By
#添加成员页面
from po.basepage import BasePage

class AddMemberPage(BasePage):
    #页面元素
    #添加成员
    _name=(By.ID,'username')
    _userid=(By.ID,'memberAdd_acctid')
    _phonenum=(By.ID,'memberAdd_phone')
    _save=(By.CSS_SELECTOR,'.js_btn_save')
    def edit_member(self,name,userid,phonenum):
        from po.contact_page import ContactPage

        logging.info('添加成员')
        self.sendkeys(self._name,name)
        self.sendkeys(self._userid,userid)
        self.sendkeys(self._phonenum,phonenum)
        with allure.step('点击保存'):
            self.find_click(self._save)
            time.sleep(3)
        return ContactPage(self.driver)
