# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestLogoutGfzl(TestBase):
    """
    未登录  购房资料页面测试用例
    """
    def setUp(self) -> None:
        self.page_name = '/page/tools/ziliaomoban/ziliaomoban?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestLogoutGfzl, self).setUp()

    def test_01_click_preview_点击文件预览(self):
        """
        未登录，进入购房百科-购房资料页面，点击预览
        """
        self.find_element('view[class="downBtn disflex disflex-alignitems-center disflex-justifycontent-center"]').tap()

        # self.verifyPageName('/page/index/login')
        self.get_screenshot()

    def test_02_click_zygw_im_点击置业顾问IM(self):
        """
        V6.29.X: 1004929，点击置业顾问IM
        """
        self.find_element('view[class="link-button im"]').tap()

        self.get_screenshot()

    def test_03_click_zygw_im_点击置业顾问电话(self):
        """
        V6.29.X: 1004929，点击置业顾问电话
        """
        self.find_element('view[class="link-button call"]').tap()

        self.get_screenshot()

