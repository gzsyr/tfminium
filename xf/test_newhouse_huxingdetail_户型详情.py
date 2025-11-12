# -*-coding:utf-8-*-
import pytest

from base.test_base import TestBase
from base.test_mine import TestMine

class TestNewhouseHuxingDetail(TestMine):
    """
    户型详情页(苏宁测试11）
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestNewhouseHuxingDetail, cls).setUpClass()
        cls().change_C()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = '/page/newhouse/hx/hxdetail?picid=3127301&pinyin=sjcs1&city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhouseHuxingDetail, self).setUp()

    def test_006_goto_户型分布(self):
        """
        V6.40.x: 点击户型分布
        """
        self.find_element('view[class="ljfx_btn flex tfAlignC tfFlexC"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhao3d')

    def test_001_click_zygw_more_置业顾问更多(self):
        """
        V6.23.X: -置业顾问楼层，点击“查看更多”
        """
        self.page.scroll_to(500, 300)
        self.delay(8)
        self.find_element('view[class="more tfFlex tfAlignC"]').tap()

        self.verifyPageName('/page/newhouse/zygw/list')
        self.get_screenshot()

    @pytest.mark.im_consult
    def test_002_click_zygw_im_置业顾问咨询(self):
        """
        V6.23.X: 置业顾问楼层，点击IM按钮 手机号13776645736
        """
        self.page.scroll_to(500, 300)
        self.delay(8)
        self.find_element('button[class="zyList_li_r_im"]').tap()


        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_6544')
        self.get_screenshot()

    def test_003_goto_zygw_进置业顾问名片(self):
        """
        V6.23.X: 置业顾问楼层，点击置业顾问头像，进置业顾问名片页
        """
        self.page.scroll_to(500, 300)
        self.delay(8)
        self.find_element('image[class="zyList_li_l-img"]').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def delete_004_click_申请入驻(self):
        """
        V6.23.X: 置业顾问楼层，点击“申请入驻”
        V6.32.X: 删除
        """
        self.find_element('navigator[class="notification"]').tap()

        self.verifyPageName('/page/index/mine')
        self.get_screenshot()

    @pytest.mark.im_consult
    def test_005_hotim_热门咨询(self):
        """
        V6.23.X: 点击热门咨询模块提问  手机号18555555555
        """
        ele = self.find_element('view[class="hotConsult_content flex tfAlignC mb20"]')

        question = ele.attribute('data-question')
        ele.tap()

        self.delay(4)
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_14508')
        imquestion = self.find_elements('view[class="record-chatting-item self"]')[-1].inner_wxml
        self.verifyContainsStr(question[0], imquestion)
        self.get_screenshot()

    @pytest.mark.im_consult
    def test_007_底部咨询(self):
        """
        页面底部咨询 手机号18555555555
        """
        self.find_element('view[class="comBottomBar--link-button comBottomBar--im"]').tap()

        self.delay(4)
        self.verifyPageName('/im/pages/chating/chating')

        self.verifyPageParams('chatTo', 'slwkgj_14508')
        self.get_screenshot()

    def test_008_底部电话(self):
        """
        页面底部电话
        """
        self.find_element('view[class="comBottomBar--link-button comBottomBar--call"]').tap()

        self.get_screenshot()

    def test_010_click_zygw_call_置业顾问电话(self):
        """
        V6.23.X: 置业顾问楼层，点击电话
        """
        self.page.scroll_to(500, 300)
        self.delay(8)
        self.find_element('button[class="zyList_li_r_tel"]').tap()

        self.get_screenshot()