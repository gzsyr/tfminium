# add by zsy
from test.test_base import TestBase


class TestMyPost(TestBase):
    """
    进入我的帖子页面
    """
    def setUp(self) -> None:
        self.page_name = "/page/mine/myTopic/myTopic?city=qz"
        self.switch = False
        super(TestMyPost, self).setUp()

    def test_my_goto_postdetail(self):
        """
        点击我的帖子，进入帖子详情
        :return:
        """
        self.page.get_element('view[class="post_cont"]').tap()

    def test_my_click_quanzi(self):
        """
        点击我的帖子，进入点击圈子名称，进入圈子详情
        :return:
        """
        self.page.get_element('view[class="posttag flex tfAlignC"]').tap()