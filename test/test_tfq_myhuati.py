from test.test_base import TestBase


class TestMyHuaTi(TestBase):
    """
    我的话题页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/mine/myHuati/myHuati?city=qz"
        self.switch = False
        super(TestMyHuaTi, self).setUp()
        print("TestMyHuaTi setup")

    def test_click(self):
        """
        我的话题页面，点击话题
        """
        self.page.get_element('view[class="title"]').tap()

