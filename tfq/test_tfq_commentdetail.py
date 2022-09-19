# add by zsy
from base.test_base import TestBase


class TestTfqCommentDetail(TestBase):
    """
    帖子的评论详情页
    """
    def setUp(self) -> None:
        self.page_name = f"/page/taofangquan/tieziCommentDetail/tieziCommentDetail?city=qz&pid={self.pinglunid}&postsid={self.postid}"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqCommentDetail, self).setUp()
        print("TestTfqCommentDetail setup atest")

    def test_click_open_arrow(self):
        """
        帖子的评论详情页，点击向下箭头，展示全部内容
        """
        self.page.get_element('view[class="open"]').tap()

        self.get_screenshot()

    def test_click_tiezi_dianzan(self):
        """
        帖子的评论详情页，帖子的点赞操作
        """
        tap = 'self.page.get_element(\'view[class="laud-btn"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞OK')

    def test_click_comments_avator(self):
        """
        帖子的评论详情页，点击主评论的头像
        """
        self.page.get_element('image[class="commentList--avator"]').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def test_click_comments_dianzai(self):
        """
        帖子的评论详情页，主评论的点赞操作
        """
        tap = 'self.page.get_element(\'view[class="commentList--laud-btn"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞Ok')
        self.get_screenshot()

    def test_click_addgroupimg(self):
        """
        帖子的评论详情页，点击左下角的“加群”icon
        """
        self.page.get_element('image[class="addgroupimg"]').tap()

        self.get_screenshot()

    def test_click_share(self):
        """
        帖子的评论详情页，点击左下角“分享”icon帖子的评论详情页，
        """
        self.page.get_element('button[class="detail-fix-share"]').tap()
        self.delay(1)
        self.verifyByScreenshot('tfq/test_click_post_share.png')

    def test_click_returnPl(self):
        """
        帖子的评论详情页，点击悬浮“返回评论”icon
        """
        self.page.get_element('image[class="returnPl"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_commention(self):
        """
        帖子的评论详情页，点击最下面一行的评论入口
        """
        self.page.get_element('view[class="detail-fix-input"]').tap()

        self.get_screenshot()

    def test_z_click_allpicture(self):
        """
        帖子的评论详情页，帖子评论详情页，点击“查看完整图片”按钮
        """
        self.page.get_element('view[id="newHouseBanner-ckmore"]').tap()

        self.get_screenshot()
