from base.test_base import TestBase


class TestTfqQuanZi(TestBase):
    """
    圈子广场
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/huati/huatiSquare?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqQuanZi, self).setUp()
        print("TestQuanZi  Setup")

    def test_click_quanzi_圈子详情(self):
        """
        圈子广场，点击圈子，进入圈子详情页
        """
        self.page.get_element('view[class="hotSearch"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_fav_关注按钮(self):
        """
        圈子广场，点击圈子列表第一条，点击”关注“按钮变为“已关注”，或（“已关注”）点击后进入圈子详情页
        """
        self.find_element('view[class="item"]/view[data-id="751"]').tap()

        self.get_screenshot()


