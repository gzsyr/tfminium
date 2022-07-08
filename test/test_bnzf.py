# -*- coding: utf-8 -*- 
# @Time : 2022/6/6 10:34 
# @Author : zcm 
# @File : test_bnzf.py
# @desc:

from test.test_base import TestBase
from test.common import delay


class TestNewsDetailBnzf(TestBase):
    """
    帮你找房页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/news/detail?id=029783880&city=qz"
        self.switch = False
        super(TestNewsDetailBnzf, self).setUp()
        delay(2)

    def test_01_click_bnzf_xf(self):
        """
        点击帮你找房，点击新房，选择住宅，丰泽，10000以上，120-140㎡，140-160㎡，点击一键找房
        :return:
        """
        e = self.page.get_element('button[class="fixBR-btn zf"]').tap()
        delay(6)
        ee = self.page.get_element('view', inner_text='新房').tap()
        delay(2)
        e1 = self.page.get_element('view[data-key="住宅"]').tap()
        delay(2)
        e2 = self.page.get_element('picker').trigger('change', {'value': [0, 2]})
        delay(2)
        e3 = self.page.get_element('view[data-key="10000以上"]').tap()
        delay(2)
        e4 = self.page.get_element('view[data-key="120-140㎡"]')
        e5 = self.page.get_element('view[data-key="140-160㎡"]')
        delay(2)
        if e4.attribute('class') == ['item']:
            e4.tap()
            e5.tap()
        delay(2)
        e6 = self.page.get_element('button[class="find bnzf_yjzf"]').tap()
        delay(2)

    def test_02_click_bnzf_esf(self):
        """
        点击帮你找房，点击二手房，选择丰泽区，二室，20-30万
        :return:
        """
        e = self.page.get_element('button[class="fixBR-btn zf"]').tap()
        delay(6)
        ee = self.page.get_element('view', inner_text='二手房').tap()
        delay(2)
        e1 = self.page.get_element('picker').trigger('change', {'value': 1})
        delay(2)
        e2 = self.page.get_element('view[data-key="二室"]').tap()
        delay(2)
        e3 = self.page.get_element('view[data-key="20-30万"]').tap()
        delay(2)

    def test_03_click_change(self):
        """
        点击帮你找房，点击一键找房，点击修改意向
        :return:
        """
        e = self.page.get_element('button[class="fixBR-btn zf"]').tap()
        delay(6)
        e1 = self.page.get_element('button[class="find bnzf_yjzf"]').tap()
        delay(2)
        e2 = self.page.get_element('view[class="change bnzf_xgyx"]').tap()
        delay(2)

    def test_04_click_remen(self):
        """
        点击帮你找房，点击一键找房，点击第一个热门楼盘
        :return:
        """
        e = self.page.get_element('button[class="fixBR-btn zf"]').tap()
        delay(6)
        e1 = self.page.get_element('button[class="find bnzf_yjzf"]').tap()
        delay(4)
        e2 = self.page.get_element('view[class="commonNewHouseLi-r"]').tap()
        delay(2)

    def test_05_click_callim(self):
        """
        点击帮你找房，点击一键找房，点击在线咨询，点击输入框，输入测试，点击发送，点击语音按钮，长按语音输入5s，再点击语音按钮，点击+按钮，点击历史消息
        :return:
        """
        e = self.page.get_element('button[class="fixBR-btn zf"]').tap()
        delay(6)
        e1 = self.page.get_element('button[class="find bnzf_yjzf"]').tap()
        delay(4)
        e2 = self.page.get_element('view[class="opt-item im bnzf_im"]').tap()
        delay(6)
        e3 = self.page.get_element('input[class="chatinput-input w500"]')
        e3.tap()
        delay(2)
        e3.input('测试')
        delay(2)
        e4 = self.page.get_element('button[class="chatinput-sendbtn fr"]').tap()
        delay(2)
        e5 = self.page.get_element('image[class="chatinput-img"]')
        e5.tap()
        delay(2)
        e6 = self.page.get_element('button[class="chatinput-voice-mask"]').long_press(5000)
        delay(2)
        e5.tap()
        delay(2)
        e7 = self.page.get_element('image[class="chatinput-img fr"]').tap()
        delay(2)
        e8 = self.page.get_element('text[class="chating-history-left"]').tap()
        delay(2)

    def test_06_click_callphone(self):
        """
        点击帮你找房，点击一键找房，点击拨打电话
        :return:
        """
        e = self.page.get_element('button[class="fixBR-btn zf"]').tap()
        delay(6)
        e1 = self.page.get_element('button[class="find bnzf_yjzf"]').tap()
        delay(4)
        e2 = self.page.get_element('view[class="opt-item tel bnzf_phone"]').tap()
        delay(2)