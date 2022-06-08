# add by zsy
import time

import minium


class TestBase(minium.MiniTest):
    """
    继承自minitest的testbase类，后面所有测试类均继承自该类
    """

    # 打開的頁面名称
    page_name = '/page/index/index'
    # 切换页面的方式，True使用navigate_to，False使用switch_to
    switch = False

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
        return self.page.get_element(selector=selector, inner_text=inner_text)

    def tearDown(self) -> None:
        self.delay(3)
        super(TestBase, self).tearDown()
        print("------tear Down test------")