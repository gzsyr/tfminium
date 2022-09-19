# add by zsy
import inspect
import os
import threading
import time

import allure
import minium
import pyautogui


class TestBase(minium.MiniTest):
    """
    继承自minitest的testbase类，后面所有测试类均继承自该类
    """
    # 当前测试类的类名(截图是需用到)，定在setup的时候，赋值self.__class__.__name__
    classname = None

    # 鼠标m、键盘k的实例，在需要使用到的地方，先判定下如果为None，需要m=PyMouse()，k=PyKeyboard()
    m = None
    k = None

    # 打開的頁面名称
    page_name = '/page/index/index'
    # 切换页面的方式，False使用navigate_to，True使用switch_to
    switch = False

    # 以下id的相关参数，根据online、dev来选择或者设置
    # 帖子的id
    postid = 12746 # online
    # postid = 3387 # dev

    # 帖子评论的id
    pinglunid = 47170 # online
    # pinglunid = 7887 # dev

    # 话题的id
    huatiid = 11536 # online
    # huatiid = 3393 # dev

    # 圈子的id
    quanzi = 751  # online
    # quanzi = 430  # dev

    # 房博士页面，房博士的uid 和roleid
    fbs_uid = 3403749
    fbs_roleid = 1081

    @classmethod
    def setUpClass(cls) -> None:
        super(TestBase, cls).setUpClass()
        print("******set up class******")

    def setUp(self) -> None:
        """
        测试用例执行前的准备工作，此处主要指进入测试用例的页面
        :return:
        """
        super(TestBase, self).setUp()
        if self.switch:
            self.app.switch_tab(self.page_name)
        else:
            # self.app.navigate_to(self.page_name)
            rp = self.app.relaunch(self.page_name)

            if rp.path != self.page_name.split("?")[0]:
                print(rp.path, 'need to relaunch')
                self.delay(1)
                self.app.relaunch(self.page_name)
        self.delay(3)

        print("++++++set up atest+++++++")

    def delay(self, second):
        time.sleep(second)
        return self

    def getShowToast(self, eval_method):
        """
        捕获 showToast的弹框
        eval_method: 需要点击的元素与操作
        return: True-捕获成功，False-捕获失败
        """
        # 监听回调, 阻塞当前主线程
        called = threading.Semaphore(0)
        callback_args = None

        def callback(args):
            nonlocal callback_args
            called.release()
            callback_args = args

        self.app.hook_wx_method("showToast", callback=callback)
        # self.page.get_element('view[class="laud-btn"]').tap()
        eval(eval_method)
        is_called = called.acquire(timeout=5)
        self.app.release_hook_wx_method("showToast")

        return is_called

    def set_pick_filter(self, selector, value):
        """
        picker选择器的选择
        selector: 元素选择器
        value: 选择的pick数值
        """
        ele = self.page.get_element(selector)
        ele.click()
        ele.pick(value)
        return self

    def input_value_by_mk(self, png, value=None):
        """
        通过键盘鼠标来输入内容
        png: 需要比对的截图，文件放在xf里面，则为: xf/xxx.png
        value: 需要键盘输入的内容
        """
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), png)
        print(path)
        btm = pyautogui.locateOnScreen(path, confidence=0.8)
        # btm = pyautogui.locateCenterOnScreen(path)
        print(btm)

        if btm is None:
            # 如果比对的图没有在屏幕上面找到 assert
            pyautogui.screenshot(png[(png.find('/')+1):-4]+'-assert.png')
            self.verifyStr(True, False, f'获取pyautogui.locateOnScreen {png} is None')
            return self

        # from pymouse import PyMouse
        # if self.m is None:
        #     self.m = PyMouse()
        # self.m.click(btm[0], btm[1])
        pyautogui.click(btm[0], btm[1])

        # self.delay(1)
        # from pykeyboard import PyKeyboard
        # if self.k is None:
        #     self.k = PyKeyboard()
        if value is not None:
        #     self.k.type_string(value)
              pyautogui.write(value)
        return self

    def verifyByScreenshot(self, png):
        """
        页面图片对比
        png: 需要比对的截图，文件放在xf里面，则为: xf/xxx.png
        """
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), png)
        print(path)
        btm = pyautogui.locateOnScreen(path, confidence=0.8)
        print(btm)

        self.get_screenshot(pname=inspect.stack()[1].function)

        if btm is None:
            # 如果比对的图没有在屏幕上面找到 assert
            raise self.failureException

    def get_screenshot(self, pname=None):
        """
        使用pyautogui的截图，将整个屏幕截屏
        """
        self.delay(1)
        if pname:
            name = pname + time.strftime('-%H-%M-%S')
        else:
            name = inspect.stack()[1].function + time.strftime('-%H-%M-%S')

        filename = "%s.png" % name
        screen_dir = './screenshot/' + self.classname
        path = os.path.join('./screenshot/'+self.classname, filename)
        if not os.path.exists(screen_dir):
            os.makedirs(screen_dir)
        pyautogui.screenshot(path)

        with open(path, "rb") as f:
            content = f.read()
        allure.attach(content, name=name, attachment_type=allure.attachment_type.PNG)

        return

    def verifyContainsStr(self, member, container, msg=None, capture=True):
        """
        结果包含关系校验
        member: 匹配的关键词
        container: 需要校验的内容
        msg: 匹配结果文案
        capture: 是否截图
                  True--默认截图
                  False--无需截图
        """
        try:
            self.assertIn(member, container, msg)
        except self.failureException as e:
            if capture:
                # self.capture(inspect.stack()[1].function)
                self.get_capture(verifyerr=True, fname=inspect.stack()[1].function)
            raise e

    def verifyStr(self, first, second, msg=None, capture=True):
        """
        结果校验
        first: 实际结果，支持bool
        second: 目标结果，支持bool
        msg: 匹配结果文案
        capture: 是否截图
                  True--默认截图
                  False--无需截图
        """
        try:
            self.assertEqual(first, second, msg)
        except self.failureException as e:
            # print("-------------------", inspect.stack())
            # name = inspect.stack()[1].function
            # print("********************", name)
            if capture:
                # self.capture(inspect.stack()[1].function)
                self.get_capture(verifyerr=True, fname=inspect.stack()[1].function)
            raise e

    def verifyPageName(self, pagename, capture=True):
        """
        对进入pagename的页面路径校验
        pagename: 目标页面名称
        capture: 是否截图
                  True--默认截图
                  False--无需截图
        """
        ret = self.app.wait_for_page(pagename)
        try:
            self.assertTrue(ret, f"wait {pagename} success")
            self.assertEqual(self.app.current_page.path, pagename, f"goto {pagename} OK")
        except self.failureException as e:
            if capture:
                # self.capture(inspect.stack()[1].function)
                self.get_capture(verifyerr=True, fname=inspect.stack()[1].function)
            raise e

    def get_capture(self, verifyerr=False, fname=None):
        """
        抓取当前页面截图
        verifyerr: 供assert出错时使用
                   False：非assert的时候使用
                   True： assert的时候使用
        fname: 供assert出错时使用，当verifyerr=True时有效
        """
        self.delay(1)
        # 抓取的文件名称，已测试用例命名
        if verifyerr:
            name = 'assert-' + fname + time.strftime('-%H-%M-%S')
        else:
            name = inspect.stack()[1].function + time.strftime('-%H-%M-%S')

        filename = "%s.png" % name
        screen_dir = './screenshot/' + self.classname
        path = os.path.join('./screenshot/'+self.classname, filename)
        if not os.path.exists(screen_dir):
            os.makedirs(screen_dir)
        self.native.screen_shot(path)
        return

    def get_third_title(self):
        """
        获取当前登录用户的身份
        """
        sf = {'fbs': '房博士', 'yunying': '运营', 'zygw': '置业顾问'}
        result = self.app.call_wx_method('getStorageSync', 'userInfoNew').\
            get('result').get('result').get('third_data')

        if result:
            # third = result.get('qz')['third_title']
            sf_tmp = result.get('qz')['third_identity']
            third = sf[sf_tmp]
            print('getStorageSync: ', third)
            return third
        else:
            return 'C端用户'

    def element_is_exist(self, selector=None, inner_text=None):
        """
        查找是否存在某个元素，参数目前就只支持selector和inner_text，后期慢慢增加
        :param selector: 查找元素的selector
        :param inner_text:  包含的text
        :return:
        """
        return self.page.element_is_exists(selector=selector, inner_text=inner_text)

    def find_element(self, selector=None, inner_text=None):
        """
        查找某个元素，参数目前就只支持selector和inner_text，后期慢慢增加
        :param selector: 查找元素的selector
        :param inner_text:  包含的text
        :return:
        """
        print("start: find_element")
        ele = self.page.get_element(selector=selector, inner_text=inner_text)
        print("end: find_element")
        return ele

    def tearDown(self) -> None:
        self.delay(1)
        super(TestBase, self).tearDown()
        print("------tear Down atest------")