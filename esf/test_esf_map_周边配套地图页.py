from ddt import file_data
from minium import ddt_class, ddt_case

from base.test_base import TestBase

@ddt_class()
class Testesfmap(TestBase):
    """
    周边配套地图页
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/map/map?type=0&blockId=3982&blockName=水佑岗小区&lat=32.067434981213204&lng=118.76024213761336"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfmap, self).setUp()
        print("Testesfmap setup")

    @ddt_case(
        1, 2, 3, 4, 5, 6
    )
    def test_click_tab_点击地图tab(self, value):
        """
        点击地图tab（公交、地铁、学校等）
        :param value:
        :return:
        """
        tabs = self.page.get_element(f'view[class="center supportType"][data-type="{value}"]')
        tabs.tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)
        items = self.page.get_elements('view[class="between item"]')
        if len(items) > 0:
            items[0].tap()
            self.delay(3)
            self.get_screenshot()
            self.delay(3)
        else:
            print("暂无内容")
            self.delay(3)
        act_tab = self.page.element_is_exists(f'view[class="center supportType active"][data-type="{value}"]')
        if act_tab == True:
            self.page.get_element(f'view[class="center supportType active"][data-type="{value}"]').tap()
            self.delay(3)
            self.get_screenshot()
            self.delay(3)
        else:
            self.page.get_element(f'view[class="center supportType"][data-type="{value}"]').tap()
            self.delay(3)
            self.get_screenshot()

