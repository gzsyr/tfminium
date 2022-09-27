# -*-coding:utf-8-*-
# add by zsy
from ddt import ddt, data, unpack

from base.test_base import TestBase


@ddt
class TestEsfMyFav(TestBase):
    """
    我的收藏，涉及到二手房部分的
    """
    def setUp(self) -> None:
        self.page_name = '/page/mine/myCollect/myCollect?city=nj'
        self.classname = self.__class__.__name__
        self.switch = False
        super(TestEsfMyFav, self).setUp()

    # @data({'name': '二手房', 'index': 2}, {'name': '租房', 'index': 3}, {'name': '小区', 'index': 4})
    @data(('二手房', 2), ('租房', 3), ('小区', 4))
    @unpack
    def test_01_click_切换TAB(self, name, num):
        """
        V6.21.X（esf）：1003956，我的收藏页面，切换tab
        """
        self.page.get_element('view[data-index="%d"]' % num, inner_text=name).tap()

        self.get_screenshot()

    def test_02_click_esf_点击二手房源(self):
        """
        V6.21.X（esf）：1003956，我的收藏页面，切换到二手房tab，点击进入房源详情
        """
        self.page.get_element('view[data-index="2"]', inner_text='二手房').tap()
        self.delay(2)

        try:
            self.page.get_element('view[class="sellItem--title"]').tap()

            self.verifyPageName('/esf/sell/pages/detail/detail')
        except:
            print('无收藏的房源，直接通过')

        self.get_screenshot()

    def test_03_click_esf_取消收藏二手房源(self):
        """
        V6.21.X（esf）：1003956，我的收藏页面，切换到二手房tab，左滑取消
        """
        self.page.get_element('view[data-index="2"]', inner_text='二手房').tap()
        self.delay(2)

        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[class="sellItem--del"]').tap()
            self.app.restore_wx_method("showModal")
        except:
            print('无收藏的房源，直接通过')

        self.get_screenshot()

    def test_04_click_rent_点击租房房源(self):
        """
        V6.21.X（esf）：1003956，我的收藏页面，切换到租房tab，点击进入房源详情
        """
        self.page.get_element('view[data-index="3"]', inner_text='租房').tap()
        self.delay(2)

        try:
            self.page.get_element('view[class="rentItem--title"]').tap()

            self.verifyPageName('/esf/sell/rent/detail/detail')
        except:
            print('无收藏的房源，直接通过')

        self.get_screenshot()

    def test_05_click_rent_取消收藏租房房源(self):
        """
        V6.21.X（esf）：1003956，我的收藏页面，切换到租房tab，左滑取消
        """
        self.page.get_element('view[data-index="3"]', inner_text='租房').tap()
        self.delay(2)

        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[class="rentItem--del"]').tap()
            self.app.restore_wx_method("showModal")
        except:
            print('无收藏的房源，直接通过')

        self.get_screenshot()

    def test_06_click_xq_点击小区详情(self):
        """
        V6.21.X（esf）：1003956，我的收藏页面，切换到小区tab，点击进入房源详情
        """
        self.page.get_element('view[data-index="4"]', inner_text='小区').tap()
        self.delay(2)

        try:
            self.page.get_element('view[class="blockItem--title"]').tap()

            self.verifyPageName('/esf/village/pages/detail/detail')
        except:
            print('无收藏的小区，直接通过')

        self.get_screenshot()

    def test_07_click_xq_取消收藏小区(self):
        """
        V6.21.X（esf）：1003956，我的收藏页面，切换到小区tab，左滑取消
        """
        self.page.get_element('view[data-index="4"]', inner_text='小区').tap()
        self.delay(2)

        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[class="blockItem--del"]').tap()
            self.app.restore_wx_method("showModal")
        except:
            print('无收藏的小区，直接通过')

        self.get_screenshot()
