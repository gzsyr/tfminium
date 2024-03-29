from minium import ddt_class

from base.test_base import TestBase
from base.test_mine import TestMine


@ddt_class()
class Testesfbroker(TestMine):
    """
    经纪人店铺
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(Testesfbroker, cls).setUpClass()
        cls().change_C()
        print("setupclass Testesfbroker")

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/broker/broker?uid=1000947&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfbroker, self).setUp()
        print("Testesfbroker setup")

    def test_01_broker_selldetail_二手房列表进入详情页(self):
        """
        点击房源列表进入房源详情页
        :return:
        """
        #types = self.page.element_is_exists('//view[@class="flex types"]')
        selltab = self.page.element_is_exists('//view[@class="list"]')
        selltext = self.page.element_is_exists('text', inner_text="二手房")
        if selltext == True:
            if selltab == True:
                s_t = self.page.get_element('//view[2]/view')
                s_t.tap()
                self.delay(2)
                elm_items = self.page.get_elements('view[class="item"]')
                elm_first_item = elm_items[0]
                elms = elm_first_item.get_element('sellitem').get_elements('view')
                elms[0].tap()
                self.verifyPageName('/esf/sell/pages/detail/detail', '房源详情 ok')
                self.delay(5)
                self.get_screenshot()
            else:
                print("没有列表数据")
        else:
            print("没有二手房房源")


    def test_02_broker_rentdetail_租房列表进入详情页(self):

        """
        租房tab进入详情
        :return: 
        """
        try:
            self.find_element('view[class="center type"]').tap()
            self.delay(2)
            self.find_element('image[class="rentItem--img"]').tap()
        except:
            print("没有租房房源")
        self.get_screenshot()


    def test_03_click_btnmsg_点击在线聊(self):
        """
        点击在线聊
        :return:
        """
        self.find_element('view[class="center btn msg positionRel"]').tap()
        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_04_click_btntel_点击打电话(self):
        """
        点击打电话
        :return:
        """
        self.find_element('view[class="center btn tel positionRel"]').tap()
        self.get_screenshot()