from ddt import file_data, ddt
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt
class Testrentofficelhdetail(TestBase):
    """
    联合办公详情页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/detail/building/building?type=2&officeId=59"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentofficelhdetail, self).setUp()
        print("Testrentofficelhdetail setup")

    def test_goto_photo_点击相册(self):
        """
        点击相册
        """
        elms = self.page.get_element('banner').get_elements('view')
        elms[0].get_element('swiper').get_element('swiper-item').tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)

    def test_click_map_点击地图图标(self):
        """
        点击地图图标
        :return:
        """
        m = self.page.element_is_exists('view[class="map"][data-type="0"]')
        if m == True:
            self.page.get_element('view[class="map"][data-type="0"]').tap()
            self.delay(1)
            self.get_screenshot()
            self.delay(1)
        else:
            print('没有该模块')

    def test_click_bllp_本楼盘房源进入详情页(self):
        """
        点击本楼盘房源进入详情页
        :return:
        """
        b = self.page.element_is_exists('text', inner_text='本楼盘房源')
        if b == True:
            e = self.page.get_element('view[class="inline_middle house"]')
            e.tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有本楼盘房源模块')

    def test_click_shadow_品牌介绍点击查看更多收起(self):
        """
        品牌介绍-点击查看更多-收起
        :return:
        """
        self.page.scroll_to(700, 500)
        self.delay(1)
        b = self.page.element_is_exists('text', inner_text='品牌介绍')
        if b == True:
            t = self.page.element_is_exists('view[class="center toggle"]')
            if t == True:
                self.page.get_element('text', inner_text='查看全部').tap()
                self.get_screenshot()
                delay(2)
                self.page.get_element('text', inner_text='收起').tap()
                self.get_screenshot()
                self.delay(2)
            else:
                print('没有更多')
        else:
            print('没有品牌介绍模块')

    def test_click_xzldetail_写字楼信息列表进入详情(self):
        """
        点击写字楼信息列表进入详情页
        :return:
        """
        self.page.scroll_to(900, 500)
        self.delay(1)
        rmlp = self.page.element_is_exists('text', inner_text='写字楼信息')
        if rmlp == True:
            flex = self.page.get_element('//view[@class="flex"]')
            flex.tap()
            self.delay(2)
            self.get_screenshot()
        else:
            print('没有写字楼信息')

    def test_click_wddetail_写字楼信息列表进入详情(self):
        """
        点击写字楼信息列表进入详情页
        :return:
        """
        self.page.scroll_to(1000, 500)
        self.delay(1)
        wd = self.page.element_is_exists('text', inner_text='其他网点')
        if wd == True:
            elm_items = self.page.get_element('//view[@class="item"]/buildingItem/view')
            elm_items.tap()
            self.delay(2)
            self.get_screenshot()
        else:
            print('没有其他网点')