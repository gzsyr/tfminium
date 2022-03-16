import os
import time

import minium

from test.common import delay


class TestFirst(minium.MiniTest):

    # def test_get_system_info(self):
    #     print(self.mini.call_wx_method("getSystemInfo"))

    def setUp(self) -> None:
        page = self.app.get_current_page()

    def test_find_xf(self):
        """
        点击首页->功能入口->新房
        :return:
        """
        print("----------------------------")
        ele = self.page.get_element("view[class='myiconTwoLi index_xf']")
        print("xf: ", ele)
        ele.tap()
        delay(2)

    def test_find_esf(self):
        """
        点击首页->功能入口->二手房
        :return:
        """
        ele = self.page.get_element("view[class='myiconTwoLi index_esf']")
        print("esf: ", ele)
        ele.tap()
        delay(2)

    def test_goto_sellhouse(self):
        """
        点击首页->功能入口->我要卖房
        :return:
        """
        ele = self.page.get_element("view[class='myiconTwoLi index_sell']")
        ele.tap()
        delay(2)

    def test_goto_error(self):
        """
        测试用例失败
        :return:
        """
        ele = self.page.get_element("dddddd")
        delay(2)

# if __name__ == "__main__":
#     import unittest
#     loaded_suite = unittest.TestLoader().loadTestsFromTestCase(TestFirst)
#     result = unittest.TextTestRunner.run(loaded_suite)