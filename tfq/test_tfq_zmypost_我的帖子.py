# add by zsy
import time

from base.test_base import TestBase


class TestTfqMyPost(TestBase):
    """
    进入我的帖子页面
    """
    third = ''
    title = ''

    def setUp(self) -> None:
        self.page_name = "/page/mine/myTopic/myTopic?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqMyPost, self).setUp()
        self.third = self.get_third_title()
        self.title = '编辑' + self.third + time.strftime('%Y-%m-%d')

    def click_post(self, text_contains=None):
        """
        点击帖子、帖子详情页“更多”
        """
        self.find_element('view[class="list-desc disflex-flex-shrink-0 flex-1"]',
                              text_contains=text_contains).tap()
        self.delay(4)
        # 点击 更多
        self.page.get_element('view[class="item more-ctr"]', text_contains='更多').tap()
        self.delay(1)
        return self

    def test_02_my_goto_postdetail_01_edit_编辑帖子(self):
        """
        我的帖子页面，对当前身份刚刚发的贴，选择对应帖子，进入帖子详情，进行编辑，保存
        :return:
        """
        self.click_post(self.third)
        # 点击 编辑
        self.page.get_element('view[class="quick-box-cont"]', inner_text='编辑').tap()
        self.verifyPageName('/page/taofangquan/writePost/editPost')

        # 更新标题
        self.page.get_element('textarea[class="tip"]').input(self.title)
        # 点击 发布 按钮
        tap = 'self.page.get_element(\'button[class="submit-btn"]\').tap()'
        self.getShowToast(tap)
        # 点击’查看发布详情'
        self.page.get_element('navigator[class="backTieZiDetailBtn"]').tap()
        self.delay(3)
        self.verifyStr(True,
                       self.page.element_is_exists('view[class="post_Title"]', text_contains='编辑'),
                       '编辑标题ok')
        self.get_screenshot()

    def test_03_my_goto_postdetail_02_delete_删除帖子(self):
        """
        我的帖子页面，对当前身份刚刚发布编辑的贴，根据当前身份，选择对应帖子，进入帖子详情，点击更多  删除
        """
        self.click_post(self.title)
        # 点击 删除
        self.page.get_element('view[class="quick-box-cont quick-box-delete"]', inner_text='删除').tap()
        # 确认框点击“删除帖子”
        tap = 'self.page.get_element(\'view[class="quick-box-cont quick-box-delete"]\', inner_text=\'删除帖子\').tap()'
        self.getShowToast(tap)

        self.get_screenshot()

    def test_01_my_click_quanzi_点击圈子(self):
        """
        我的帖子页面，点击我的帖子，进入点击圈子名称，进入圈子详情
        :return:
        """
        self.page.get_element('view[class="posttag flex tfAlignC"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

