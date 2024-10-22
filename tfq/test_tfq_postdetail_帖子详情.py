# add by zzh
import time

import minium

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

    def test_36_click_default_comment_默认评论图片(self):
        """
        V6.26.X: 1004927, 后台已添加默认评论, 点击默认评论图片
        """
        try:
            self.find_element('text[class="default_comments_addgroup"]').tap()
            self.get_screenshot()

        except minium.MiniElementNotFoundError:
            self.get_screenshot('test_35_click_default_comment_无默认评论按钮')

    def test_35_click_default_comment_默认评论按钮(self):
        """
        V6.26.X: 1004927, 后台已添加默认评论, 点击默认评论按钮
        """
        try:
            self.find_element('image[class="default_comments_img"]').tap()
            self.get_screenshot()
        except minium.MiniElementNotFoundError:
            self.get_screenshot('test_35_click_default_comment_无默认评论图片')

    def test_34_check_tuomin_脱敏号码(self):
        """
        V6.20.X: 查看详情页包含手机号码的正文
        """
        if self.get_wxBackgroundFetchData() == '1':
            self.get_screenshot()
        else:
            self.get_screenshot('test_34_check_tuomin_无脱敏号码')

    def test_09_click_content_and_reply_帖子评论(self):
        """
        帖子详情页，点击帖子正文，输入评论，发布成功，并点击该评论，进入评论详情页
        """
        content = '回复主评论'+time.strftime('%Y-%m-%d')

        # 点击正文，并输入评论
        # 如果此处修改，需要同步修改 test_jjr_ctiezi_帖子相关.py
        self.find_element('view[class="post_cont"]').tap()
        self.find_element('textarea[name="quick_reply_content"][placeholder="说点什么吧"]').\
            input(content)
        # tap = 'self.page.get_element(\'button[class="send-btn"]\').tap()'
        # self.verifyStr(True, self.getShowToast(tap), '发表主评论OK')
        self.find_element('button[class="send-btn"]').tap()
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

    def test_13_click_laud_帖子点赞(self):
        """
        帖子详情页，点击帖子点赞
        """
        tap = 'self.page.get_element(\'view[class="item laud"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), 'show toast')
        self.get_screenshot()

    def test_28_click_tipoff_举报(self):
        """
        帖子详情页，点击帖子"更多"-“举报”按钮，输入“其他”点击提交
        """
        # 点击“更多”
        self.find_element('view[class="item more-ctr"]').tap()
        # 点击“举报”
        self.find_element('view[class="quick-box-cont"]').tap()
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

    def del_test_15_click_newpost_最新热帖(self):
        """
        DEL V7.19
        帖子详情页，点击帖子"最新热帖"按钮，进入帖子详情页
        :return:
        """
        # e = self.page.get_element('view[class="toutiao-swiper-item tfLine1"]')
        self.page.scroll_to(500, 500)
        self.find_element('swiper-item[id="ontieziDetail"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_14_click_moren_默认排序(self):
        """
        帖子详情页，点击帖子"默认"按钮
        """
        self.find_element('view[class="moren_sort active_sort"]').tap()

        self.get_screenshot()

    def click_new_sort(self):
        """
        帖子详情页，点击帖子"最新"按钮
        """
        self.find_element('view[class="new_sort"]').tap()

    def test_10_click_fbsavator_房博士头像(self):
        """
        帖子详情页，点击房博士评论的头像，进入房博士主页
        """
        self.find_element('image[class="commentList--avator"][data-useridentity="fbs"]').tap()

        self.verifyPageName('/page/taofangquan/personalDetails/fbs/fbs')
        self.get_screenshot()

    def test_11_click_fbscontact_房博士联系(self):
        """
        帖子详情页，点击评论第一个房博士的“点击联系”按钮
        """
        self.page.scroll_to(2300, 500)
        self.find_element('view[class="commentList--contact-fbs commentList--fbs_contact_tap"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_29_click_zygwavator_置业顾问头像(self):
        """
        帖子详情页，点击置业顾问评论的头像，进入置业顾问主页
        """
        self.find_element('image[class="commentList--avator"][data-useridentity="zygw"]').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def test_30_click_zygwcontact_置业顾问IM(self):
        """
        帖子详情页，点击评论第一个置业顾问的“点击联系”按钮，进IM聊天
        """
        self.page.scroll_to(2300, 500)
        self.find_element('view[class="commentList--contact-fbs commentList--zygw_contact_tap"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def click_content_text(self):
        """
        帖子详情页，点击第一个评论的评论内容，进入评论详情页
        """
        self.find_element('navigator[class="commentList--content-rich-text"]').tap()

    def test_07click_commentlist_laud_评论点赞(self):
        """
        帖子详情页，点击第一个评论的点赞
        """
        self.verifyStr(True,
                       self.getShowToast('self.page.get_element(\'view[class="commentList--laud-btn"]\').tap()'),
                       '点赞校验ok')

        self.get_screenshot()

    def test_08_click_commentlist_reply_回复按钮评论(self):
        """
        帖子详情页，点击第一个评论的“回复”按钮，弹出回复框，回复内容，并发布
        :return:
        """
        content = '回复第一条主评论'+time.strftime('%Y-%m-%d')
        self.find_element('view[class="commentList--reply-btn"]').tap()

        # 输入评论
        zjele = self.find_element('comment-list').get_element('form')
        zjele.get_element('textarea[name="quick_reply_content"]').input(content)

        # iscall = self.getShowToast('self.page.get_element(\'button[class="commentList--send-btn"]\').tap()')
        # self.verifyStr(True, iscall, '发布完成的提示 ok')
        self.find_element('button[class="commentList--send-btn"]').tap()
        self.delay(1)

        # 验证查看第一条评论的回复评论
        self.verifyStr(content, self.find_element('view[class="commentList--reply-content"]').inner_text,
                       '第一个主评论的回复ok')

        self.get_screenshot()

    def test_22_click_replycontent_发布评论回复(self):
        """
        帖子详情页，点击第一个评论的回复内容，弹出“回复、删除”框，点击“回复”，输入“test_click_replydelete”并发布
        """
        content = 'test_click_replydelete'
        self.find_element('view[class="commentList--reply-content"]').tap()
        self.delay(1)
        self.find_element('view[class="commentList--quick-box-cont commentList--quick-box-edit"]', inner_text='回复').tap()
        # print(self.page.get_element('comment-list').inner_wxml)

        # 输入评论
        zjele = self.find_element('comment-list').get_element('form')
        zjele.get_element('textarea[name="quick_reply_content"]').input(content)

        # iscall = self.getShowToast('self.page.get_element(\'button[class="commentList--send-btn"]\').tap()')
        # self.verifyStr(True, iscall, '发布完成的提示 ok')
        self.find_element('button[class="commentList--send-btn"]').tap()
        self.delay(1)

        self.get_screenshot()

    def test_23_click_replydelete_删除评论回复(self):
        """
        帖子详情页，点击第一个评论的回复内容，弹出“回复、删除”框，点击“删除”，确认删除
        """
        content = 'test_click_replydelete'
        self.find_element('view[class="commentList--reply-content"]', text_contains=content).tap()
        self.delay(1)
        self.find_element('view[class="commentList--quick-box-cont commentList--quick-box-delete"]',
                              inner_text='删除').tap()
        self.find_element('view[class="commentList--quick-box-cont commentList--quick-box-delete"]',
                              inner_text='删除回复').tap()
        self.delay(2)
        self.verifyStr(False,
                       self.page.element_is_exists('view[class="commentList--reply-content"]', text_contains=content),
                       '删除第一个主评论的第一个回复完成ok')

        self.get_screenshot()

    def test_19_click_reply_more_评论全部回复(self):
        """
        帖子详情页，点击评论的"查看全部X条回复"，弹出全部回复
        """
        if self.page.element_is_exists('view[class="commentList--more-reply"]'):
            self.find_element('view[class="commentList--more-reply"]').tap()

        self.get_screenshot()

    def test_21_click_reply_more_laud_全部回复点赞(self):
        """
        帖子详情页，点击评论的“查看全部x条回复”，如有，弹出全部回复，点击第一条的点赞
        """
        if self.page.element_is_exists('view[class="commentList--more-reply"]'):
            self.find_element('view[class="commentList--more-reply"]').tap()
            self.delay(1)
            tap = 'self.page.get_element(\'view[class="commentList--laud-btn"][data-laudtype="son_all"]\').tap()'
            self.verifyStr(True, self.getShowToast(tap), '点赞OK')

        self.get_screenshot()

    def test_17_click_replay_more_content_reply_全部回复框(self):
        """
        帖子详情页，点击评论的“查看全部x条回复”，如有，弹出全部回复，点击第一条内容，弹出回复框
        """
        if self.page.element_is_exists('view[class="commentList--more-reply"]'):
            self.find_element('view[class="commentList--more-reply"]').tap()
            self.delay(1)

            e = self.find_element('view[class="commentList--comment-item"][data-replytype="allReply"]')
            e.get_element('view[class="commentList--reply-content"]').tap()

        self.get_screenshot()

    def test_20_click_reply_more_fabu_全部回复按钮(self):
        """
        帖子详情页，点击评论的“查看全部x条回复”，如有，弹出全部回复，点击下方回复按钮，弹出回复框
        """
        if self.page.element_is_exists('view[class="commentList--more-reply"]'):
            self.find_element('view[class="commentList--more-reply"]').tap()
            self.delay(1)

            self.find_element('view[class="commentList--m-name"]').tap()

        self.get_screenshot()

    def test_18_click_reply_laud_回复点赞(self):
        """
         帖子详情页，点击第一个评论的回复的点赞按钮\
        """
        tap = 'self.page.get_element(\'view[class="commentList--laud-btn"][data-laudtype="son"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '第一个评论的第一个回复点赞ok')
        self.get_screenshot()

    def test_24_click_returnPl_更多热帖(self):
        """
        帖子详情页，点击“更多热帖”按钮
        :return:
        """
        self.find_element('image[class="returnPl"]').tap()

        self.verifyPageName('/page/find/find')
        self.get_screenshot()

    def test_33_goto_housedetail_楼盘卡片(self):
        """
        帖子详情页，点击楼盘卡片，进入楼盘详情页
        :return:
        """
        exist = self.page.element_is_exists('view[class="lpcard_wrap tfFlex"]')
        if exist:
            self.find_element('view[class="lpcard_hname tfLine1"]').tap()

            self.verifyPageName('/page/newhouse/detail')
        else:
            print("本帖子没有带楼盘名片，该用例直接pass")

        self.get_screenshot()

    def delete_test_01_click_add_加入群聊(self):
        """
        V6.44.x: delete
        帖子详情页，点击“加入群聊”入口，进入配置的页面
        """
        self.find_element('view[class="add_jqbtn"]').tap()

        self.get_screenshot()

    def delete_test_02_click_add_close_关闭群聊入口(self):
        """
        V6.44.x: delete
        帖子详情页，点击“加入群聊”入口的关闭按钮
        """
        self.find_element('view[class="close"]').tap()

        self.get_screenshot()

    def test_12_click_fix_input_发布评论入口(self):
        """
        帖子详情页，点击底部发布评论入口，弹出回复框
        """
        self.find_element('view[class="detail-fix-input"]').tap()

        self.get_screenshot()

    def delete_test_03_click_addgroup_购房群(self):
        """
        帖子详情页，点击底部“购房群”按钮
        :return:
        V6.34.X: delete
        """
        self.find_element('view[class="item bottom-add-group"]').tap()

        self.get_screenshot()

    def test_06_click_collect_底部收藏(self):
        """
        帖子详情页，点击底部“收藏”按钮
        """
        # e = self.page.get_element('view[class="item bottom-collect is_collect"]')
        # e.tap()
        # 收藏和未收藏显示的上面class不一样，更新为下面的方法
        self.find_element('view[class="text"]', inner_text="收藏").tap()

        self.get_screenshot()

    def test_04_click_bottom_laud_底部点赞(self):
        """
        帖子详情页，点击底部“点赞”按钮
        :return:
        """
        self.find_element('view[class="item bottom-laud"]').tap()

        self.get_screenshot()

    def test_05_click_bottom_zygwim_置业顾问IM(self):
        """
        帖子详情页，点击底部“置业顾问在线咨询”按钮，如无，则通过
        """
        exist = self.page.element_is_exists('image[class="bottom-connect-avatar"]')
        if exist:
            self.find_element('image[class="bottom-connect-avatar"]').tap()

            self.delay(6)
            self.verifyPageName('/im/pages/chating/chating')
        else:
            print("本帖子没有配置关联置业顾问，该用例直接pass")

        self.get_screenshot()

    def delete_test_25_click_share_分享(self):
        """
        帖子详情页，点击”分享“按钮
        V6.34.X: delete
        """
        self.find_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(1)

        self.verifyByScreenshot('tfq/test_click_post_share.png')

    def delete_test_26_click_share_close_分享后取消(self):
        """
        帖子详情页，点击”分享“按钮，点击取消按钮
        :return:
        V6.34.X: delete
        """
        self.find_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(1)
        self.find_element('view[class="closeBtn"]').tap()

        self.get_screenshot()

    def delete_test_27_click_share_hb_分享海报(self):
        """
        帖子详情页，点击”分享“按钮，点击海报
        :return:
        V6.34.X: delete
        """
        self.delay(2)
        self.find_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(1)
        self.find_element('button[class="share-btn pyq"]').tap()
        self.delay(2)
        self.verifyStr(True,
                       self.page.element_is_exists('button[class="canvasToImage--saveToAlbumButton"]'),
                       '生成海报页 ok')
        self.get_screenshot()

    def delete_test_98_z_click_share_hy_分享好友(self):
        """
        帖子详情页，点击”分享“按钮，点击分享给好友
        V6.34.X: delete
        """
        self.find_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(1)
        self.find_element('button[class="share-btn hy"]').tap()

        self.get_screenshot()

    def del_test_16_click_newpost_more_最新热帖更多(self):
        """
        del v7.19
        帖子详情页，点击最新热帖的，“更多”按钮\
        """
        self.page.scroll_to(500, 500)
        self.find_element('view[id="goTieZiList"]').tap()

        self.verifyPageName('/page/taofangquan/tieziList/tieziList')
        self.get_screenshot()

    def test_99_z_click_allpicture_查看完整图片(self):
        """
        帖子详情页，点击“查看完整图片”按钮
        """
        self.find_element('view[id="newHouseBanner-ckmore"]').tap()

        self.get_screenshot()

    def test_31_goto_command_house_热门新房(self):
        """
        帖子详情页，点击热门新房模块 第一个
        """
        self.find_element('view[class="commonNewHouseLi-l"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_32_goto_command_post_相关推荐(self):
        """
        帖子详情页，点击 相关推荐 第一条帖子
        """
        self.delay(3)
        self.find_element('view[class="recommend_post_cont"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

