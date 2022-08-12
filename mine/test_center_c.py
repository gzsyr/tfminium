# -*- coding: utf-8 -*- 
# @Time : 2022/7/21 13:44 
# @Author : zcm 
# @File : test_center_c.py 
# @desc:

from base.test_mine import TestMine


class TestCenterC(TestMine):
    """
    个人中心页，C端用户
    头像入口，上方3入口，淘房圈板块5入口，广告入口，常用工具板块5入口，更多服务板块4入口，协议入口
    全部使用的class定位
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        切换到C端用户
        :return:
        """
        super(TestCenterC, cls).setUpClass()
        cls().change_C()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/page/index/mine"
        self.switch = True
        super(TestCenterC, self).setUp()

    def test_01_C_click_avatar(self):
        """
        C端用户点击头像
        :return:
        """
        self.page.get_element('view[class="avatar"]').tap()

    def test_02_C_click_icon1(self):
        """
        C端用户点击上方第一个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-icon"]')
        e[0].tap()

    def test_03_C_click_icon2(self):
        """
        C端用户点击上方第二个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-icon"]')
        e[1].tap()

    def test_04_C_click_icon3(self):
        """
        C端用户点击上方第三个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-icon"]')
        e[2].tap()

    def test_05_C_click_tfq_icon1(self):
        """
        C端用户点击淘房圈板块第1个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[0].tap()

    def test_06_C_click_tfq_icon2(self):
        """
        C端用户点击淘房圈板块第2个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[1].tap()

    def test_07_C_click_tfq_icon3(self):
        """
        C端用户点击淘房圈板块第3个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[2].tap()

    def test_08_C_click_tfq_icon4(self):
        """
        C端用户点击淘房圈板块第4个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[3].tap()

    def test_09_C_click_tfq_icon5(self):
        """
        C端用户点击淘房圈板块第5个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[4].tap()

    def test_10_C_click_ad(self):
        """
        C端用户点击广告
        :return:
        """
        self.page.get_element('image[class="ad"]').tap()

    def test_11_C_click_tool_icon1(self):
        """
        C端用户点击常用工具板块第1个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-small-icon"]')
        e[0].tap()

    def test_12_C_click_tool_icon2(self):
        """
        C端用户点击常用工具板块第2个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-small-icon"]')
        e[1].tap()

    def test_13_C_click_tool_icon3(self):
        """
        C端用户点击常用工具板块第3个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-small-icon"]')
        e[2].tap()

    def test_14_C_click_tool_icon4(self):
        """
        C端用户点击常用工具板块第4个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-small-icon"]')
        e[3].tap()

    def test_15_C_click_tool_icon5(self):
        """
        C端用户点击常用工具板块第5个图标
        :return:
        """
        e = self.page.get_elements('view[class="tab-small-icon"]')
        e[4].tap()

    def test_16_C_click_more_icon1(self):
        """
        C端用户点击更多服务板块第1个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[5].tap()

    def test_17_C_click_more_icon2(self):
        """
        C端用户点击更多服务板块第2个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[6].tap()

    def test_18_C_click_more_icon3(self):
        """
        C端用户点击更多服务板块第3个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[7].tap()

    def test_19_C_click_more_icon4(self):
        """
        C端用户点击更多服务板块第4个图标
        :return:
        """
        e = self.page.get_elements('image[class="ico"]')
        e[8].tap()

    def test_20_C_click_notice(self):
        """
        C端用户点击365淘房用户服务协议
        :return:
        """
        self.page.get_element('view[class="notice"]').tap()