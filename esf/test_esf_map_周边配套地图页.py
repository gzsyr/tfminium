from ddt import file_data
from minium import ddt_class, ddt_case

from base.test_base import TestBase


class Testesfmap(TestBase):
    """
    周边配套地图页
    """

    def setUp(self, true=None) -> None:
        # self.page_name = "/esf/sell/pages/map/map?type=0&blockId=3982&blockName=水佑岗小区&lat=32.067434981213204&lng=118.76024213761336"
        self.page_name = "/page/publicPages/map/map?city=nj&tbl=block&id=3982&blockName=水佑岗小区&lat=32.067434981213204&lng=118.76024213761336&poiType=教育"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfmap, self).setUp()
        print("Testesfmap setup")

    def test_click_tab_点击地图tab(self):
        """
        V6.42.X: 点击地图tab（公交、地铁、学校等）
        """
        eles = self.find_elements('image[class="icon"]')
        for e in eles:
            e.tap()
            self.get_screenshot()

    def test_click_上拉下拉展示(self):
        """
        V6.42.X: 上拉、下拉展示收起内容
        """
        self.find_element('view[class="center expand"]').tap()
        self.delay(2)
        self.get_screenshot('展开')

        self.find_element('view[class="center expand"]').tap()
        self.delay(2)
        self.get_screenshot('收起')

    def test_click_IM(self):
        """
        V6.42.X: 点击咨询
        """
        self.find_element('view[class="icon"]').tap()
        self.delay(2)
        self.get_screenshot()

    def test_click_文字(self):
        """
        V6.42.X: 点击文字
        """
        self.find_element('view[class="line_1 address"]').tap()
        self.get_screenshot()

