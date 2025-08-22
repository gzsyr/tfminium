# add by zsy 2023.10.10
from base.test_base import TestBase


class TestLogoutXq(TestBase):
    """
    小区详情页未登录  中冶钟鼎山庄
    """
    def setUp(self) -> None:
        self.page_name = '/esf/village/pages/detail/detail?blockId=8850&city=nj'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestLogoutXq, self).setUp()

    def test_点击楼盘测评(self):
        """
        V6.43.X: 点击楼盘测评
        """
        self.delay(10)
        self.find_element('view[class="price--name"]', inner_text='深度测评').tap()
        self.delay(5)
        self.get_screenshot('进入楼盘测评详情页')
