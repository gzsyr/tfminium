# add by zsy
from base.test_base import TestBase


class TestMyComments(TestBase):
    """
    进入我的评论页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/mine/myComment/myComment?city=qz"
        self.switch = False

        super(TestMyComments, self).setUp()
        print("TestMyComments setup")

    def is_comment_exist(self):
        """
        页面是否有评论数据
        :return:
        """
        return self.page.element_is_exists('view[class="post_cont"]')

    def test_goto_more_post(self):
        """
        点击“更多话题“，这个用例在没有评论的时候有效
        :return:
        """
        if self.is_comment_exist():
            print("页面有评论数据，此用例直接pass")
        else:
            self.page.get_element('view[class="morewall"]').tap()

    def test_goto_first_post(self):
        """
        点击热帖墙的第一个帖子，这个用例在没有评论的时候有效
        :return:
        """
        if self.is_comment_exist():
            print("页面有评论数据，此用例直接pass")
        else:
            self.page.get_element('view[class="hotCont list-desc"]').tap()

    def test_click_zanicon(self):
        """
        点击第一个评论的点赞图标
        :return:
        """
        if self.is_comment_exist():
            self.page.get_element('view[class="laud-btn"]').tap()
        else:
            print("页面无评论数据，此用例直接pass")

    def test_click_replyBtn(self):
        """
        点击第一个评论的回复按钮
        :return:
        """
        if self.is_comment_exist():
            self.page.get_element('view[class="replyBtn"]').tap()
        else:
            print("页面无评论数据，此用例直接pass")

    def test_goto_commentdetail(self):
        """
        点击第一个评论内容，进入详情
        :return:
        """
        if self.is_comment_exist():
            self.page.get_element('view[class="post_cont"]').tap()
        else:
            print("页面无评论数据，此用例直接pass")

    def test_goto_housedetail(self):
        """
        点击第一个评论内容的楼盘名称右边箭头，进入新房详情页
        :return:
        """
        if self.is_comment_exist():
            self.page.get_element('image[class="lp_icon disflex-flex-shrink-0"]').tap()
        else:
            print("页面无评论数据，此用例直接pass")

