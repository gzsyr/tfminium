from ddt import file_data, ddt
from minium import ddt_class, ddt_case

from base.common import delay
from base.test_base import TestBase

@ddt
class Testrentofficebgdetail(TestBase):
    """
    办公楼盘详情页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/detail/building/building?type=1&officeId=1139"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentofficebgdetail, self).setUp()
        print("Testrentofficebgdetail setup")

    def test_goto_photo(self):
        """
        点击相册
        """
        elms = self.page.get_element('banner').get_elements('view')
        elms[0].get_element('swiper').get_element('swiper-item').tap()
        delay(3)
        self.get_screenshot()
        delay(3)

    def test_click_map(self):
        """
        点击地图图标
        :return:
        """
        m = self.page.element_is_exists('view[class="map"][data-type="0"]')
        if m == True:
            self.page.get_element('view[class="map"][data-type="0"]').tap()
            self.get_screenshot()
            delay(1)
        else:
            print('没有该模块')

    def test_click_prmap(self):
        """
        点击周边配套
        :return:
        """
        self.page.scroll_to(1350, 500)
        delay(1)
        pr = self.page.element_is_exists('text', inner_text='周边配套')
        if pr == True:
            m = self.page.get_element('view[class="pr map"][data-type="0"]')
            m.tap()
            self.get_screenshot()
        else:
            print('没有周边配套模块')

    def test_click_fjall(self):
        """
        附近楼盘-点击查看更多
        :return:
        """
        self.page.scroll_to(900, 500)
        delay(1)
        rmlp = self.page.element_is_exists('text', inner_text='附近楼盘')
        if rmlp == True:
            e = self.page.get_element('view[class="center check"]')
            e.tap()
            self.get_screenshot()
        else:
            print('没有附近楼盘')

    def test_click_fjdetail(self):
        """
        点击附近楼盘进入详情页
        :return:
        """
        self.page.scroll_to(900, 500)
        delay(1)
        rmlp = self.page.element_is_exists('text', inner_text='附近楼盘')
        if rmlp == True:
            elm_items = self.page.get_elements('//view[@class="item"]')
            if len(elm_items) == 0:
                print("没有附近楼盘")
            else:
                # 第一个item
                elm_first_item = elm_items[0]
                # 点击第一条房源
                elms = elm_first_item.get_element('buildingitem').get_elements('view')
                elms[0].tap()
                self.get_screenshot()
        else:
            print('没有附近楼盘')