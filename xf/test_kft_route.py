from base.test_base import TestBase


class TestKFTRoute(TestBase):
    """
    看房团路线页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/houseteam/detail?id=8359&city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestKFTRoute, self).setUp()

    def test_click_list(self):
        """
        看房团路线页面，点击第一个楼盘，进入楼盘详情页
        """
        self.page.get_element('image[class="list-poster houseteam"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_click_first(self):
        """
        看房团路线页面，点击首页
        """
        self.page.get_element('image[class="toHomeBtn--img-style"]').tap()

        self.verifyPageName('/page/index/index')
        self.get_screenshot()

    def test_click_signup(self):
        """
        看房团路线页面，点击立即报名,点击我已阅读小√，输入手机号，点击获取验证码
        """
        self.page.get_element('view[class="f30 white t-c"]').tap()

        self.verifyPageName('/page/houseteam/apply')
        self.get_screenshot()

    def test_click_activity(self):
        """
        看房团路线页面，点击活动流程
        """
        self.page.get_element('view[class="activity"]').tap()

        self.verifyPageName('/page/houseteam/activity')
        self.get_screenshot()

    def test_click_declare(self):
        """
        看房团路线页面，点击免责声明
        """
        self.page.get_element('view[class="declare"]').tap()

        self.verifyPageName('/page/houseteam/declare')
        self.get_screenshot()

    def test_click_zphone(self):
        """
        看房团路线页面，点击电话咨询图标
        """
        self.page.get_element('icon[class="icon-tel mt15"]').tap()
        self.delay(1)

        self.verifyByScreenshot('xf/call.png')
