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
        self.page.get_element('view[class="commonNewHouseLi-name tfLine1"]').tap()

        # 校验
        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()