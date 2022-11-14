# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestNewhouseYfyjDetail(TestBase):
    """
    一房一价，房源详情页(苏宁测试11）
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/fd/fdfydetail?roomid=11329036&blockid=150722&pinyin=sjcs1&city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhouseYfyjDetail, self).setUp()

    def test_001_hotim_热门咨询(self):
        """
        V6.23.X: 点击热门咨询模块提问
        """
        ele = self.find_element('view[class="hotConsult_content flex tfAlignC mb20"]')

        question = ele.attribute('data-question')
        ele.tap()

        self.delay(4)
        self.verifyPageName('/im/pages/chating/chating')
        imquestion = self.find_elements('view[class="record-chatting-item self"]')[-1].inner_wxml
        self.verifyContainsStr(question[0], imquestion)
        self.get_screenshot()
