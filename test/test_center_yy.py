# -*- coding: utf-8 -*- 
# @Time : 2022/7/21 13:44 
# @Author : zcm 
# @File : test_center_c.py 
# @desc:

from test.test_base import TestBase
from common import delay
from test.test_mine import TestMine


class TestCenterYY(TestMine):
    """
    个人中心页，运营用户
    头像入口，上方3入口，淘房圈板块5入口，广告入口，常用工具板块5入口，更多服务板块4入口，协议入口
    全部使用的class定位
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        切换到运营用户
        :return:
        """
        super(TestCenterYY, cls).setUpClass()
        cls().change_yy()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/page/index/mine"
        self.switch = True
        super(TestCenterYY, self).setUp()
        delay(2)

    def test_01_yy_click_avatar(self):
        """
        运营用户点击头像
        :return:
        """
        self.page.get_element('view[class="avatar"]').tap()

    def test_02_yy_click_icon1(self):
        """
        运营用户点击上方第一个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-icon"]')
        e[0].tap()

    def test_03_yy_click_icon2(self):
        """
        运营用户点击上方第二个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-icon"]')
        e[1].tap()

    def test_04_yy_click_icon3(self):
        """
        运营用户点击上方第三个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-icon"]')
        e[2].tap()

    def test_05_yy_click_tfq_icon1(self):
        """
        运营用户点击淘房圈板块第1个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[0].tap()

    def test_06_yy_click_tfq_icon2(self):
        """
        运营用户点击淘房圈板块第2个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[1].tap()

    def test_07_yy_click_tfq_icon3(self):
        """
        运营用户点击淘房圈板块第3个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[2].tap()

    def test_08_yy_click_tfq_icon4(self):
        """
        运营用户点击淘房圈板块第4个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[3].tap()

    def test_09_yy_click_tfq_icon5(self):
        """
        运营用户点击淘房圈板块第5个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[4].tap()

    def test_10_yy_click_ad(self):
        """
        运营用户点击广告
        :return:
        """
        self.page.get_element('image[class="ad"]').tap()

    def test_11_yy_click_tool_icon1(self):
        """
        运营用户点击常用工具板块第1个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-small-icon"]')
        e[0].tap()

    def test_12_yy_click_tool_icon2(self):
        """
        运营用户点击常用工具板块第2个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-small-icon"]')
        e[1].tap()

    def test_13_yy_click_tool_icon3(self):
        """
        运营用户点击常用工具板块第3个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-small-icon"]')
        e[2].tap()

    def test_14_yy_click_tool_icon4(self):
        """
        运营用户点击常用工具板块第4个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-small-icon"]')
        e[3].tap()

    def test_15_yy_click_tool_icon5(self):
        """
        运营用户点击常用工具板块第5个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-small-icon"]')
        e[4].tap()

    def test_16_yy_click_more_icon1(self):
        """
        运营用户点击更多服务板块第1个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[5].tap()

    def test_17_yy_click_more_icon2(self):
        """
        运营用户点击更多服务板块第2个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[6].tap()

    def test_18_yy_click_more_icon3(self):
        """
        运营用户点击更多服务板块第3个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[7].tap()

    def test_19_yy_click_more_icon4(self):
        """
        运营用户点击更多服务板块第4个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[8].tap()

    def test_20_yy_click_notice(self):
        """
        运营用户点击365淘房用户服务协议
        :return:
        """
        self.page.get_element('view[class="notice"]').tap()