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
        print(self.page_name)
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

    def tearDown(self) -> None:
        self.delay(3)
        super(TestBase, self).tearDown()
        print("------tear Down test------")