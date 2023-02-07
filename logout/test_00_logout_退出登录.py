# -*-coding:utf-8-*-
import minium

from base.test_base import TestBase


class TestLogout(TestBase):
    """
    退出登录
    """
    def setUp(self) -> None:
        self.classname = self.__class__.__name__
        super(TestLogout, self).setUp()

    def test_logout_登出(self):
        """
        退出登录
        """
        print("当前页面路径", self.page.path)
        count = 0
        while self.page.path != "/page/index/mine" and count < 3:
            self.app.switch_tab("/page/index/mine?city=qz")
            self.delay(3)
            count += 1

        # 点击头像
        try:
            if self.get_third_title() == '置业顾问':
                self.page.get_element('image[class="avatar"]').tap()
            else:
                self.page.get_element('image[class="headL"]').tap()
            self.app.wait_for_page('/page/mine/myinfo/myinfo')
            # 点击确定“退出登录”
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[class="login-out"]').tap()
            self.app.restore_wx_method("showModal")
            self.delay(2)
            self.capture("确定")
            self.native.handle_modal("取消", "确定")
        except minium.MiniElementNotFoundError:
            print('没有找到登录状态的头像，说明已经退出登录')

        self.get_screenshot()
        return
