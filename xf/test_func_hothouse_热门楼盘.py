# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestFuncHothouse(TestBase):
    """
    热门楼盘页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/juhe/juhe?objid=107&city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncHothouse, self).setUp()

    def test_001_goto_housedetail(self):
        """
        点击第一个楼盘进入楼盘详情页
        """
        self.find_element('view[class="commonNewHouseLi-l"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_002_click_im(self):
        """
        V6.23.X: “在线咨询”按钮
        """
        self.find_element('view[class="consult_imicon"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_003_click_call(self):
        """
        V6.23.X: “拨打电话”按钮
        """
        self.find_element('view[class="consult_phoneicon"]').tap()

        self.get_screenshot()
