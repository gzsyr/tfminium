# add by zsy
from ddt import ddt, file_data

from base.test_base import TestBase


@ddt
class TestFuncBangDan(TestBase):
    """
    楼盘榜单页
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/bangdan/bangdan?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncBangDan, self).setUp()
        print('TestFuncBangDan setup test')

    def click_tab(self, bd=2):
        """
        楼盘榜单页，点击总tab
        """
        self.page.get_element(f'swiper-item[data-kind="{bd}"]').click()
        return self

    def picker_area(self, value):
        """
        区域的选择
        """
        self.set_pick_filter('picker', value)
        return self

    def click_house_cover(self):
        """
        点击列表项，第一个数据
        """
        if self.page.wait_for('view[class="item xfxq_bd_lp"]'):
            self.page.get_element('view[class="item xfxq_bd_lp"]').click()

    @file_data('./test_func_bangdan.yml')
    def test_goto_detail_点击楼盘(self, **kwargs):
        """
        楼盘榜单页，”热搜榜“，选择区域后，点击第一个楼盘
        """
        self.click_tab(kwargs['tab']).picker_area(kwargs['area']).click_house_cover()

        self.verifyPageName('/page/newhouse/detail')

        self.get_screenshot()

    # def test_filepath(self):
    #     self.get_capture()
    #     self.verifyStr(True, False)

