# add by zsy
from base.test_base import TestBase


class TestMineFbs(TestBase):
    """
    我的问答页
    """
    def setUp(self) -> None:
        self.page_name = '/fbs/mine/mine?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestMineFbs, self).setUp()

    def test_goto_ask_detail_进入问答详情(self):
        """
        我的问答页面，点击第一个问答，进入问答详情页
        """
        self.page.get_element('view[class="question-text ml30"]').tap()

        self.verifyPageName('/fbs/detail/detail')
        self.get_screenshot()