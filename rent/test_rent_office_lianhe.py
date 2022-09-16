from ddt import file_data, ddt
from minium import ddt_class, ddt_case

from base.common import delay
from base.test_base import TestBase

@ddt
class Testrentofficelianhe(TestBase):
    """
    联合办公列表页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/office/list/list?listType=3"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentofficelianhe, self).setUp()
        print("Testrentofficelianhe setup")

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
        点击列表进入详情页
        :return:
        """
        elm_items = self.page.get_elements('//view[@class="list"]')
        # 第一个item
        elm_first_item = elm_items[0]
        # 点击第一条房源
        elms = elm_first_item.get_element('buildingItem').get_elements('view')
        elms[0].tap()
        self.get_capture()

    def test_click_pprz(self):
        """
        点击品牌入驻
        :return:
        """
        self.page.get_element('view[class="pprz"]').tap()
        self.page.get_element('input[class="input"]').input("13776654691")
        self.page.get_element('view[class="center getCode"]').tap()
        delay(5)
        self.page.get_element('input[class="flex_1 input"]').input("916696")
        sub = 'self.page.get_element(\'view[class="center submit"]\').tap()'
        self.verifyStr(True, self.getShowToast(sub), '提交成功ok')
        self.get_screenshot()
        delay(5)
