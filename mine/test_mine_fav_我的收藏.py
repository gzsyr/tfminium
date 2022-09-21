# add by zsy
from base.test_base import TestBase


class TestMineFav(TestBase):
    """
    我的收藏页
    """
    def setUp(self) -> None:
        self.page_name = '/page/mine/myCollect/myCollect?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestMineFav, self).setUp()

    def test_goto_first_post_进入帖子详情(self):
        """
        我的收藏页，点击帖子进入帖子详情
        """
        self.page.get_element('view[data-index="0"]').tap()
        self.page.get_element('navigator[class="item"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_goto_fav_first_house_进入楼盘详情(self):
        """
        我的收藏页，点击楼盘tab，点击第一个楼盘进入楼盘详情页
        """
        self.page.get_element('view[data-index="1"]').tap()
        self.delay(2)
        self.page.get_element('image[class="commonNewHouseLi-l-img"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

