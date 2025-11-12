# add by zsy
import pytest
from ddt import ddt, file_data

from base.test_base import TestBase


class TestFuncTejiaFang(TestBase):
    """
    特价房
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/tjfList/tjfList?city=qz&pinyin=shanhaiguojixzl&h_name=山海国际写字楼12123'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncTejiaFang, self).setUp()
        print('TestFuncBangDan setup test')


    @pytest.mark.im_consult
    def test_点击底部IM咨询(self):
        """
        点击底部在线咨询按钮 手机号15000000002
        """
        self.find_element('view[class="pr center chat"]').tap()

        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_10858')
        self.get_screenshot()

    @pytest.mark.im_consult
    def test_点击列表IM咨询(self):
        """
        点击底部在线咨询按钮 手机号15000000002
        """
        self.find_element('view[class="center chat"]').tap()

        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_10858')
        self.get_screenshot()

    def test_点击列表项(self):
        """
        点击列表项
        """
        self.find_element('view[class="flex item"]').tap()

        self.verifyPageName('/page/newhouse/fd/fdfydetail')
        self.get_screenshot()
