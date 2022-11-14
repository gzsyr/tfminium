# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestNewhouseKpxx(TestBase):
    """
    历史开盘信息页面（山海国际写字楼
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/historyLp/historyLp?city=qz&pinyin=shanhaiguojixzl&zygw_id='
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhouseKpxx, self).setUp()

    def test_01_点击咨询(self):
        """
        V6.24.X: 点击“咨询开盘详情”按钮
        """
        self.find_element('view[class="title-im"]').tap()

        self.delay(4)
        self.get_screenshot()