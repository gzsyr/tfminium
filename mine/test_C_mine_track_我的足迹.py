# add by zsy
from base.test_base import TestBase


class TestMineTrack(TestBase):
    """
    我的足迹页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/mine/myFootPrint/myFootPrint?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestMineTrack, self).setUp()

    def test_goto_first_house_进入楼盘详情(self):
        """
        点击足迹的第一个楼盘
        """
        self.find_element('view[class="commonNewHouseLi-name commonNewHouseLi-name-flex tfLine1"]').tap()

        # 校验
        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_click_IM_在线咨询(self):
        """
        V6.21.X: 1003947   我的足迹页楼盘对应的【在线咨询】按钮
        """
        self.page.get_element('view[data-pinyin="liuyijun"]', inner_text='在线咨询').tap()
        self.delay(3)

        self.get_screenshot()

    def test_click_call_拨打电话(self):
        """
        V6.21.X: 1003947   我的足迹页楼盘对应的【拨打电话】按钮
        """
        self.page.get_element('view[data-pinyin="liuyijun"]', inner_text='拨打电话').tap()
        self.delay(3)

        self.get_screenshot()
