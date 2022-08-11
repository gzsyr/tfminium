# add by zzh
import unittest

from test.test_base import TestBase


class TestQuanZiDetail(TestBase):
    """
    圈子详情页
    """

    def setUp(self) -> None:
        self.page_name = f"/page/taofangquan/huati/huatiDetail?city=qz&topicid={self.quanzi}"    # dev
        self.switch = False
        super(TestQuanZiDetail, self).setUp()
        print("TestQuanZiDetail  Setup")

    def test_click_forcebtn(self):
        """
        圈子详情页，点击顶部关注/已关注按钮
        :return:
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
            e = self.page.get_element('view[id="qz_nofocuson"]')
            e.tap()


    def test_click_linked_huati(self):
        """
        圈子详情页 ，点击关联话题
        :return:
        """
        e = self.page.get_element('view[class="associate_huatiInfo list-desc"]')
        e.tap()

    def test_click_linked_quanzi(self):
        """
        圈子详情页，点击关联圈子

        :return:
        """
        e = self.page.get_element('view[class="groupInfo tfline2"]')
        e.tap()

    def test_click_fbs_avat0r(self):
        """
        圈子详情页，点击房博士头像
        :return:
        """
        e = self.page.get_element('image[class="avatar"][data-user_identity="fbs"]')
        e.tap()

    def test_click_fbs_im(self):
        """
        圈子详情页，点击房博士“在线咨询”
        :return:
        """
        e = self.page.get_element('view[class="connect connectfbs"]')
        e.tap()

    def test_click_zygw_avator(self):
        """
        圈子详情页，点击置业顾问头像
        :return:
        """
        e = self.page.get_element('image[class="avatar"][data-user_identity="zygw"]')
        e.tap()

    def test_click_zygw_im(self):
        """
        圈子详情页，点击置业顾问“在线咨询”
        :return:
        """
        e = self.page.get_element('view[class="connect connectzygw"]')
        e.tap()

    def test_click_content(self):
        """
        圈子详情页，点击帖子正文
        :return:
        """
        e = self.page.get_element('view[class="post_Title flex tfAlignC"]')
        e.tap()

    def test_click_posttag(self):
        """
        圈子详情页，点击帖子的关联圈子
        """
        # e = self.page.get_element('view[class="posttag tfFlex tfAlignC"]')
        e = self.page.get_element('view[class="posttag flex tfAlignC"]')
        e.tap()

    def test_click_laud_btn(self):
        """
        圈子详情页，点击帖子的点赞
                """
        e = self.page.get_element('view[class="laud-btn"]')
        e.tap()

    def test_click_reply(self):
        """
        圈子详情页，点击回复按钮
        """
        e = self.page.get_element('view[class="replyBtn"]')
        e.tap()

    def test_click_post_share(self):
        """
        圈子详情页，点击帖子分享按钮
        """
        e = self.page.get_element('button[class="shareDetail"]')
        e.tap()

    def test_click_returnPl(self):
        """
        圈子详情页，点击右下角“更多热帖”
        """
        e = self.page.get_element('image[class="returnPl"]')
        e.tap()

    @unittest.skip("v6.13.x删除此功能")
    def test_click_page_share(self):
        """
        圈子详情页，点击底部分享按钮
                """
        e = self.page.get_element('button[class="shareBtn"]')
        e.tap()

    def test_click_postBtn(self):
        """
        圈子详情页，点击“发布帖子”按钮
        """
        # e = self.page.get_element('view[class="postBtn"]')
        e = self.page.get_element('image[class="postBtn_img"]')
        e.tap()

