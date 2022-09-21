from ddt import file_data, ddt
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt
class Testrenthouseingdetail(TestBase):
    """
    找室友详情页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/detail/roommate/roommate?rmId=24197&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrenthouseingdetail, self).setUp()
        print("Testrenthouseingdetail setup")

    def test_goto_photo_点击相册(self):
        """
        点击相册
        """
        elms = self.page.get_element('banner').get_elements('view')
        elms[0].get_element('swiper').get_element('swiper-item').tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(2)

    def test_goto_collect_点击收藏取消收藏(self):
        """
        点击收藏
        :return:
        """
        e = self.page.get_element('view[class="button collect"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(2)
        """
        取消收藏
        """
        e1 = self.page.get_element('view[class="button collect"]')
        e1.tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(2)

    def test_goto_share_点击分享(self):
        """
        点击分享
        :return:
        """
        e = self.page.get_element('button[class="button"]')
        e.tap()
        self.delay(3)
        # self.get_capture()
        self.get_screenshot()
        self.delay(1)

    def test_goto_report_点击举报(self):
        """
        点击举报
        :return:
        """
        e = self.page.get_element('view[class="center button report"]')
        e.tap()
        self.delay(3)
        # self.get_capture()
        self.get_screenshot()
        self.delay(1)

    def test_click_map_点击地图图标(self):
        """
        点击地图图标
        :return:
        """
        m = self.page.element_is_exists('view[class="map"]')
        if m == True:
            self.page.get_element('view[class="map"]').tap()
            self.delay(3)
            self.get_screenshot()
            self.delay(1)
        else:
            print('没有该模块')

    def test_click_module_点击相关推荐列表进入详情(self):
        """
        点击相关推荐列表进入详情
        :return:
        """
        self.page.scroll_to(850, 500)
        self.delay(1)
        re = self.page.element_is_exists('//view[@class="relevant"]')
        if re == True:
            elm_items = self.page.get_elements('view[class="flex itemHas"]')
            elm_items[0].tap()
            self.delay(3)
            self.get_screenshot()
            self.delay(2)
        else:
            print('没有相关推荐')

    def test_click_more_点击相关推荐列表查看更多(self):
        """
        点击相关推荐列表-查看更多
        :return:
        """
        self.page.scroll_to(950, 500)
        self.delay(1)
        mo = self.page.element_is_exists('//view[@class="relevant"]')
        if mo == True:
            e = self.page.element_is_exists('view[class="center checkMore"]')
            if e == True:
                m = self.page.get_element('view[class="center checkMore"]')
                m.tap()
                self.delay(1)
                self.get_screenshot()
                self.delay(1)
            else:
                print('没有更多')
        else:
            print('没有相关推荐')

    def test_click_msg_点击在线聊(self):
        """
        点击在线聊
        :return:
        """
        self.page.scroll_to(950, 500)
        self.delay(1)
        m = self.page.get_element('view[class="center msg"]')
        m.tap()
        self.delay(1)
        self.get_screenshot()
        self.delay(1)
