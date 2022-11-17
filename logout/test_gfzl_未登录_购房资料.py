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

    def test_click_preview_点击文件预览(self):
        """
        未登录，进入购房百科-购房资料页面，点击预览
        """
        self.find_element('view[class="downBtn disflex disflex-alignitems-center disflex-justifycontent-center"]').tap()

        self.verifyPageName('/page/index/login')
        self.get_screenshot()

