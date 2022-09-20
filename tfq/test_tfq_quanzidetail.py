# add by zzh
import threading
import unittest

from base.test_base import TestBase


class TestTfqQuanZiDetail(TestBase):
    """
    圈子详情页
    """

    def setUp(self) -> None:
        self.page_name = f"/page/taofangquan/huati/huatiDetail?city=qz&topicid={self.quanzi}"    # dev
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqQuanZiDetail, self).setUp()
        print("TestTfqQuanZiDetail  Setup")

    def test_click_forcebtn(self):
        """
        圈子详情页，点击顶部关注/已关注按钮
        """
        b_l = self.page.element_is_exists('view[id="qz_focuson"]')
        if b_l == True:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[id="qz_focuson"]').tap()
            self.app.restore_wx_method("showModal")
            self.delay(2)
            self.capture("取消关注")
            self.native.handle_modal("确定", "取消关注")
        else:
            self.page.get_element('view[id="qz_nofocuson"]').tap()

        self.get_screenshot()

    def test_click_linked_huati(self):
        """
        圈子详情页 ，点击关联话题进入详情页
        """
        self.page.get_element('view[class="associate_huatiInfo list-desc"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_linked_quanzi(self):
        """
        圈子详情页，点击关联圈子，进入圈子详情
        """
        self.page.get_element('view[class="groupInfo tfline2"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_fbs_avator(self):
        """
        圈子详情页，点击房博士头像，进入淘房顾问主页
        """
        self.page.get_element('image[class="avatar"][data-user_identity="fbs"]').tap()

        self.verifyPageName('/page/taofangquan/personalDetails/fbs/fbs')
        self.get_screenshot()

    def test_click_fbs_im(self):
        """
        圈子详情页，点击房博士“在线咨询”，看配置，有的进IM，有的进企微
        """
        self.page.get_element('view[class="connect connectfbs"]').tap()

        self.get_screenshot()

    def test_click_zygw_avator(self):
        """
        圈子详情页，点击置业顾问头像，进入详情页
        """
        self.page.get_element('image[class="avatar"][data-user_identity="zygw"]').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def test_click_zygw_im(self):
        """
        圈子详情页，点击置业顾问“在线咨询”
        """
        self.page.get_element('view[class="connect connectzygw"]').tap()
        self.delay(3)

        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_click_content(self):
        """
        圈子详情页，点击帖子正文，进入详情页
        """
        self.page.get_element('view[class="post_Title flex tfAlignC"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_posttag(self):
        """
        圈子详情页，点击帖子的关联圈子
        """
        self.page.get_element('view[class="posttag flex tfAlignC"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_laud_btn(self):
        """
        圈子详情页，点击帖子的点赞
        """
        # 监听回调, 阻塞当前主线程
        # called = threading.Semaphore(0)
        # callback_args = None
        #
        # def callback(args):
        #     nonlocal callback_args
        #     called.release()
        #     callback_args = args
        #
        # self.app.hook_wx_method("showToast", callback=callback)
        # self.page.get_element('view[class="laud-btn"]').tap()
        # is_called = called.acquire(timeout=5)
        # self.app.release_hook_wx_method("showToast")


        self.verifyStr(True, self.getShowToast('self.page.get_element(\'view[class="laud-btn"]\').tap()'), "toast called ")
        self.get_screenshot()

    def test_click_reply(self):
        """
        圈子详情页，点击回复按钮
        """
        self.page.get_element('view[class="replyBtn"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_post_share(self):
        """
        圈子详情页，点击帖子分享按钮
        """
        self.page.get_element('button[class="shareDetail"]').tap()
        self.delay(1)
        self.verifyByScreenshot('tfq/test_click_post_share.png')

    def test_click_returnPl(self):
        """
        圈子详情页，点击右下角“更多热帖”回首页
        """
        self.page.get_element('image[class="returnPl"]').tap()

        self.verifyPageName('/page/find/find')
        self.get_screenshot()

    # @unittest.skip("v6.13.x删除此功能")
    # def test_click_page_share(self):
    #     """
    #     圈子详情页，点击底部分享按钮
    #             """
    #     e = self.page.get_element('button[class="shareBtn"]')
    #     e.tap()

    def test_click_postBtn(self):
        """
        圈子详情页，点击“发布帖子”按钮
        """
        # e = self.page.get_element('view[class="postBtn"]')
        self.page.get_element('image[class="postBtn_img"]').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

