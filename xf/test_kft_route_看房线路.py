from base.test_base import TestBase


class TestKFTRoute(TestBase):
    """
    看房团路线页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/houseteam/detail?id=5&city=qz&isSecond=1'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestKFTRoute, self).setUp()

    def test_04_click_list_进入楼盘详情(self):
        """
        看房团路线页面，点击第一个楼盘，进入楼盘详情页
        """
        self.find_element('image[class="list-poster houseteam"]').tap()
        self.delay(5)
        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_03_click_first_回首页(self):
        """
        看房团路线页面，点击首页
        """
        self.find_element('image[class="toHomeBtn--img-style"]').tap()

        self.verifyPageName('/page/index/index')
        self.get_screenshot()

    def test_05_click_signup_立即报名(self):
        """
        看房团路线页面，点击立即报名,点击我已阅读小√，输入手机号，点击获取验证码
        """
        self.find_element('view[class="f30 white t-c"]').tap()

        self.verifyPageName('/page/houseteam/apply')
        self.get_screenshot()

    def test_01_click_activity_活动流程(self):
        """
        看房团路线页面，点击活动流程
        """
        self.find_element('view[class="activity"]').tap()

        self.verifyPageName('/page/houseteam/activity')
        self.get_screenshot()

    def test_02_click_declare_免责声明(self):
        """
        看房团路线页面，点击免责声明
        """
        self.find_element('view[class="declare"]').tap()
        self.delay(5)
        self.verifyPageName('/page/houseteam/declare')
        self.get_screenshot()

    def test_06_click_zphone_电话咨询(self):
        """
        看房团路线页面，点击电话咨询图标
        """
        self.find_element('icon[class="icon-tel mt15"]').tap()
        self.delay(1)

        self.verifyByScreenshot('xf/call.png')
