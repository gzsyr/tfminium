# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestNewhouseZxdt(TestBase):
    """
    最新动态详情页（山海国际别墅）
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/zxdt/zxdt?pinyin=shanhaiguojibieshu&city=qz&zygw_id='
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhouseZxdt, self).setUp()

    def test_001_点击置业顾问头像(self):
        """
        V6.29.X: 1004932，点击置业顾问头像
        """
        self.find_element('view[class="avator"]').tap()

        self.get_screenshot()

    def test_002_点击置业顾问正文(self):
        """
        V6.29.X: 置业顾问楼层，点击IM按钮
        """
        self.page.scroll_to(500, 100)
        self.find_element('view[id="dp_1_0_0"][class="contenttext"]').tap()

        self.get_screenshot()

    def test_003_点击实地看盘(self):
        """
        V6.29.X: 1004932，点击实地看盘
        """
        self.find_element('view[class="zxdtTab-li xfxq_zxdt_qbdt"]', inner_text='实地看盘').tap()
        self.get_screenshot()

    def test_004_点击户型解析(self):
        """
        V6.29.X: 1004932，点击户型解析
        """
        self.find_element('view[class="zxdtTab-li xfxq_zxdt_qbdt"]', inner_text='户型解析').tap()
        self.get_screenshot()

    def test_005_点击交通配套(self):
        """
        V6.29.X: 1004932，点击交通配套
        """
        self.find_element('view[class="zxdtTab-li xfxq_zxdt_qbdt"]', inner_text='交通配套').tap()
        self.get_screenshot()

    def test_006_点击展开(self):
        """
        V6.29.X: 1004932，点击楼盘动态正文“展开”按钮
        """
        self.page.scroll_to(1000, 500)
        # self.find_element('view[class="btn"]').tap()
        self.find_element('.zxdtAllListBR-b > .btn').tap()

        self.get_screenshot()

    def test_007_回顶部(self):
        """
        V6.29.X: 1004932，点击"回顶部"按钮
        """
        self.page.scroll_to(1000, 500)
        self.find_element('view[class="newHouseRfixed-backtop"]').tap()

        self.get_screenshot()

