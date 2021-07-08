import logging
import time

import allure
from selenium.webdriver.common.by import By

from po.basepage import BasePage
#通讯录页面
class ContactPage(BasePage):
    _ADDMEMBER = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")

    _NAMES = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _DEPNAMES=(By.CSS_SELECTOR,'.jstree-anchor')
    _ADD = (By.CSS_SELECTOR, '.js_create_dropdown')
    _DEP = (By.CSS_SELECTOR, '.js_create_party')
    #点击添加成员
    def click_add_member(self):
        from po.add_member_bage import AddMemberPage
        logging.info('添加成员')
        with allure.step('点击添加成员'):

            self.find_click(self._ADDMEMBER)
            time.sleep(3)
            return AddMemberPage(self.driver)
    #获取成员信息，进行返回
    def get_member_name(self):
        logging.info('获取成员信息')
        time.sleep(3)
        name_list=[]
        eles=self.finds(self._NAMES)

        for ele in eles:
            name_list.append(ele.get_attribute("title"))
        return name_list
    #点击添加部门
    def add_department(self):
        from po.new_department import New_Department
        with allure.step('点击加号'):
            self.find_click(self._ADD)
            self.wait(2)
        with allure.step('点击添加部门'):
            self.find_click(self._DEP)
            self.wait(2)
        return New_Department(self.driver)
    #获取部分名字
    def get_dep_name(self):
         eles=self.finds(self._DEPNAMES)
         dep_list=[]
         for v in eles:
             dep_list.append(v.get_attribute('text'))
         return dep_list

