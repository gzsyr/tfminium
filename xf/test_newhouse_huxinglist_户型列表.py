# add by zsy
from ddt import ddt, file_data

from base.test_base import TestBase


class TestFuncHxList(TestBase):
    """
    特价房
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/hx/hxlist?pinyin=sjcs1&city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncHxList, self).setUp()
        print('TestFuncHxList setup test')


    def test_点击底部IM咨询(self):
        """
        点击底部在线咨询按钮 手机号18555555555
        """
        self.find_element('view[class="IMBtn positionRel"]').tap()

        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_14508')
        self.get_screenshot()

    def test_点击列表IM咨询(self):
        """
        点击列表项在线咨询按钮  手机号18555555555
        """
        self.find_element('view[class="consultWrap tfFlex tfAlignC tfFlexC"]').tap()

        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_14508')
        self.get_screenshot()

    def test_点击底部拨打电话咨询(self):
        """
        点击底部拨打电话咨询按钮
        """
        self.find_element('view[class="tellBtn positionRel"]').tap()

        self.get_screenshot()

    def test_点击列表项(self):
        """
        点击列表项，进入户型详情
        """
        self.find_element('view[class="z-list-item flex tfAlignC"]').tap()

        self.verifyPageName('/page/newhouse/hx/hxdetail')
        self.get_screenshot()
