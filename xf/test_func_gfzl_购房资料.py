# add by zsy
from ddt import ddt, file_data

from base.test_base import TestBase


class TestFuncGfzl(TestBase):
    """
    特价房
    """
    def setUp(self) -> None:
        self.page_name = '/page/tools/ziliaomoban/ziliaomoban?id=&type=xf&city=qz&navTitle=%E8%B4%AD%E6%88%BF%E8%B5%84%E6%96%99'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncGfzl, self).setUp()
        print('TestFuncGfzl setup test')


    def test_点击底部IM咨询(self):
        """
        点击底部在线咨询按钮 手机号13776640000
        """
        self.find_element('view[class="flex-1 flex tfAlignC tfFlexC link-button im positionRel"]').tap()

        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'fxzj_8')
        self.get_screenshot()

    def test_点击列表IM咨询(self):
        """
        点击底部在线咨询按钮 手机号13776640000
        """
        self.find_element('view[class="tfFlex tfAlignC tfFlexC chat"]').tap()

        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'fxzj_8')
        self.get_screenshot()
