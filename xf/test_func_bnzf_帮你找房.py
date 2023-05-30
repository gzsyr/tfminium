# -*- coding: utf-8 -*- 
# @Time : 2022/6/6 10:34 
# @Author : zcm 
# @File : test_func_bnzf_帮你找房.py
# @desc:
from ddt import ddt, file_data

from base.test_base import TestBase


@ddt
class TestFuncBnzf(TestBase):
    """
    帮你找房页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/newhouse/bnzf/bnzf?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncBnzf, self).setUp()

    def test_06_wait_click_im_咨询房博士(self):
        """
        V6.23.X: 进入页面5S后展示咨询入口, 点击咨询按钮
        """
        self.delay(5)

        self.find_element('view[class="consult_btn"]').tap()
        self.delay(4)
        self.get_screenshot()

    def test_07_result_click_im_结果页咨询房博士(self):
        """
        V6.23.X: 找房结果页面，进入页面5S后展示咨询入口、点击咨询按钮
        """
        self.page.get_element('button[class="find"]').tap()
        self.delay(8)

        self.find_element('view[class="consult_btn"]').tap()
        self.delay(4)
        self.get_screenshot()

    @file_data('./test_func_bnzf_01_xf.yml')
    def test_02_click_bnzf_xf_新房一键找房(self, **kwargs):
        """
        点击新房，选择住宅，丰泽，10000以上，120-140㎡，140-160㎡，点击一键找房
        """
        self.find_element('view', inner_text='新房').tap()

        # 选择物业类型
        wylx = kwargs['wylx']
        self.find_element(f'view[data-key="{wylx}"]').tap()

        # 默认选择 区域 丰泽
        self.find_element('picker').trigger('change', {'value': [0, 2]})

        # 选择买房预算
        mfys = kwargs['mfys']
        self.page.get_element(f'view[data-key="{mfys}"]').tap()

        # 选择购房面积
        gfmj = kwargs['gfmj']
        for i in range(len(gfmj)):
            self.find_element(f'view[data-key="{gfmj[i]}"]').tap()

        # 点击“一键找房”按钮
        self.find_element('button[class="find"]').tap()
        self.delay(1)

        self.verifyPageName('/page/newhouse/bnzf_result/bnzf_result')
        self.get_screenshot()

    @file_data('./test_func_bnzf_02_esf.yml')
    def test_01_click_bnzf_esf_二手房一键找房(self, **kwargs):
        """
        点击二手房，选择丰泽区，二室，20-30万
        """
        self.page.get_element('view', inner_text='二手房').tap()

        # 选择意向位置
        self.page.get_element('picker').trigger('change', {'value': 1})

        # 选择户型
        hx = kwargs['hx']
        self.page.get_element(f'view[data-key="{hx}"]').tap()

        # 选择买房预算
        mfys = kwargs['mfys']
        self.page.get_element(f'view[data-key="{mfys}"]').tap()

        # 点击“一键找房”按钮
        self.page.get_element('button[class="find"]').tap()
        self.delay(1)

        self.verifyPageName('/page/newhouse/bnzf_result/bnzf_result')
        self.get_screenshot()

    def test_03_click_change_修改意向(self):
        """
        新房，一键找房结果页面，点击修改意向
        """
        self.app.navigate_to('/page/newhouse/bnzf_result/bnzf_result?city=qz')
        self.page.get_element('view[class="change bnzf_xgyx"]').tap()
        self.delay(1)

        self.verifyPageName('/page/newhouse/bnzf/bnzf')
        self.get_screenshot()

    def test_04_click_remen_热门楼盘(self):
        """
        新房，一键找房结果页面，点击第一个热门楼盘
        """
        self.page.get_element('button[class="find"]').tap()
        self.delay(3)
        self.page.get_element('image[class="commonNewHouseLi-l-img"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_05_click_callim_IM咨询(self):
        """
        点击一键找房，点击在线咨询
        # ，点击输入框，输入测试，点击发送，点击语音按钮，长按语音输入5s，再点击语音按钮，点击+按钮，点击历史消息
        """
        self.page.get_element('button[class="find"]').tap()
        self.delay(2)
        self.page.get_element('view[class="opt-item im bnzf_im"]').tap()
        self.delay(2)

        # self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

        # 以下是IM聊天页面内容
        # e3 = self.page.get_element('input[class="chatinput-input"]')
        # self.delay(1)
        # e3.input('测试')
        # self.delay(1)
        # e4 = self.page.get_element('button[class="chatinput-sendbtn fr"]').tap()
        # self.delay(1)
        # e5 = self.page.get_element('image[class="chatinput-img"]')
        # e5.tap()
        # self.delay(1)
        # e6 = self.page.get_element('button[class="chatinput-voice-mask"]').long_press(5000)
        # self.delay(1)
        # # 上面这步之后需要使用麦克风授权
        # self.native.allow_record()
        # e5.tap()
        # self.delay(1)
        # self.page.get_element('image[class="chatinput-img fr"]').tap()
        # self.delay(1)
        # self.page.get_element('text[class="chating-history-left"]').tap()
        # self.delay(1)

    def test_10_click_callphone_拨打电话(self):
        """
        点击一键找房，点击拨打电话
        :return:
        """
        self.page.get_element('button[class="find"]').tap()
        self.delay(2)
        self.page.get_element('view[class="opt-item tel bnzf_phone"]').tap()
        self.delay(1)

        self.verifyByScreenshot('xf/call.png')