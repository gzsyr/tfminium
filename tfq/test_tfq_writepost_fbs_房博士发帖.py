# add by zzh
import threading
import time

from ddt import ddt, file_data

from tfq.writepost import WritePost


@ddt
class TestTfqFbsWritePost(WritePost):
    """
    房博士身份发帖
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestTfqFbsWritePost, cls).setUpClass()
        cls().change_fbs()
        print("TestFbsWritePost setupclass")

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/writePost/writePost?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqFbsWritePost, self).setUp()
        print("TestFbsWritePost setup")

    def test_fbs_02_save_draft_保存草稿(self):
        """
        房博士身份，发帖页面，点击“保存草稿”按钮
        """
        self.wp_input_title('房博士' + time.strftime('%Y-%m-%d--%H:%M:%S')).wp_input_content()

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

    def test_fbs_01_quanzi_show_my_fav_我关注的(self):
        """
        房博士身份，发帖页面，点击同步到圈子，展示“我关注的”内容列表
        """
        self.wp_quanzi_show_my_fav()


        # self.verifyByScreenshot('tfq/test_yy_quanzi_show_my_fav.png')
        self.verifyStr(True, self.element_is_exist('view[class="quick_unm_choose flex tfAlignC tfFlexC"]/view', text_contains='我订阅的'))

    @file_data('./test_tfq_writepost_fbs.yml')
    def test_fbs_03_write_post_发布帖子(self, **kwargs):
        """
        房博士身份，发帖页面，输入标题，内容，选择关联板块，关联楼盘，同步到圈子，点击“发布”按钮
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

    def test_fbs_05_write_pk_发布PK(self, **kwargs):
        """
        V6.26.X: 1004926, 房博士，带pk插件，成功发帖
        """
        kwargs['title'] = 'PK插件'
        kwargs['content'] = '这是房博士发布的含有PK插件帖子'
        self.wp_input_title(time.strftime('%Y-%m-%d') + kwargs['title']).wp_input_content(kwargs['content'])

        # 输入PK
        self.write_pk()
        self.wp_submit()

        self.goto_post_detail()
        self.delay(3)
        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()


    @file_data('./test_tfq_writepost_yunying_vote.yml')
    def test_fbs_04_write_vote_post_发布投票(self, **kwargs):
        """
        V6.26.X: 1004926, 房博士，发帖页面，输入标题，内容，新增投票，点击“发布”按钮
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

