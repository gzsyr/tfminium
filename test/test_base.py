# add by zsy
import inspect
import time

import minium


class TestBase(minium.MiniTest):
    """
    继承自minitest的testbase类，后面所有测试类均继承自该类
    """

    # 打開的頁面名称
    page_name = '/page/index/index'
    # 切换页面的方式，False使用navigate_to，True使用switch_to
    switch = False

    # 以下id的相关参数，根据online、dev来选择或者设置
    # 帖子的id
    # postid = 12746 # online
    postid = 3387 # dev

    # 帖子评论的id
    # pinglunid = 47170 # online
    pinglunid = 7887 # dev

    # 话题的id
    # huatiid = 11536 # online
    huatiid = 3393 # dev

    # 圈子的id
    # quanzi = 751  # online
    quanzi = 430  # dev

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
            self.app.navigate_to(self.page_name)
        self.delay(3)
        self.app.get_current_page()
        print("++++++set up test+++++++")

    def delay(self, second):
        time.sleep(second)
        return self

    def verifyStr(self, first, second, msg, capture=True):
        """
        结果校验
        first: 实际字串
        second: 目标字串
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
                self.capture(inspect.stack()[1].function)
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
                self.capture(inspect.stack()[1].function)
            raise e

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
        print("------tear Down test------")