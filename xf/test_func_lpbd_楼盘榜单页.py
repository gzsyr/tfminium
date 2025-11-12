# add by zsy
import pytest
from ddt import ddt, file_data

from base.test_base import TestBase


class TestFuncLouPanBangdan(TestBase):
    """
    楼盘榜单
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/rankinglist/rankinglist?city=qz&rank_id=1'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncLouPanBangdan, self).setUp()
        print('TestFuncLouPanBangdan setup test')


    @pytest.mark.im_consult
    def test_点击底部IM咨询(self):
        """
        点击底部在线咨询按钮
        """
        self.find_element('view[class="newhouselist--consult_btn newhouselist--consult_btn_1"]').tap()

        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'qlt_530')
        self.get_screenshot()

    def test_点击底部电话(self):
        """
        点击底部电话
        """
        self.find_element('view[class="newhouselist--consult_btn newhouselist--consult_btn_1"]/view', inner_text='拨打电话').tap()

        self.get_screenshot()

    def test_点击列表项(self):
        """
        点击列表项，进入楼盘详情
        """
        self.find_element('view[class="newhouselist--commonNewHouseLi"]').tap()
        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_切换tab(self):
        """
        切换到第二个tab榜单
        """
        self.find_element('view[class="rankName rankName_1"]').tap()

        self.get_screenshot()
        
