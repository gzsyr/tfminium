from base.test_base import TestBase


class TestTfqMyHuaTi(TestBase):
    """
    我的话题页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/mine/myHuati/myHuati?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqMyHuaTi, self).setUp()
        print("TestTfqMyHuaTi setup")

    def test_click_点击话题(self):
        """
        我的话题页面，点击话题
        """
        self.page.get_element('view[class="title"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

