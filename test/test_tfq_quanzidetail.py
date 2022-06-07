# add by zzh
import minium
from test.common import delay
from test.test_base import TestBase


class TestQuanZiDetail(TestBase):
    """
    圈子详情页
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/huati/huatiDetail?city=qz&topicid=751"
        self.switch = False
        super(TestQuanZiDetail, self).setUp()
        print("TestQuanZiDetail  Setup")

    def test_click_forcebtn(self):
        """
        圈子详情页，点击顶部关注/已关注按钮
        :return:
        """
        b_l = self.page.element_is_exists('text[data-type="2"]', inner_text="已关注")
        if b_l == True:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            e = self.page.get_element('text[data-type="2"]', inner_text="已关注")
            e.tap()
            self.app.restore_wx_method("showModal")
            delay(2)
            self.capture("取消关注")
            self.native.handle_modal("确定", "取消关注")
        else:
            e = self.page.get_element('text[class="add"]', inner_text="+")
            e.tap()
            delay(1)


    def test_click_linked_huati(self):
        """
        圈子详情页 ，点击关联话题
        :return:
        """
        e = self.page.get_element('view[class="associate_huatiInfo list-desc"]')
        e.tap()
        delay(1)

    def test_click_linked_quanzi(self):
        """
        圈子详情页，点击关联圈子

        :return:
        """
        e = self.page.get_element('view[class="groupInfo tfline2"]')
        e.tap()
        delay(1)

    def test_click_fbs_avat0r(self):
        """
        圈子详情页，点击房博士头像
        :return:
        """
        e = self.page.get_element('image[class="avatar"][data-user_identity="fbs"]')
        e.tap()
        delay(1)

    def test_click_fbs_im(self):
        """
        圈子详情页，点击房博士“在线咨询”
        :return:
        """
        e = self.page.get_element('view[class="connect connectfbs"]')
        e.tap()
        delay(1)

    def test_click_zygw_avator(self):
        """
        圈子详情页，点击置业顾问头像
        :return:
        """
        e = self.page.get_element('image[class="avatar"][data-user_identity="zygw"]')
        e.tap()
        delay(1)

    def test_click_zygw_im(self):
        """
        圈子详情页，点击置业顾问“在线咨询”
        :return:
        """
        e = self.page.get_element('view[class="connect connectzygw"]')
        e.tap()
        delay(1)

    def test_click_content(self):
        """
        圈子详情页，点击帖子正文
        :return:
        """
        e = self.page.get_element('view[class="post_Title flex tfAlignC"]')
        e.tap()
        delay(1)

    def test_click_posttag(self):
        """
        圈子详情页，点击帖子的关联圈子
        """
        e = self.page.get_element('view[class="posttag tfFlex tfAlignC"]')
        e.tap()
        delay(1)

    def test_click_laud_btn(self):
        """
        圈子详情页，点击帖子的点赞
                """
        e = self.page.get_element('view[class="laud-btn"]')
        e.tap()
        delay(1)

    def test_click_reply(self):
        """
        圈子详情页，点击回复按钮
        """
        e = self.page.get_element('view[class="replyBtn"]')
        e.tap()
        delay(1)

    def test_click_post_share(self):
        """
        圈子详情页，点击帖子分享按钮
        """
        e = self.page.get_element('button[class="shareDetail"]')
        e.tap()
        delay(1)

    def test_click_returnPl(self):
        """
        圈子详情页，点击右下角“更多热帖”
        """
        e = self.page.get_element('image[class="returnPl"]')
        e.tap()
        delay(1)

    def test_click_page_share(self):
        """
        圈子详情页，点击底部分享按钮
                """
        e = self.page.get_element('button[class="shareBtn"]')
        e.tap()
        delay(1)

    def test_click_postBtn(self):
        """
        圈子详情页，点击“发布帖子”按钮
        """
        e = self.page.get_element('view[class="postBtn"]')
        e.tap()
        delay(1)







