from ddt import file_data
from minium import ddt_class, ddt_case
from minium.miniprogram.base_driver import page

from base.common import delay
from base.test_base import TestBase


@ddt_class()
class Testesfwd(TestBase):
    """
    二手房首页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/detail/detail?sellId=329209949"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfwd, self).setUp()
        print("Testesfwd setup")

    def test_goto_share(self):
        """
        点击分享
        :return:
        """
        e = self.page.get_element('button[class="button"]')
        e.tap()
        #self.get_capture()
        self.get_screenshot()
        delay(5)