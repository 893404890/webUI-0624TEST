import allure
import pytest


from po.main_page import MainPage


class TestAddMember():
    def setup(self):
        self.main=MainPage()
    def teardown(self):
        self.main.close_driver()
    @pytest.mark.adduser
    @pytest.mark.parametrize('name,userid,phonenum',[('周栒0','testzx01','13645672951'),('周栒0','testzx02','13645673951')])
    @allure.feature('测试添加成员')
    def test_add_user(self,name,userid,phonenum):

        result=self.main.goto_contact().click_add_member().edit_member(name,userid,phonenum).get_member_name()
        assert name in result