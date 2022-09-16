from ddt import file_data, ddt
from minium import ddt_class, ddt_case

from base.common import delay
from base.test_base import TestBase

@ddt
class Testrenthouseinglist(TestBase):
    """
    找室友列表页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/list/list?houseType=3"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrenthouseinglist, self).setUp()
        print("Testrenthouseinglist setup")

    def test_click_search(self):
        """
        筛选
        :return:
        """


    def test_click_homelist(self):
        """
        点击列表
        :return:
        """
        list = self.page.get_elements('//view[@class="rent-home-list"]/findRoommateItem/view')
        list[0].tap()
        self.get_capture()

    def test_click_sc(self):
        """
        点击列表-收藏-取消收藏
        :return:
        """
        sc = self.page.get_elements('//view[@class="rent-home-list"]/findRoommateItem/view/view[5]/view[2]')
        sc[0].tap()
        self.get_capture()
        delay(3)
        qxsc = self.page.get_elements('//view[@class="rent-home-list"]/findRoommateItem/view/view[5]/view[2]')
        qxsc[0].tap()
        self.get_capture()
        delay(3)

    def test_click_zxim(self):
        """
        点击列表-在线聊
        :return:
        """
        im = self.page.get_elements('//view[@class="rent-home-list"]/findRoommateItem/view/view[5]/view[3]')
        im[0].tap()
        self.get_capture()
        delay(3)
