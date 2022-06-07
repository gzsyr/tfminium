# add by zzh  淘房圈正在热议页面
from test.test_base import TestBase


class TestReYi(TestBase):
    """
    淘房圈正在热议页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/tieziList/tieziList?city=qz"
        self.switch = False
        super(TestReYi, self).setUp()
        print("TestReYi  Setup")

    def test_click_title(self):
        """
        正在热议页面，点击帖子标题
        """
        self.page.get_element('view[class="hotCont list-desc"]').tap()

    def test_click_postbt(self):
        """
        正在热议页面，点击底部发帖入口
        """
        self.page.get_element('view[class="write_Post tfFlex tfAlignC tfFlexC"]').tap()

