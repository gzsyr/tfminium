# -*- coding:utf-8 -*-
# add by zsy
import threading
import time

from base.test_base import TestBase


class TestFuncXxts(TestBase):
    """
    消协投诉页
    """
    def setUp(self) -> None:
        self.page_name = '/page/complaintSite/index?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncXxts, self).setUp()
        print('TestFuncXxts setup test')

    def test_submit(self):
        """
        消协投诉页面，提交投诉内容
        """
        cont = 'test_submit' + time.strftime('%Y-%m-%d')
        self.page.get_element('textarea').input(cont)

        # 监听回调, 阻塞当前主线程
        called = threading.Semaphore(0)
        callback_args = None
        def callback(args):
            nonlocal callback_args
            called.release()
            callback_args = args

        self.app.hook_wx_method("showToast", callback=callback)
        self.page.get_element('view[class="submit-btn"]').click()
        is_called = called.acquire(timeout=5)
        self.app.release_hook_wx_method("showToast")

        self.verifyStr(True, is_called, "toast called ")
        self.get_capture()

    def test_fbs_im(self):
        """
        消协投诉页，点击房博士咨询im
        """
        self.page.get_element('view[class="im-icon"]').click()
        self.delay(1)
        # 验证
        self.verifyPageName('/im/pages/chating/chating')
        self.get_capture()

    def test_fbs_call(self):
        """
        消协投诉页，点击房博士 拨打电话按钮
        """
        # 监听回调, 阻塞当前主线程

        self.page.get_element('view[class="tel-icon"]').tap()

        self.delay(1)
        self.verifyByScreenshot('xf/call.png')