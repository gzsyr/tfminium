# add by zzh
import minium
from test.common import delay
import threading

class TestPostDetail(minium.MiniTest):
    """
    帖子详情页
    """

    def setUp(self) -> None:
        self.app.navigate_to("/page/taofangquan/tieziDetail/tieziDetail?city=qz&postsid=12746")
        delay(2)
        self.app.get_current_page()
        print("setUp!!!!")

    def test_click_content(self):
        """
        帖子详情页，点击帖子正文
        :return:
        """
        e = self.page.get_element('view[class="post_cont"]')
        e.tap()
        delay(2)

    def test_click_laud(self):
        """
        帖子详情页，点击帖子点赞
        :return:
        """
        e = self.page.get_element('view[class="item laud"]')
        e.tap()
        delay(2)

    def test_click_more(self):
        """
        帖子详情页，点击帖子"更多"按钮
        :return:
        """
        e = self.page.get_element('view[class="item more-ctr"]')
        e.tap()
        delay(2)

    def test_click_newpost(self):
        """
        帖子详情页，点击帖子"最新热帖"按钮
        :return:
        """
        e = self.page.get_element('view[class="toutiao-swiper-item tfLine1"]')
        e.tap()
        delay(2)

    def test_click_moren(self):
        """
        帖子详情页，点击帖子"默认"按钮
        :return:
        """
        e = self.page.get_element('view[class="moren_sort active_sort"]')
        e.tap()
        delay(2)

    def test_click_new(self):
        """
        帖子详情页，点击帖子"最新"按钮
        :return:
        """
        e = self.page.get_element('view[class="new_sort"]')
        e.tap()
        delay(2)

    def test_click_fbsavator(self):
        """
        帖子详情页，点击房博士评论的头像
        :return:
        """
        e = self.page.get_element('image[class="commentList--avator"][data-useridentity="fbs"]')
        e.tap()
        delay(2)


    def test_click_fbscontact(self):
        """
        帖子详情页，点击评论第一个房博士的“点击联系”按钮
        :return:
        """
        e = self.page.get_element('view[class="commentList--contact-fbs commentList--connectfbs"]')
        e.tap()
        delay(2)

    def test_click_zygwavator(self):
        """
        帖子详情页，点击置业顾问评论的头像
        :return:
        """
        e = self.page.get_element('image[class="commentList--avator"][data-useridentity="zygw"]')
        e.tap()
        delay(2)

    def test_click_zygwcontact(self):
        """
        帖子详情页，点击评论第一个置业顾问的“点击联系”按钮
        :return:
        """
        e = self.page.get_element('view[class="commentList--contact-fbs commentList--connectzygw"]')
        e.tap()
        delay(2)

    def test_click_text(self):
        """
        帖子详情页，点击第一个评论的评论内容
        :return:
        """
        e = self.page.get_element('navigator[class="commentList--content-rich-text"]')
        e.tap()
        delay(2)

    def test_click_commentlist_laud(self):
        """
        帖子详情页，点击第一个评论的点赞
        :return:
        """
        e = self.page.get_element('view[class="commentList--laud-btn"]')
        e.tap()
        delay(2)

    def test_click_commentlist_reply(self):
        """
        帖子详情页，点击第一个评论的“回复”按钮
        :return:
        """
        e = self.page.get_element('view[class="commentList--reply-btn"]')
        e.tap()
        delay(2)

    def test_send_commentlist_reply(self):
        """
        帖子详情页，点击第一个评论的“回复”按钮，发布评论回复
        :return:
        """
        self.page.get_element('view[class="commentList--reply-btn"]').tap()
        e2 = self.page.get_element('textarea[placeholder="说点什么吧"]')
        e2.input("帖子的评论回复测试")
        e3 = self.page.get_element('button[class="send-btn"]')
        delay(1)
        e3.tap()

    def test_click_replycontent(self):
        """
        帖子详情页，点击第一个评论的回复内容
        :return:
        """
        e = self.page.get_element('view[class="commentList--reply-content"]')
        e.tap()
        delay(2)

    def test_click_reply_more(self):
        """
        帖子详情页，点击第一个评论的"查看全部X条回复"
        :return:
        """
        e = self.page.get_element('view[class="commentList--more-reply"]')
        e.tap()
        delay(2)

    def test_click_reply_laud(self):
        """
         帖子详情页，点击第一个评论的回复的点赞按钮
        :return:
        """
        e = self.page.get_element('view[class="commentList--laud-btn"][data-laudtype="son"]')
        e.tap()
        delay(2)

    def test_click_returnPl(self):
        """
        帖子详情页，点击“更多热帖”按钮
        :return:
        """
        e = self.page.get_element('image[class="returnPl"]')
        e.tap()
        delay(2)

    def test_click_add(self):
        """
        帖子详情页，点击“加入群聊”入口
        :return:
        """
        e = self.page.get_element('view[class="add"]')
        e.tap()
        delay(2)

    def test_click_add_close(self):
        """
        帖子详情页，点击“加入群聊”入口的关闭按钮
        :return:
        """
        e = self.page.get_element('view[class="close"]')
        e.tap()
        delay(2)


    def test_click_fix_input(self):
        """
        帖子详情页，点击底部发布评论入口
        :return:
        """
        e = self.page.get_element('view[class="detail-fix-input"]')
        e.tap()
        delay(2)

    def test_click_addgroup(self):
        """
        帖子详情页，点击底部“购房群”按钮
        :return:
        """
        e = self.page.get_element('view[class="item bottom-add-group"]')
        e.tap()
        delay(2)

    def test_click_collect(self):
        """
        帖子详情页，点击底部“收藏”按钮
        :return:
        """
        e = self.page.get_element('view[class="item bottom-collect"]')
        e.tap()
        delay(2)

    def test_click_bottom_laud(self):
        """
        帖子详情页，点击底部“点赞”按钮
        :return:
        """
        e = self.page.get_element('view[class="item bottom-laud"]')
        e.tap()
        delay(2)

    def test_click_share(self):
        """
        帖子详情页，点击”分享“按钮
        :return:
        """
        e = self.page.get_element('button[class="newHouseRfixed-share"]')
        e.tap()
        delay(2)

    def test_click_share_close(self):
        """
        帖子详情页，点击”分享“按钮，点击取消按钮
        :return:
        """
        e = self.page.get_element('button[class="newHouseRfixed-share"]')
        e.tap()
        delay(1)
        self.page.get_element('view[class="closeBtn"]').tap()
        delay(1)

    def test_click_share_hy(self):
        """
        帖子详情页，点击”分享“按钮，点击分享给好友
        :return:
        """
        e = self.page.get_element('button[class="newHouseRfixed-share"]')
        e.tap()
        delay(1)
        self.page.get_element('button[class="share-btn hy"]').tap()
        delay(1)

    def test_click_share_hb(self):
        """
        帖子详情页，点击”分享“按钮，点击海报
        :return:
        """
        e = self.page.get_element('button[class="newHouseRfixed-share"]')
        e.tap()
        delay(1)
        self.page.get_element('button[class="share-btn pyq"]').tap()
        delay(1)

    def test_send_reply(self):
        """
        帖子详情页，点击底部发布评论弹窗，发布评论
        :return:
        """
        e1 = self.page.get_element('view[class="detail-fix-input"]')
        e1.tap()
        e2 = self.page.get_element('textarea[placeholder="说点什么吧"]')
        e2.input("UIceshi2")
        e3 = self.page.get_element('button[class="send-btn"]')
        delay(1)
        e3.tap()


































        


