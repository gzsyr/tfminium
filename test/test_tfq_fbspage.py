# add by zsy
from test.test_base import TestBase


class TestFbsPage(TestBase):
    """
    房博士主页
    """
    def setUp(self) -> None:
        self.page_name = '/page/taofangquan/personalDetails/fbs/fbs?city=qz&uid=3403749&role_uid=1081'
        self.switch = False
        super(TestFbsPage, self).setUp()
        print("TestFbsPage setup")

    def test_z_click_call(self):
        """
        房博士主页，点击下方“拨打电话”
        :return:
        """
        self.page.get_element('view[class="link-button call"]').tap()

    def test_click_shidikanpan(self):
        """
        点击“实地看盘
        :return:
        """
        self.page.get_element('view[data-eventid="2951"]').tap()

    def test_click_huxingjiexi(self):
        """
        点击“户型解析”
        :return:
        """
        self.page.get_element('view[data-eventid="2952"]').tap()

    def test_click_jiaotongpeitao(self):
        """
        点击“交通配套”
        :return:
        """
        self.page.get_element('view[data-eventid="2953"]').tap()

    def test_click_loupanpinglun(self):
        """
        点击“楼盘评论”
        :return:
        """
        self.page.get_element('view[data-eventid="2954"]').tap()

    def test_click_huati(self):
        """
        点击“话题“
        :return:
        """
        self.page.get_element('view[data-eventid="2955"]').tap()
        return self

    def test_goto_loupanpinglun(self):
        """
        点击楼盘评论，进入楼盘评论详情页
        :return:
        """
        self.page.get_element('view[class="post_cont"]').tap()

    def test_loupanpinglun_dianzan(self):
        """
        点击楼盘评论的“点赞”icon
        :return:
        """
        self.page.get_element('view[class="laud-btn"]').tap()

    def test_loupanpinglun_reply(self):
        """
        点击楼盘评论的“回复”icon
        :return:
        """
        self.page.get_element('view[class="replyBtn"]').tap()

    def test_loupanpinglun_quanzi(self):
        """
        点击楼盘评论的圈子，进入圈子页面
        :return:
        """
        self.page.get_element('view[class="posttag tfFlex tfAlignC"]').tap()

    def test_huati_dianzan(self):
        """
        点击话题tab下第一条的“点赞”icon
        :return:
        """
        self.test_click_huati().delay(2).page.get_element('view[class="laud-btn"][data-index="0"]').tap()

    def test_huati_reply(self):
        """
        点击话题tab下的第一条的“回复”icon
        :return:
        """
        self.test_click_huati().delay(2).page.get_element('view[class="replyBtn"]').tap()

    def test_goto_huatidetail(self):
        """
        点击话题tab下的一条postsid="13684"，进入详情页
        :return:
        """
        self.test_click_huati().delay(2).page.get_element('view[class="postitem"][data-postsid="13684"]').tap()

    def test_huati_quanzi(self):
        """
        点击话题tab下的第一条带圈子的内容，进入对应圈子详情
        :return:
        """
        self.test_click_huati().delay(2).page.get_element('view[class="posttag tfFlex tfAlignC"]').tap()

