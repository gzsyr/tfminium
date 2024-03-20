# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestLogin(TestBase):
    """
    登录
    """

    def setUp(self) -> None:
        self.classname = self.__class__.__name__
        super(TestLogin, self).setUp()

    def test_login_登录(self):
        """
        登录
        """
        print("当前页面路径", self.page.path)
        if self.page.path != "/page/index/mine":
            self.app.switch_tab("/page/index/mine?city=qz")
            self.delay(3)

        try:
            # 点击头像
            # self.find_element('image[class="headL login"]').tap()
            self.find_element('button[class="logincomponent--loginBtn"]').tap()


            # self.app.wait_for_page('/page/index/login')
            #
            # # 勾选协议
            # self.find_element('checkbox').tap()
            # self.delay(2)
            #
            # # 点击 微信授权登录
            # self.page.get_element('button').tap()
            self.delay(2)

            # 点击 允许
            self.input_value_by_mk('logout/phone_allow.png')

        except:
            print('没有找到退出登录状态的头像，说明已经登录')
            assert 1==0

        self.get_screenshot()

