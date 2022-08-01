# add by zzh
from test.test_base import TestBase


class TestHuaTiDetail(TestBase):

    """
    话题详情页
    """
    def setUp(self) -> None:
        self.page_name = f"/page/taofangquan/tieziDetail/tieziDetail?city=qz&postsid={self.huatiid}"
        self.switch = False

        super(TestHuaTiDetail, self).setUp()
        print("TestHuaTiDetail setup")

    def test_click_content(self):
        """
        话题详情页，点击话题正文
        :return:
        """
        e = self.page.get_element('view[class="post_cont"]')
        e.tap()

    def test_click_moren(self):
        """
        话题详情页，点击话题"默认"按钮
        :return:
        """
        e = self.page.get_element('view[class="moren_sort active_sort"]')
        e.tap()

    def test_click_new(self):
        """
        话题详情页，点击话题"最新"按钮
        :return:
        """
        e = self.page.get_element('view[class="new_sort"]')
        e.tap()

    def test_click_fbsavator(self):
        """
        话题详情页，点击房博士评论的头像
        :return:
        """
        e = self.page.get_element('image[class="commentList--avator"][data-useridentity="fbs"]')
        e.tap()

    def test_click_fbscontact(self):
        """
        话题详情页，点击评论第一个房博士的“点击联系”按钮
        :return:
        """
        e = self.page.get_element('view[class="commentList--contact-fbs commentList--connectfbs"]')
        e.tap()

    def test_click_zygwavator(self):
        """
        话题详情页，点击置业顾问评论的头像
        :return:
        """
        e = self.page.get_element('image[class="commentList--avator"][data-useridentity="zygw"]')
        e.tap()

    def test_click_zygwcontact(self):
        """
        话题详情页，点击评论第一个置业顾问的“点击联系”按钮
        :return:
        """
        e = self.page.get_element('view[class="commentList--contact-fbs commentList--connectzygw"]')
        e.tap()

    def test_click_text(self):
        """
        话题详情页，点击第一个评论的评论内容
        :return:
        """
        e = self.page.get_element('navigator[class="commentList--content-rich-text"]')
        e.tap()

    def test_click_commentlist_laud(self):
        """
        话题详情页，点击第一个评论的点赞
        :return:
        """
        e = self.page.get_element('view[class="commentList--laud-btn"]')
        e.tap()

    def test_click_commentlist_reply(self):
        """
        话题详情页，点击第一个评论的“回复”按钮
        :return:
        """
        e = self.page.get_element('view[class="commentList--reply-btn"]')
        e.tap()

    def test_send_commentlist_reply(self):
        """
        话题详情页，点击第一个评论的“回复”按钮，发布评论回复
        :return:
        """
        self.page.get_element('view[class="commentList--reply-btn"]').tap()
        e2 = self.page.get_element('textarea[placeholder="说点什么吧"]')
        e2.input("话题的评论回复测试")
        e3 = self.page.get_element('button[class="send-btn"]')
        self.delay(1)
        e3.tap()

    def test_click_replycontent(self):
        """
        话题详情页，点击第一个评论的回复内容
        :return:
        """
        e = self.page.get_element('view[class="commentList--reply-content"]')
        e.tap()

    def test_click_reply_more(self):
        """
        话题详情页，点击第一个评论的"查看全部X条回复"
        :return:
        """
        e = self.page.get_element('view[class="commentList--more-reply"]')
        e.tap()

    def test_click_reply_laud(self):
        """
         话题详情页，点击第一个评论的回复的点赞按钮
        :return:
        """
        e = self.page.get_element('view[class="commentList--laud-btn"][data-laudtype="son"]')
        e.tap()

    def test_click_returnPl(self):
        """
        话题详情页，点击“更多热帖”按钮
        :return:
        """
        e = self.page.get_element('image[class="returnPl"]')
        e.tap()

    def test_click_fix_input(self):
        """
        话题详情页，点击底部发布评论入口
        :return:
        """
        e = self.page.get_element('view[class="detail-fix-input"]')
        e.tap()

    def test_click_addgroup(self):
        """
        话题详情页，点击底部“购房群”按钮
        :return:
        """
        e = self.page.get_element('view[class="item bottom-add-group"]')
        e.tap()

    def test_click_share(self):
        """
        话题详情页，点击”分享“按钮
        :return:
        """
        e = self.page.get_element('button[class="newHouseRfixed-share"]')
        e.tap()

    def test_send_reply(self):
        """
        话题详情页，点击底部发布评论弹窗，发布评论
        :return:
        """
        e1 = self.page.get_element('view[class="detail-fix-input"]')
        e1.tap()
        e2 = self.page.get_element('textarea[placeholder="说点什么吧"]')
        e2.input("话题评论")
        e3 = self.page.get_element('button[class="send-btn"]')
        self.delay(1)
        e3.tap()

