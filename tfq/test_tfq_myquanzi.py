# add by zzh

from base.test_base import TestBase


class TestTfqMyQuzi(TestBase):
    """
    我的圈子页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/mine/myQuanzi/myQuanzi?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqMyQuzi, self).setUp()
        print("TestMyQuzi setup")

    def test_click(self):
        """
        我的圈子页面，点击圈子
        """
        self.page.get_element('view[class="title tfline2"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

