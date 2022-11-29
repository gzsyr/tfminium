# add by zsy
import minium

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

    def test_05_click_open_arrow_展示全部内容(self):
        """
        帖子的评论详情页，点击向下箭头，展示全部内容
        """
        self.find_element('view[class="open"]').tap()

        self.get_screenshot()

    def test_08_click_tiezi_dianzan_帖子点赞(self):
        """
        帖子的评论详情页，帖子的点赞操作
        """
        tap = 'self.page.get_element(\'view[class="laud-btn"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞OK')

    def test_03_click_comments_avator_主评论头像(self):
        """
        帖子的评论详情页，点击主评论的头像
        """
        self.find_element('image[class="commentList--avator"]').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def test_04_click_comments_dianzai_主评论点赞(self):
        """
        帖子的评论详情页，主评论的点赞操作
        """
        tap = 'self.page.get_element(\'view[class="commentList--laud-btn"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞Ok')
        self.get_screenshot()

    def test_01_click_addgroupimg_加群(self):
        """
        帖子的评论详情页，点击左下角的“加群”icon
        """
        try:
            self.find_element('image[class="addgroupimg"]').tap()
        except minium.MiniElementNotFoundError:
            print('没有加群广告')

        self.get_screenshot()

    def test_07_click_share_分享(self):
        """
        帖子的评论详情页，点击左下角“分享”icon帖子的评论详情页，
        """
        self.find_element('button[class="detail-fix-share"]').tap()
        self.delay(1)
        self.verifyByScreenshot('tfq/test_click_post_share.png')

    def test_06_click_returnPl_返回评论(self):
        """
        帖子的评论详情页，点击悬浮“返回评论”icon
        """
        self.find_element('image[class="returnPl"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_02_click_commention_评论入口(self):
        """
        帖子的评论详情页，点击最下面一行的评论入口
        """
        self.find_element('view[class="detail-fix-input"]').tap()

        self.get_screenshot()

    def test_09_z_click_allpicture_查看完整图片(self):
        """
        帖子的评论详情页，帖子评论详情页，点击“查看完整图片”按钮
        """
        self.find_element('view[id="newHouseBanner-ckmore"]').tap()

        self.get_screenshot()
