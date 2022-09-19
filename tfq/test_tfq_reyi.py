# add by zzh  淘房圈正在热议页面
from base.test_base import TestBase


class TestTfqReYi(TestBase):
    """
    淘房圈正在热议页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/tieziList/tieziList?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqReYi, self).setUp()
        print("TestReYi  Setup")

    def test_click_title(self):
        """
        正在热议页面，点击帖子标题
        """
        self.page.get_element('view[class="hotCont list-desc"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_postbt(self):
        """
        正在热议页面，点击底部发帖入口
        """
        self.page.get_element('view[class="write_Post tfFlex tfAlignC tfFlexC"]').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def test_click_wpbtn(self):
        """
        正在热议页面，点击底部“发布”按钮
        """
        self.page.get_element('view[class="send_Post"]').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()


