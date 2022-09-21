from minium import ddt_class

from base.common import delay
from base.test_base import TestBase


@ddt_class()
class Testesfbroker(TestBase):
    """
    经纪人店铺
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/broker/broker?uid=892737"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfbroker, self).setUp()
        print("Testesfbroker setup")

    def test_broker_housedetail(self):
        """
        点击房源列表进入房源详情页
        :return:
        """
        elm_items = self.page.get_elements('view[class="item"]')
        elm_first_item = elm_items[0]
        elms = elm_first_item.get_element('sellitem').get_elements('view')
        elms[0].tap()
        self.verifyPageName('/esf/sell/pages/detail/detail', '房源详情 ok')
        delay(5)
        self.get_screenshot()

    def test_btnmsg(self):
        """
        点击在线聊
        :return:
        """
        self.page.get_element('view[class="center btn msg"]').tap()
        delay(5)
        self.get_screenshot()

    def test_btntel(self):
        """
        点击打电话
        :return:
        """
        self.page.get_element('view[class="center btn tel"]').tap()
        delay(2)
        self.get_screenshot()
        delay(5)