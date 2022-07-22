# add by zsy
from test.test_base import TestBase


class TestIndexShouye(TestBase):
    """
    淘房小程序首页
    """
    def setUp(self) -> None:
        self.page_name = "/page/index/index"
        self.switch = True
        super(TestIndexShouye, self).setUp()
        print("TestIndexShouye setup test")

    def test_click_banner_one(self):
        """
        点击首页联板广告第一张
        :return:
        """
        self.page.get_element('image[class="bannerTwo-img index_banner"]').click()

    def test_goto_newhouse(self):
        """
        点击功能入口：第一个，新房
        :return:
        """
        self.page.get_element('view[class="myiconTwoLi index_xf"]').click()