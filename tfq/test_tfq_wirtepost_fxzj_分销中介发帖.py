# add by zsy
import threading
import time

import minium
from ddt import ddt, file_data

from tfq.writepost import WritePost

@ddt
class TestTfqFxzjWritePost(WritePost):
    """
    分销中介身份发帖
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestTfqFxzjWritePost, cls).setUpClass()
        cls().change_fxzj()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/writePost/writePost?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqFxzjWritePost, self).setUp()
        print("TestFxzjWritePost setup")

    def del_test_fxzj_06_带入内容库(self):
        """
        V6.30.X: 1005035, 分销中介发帖页面，点击底部“内容库”, 进入内容库列表，点击“生成帖子”
        """
        self.click_sucaiku()

        try:
            self.select_sucaiku()
            self.verifyPageName('/page/taofangquan/writePost/writePost')
        except minium.MiniElementNotFoundError:
            print('没有内容库')

        self.get_screenshot()

    def del_test_fxzj_08_内容库点击正文(self):
        """
        V6.30.X: 1005035, 分销中介发帖页面，点击底部“内容库”, 点击正文
        """
        self.find_element('button[class="content-store"]').tap()
        self.delay(5)

        try:
            self.find_element('text[class="content tfline3"]').tap()
            self.delay(3)
            self.verifyPageName('/page/taofangquan/contentstore/storedetail')
        except minium.MiniElementNotFoundError:
            print('没有内容库')

        self.get_screenshot()

    def del_test_fxzj_07_内容库查看详情(self):
        """
        V6.30.X: 1005035, 分销中介发帖页面，点击底部“内容库”, 点击“查看详情”按钮
        """
        self.find_element('button[class="content-store"]').tap()
        self.delay(5)

        try:
            self.find_element('view[class="toDetail"]', inner_text='查看详情').tap()
            self.delay(3)
            self.verifyPageName('/page/taofangquan/contentstore/storedetail')
        except minium.MiniElementNotFoundError:
            print('没有内容库')

        self.get_screenshot()

    def del_test_fxzj_09_内容库一键生成帖子(self):
        """
        V6.30.X: 1005035, 分销中介发帖页面，点击底部“内容库”, 点击“查看详情”按钮，点击‘一键生成帖子’
        """
        self.find_element('button[class="content-store"]').tap()
        self.delay(5)

        try:
            self.find_element('view[class="toDetail"]', inner_text='查看详情').tap()
            self.delay(3)
            self.find_element('view[class="btn"]', inner_text='一键生成帖子').tap()
            self.verifyPageName('/page/taofangquan/writePost/writePost')
        except minium.MiniElementNotFoundError:
            print('没有内容库')

        self.get_screenshot()

    def del_test_fxzj_10_内容库发布帖子(self):
        """
        V6.30.X: 1005035, 分销中介发帖页面，点击底部“内容库”, 点击“查看详情”按钮，点击‘一键生成帖子’，点击“发布”
        """
        self.find_element('button[class="content-store"]').tap()
        self.delay(5)

        try:
            self.find_element('view[class="toDetail"]', inner_text='查看详情').tap()
            self.delay(3)
            self.find_element('view[class="btn"]', inner_text='一键生成帖子').tap()
            self.delay(2)
            self.find_element('button[class="submit-btn"]').tap()
        except minium.MiniElementNotFoundError:
            print('没有内容库')

        self.get_screenshot()

    def test_fxzj_02_save_draft_保存草稿(self):
        """
        分销中介身份，发帖页面，点击“保存草稿”按钮
        """
        self.wp_input_title('分销中介' + time.strftime('%Y-%m-%d--%H:%M:%S')).wp_input_content()

        # 监听回调, 阻塞当前主线程
        called = threading.Semaphore(0)
        callback_args = None

        def callback(args):
            nonlocal callback_args
            called.release()
            callback_args = args

        self.app.hook_wx_method("showToast", callback=callback)
        self.wp_save_draft()
        is_called = called.acquire(timeout=5)
        self.app.release_hook_wx_method("showToast")

        self.verifyStr(True, is_called, "toast called ")
        self.get_screenshot()

    def test_fxzj_01_quanzi_show_my_fav_我关注的(self):
        """
        分销中介身份，发帖页面，点击同步到圈子，展示“我关注的”内容列表
        """
        self.wp_quanzi_show_my_fav()


        # self.verifyByScreenshot('tfq/test_yy_quanzi_show_my_fav.png')
        self.verifyStr(True, self.element_is_exist('view[class="quick_unm_choose flex tfAlignC tfFlexC"]/view', text_contains='我订阅的'))

    @file_data('./test_tfq_writepost_fxzj.yml')
    def test_fxzj_03_write_post_发布帖子(self, **kwargs):
        """
        分销中介身份，发帖页面，输入标题，内容，选择关联板块，关联楼盘，同步到圈子，点击“发布”按钮
        """
        self.wp_input_title(kwargs['title']).\
            wp_input_content(kwargs['content']).\
            wp_choose_bk().\
            wp_choose_lp(kwargs['lpname']).\
            wp_choose_quanzi(kwargs['quanzi']).\
            wp_submit()

        self.goto_post_detail()
        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def del_test_fxzj_05_write_pk_发布PK(self, **kwargs):
        """
        V6.26.X: 1004926, 分销中介，带pk插件，成功发帖
        """
        kwargs['title'] = 'PK插件'
        kwargs['content'] = '这是分销中介发布的含有PK插件帖子'
        self.wp_input_title(time.strftime('%Y-%m-%d') + kwargs['title']).wp_input_content(kwargs['content'])

        # 输入PK
        self.write_pk()
        self.wp_submit()

        self.goto_post_detail()
        self.delay(3)
        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()


    @file_data('./test_tfq_writepost_yunying_vote.yml')
    def del_test_fxzj_04_write_vote_post_发布投票(self, **kwargs):
        """
        V6.26.X: 1004926, 分销中介，发帖页面，输入标题，内容，新增投票，点击“发布”按钮
        """
        self.wp_input_title(time.strftime('%Y-%m-%d')+kwargs['title']).wp_input_content(kwargs['content'])

        # 输入投票
        self.yy_write_vote(title=time.strftime('%Y-%m-%d')+kwargs['votetitle'],
                           ipt=kwargs['votelist'],
                           ismultiple=kwargs['ismultiple'])
        self.wp_submit()

        self.goto_post_detail()
        self.delay(3)
        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_11_新房二手房切换(self):
        """
        V6.38.X: 切换新房 二手房tab
        """
        self.wp_change_esftab()

        self.get_screenshot()