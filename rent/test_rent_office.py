from ddt import file_data, ddt
from minium import ddt_class, ddt_case

from base.common import delay
from base.test_base import TestBase

@ddt
class Testrentoffice(TestBase):
    """
    写字楼首页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/office/index/index"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentoffice, self).setUp()
        print("Testrentoffice setup")

    def test_click_search(self):
        """
        点击搜索框
        :return:
        """
        e = self.page.get_element('//view/search/view/view')
        e.tap()
        self.verifyPageName('/esf/sell/rent/office/search/search', '搜索 ok')
        delay(3)

    @ddt_case(
        1, 2, 3, 4, 5
    )
    def test_click_tileJump(self, value):
        """
        点击金刚区
        :param value:
        :return:
        """
        tile = self.page.get_element(f'view[class="text_center tile"][data-type="{value}"]')
        tile.tap()
        self.get_capture()
        delay(3)
