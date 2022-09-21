# add by zsy
from base.test_base import TestBase


class TestTfqMyComments(TestBase):
    """
    进入我的评论页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/mine/myComment/myComment?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqMyComments, self).setUp()
        print("TestMyComments setup")

    def is_comment_exist(self):
        """
        页面是否有评论数据
        :return:
        """
        return self.page.element_is_exists('view[class="post_cont"]')

    def test_06_goto_more_post_更多话题(self):
        """
        我的评论页面，点击“更多话题“，这个用例在没有评论的时候有效
        """
        if self.is_comment_exist():
            print("页面有评论数据，此用例直接pass")
        else:
            self.page.get_element('view[class="morewall"]').tap()

        self.get_screenshot()

    def test_04_goto_first_post_帖子详情(self):
        """
        我的评论页面，点击第一个帖子，这个用例在没有评论的时候有效
        """
        if self.is_comment_exist():
            print("页面有评论数据，此用例直接pass")
        else:
            self.page.get_element('view[class="hotCont list-desc"]').tap()

        self.get_screenshot()

    def test_02_click_zanicon_评论点赞(self):
        """
        我的评论页面，点击第一个评论的点赞图标
        """
        if self.is_comment_exist():
            self.page.get_element('view[class="laud-btn"]').tap()
        else:
            print("页面无评论数据，此用例直接pass")

        self.get_screenshot()

    def test_01_click_replyBtn_评论回复按钮(self):
        """
        我的评论页面，点击第一个评论的回复按钮
        """
        if self.is_comment_exist():
            self.page.get_element('view[class="replyBtn"]').tap()

            self.verifyPageName('/page/taofangquan/commentDetail/commentDetail')
        else:
            print("页面无评论数据，此用例直接pass")

    def test_03_goto_commentdetail_评论详情(self):
        """
        我的评论页面，点击第一个评论内容，进入详情
        """
        if self.is_comment_exist():
            self.page.get_element('view[class="post_cont"]').tap()

            self.verifyPageName('/page/taofangquan/commentDetail/commentDetail')
        else:
            print("页面无评论数据，此用例直接pass")

        self.get_screenshot()

    def test_05_goto_housedetail_楼盘详情(self):
        """
        我的评论页面，点击第一个评论内容的楼盘名称右边箭头，进入新房详情页
        """
        if self.is_comment_exist():
            self.page.get_element('image[class="lp_icon disflex-flex-shrink-0"]').tap()

            self.verifyPageName('/page/newhouse/detail')
        else:
            print("页面无评论数据，此用例直接pass")

        self.get_screenshot()

