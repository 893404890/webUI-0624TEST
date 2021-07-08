import pytest
import yaml

from po.main_page import MainPage


class TestAddDepartment:
    def setup(self):
        self.main=MainPage()
    def teardown(self):
        self.main.screenshot()
        self.main.close_driver()
    @pytest.mark.parametrize('name',yaml.safe_load(open('./datas/adddep.yaml',encoding='utf-8')))
    def test_add_department(self,name):
        result=self.main.goto_contact().add_department().sava_info(name).get_dep_name()
        assert name in result
