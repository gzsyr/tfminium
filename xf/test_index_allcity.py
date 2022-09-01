# add by zsy
from base.test_base import TestBase


class TestAllcity(TestBase):
    def setUp(self) -> None:
        self.page_name = "/page/index/city"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestAllcity, self).setUp()
        print("TestAllcity setup atest")

    def test_select_qz(self):
        """
        选择站点：泉州
        :return:
        """
        self.page.get_element('text[class="hot-city"]', inner_text="泉州").tap()

        self.get_screenshot()

