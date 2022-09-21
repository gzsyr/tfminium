# add by zsy
import threading
import time

from ddt import ddt, file_data

from tfq.writepost import WritePost

@ddt
class TestTfqZygwWritePost(WritePost):
    """
    置业顾问身份发帖
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestTfqZygwWritePost, cls).setUpClass()
        cls().change_zygw()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/writePost/writePost?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqZygwWritePost, self).setUp()
        print("TestZygwWritePost setup")

    def test_zygw_02_save_draft_保存草稿(self):
        """
        置业顾问身份，发帖页面，点击“保存草稿”按钮
        """
        self.wp_input_title('置业顾问' + time.strftime('%Y-%m-%d--%H:%M:%S')).wp_input_content()

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

    def test_zygw_01_quanzi_show_my_fav_我关注的(self):
        """
        置业顾问身份，发帖页面，点击同步到圈子，展示“我关注的”内容列表
        """
        self.wp_quanzi_show_my_fav()

        self.verifyByScreenshot('tfq/test_yy_quanzi_show_my_fav.png')

    @file_data('./test_tfq_writepost_zygw.yml')
    def test_zygw_03_write_post_发布帖子(self, **kwargs):
        """
        置业顾问身份，发帖页面，输入标题，内容，选择关联板块，关联楼盘，同步到圈子，点击“发布”按钮
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

