# add by zsy
import os
import time

import pyautogui
from ddt import ddt, file_data

from base.test_base import TestBase


@ddt
class TestFuncJsq(TestBase):
    """
    房贷计算器页
    """
    def setUp(self) -> None:
        self.page_name = '/page/tools/fdjsq/sd/index?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncJsq, self).setUp()
        print("TestFuncJsq setup atest")

    # def test_input_value_by_mk(self):
    #     """
    #     通过键盘鼠标来输入内容
    #     png: 需要比对的截图，与当前文件在同一文件夹
    #     value: 需要键盘输入的值，为list
    #     """
    #     btm = pyautogui.locateOnScreen('./pricetotal.png')
    #     print(btm)
    #
    #     from pymouse import PyMouse
    #     if self.m is None:
    #         self.m = PyMouse()
    #     self.m.click(btm[0], btm[1])
    #
    #     self.delay(2)
    #     from pykeyboard import PyKeyboard
    #     if self.k is None:
    #         self.k = PyKeyboard()
    #     # self.k.press_keys(characters=['1', '1', '1', '1'])
    #     self.k.type_string('100')
    #     return self

    # def input_value_by_mk(self, png, value):
    #     """
    #     通过键盘鼠标来输入内容
    #     png: 需要比对的截图，与当前文件在同一文件夹
    #     value: 需要键盘输入的内容
    #     """
    #     path = os.path.join(os.path.dirname(os.path.realpath(__file__)), png)
    #     print(path)
    #     btm = pyautogui.locateOnScreen(path)
    #     print(btm)
    #
    #     if btm is None:
    #         # 如果比对的图没有在屏幕上面找到 assert
    #         pyautogui.screenshot(png[:-4]+'-assert.png')
    #         self.verifyStr(True, False, f'获取pyautogui.locateOnScreen {png} is None')
    #         return self
    #
    #     from pymouse import PyMouse
    #     if self.m is None:
    #         self.m = PyMouse()
    #     self.m.click(btm[0], btm[1])
    #
    #     self.delay(1)
    #     from pykeyboard import PyKeyboard
    #     if self.k is None:
    #         self.k = PyKeyboard()
    #     # self.k.press_keys(characters=value) # 如果是‘1’，‘0’，‘0’则输入之后显示为10
    #     self.k.type_string(value)
    #     return self

    # 以下 商业贷款 的测试用例
    @file_data('./test_func_jsq.yml')
    def test_sydk_dben_total(self, **kargs):
        """
        房贷计算器页面，“商业贷款”，等额本金-按贷款总额
        """
        self.sydk_click_hkfs_debj().\
            input_value_by_mk(png='xf/pricetotal.png', value=kargs['total']).\
            sydk_slider_years(kargs['years']).\
            sydk_input_Lpr(kargs['lpr']).\
            sydk_input_lprbp(kargs['lprbp']).\
            click_submitbtn()

        self.verifyPageName('/page/tools/fdjsq/result/result', '跳到计算结果页 ok')
        self.verifyContainsStr(kargs['bjret'], self.page.get_elements('view[class="monthly-num"]')[1].inner_text, 'result ok')
        self.get_capture()

    @file_data('./test_func_jsq.yml')
    def test_sydk_dxi_total(self, **kargs):
        """
        房贷计算器页面，“商业贷款”，等额本息-按贷款总额
        """
        self.input_value_by_mk(png='xf/pricetotal.png', value=kargs['total']). \
            sydk_slider_years(kargs['years']). \
            sydk_input_Lpr(kargs['lpr']). \
            sydk_input_lprbp(kargs['lprbp']). \
            click_submitbtn()

        self.verifyPageName('/page/tools/fdjsq/result/result', '跳到计算结果页 ok')
        self.page.wait_for('view[class="monthly-num"]')
        self.verifyContainsStr(kargs['bxret'], self.page.get_elements('view[class="monthly-num"]')[0].inner_text, 'result ok')
        self.get_capture()

    @file_data('./test_func_jsq.yml')
    def test_sydk_dben_price(self, **kargs):
        """
        房贷计算器页面，“商业贷款”，等额本金-按单价
        """
        self.sydk_click_hkfs_debj().\
            sydk_click_jsfs_adj().\
            input_value_by_mk(png='xf/price.png', value=kargs['price']).\
            input_value_by_mk(png='xf/area.png', value=kargs['area']).\
            sydk_slider_years(kargs['years']).\
            sydk_input_Lpr(kargs['lpr']).\
            sydk_input_lprbp(kargs['lprbp']).\
            click_submitbtn()

        self.verifyPageName('/page/tools/fdjsq/result/result', '跳到计算结果页 ok')
        self.page.wait_for('view[class="monthly-num"]')
        self.verifyContainsStr(kargs['bjpriceret'], self.page.get_elements('view[class="monthly-num"]')[1].inner_text,
                               'result ok')
        self.get_capture()

    @file_data('./test_func_jsq.yml')
    def test_sydk_dxi_price(self, **kargs):
        """
        房贷计算器页面，“商业贷款”，等额本息-按单价
        """
        self.sydk_click_jsfs_adj(). \
            input_value_by_mk(png='xf/price.png', value=kargs['price']). \
            input_value_by_mk(png='xf/area.png', value=kargs['area']). \
            sydk_slider_years(kargs['years']).\
            sydk_input_Lpr(kargs['lpr']).\
            sydk_input_lprbp(kargs['lprbp']).\
            click_submitbtn()

        self.verifyPageName('/page/tools/fdjsq/result/result', '跳到计算结果页 ok')
        self.page.wait_for('view[class="monthly-num"]')
        self.verifyContainsStr(kargs['bxpriceret'], self.page.get_elements('view[class="monthly-num"]')[0].inner_text,
                               'result ok')
        self.get_capture()

    # 以下 公积金贷款 的测试用例
    @file_data('./test_func_jsq.yml')
    def test_gjj_dben(self, **kwargs):
        """
        “公积金”，等额本金、贷款总额、贷款期限
        """
        self.click_gjjtab().gjj_click_debj().\
            input_value_by_mk(png='xf/pricetotal.png', value=kwargs['gjjtotal']).\
            gjj_slider_years(kwargs['gjjyears']).\
            click_submitbtn()

        self.verifyPageName('/page/tools/fdjsq/result/result', '跳到计算结果页 ok')
        self.page.wait_for('view[class="monthly-num"]')
        self.verifyContainsStr(kwargs['gjjbjret'], self.page.get_elements('view[class="monthly-num"]')[1].inner_text,
                               'result ok')
        self.get_capture()

    @file_data('./test_func_jsq.yml')
    def test_gjj_dxi(self, **kwargs):
        """
        “公积金”，等额本金、贷款总额、贷款期限
        """
        self.click_gjjtab().\
            input_value_by_mk(png='xf/pricetotal.png', value=kwargs['gjjtotal']).\
            gjj_slider_years(kwargs['gjjyears']).\
            click_submitbtn()

        self.verifyPageName('/page/tools/fdjsq/result/result', '跳到计算结果页 ok')
        self.page.wait_for('view[class="monthly-num"]')
        self.verifyContainsStr(kwargs['gjjbxret'], self.page.get_elements('view[class="monthly-num"]')[0].inner_text,
                               'result ok')
        self.get_capture()

    # 以下 组合贷款 的测试用例
    @file_data('./test_func_jsq.yml')
    def test_zhdk_dxi(self, **kwargs):
        """
        “组合贷款”，等额本金
        """
        self.click_zhtab().\
            input_value_by_mk(png='xf/pricetotal.png', value=kwargs['total']).\
            sydk_slider_years(kwargs['years']).\
            sydk_input_Lpr(kwargs['lpr']).\
            sydk_input_lprbp(kwargs['lprbp']).\
            input_value_by_mk(png='xf/pricetotal.png', value=kwargs['gjjtotal']).\
            gjj_slider_years(kwargs['years']).\
            click_submitbtn()

        self.verifyPageName('/page/tools/fdjsq/result/result', '跳到计算结果页 ok')
        self.page.wait_for('view[class="monthly-num"]')
        self.verifyContainsStr(kwargs['bxret'],
                               self.page.get_elements('view[class="monthly-num-black pl40"]')[0].inner_text,
                               'result ok')
        self.verifyContainsStr(kwargs['gjjbxret'], self.page.get_elements('view[class="monthly-num-black pl40"]')[1].inner_text,
                               'result ok')
        self.get_capture()

    @file_data('./test_func_jsq.yml')
    def test_zhdk_dben(self, **kwargs):
        """
        “组合贷款”，等额本金
        """
        self.click_zhtab().\
            sydk_click_hkfs_debj().\
            input_value_by_mk(png='xf/pricetotal.png', value=kwargs['total']).\
            sydk_slider_years(kwargs['years']).\
            sydk_input_Lpr(kwargs['lpr']).\
            sydk_input_lprbp(kwargs['lprbp']).\
            input_value_by_mk(png='xf/pricetotal.png', value=kwargs['gjjtotal']).\
            gjj_slider_years(kwargs['years']).\
            click_submitbtn()

        self.verifyPageName('/page/tools/fdjsq/result/result', '跳到计算结果页 ok')
        self.page.wait_for('view[class="monthly-num"]')
        self.verifyContainsStr(kwargs['bjret'],
                               self.page.get_elements('view[class="monthly-num-black pl30"]')[0].inner_text,
                               'result ok')
        self.verifyContainsStr(kwargs['gjjbjret'], self.page.get_elements('view[class="monthly-num-black pl30"]')[1].inner_text,
                               'result ok')
        self.get_capture()

    # 以下是页面相关元素的点击
    def click_gjjtab(self):
        """
        房贷计算器页面，点击tab“公积金贷款”
        """
        self.page.get_element('view[class="flex-1 dk-mt-list"][data-idx="1"]').tap()
        return self
        # self.verifyStr(True, self.page.element_is_exists('view[class="fl fz34"]', inner_text='公积金贷款总额'),
        #                '切换到“公积金贷款” ok')

    def click_zhtab(self):
        """
        房贷计算器页面，点击tab“组合贷款”
        """
        self.page.get_element('view[class="flex-1 dk-mt-list"][data-idx="2"]').tap()
        return self

        # self.verifyStr(False, self.page.element_is_exists('view[class="fl fz34"]', inner_text='计算方式'),
        #                '切换到“组合贷款” ok')

    def click_submitbtn(self):
        """
        点击“开始计算”按钮
        """
        self.delay(1)
        self.page.get_element('button[class="submitbtn"]', inner_text='开始计算').tap()
        return self


    # 以下是“商业贷款”tab页面的元素点击
    def sydk_click_hkfs_debj(self):
        """
        房贷计算器页面，“商业贷款”，点击“等额本金”
        """
        ele = self.page.get_element('view[class="inline-block ml30"][data-idx="en"]')
        ele.tap()
        return self

        # print(ele.inner_wxml)
        # self.verifyContainsStr('success', ele.inner_wxml, '还款方式勾选“等额本金” ok')

    def sydk_click_jsfs_adj(self):
        """
        房贷计算器页面，“商业贷款”，点击“按单价”
        """
        ele = self.page.get_element('label[class="ml30"][data-idx="prize"]')
        ele.tap()
        self.delay(1)
        return self

        # self.verifyContainsStr('success', ele.inner_wxml, '还款方式勾选“按单价” ok')

    def sydk_input_total(self, total='100'):
        """
        房贷计算器页面，“商业贷款”，输入“贷款总额”，100
        """
        ele = self.page.get_element('input[class="inp fl"][name="total"]')
        ele.input(total)
        return self

    def sydk_input_price(self, price):
        """
        房贷计算器页面，“商业贷款”，输入“单价”，51200
        """
        # 点击单价
        self.page.get_element('label[class="ml30"][data-idx="prize"]').tap()
        # 输入价格
        self.page.get_element('input[class="inp fl"][name="price"]').input(price)
        return self

    def sydk_input_area(self, area):
        """
        房贷计算器页面，“商业贷款”，输入“面积”，100
        """
        # 点击单价
        self.page.get_element('label[class="ml30"][data-idx="prize"]').tap()
        # 输入价格
        self.page.get_element('input[class="inp fl"][name="area"]').input(area)
        return self

    def sydk_pick_shoufu(self, percent=0):
        """
        房贷计算器页面，“商业贷款”，“首付”，“5成”
        """
        # 点击单价
        self.page.get_element('label[class="ml30"][data-idx="prize"]').tap()
        # 选择 5成
        self.set_pick_filter('picker[name="firstpay"]', percent)
        return self

        # self.verifyStr(True, self.page.element_is_exists('view[class="picker"]', inner_text='5成'),
        #                '“商业贷款”，“首付”，“5成” ok')

    def sydk_slider_years(self, years=20):
        """
        房贷计算器页面，“商业贷款”，滑动贷款年限到“25”
        """
        element_slider = self.page.get_element('slider[id="qishu"]')
        element_slider.slide_to(years)
        return self

        # self.verifyStr(element_slider.value, 25, "slider ok")

    def sydk_pick_lilv(self):
        """
        房贷计算器页面，“商业贷款”，利率方式“按旧版基准利率”
        """
        self.set_pick_filter('picker[name="lprname"]', 1)
        return self

        # self.verifyStr(True, self.page.element_is_exists('view[class="picker"]', inner_text='按旧版基准利率 '),
        #                '“商业贷款”，利率方式“按旧版基准利率” ok')

    def sydk_input_Lpr(self, value):
        """
        房贷计算器页面，“商业贷款”，利率方式“按最新LPR”，输入“LPR”为“5”
        """
        ele = self.page.get_element('input[id="lprvalue"]')
        ele.input(value)
        return self

    def sydk_input_lprbp(self, lprbp='4'):
        """
        房贷计算器页面，“商业贷款”，利率方式“按最新LPR”，输入“基点”
        """
        self.page.get_element('input[name="lprbp"]').input(lprbp)
        return self

    # 以下是“公积金贷款”tab页面元素的点击
    def gjj_click_debj(self):
        """
        “公积金贷款”，点击“等额本金”
        """
        ele = self.page.get_element('view[class="inline-block ml30"][data-idx="en"]')
        ele.tap()
        return self

    def gjj_input_total(self, total='100'):
        """
        “公积金贷款”，输入贷款总额
        """
        ele = self.page.get_element('input[class="inp fl"][name="gjj_total"]')
        ele.input(total)
        return self

    def gjj_slider_years(self, years=20):
        """
        “公积金贷款”，滑动贷款期限
        """
        element_slider = self.page.get_element('slider[id="gjj_qishu"]')
        element_slider.slide_to(years)
        return self


    # 以下是“组合贷款”tab页面元素点击
    # 直接调用商业贷款和公积金贷款的元素即可

