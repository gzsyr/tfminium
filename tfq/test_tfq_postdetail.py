# add by zzh
import time

from base.test_base import TestBase


class TestTfqPostDetail(TestBase):
    """
    帖子详情页
    """

    def setUp(self) -> None:
        self.page_name = f"/page/taofangquan/tieziDetail/tieziDetail?city=qz&postsid={self.postid}"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqPostDetail, self).setUp()
        print("TestPostDetail  Setup")

    def test_click_content_and_reply(self):
        """
        帖子详情页，点击帖子正文，输入评论，发布成功，并点击该评论，进入评论详情页
        """
        content = '回复主评论'+time.strftime('%Y-%m-%d')
        self.page.get_element('view[class="post_cont"]').tap()
        self.page.get_element('textarea[name="quick_reply_content"][placeholder="说点什么吧"]').\
            input(content)
        # tap = 'self.page.get_element(\'button[class="send-btn"]\').tap()'
        # self.verifyStr(True, self.getShowToast(tap), '发表主评论OK')
        self.page.get_element('button[class="send-btn"]').tap()
        self.delay(2)

        # 切换到“最新”tab下，
        self.click_new_sort()
        self.delay(2)
        # 查看第一条，是否是该条评论
        # self.verifyContainsStr(content, self.page.get_element('navigator[class="commentList--content-rich-text"]').inner_wxml,
        #                        '能够获取到刚刚发表的主评论 ok')
        # 点击该第一条评论，进入评论详情页
        self.click_content_text()

        self.verifyPageName('/page/taofangquan/tieziCommentDetail/tieziCommentDetail')
        self.get_screenshot()

    def test_click_laud(self):
        """
        帖子详情页，点击帖子点赞
        """
        tap = 'self.page.get_element(\'view[class="item laud"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), 'show toast')
        self.get_screenshot()

    def test_click_tipoff(self):
        """
        帖子详情页，点击帖子"更多"-“举报”按钮，输入“其他”点击提交
        """
        # 点击“更多”
        self.page.get_element('view[class="item more-ctr"]').tap()
        # 点击“举报”
        self.page.get_element('view[class="quick-box-cont"]').tap()
        self.delay(1)
        # 勾选最后一个选项“其他”
        self.input_value_by_mk('tfq/tipoff-other.png')
        self.delay(2)

        if self.page.element_is_exists('view[class="report-submit disable"]'):
            # 如果勾选项没有勾上，再勾选一遍
            self.input_value_by_mk('tfq/tipoff-other.png')
            self.delay(2)

        self.verifyStr(True, self.getShowToast('self.page.get_element(\'view[class="report-submit"]\').tap()'), '举报成功弹框')
        self.get_screenshot()

    def test_click_newpost(self):
        """
        帖子详情页，点击帖子"最新热帖"按钮，进入帖子详情页
        :return:
        """
        # e = self.page.get_element('view[class="toutiao-swiper-item tfLine1"]')
        self.page.get_element('swiper-item[id="ontieziDetail"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_moren(self):
        """
        帖子详情页，点击帖子"默认"按钮
        """
        self.page.get_element('view[class="moren_sort active_sort"]').tap()

        self.get_screenshot()

    def click_new_sort(self):
        """
        帖子详情页，点击帖子"最新"按钮
        """
        self.page.get_element('view[class="new_sort"]').tap()

    def test_click_fbsavator(self):
        """
        帖子详情页，点击房博士评论的头像，进入房博士主页
        """
        self.page.get_element('image[class="commentList--avator"][data-useridentity="fbs"]').tap()

        self.verifyPageName('/page/taofangquan/personalDetails/fbs/fbs')
        self.get_screenshot()

    def test_click_fbscontact(self):
        """
        帖子详情页，点击评论第一个房博士的“点击联系”按钮
        """
        self.page.get_element('view[class="commentList--contact-fbs commentList--connectfbs"]').tap()

        self.get_screenshot()

    def test_click_zygwavator(self):
        """
        帖子详情页，点击置业顾问评论的头像，进入置业顾问主页
        """
        self.page.get_element('image[class="commentList--avator"][data-useridentity="zygw"]').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def test_click_zygwcontact(self):
        """
        帖子详情页，点击评论第一个置业顾问的“点击联系”按钮，进IM聊天
        """
        self.page.get_element('view[class="commentList--contact-fbs commentList--connectzygw"]').tap()
        self.delay(2)

        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def click_content_text(self):
        """
        帖子详情页，点击第一个评论的评论内容，进入评论详情页
        """
        self.page.get_element('navigator[class="commentList--content-rich-text"]').tap()

    def test_click_commentlist_laud(self):
        """
        帖子详情页，点击第一个评论的点赞
        """
        self.verifyStr(True,
                       self.getShowToast('self.page.get_element(\'view[class="commentList--laud-btn"]\').tap()'),
                       '点赞校验ok')

        self.get_screenshot()

    def test_click_commentlist_reply(self):
        """
        帖子详情页，点击第一个评论的“回复”按钮，弹出回复框，回复内容，并发布
        :return:
        """
        content = '回复第一条主评论'+time.strftime('%Y-%m-%d')
        self.page.get_element('view[class="commentList--reply-btn"]').tap()

        # 输入评论
        zjele = self.page.get_element('comment-list').get_element('form')
        zjele.get_element('textarea[name="quick_reply_content"]').input(content)

        # iscall = self.getShowToast('self.page.get_element(\'button[class="commentList--send-btn"]\').tap()')
        # self.verifyStr(True, iscall, '发布完成的提示 ok')
        self.page.get_element('button[class="commentList--send-btn"]').tap()
        self.delay(1)

        # 验证查看第一条评论的回复评论
        self.verifyStr(content, self.page.get_element('view[class="commentList--reply-content"]').inner_text,
                       '第一个主评论的回复ok')

        self.get_screenshot()

    def test_click_replycontent(self):
        """
        帖子详情页，点击第一个评论的回复内容，弹出“回复、删除”框，点击“回复”，输入“test_click_replydelete”并发布
        """
        content = 'test_click_replydelete'
        self.page.get_element('view[class="commentList--reply-content"]').tap()
        self.delay(1)
        self.page.get_element('view[class="commentList--quick-box-cont commentList--quick-box-edit"]', inner_text='回复').tap()
        # print(self.page.get_element('comment-list').inner_wxml)

        # 输入评论
        zjele = self.page.get_element('comment-list').get_element('form')
        zjele.get_element('textarea[name="quick_reply_content"]').input(content)

        # iscall = self.getShowToast('self.page.get_element(\'button[class="commentList--send-btn"]\').tap()')
        # self.verifyStr(True, iscall, '发布完成的提示 ok')
        self.page.get_element('button[class="commentList--send-btn"]').tap()
        self.delay(1)

        self.get_screenshot()

    def test_click_replydelete(self):
        """
        帖子详情页，点击第一个评论的回复内容，弹出“回复、删除”框，点击“删除”，确认删除
        """
        content = 'test_click_replydelete'
        self.page.get_element('view[class="commentList--reply-content"]', text_contains=content).tap()
        self.delay(1)
        self.page.get_element('view[class="commentList--quick-box-cont commentList--quick-box-delete"]',
                              inner_text='删除').tap()
        self.page.get_element('view[class="commentList--quick-box-cont commentList--quick-box-delete"]',
                              inner_text='删除回复').tap()
        self.delay(2)
        self.verifyStr(False,
                       self.page.element_is_exists('view[class="commentList--reply-content"]', text_contains=content),
                       '删除第一个主评论的第一个回复完成ok')

        self.get_screenshot()

    def test_click_reply_more(self):
        """
        帖子详情页，点击评论的"查看全部X条回复"，弹出全部回复
        """
        if self.page.element_is_exists('view[class="commentList--more-reply"]'):
            self.page.get_element('view[class="commentList--more-reply"]').tap()

        self.get_screenshot()

    def test_click_reply_more_laud(self):
        """
        帖子详情页，点击评论的“查看全部x条回复”，如有，弹出全部回复，点击第一条的点赞
        """
        if self.page.element_is_exists('view[class="commentList--more-reply"]'):
            self.page.get_element('view[class="commentList--more-reply"]').tap()
            self.delay(1)
            tap = 'self.page.get_element(\'view[class="commentList--laud-btn"][data-laudtype="son_all"]\').tap()'
            self.verifyStr(True, self.getShowToast(tap), '点赞OK')

        self.get_screenshot()

    def test_click_replay_more_content_reply(self):
        """
        帖子详情页，点击评论的“查看全部x条回复”，如有，弹出全部回复，点击第一条内容，弹出回复框
        """
        if self.page.element_is_exists('view[class="commentList--more-reply"]'):
            self.page.get_element('view[class="commentList--more-reply"]').tap()
            self.delay(1)

            e = self.page.get_element('view[class="commentList--comment-item"][data-replytype="allReply"]')
            e.get_element('view[class="commentList--reply-content"]').tap()

        self.get_screenshot()

    def test_click_reply_more_fabu(self):
        """
        帖子详情页，点击评论的“查看全部x条回复”，如有，弹出全部回复，点击下方回复按钮，弹出回复框
        """
        if self.page.element_is_exists('view[class="commentList--more-reply"]'):
            self.page.get_element('view[class="commentList--more-reply"]').tap()
            self.delay(1)

            self.page.get_element('view[class="commentList--m-reply-btn"]').tap()

        self.get_screenshot()

    def test_click_reply_laud(self):
        """
         帖子详情页，点击第一个评论的回复的点赞按钮\
        """
        tap = 'self.page.get_element(\'view[class="commentList--laud-btn"][data-laudtype="son"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '第一个评论的第一个回复点赞ok')
        self.get_screenshot()

    def test_click_returnPl(self):
        """
        帖子详情页，点击“更多热帖”按钮
        :return:
        """
        self.page.get_element('image[class="returnPl"]').tap()

        self.verifyPageName('/page/find/find')
        self.get_screenshot()

    def test_goto_housedetail(self):
        """
        帖子详情页，点击楼盘卡片，进入楼盘详情页
        :return:
        """
        exist = self.page.element_is_exists('view[class="lpcard_wrap tfFlex"]')
        if exist:
            self.page.get_element('view[class="lpcard_hname tfLine1"]').tap()

            self.verifyPageName('/page/newhouse/detail')
        else:
            print("本帖子没有带楼盘名片，该用例直接pass")

        self.get_screenshot()

    def test_click_add(self):
        """
        帖子详情页，点击“加入群聊”入口，进入配置的页面
        """
        self.page.get_element('view[class="add_jqbtn"]').tap()

        self.get_screenshot()

    def test_click_add_close(self):
        """
        帖子详情页，点击“加入群聊”入口的关闭按钮
        """
        self.page.get_element('view[class="close"]').tap()

        self.get_screenshot()

    def test_click_fix_input(self):
        """
        帖子详情页，点击底部发布评论入口，弹出回复框
        """
        self.page.get_element('view[class="detail-fix-input"]').tap()

        self.get_screenshot()

    def test_click_addgroup(self):
        """
        帖子详情页，点击底部“购房群”按钮
        :return:
        """
        self.page.get_element('view[class="item bottom-add-group"]').tap()

        self.get_screenshot()

    def test_click_collect(self):
        """
        帖子详情页，点击底部“收藏”按钮
        """
        # e = self.page.get_element('view[class="item bottom-collect is_collect"]')
        # e.tap()
        # 收藏和未收藏显示的上面class不一样，更新为下面的方法
        self.page.get_element('view[class="text"]', inner_text="收藏").tap()

        self.get_screenshot()

    def test_click_bottom_laud(self):
        """
        帖子详情页，点击底部“点赞”按钮
        :return:
        """
        self.page.get_element('view[class="item bottom-laud"]').tap()

        self.get_screenshot()

    def test_click_bottom_zygwim(self):
        """
        帖子详情页，点击底部“置业顾问在线咨询”按钮，如无，则通过
        """
        exist = self.page.element_is_exists('image[class="bottom-connect-avatar"]')
        if exist:
            self.page.get_element('image[class="bottom-connect-avatar"]').tap()
            self.delay(2)
        else:
            print("本帖子没有配置关联置业顾问，该用例直接pass")

        self.get_screenshot()

    def test_click_share(self):
        """
        帖子详情页，点击”分享“按钮
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(1)

        self.verifyByScreenshot('tfq/test_click_post_share.png')

    def test_click_share_close(self):
        """
        帖子详情页，点击”分享“按钮，点击取消按钮
        :return:
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(1)
        self.page.get_element('view[class="closeBtn"]').tap()

        self.get_screenshot()

    def test_click_share_hb(self):
        """
        帖子详情页，点击”分享“按钮，点击海报
        :return:
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(1)
        self.page.get_element('button[class="share-btn pyq"]').tap()

        self.verifyStr(True,
                       self.page.element_is_exists('button[class="canvasToImage--saveToAlbumButton"]'),
                       '生成海报页 ok')
        self.get_screenshot()

    def test_z_click_share_hy(self):
        """
        帖子详情页，点击”分享“按钮，点击分享给好友
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(1)
        self.page.get_element('button[class="share-btn hy"]').tap()

        self.get_screenshot()

    def test_click_newpost_more(self):
        """
        帖子详情页，点击最新热帖的，“更多”按钮\
        """
        self.page.get_element('view[id="goTieZiList"]').tap()

        self.verifyPageName('/page/taofangquan/tieziList/tieziList')
        self.get_screenshot()

    def test_z_click_allpicture(self):
        """
        帖子详情页，点击“查看完整图片”按钮
        """
        self.page.get_element('view[id="newHouseBanner-ckmore"]').tap()

        self.get_screenshot()

    def test_goto_command_house(self):
        """
        帖子详情页，点击热门新房模块 第一个
        """
        self.page.get_element('view[class="commonNewHouseLi-l"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_goto_command_post(self):
        """
        帖子详情页，点击 相关推荐 第一条帖子
        """
        self.page.get_element('view[class="recommend_post_cont"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

