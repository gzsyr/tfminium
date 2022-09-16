from ddt import file_data, ddt
from minium import ddt_class, ddt_case

from base.common import delay
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

    def test_goto_photo(self):
        """
        点击相册
        """
        elms = self.page.get_element('banner').get_elements('view')
        elms[0].get_element('swiper').get_element('swiper-item').tap()
        delay(3)
        self.get_screenshot()
        delay(3)

    def test_goto_collect(self):
        """
        点击收藏
        :return:
        """
        e = self.page.get_element('view[class="button collect"]')
        e.tap()
        self.get_capture()
        delay(3)
        """
        取消收藏
        """
        e1 = self.page.get_element('view[class="button collect"]')
        e1.tap()
        self.get_capture()

    def test_goto_share(self):
        """
        点击分享
        :return:
        """
        e = self.page.get_element('button[class="button"]')
        e.tap()
        # self.get_capture()
        self.get_screenshot()
        delay(1)

    def test_goto_report(self):
        """
        点击举报
        :return:
        """
        e = self.page.get_element('view[class="center report"]')
        e.tap()
        # self.get_capture()
        self.get_screenshot()
        delay(1)

    def test_click_map(self):
        """
        点击地图图标
        :return:
        """
        m = self.page.element_is_exists('view[class="map"]')
        if m == True:
            self.page.get_element('view[class="map"]').tap()
            self.get_capture()
            delay(2)
        else:
            print('没有该模块')
            self.get_capture()
            delay(1)

    def test_click_module(self):
        """
        点击相关推荐列表进入详情
        :return:
        """
        self.page.scroll_to(850, 500)
        delay(1)
        re = self.page.element_is_exists('//view[@class="relevant"]')
        if re == True:
            elm_items = self.page.get_elements('view[class="flex itemHas"]')
            elm_items[0].tap()
            self.get_capture()
            delay(2)
        else:
            print('没有相关推荐')

    def test_click_more(self):
        """
        点击相关推荐列表-查看更多
        :return:
        """
        self.page.scroll_to(950, 500)
        delay(1)
        mo = self.page.element_is_exists('//view[@class="relevant"]')
        if mo == True:
            m = self.page.get_element('view[class="center checkMore"]')
            m.tap()
            self.get_capture()
            delay(2)
        else:
            print('没有相关推荐')

    def test_click_msg(self):
        """
        点击在线聊
        :return:
        """
        self.page.scroll_to(950, 500)
        delay(1)
        m = self.page.get_element('view[class="center msg"]')
        m.tap()
        self.get_capture()
        delay(2)
