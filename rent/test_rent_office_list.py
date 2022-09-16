from ddt import file_data, ddt
from minium import ddt_class, ddt_case

from base.common import delay
from base.test_base import TestBase

@ddt
class Testrentofficelist(TestBase):
    """
    租写字楼列表
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/office/list/list?listType=1"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentofficelist, self).setUp()
        print("Testrentofficelist setup")

    def test_click_search(self):
        """
        搜索
        :return:
        """
        e = self.page.get_element('//search/view/view')
        e.tap()
        self.verifyPageName('/esf/sell/rent/office/search/search', '搜索 ok')
        delay(3)

        """
        筛选
        """

    def test_click_officedetail(self):
        """
        点击租写字楼列表进入详情页
        :return:
        """
        elm_items = self.page.get_elements('//view[@class="list"]')
        # 第一个item
        elm_first_item = elm_items[0]
        # 点击第一条房源
        elms = elm_first_item.get_element('officeItem').get_elements('view')
        elms[0].tap()
        self.get_capture()
