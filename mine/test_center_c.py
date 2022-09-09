# -*- coding: utf-8 -*- 
# @Time : 2022/7/21 13:44 
# @Author : zcm 
# @File : test_center_c.py 
# @desc:
from ddt import data, ddt

from base.test_mine import TestMine

@ddt
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
        self.classname = self.__class__.__name__
        super(TestCenterC, self).setUp()

    def test_01_C_click_avatar(self):
        """
        C端用户个人中心页面，点击头像
        """
        self.page.get_element('view[class="avatar"]').tap()

        self.verifyPageName('/page/mine/myinfo/myinfo')
        self.get_screenshot()

    def test_02_C_click_yaohao(self):
        """
        C端用户个人中心页面，点击我的摇号
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的摇号').tap()

        self.verifyPageName('/page/mine/myLottery/myLottery')
        self.get_screenshot()

    def test_03_C_click_zuji(self):
        """
        C端用户个人中心页面，点击我的足迹
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的足迹').tap()

        self.verifyPageName('/page/mine/myFootPrint/myFootPrint')
        self.get_screenshot()

    def test_04_C_click_shoucang(self):
        """
        C端用户个人中心页面，点击我的收藏
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的收藏').tap()

        self.verifyPageName('/page/mine/myCollect/myCollect')
        self.get_screenshot()

    def test_05_C_click_wenda(self):
        """
        C端用户个人中心页面，点击我的问答
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的问答').tap()

        self.verifyPageName('/fbs/mine/mine')
        self.get_screenshot()

    def test_06_C_click_tfq_qz(self):
        """
        C端用户个人中心页面，点击我的圈子
        """
        self.page.get_element('view[class="name"]', inner_text='我的圈子').tap()

        self.verifyPageName('/page/mine/myQuanzi/myQuanzi')
        self.get_screenshot()

    def test_07_C_click_tfq_ht(self):
        """
        C端用户个人中心页面，点击我的话题
        """
        self.page.get_element('view[class="name"]', inner_text='我的话题').tap()

        self.verifyPageName('/page/mine/myHuati/myHuati')
        self.get_screenshot()

    def test_08_C_click_tfq_tz(self):
        """
        C端用户个人中心页面，点击我的帖子
        """
        self.page.get_element('view[class="name"]', inner_text='我的帖子').tap()

        self.verifyPageName('/page/mine/myTopic/myTopic')
        self.get_screenshot()

    def test_09_C_click_tfq_pl(self):
        """
        C端用户个人中心页面，点击我的评论
        """
        self.page.get_element('view[class="name"]', inner_text='我的评论').tap()

        self.verifyPageName('/page/mine/myComment/myComment')
        self.get_screenshot()

    def test_10_C_click_ad(self):
        """
        C端用户个人中心页面，C端用户点击广告
        """
        self.page.get_element('image[class="ad"]').tap()

        self.verifyPageName('/page/index/webview')
        self.get_screenshot()

    @data(0, 1, 2, 3, 4)
    def test_11_C_click_tool_icon1(self, index):
        """
        C端用户个人中心页面，C端用户点击常用工具
        """
        self.page.get_element(f'view[class="tab-item"][data-index="{index}"]').tap()

        self.get_screenshot()

    def test_16_C_click_more_rz(self):
        """
        C端用户个人中心页面，C端用户点击置业顾问入驻
        """
        self.page.get_element('view[id="businessRegister"]').tap()

        self.verifyPageName('/page/business/checkzygw')
        self.get_screenshot()

    def test_17_C_click_more_ys(self):
        """
        C端用户个人中心页面，C端用户点击隐私权政策
        """
        self.page.get_element('view[id="privacyPolicy"]').tap()

        self.verifyPageName('/page/index/notice')
        self.get_screenshot()

    def test_18_C_click_more_fk(self):
        """
        C端用户个人中心页面，C端用户点击意见反馈
        """
        self.page.get_element('view[id="yjfk"]').tap()

        self.verifyPageName('/page/mine/wtfk/wtfk')
        self.get_screenshot()

    def test_19_C_click_more_icon4(self):
        """
        C端用户个人中心页面，C端用户点击我的红包
        """
        self.page.get_element('view[id="myHongBao"]').tap()

        self.verifyPageName('/page/mine/wdhb/wdhb')
        self.get_screenshot()

    def test_20_C_click_notice(self):
        """
        C端用户点击365淘房用户服务协议
        """
        self.page.get_element('view[id="notice"]').tap()

        self.verifyPageName('/page/index/notice')
        self.get_screenshot()

