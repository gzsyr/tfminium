# -*-coding:utf-8-*-
from ddt import ddt, data, unpack

from base.test_base import TestBase


@ddt
class TestEsfMyTrack(TestBase):
    """
    我的足迹，涉及到二手房部分的
    """
    def setUp(self) -> None:
        self.page_name = '/page/mine/myFootPrint/myFootPrint?city=nj'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestEsfMyTrack, self).setUp()

    @data(('二手房', 2), ('租房', 3))
    @unpack
    def test_01_切换TAB(self, name, num):
        """
        V6.21.X（esf）：1003956，我的足迹页面，切换tab
        """
        self.page.get_element('view[data-id="%d"]' % num, inner_text=name).tap()

        self.get_screenshot()

    def test_02_click_点击二手房源(self):
        """
        V6.21.X（esf）：1003956，我的足迹页面，点击二手房源
        """
        self.page.get_element('view[data-id="2"]', inner_text='二手房').tap()
        self.delay(2)

        try:
            self.page.get_element('view[class="sellItem--flex_1"]').tap()

            self.verifyPageName('/esf/sell/rent/r_detail/detail')
        except:
            print('无二手房的足迹')

        self.get_screenshot()

    def test_04_click_点击租房房源(self):
        """
        V6.21.X（esf）：1003956，我的足迹页面，点击租房房源
        """
        self.page.get_element('view[data-id="3"]', inner_text='租房').tap()
        self.delay(2)

        try:
            self.page.get_element('view[class="rentItem--flex_1"]').tap()

            self.verifyPageName('/esf/sell/rent/detail/detail')
        except:
            print('无租房的足迹')

        self.get_screenshot()
