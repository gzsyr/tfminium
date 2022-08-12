# add by zsy
from base.test_base import TestBase


class TestCommentDetail(TestBase):
    """
    帖子的评论详情页
    """
    def setUp(self) -> None:
        self.page_name = f"/page/taofangquan/tieziCommentDetail/tieziCommentDetail?city=qz&pid={self.pinglunid}&postsid={self.postid}"
        self.switch = False
        super(TestCommentDetail, self).setUp()
        print("TestCommentDetail setup atest")

    def test_click_open_arrow(self):
        """
        点击向下箭头，展示全部内容
        :return:
        """
        self.page.get_element('view[class="open"]').tap()

    def test_click_tiezi_dianzan(self):
        """
        帖子的点赞操作
        :return:
        """
        self.page.get_element('view[class="laud-btn"]').tap()

    def test_click_comments_avator(self):
        """
        点击主评论的头像
        :return: 
        """
        self.page.get_element('image[class="commentList--avator"]').tap()

    def test_click_comments_dianzai(self):
        """
        主评论的点赞操作
        :return:
        """
        self.page.get_element('view[class="commentList--laud-btn"]').tap()

    def test_click_addgroupimg(self):
        """
        点击左下角的“加群”icon
        :return:
        """
        self.page.get_element('image[class="addgroupimg"]').tap()

    def test_click_share(self):
        """
        点击左下角“分享”icon
        :return:
        """
        self.page.get_element('button[class="detail-fix-share"]').tap()

    def test_click_returnPl(self):
        """
        点击悬浮“返回评论”icon
        :return:
        """
        self.page.get_element('image[class="returnPl"]').tap()

    def test_click_commenticon(self):
        """
        点击最下面一行的评论入口
        :return:
        """
        self.page.get_element('view[class="detail-fix-input"]').tap()

    def test_z_click_allpicture(self):
        """
        帖子评论详情页，点击“查看完整图片”按钮
        :return:
        """
        self.page.get_element('view[id="newHouseBanner-ckmore"]').tap()
