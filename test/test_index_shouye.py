# add by zsy
import minium
from minium import ddt_class

from test.test_base import TestBase


@ddt_class()
class TestIndexShouye(TestBase):
    """
    淘房小程序首页
    """
    def setUp(self) -> None:
        self.page_name = "/page/index/index"
        self.switch = True
        super(TestIndexShouye, self).setUp()
        print("TestIndexShouye setup test")

    def test_click_banner_one(self):
        """
        首页，点击联板广告第一张
        :return:
        """
        self.page.get_element('image[class="bannerTwo-img index_banner"]').click()

    @minium.ddt_case(
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    )
    def test_click_func_entry(self, value):
        """
        首页，点击功能入口,第一页的十项
        :return:
        """
        # self.page.get_element('view[data-index2="0"]').click()
        self.page.get_element(f'view[data-index2="{value-1}"]').click()

    def test_click_toutiao(self):
        """
        首页，点击“淘房头条”
        :return:
        """
        self.page.get_element('view[class="toutiao-swiper-item tfLine1"]').click()

    def test_click_reyi_more(self):
        """
        首页，点击“正在热议”更多按钮
        :return:
        """
        self.page.get_element('view[class="jujiao-icon"]').click()

    def test_click_reyi_first(self):
        """
        首页，点击“正在热议”滚动的第一条
        :return:
        """
        self.page.get_element('view[class="jujiao-swiper-item tfLine1"]').click()

    def test_click_middle_adv(self):
        """
        首页，点击正在热议下方的大广告
        :return:
        """
        self.page.get_element('image[class="game-enter-img"]').click()

    @minium.ddt_case(
        1, 2, 3, 4
    )
    def test_click_qukuai(self, value):
        """
        首页，点击导购楼层的4个区块（摇号查询上方）
        :return:
        """
        self.page.get_element(f'view[class="guide-item"][data-index="{value-1}"]').click()

    def test_click_yaohao_loupan_name(self):
        """
        首页，点击摇号查询模块的，楼盘名称
        :return:
        """
        self.page.get_element('view[class="bd yhcx-picker"]').click()

    def test_click_yaohao_input(self):
        """
        首页，摇号查询模块，输入框输入内容
        :return:
        """
        self.page.get_element('input[type="text"]').input("test minitest")

    def test_click_yaohao_inquire(self):
        """
        首页，摇号查询模块，点击“一键查询”
        :return:
        """
        self.page.get_element('navigator[class="link-btn"]').click()

    @minium.ddt_case(
        1, 2
    )
    def test_click_sell_yaohao(self, value):
        """
        首页，点击销售节点楼层，“1-新领销许、2-最新摇号”
        :return:
        """
        self.page.get_element(f'view[class="yhcx-tab-item"][data-index="{value}"]').click()

    def test_click_sell_loupan(self):
        """
        首页，点击销售节点楼层，“近期开盘”下的第一个楼盘
        :return:
        """
        self.page.get_element('view[class="name oneline"]').click()

    def test_click_zhibo_more(self):
        """
        首页，点击直播看房模块，右侧“更多”按钮
        :return:
        """
        self.page.get_element('view[class="indexTitRsj"]').click()

    def test_click_zhibo_first(self):
        """
        首页，点击直播看房模块，第一个直播
        :return:
        """
        self.page.get_element('view[class="zhlc-item"]').click()
