# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestFuncGfzg(TestBase):
    """
    购房资格页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/tools/goufangzige/goufangzige?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncGfzg, self).setUp()

    def test_001_im_结果页咨询(self):
        """
        V6.23.X: 热门咨询模块, 点击提问
        """
        # 点击“立即查询”
        self.find_element('view[class="jftxt3"]').tap()

        # 点击D、外地户籍
        self.find_element('view[class="wtAnitemL disflex-flexgrow-1"]', inner_text='D、外地户籍').tap()
        # 点击下一步
        self.find_element('view[class="wtBtnR"]').tap()

        # 点击“E、港澳籍人士”
        self.find_element('view[class="wtAnitemL disflex-flexgrow-1"]', inner_text='E、港澳台及外籍人士').tap()
        # 点击下一步
        self.find_element('view[class="wtBtnR"]').tap()

        # 点击 热门咨询
        ele = self.find_element('view[class="hotConsult_content flex tfAlignC mb20"]')

        question = ele.attribute('data-question')
        ele.tap()

        self.delay(4)
        self.verifyPageName('/im/pages/chating/chating')
        imquestion = self.find_elements('view[class="record-chatting-item self"]')[-1].inner_wxml
        self.verifyContainsStr(question[0], imquestion)
        self.get_screenshot()