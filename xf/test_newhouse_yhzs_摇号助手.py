# -*-coding:utf-8-*-
import minium
from ddt import data, ddt, unpack

from base.test_base import TestBase


@ddt
class TestNewHouseYhzs(TestBase):
    """
    摇号助手查询页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/yaohao/list?city=qz'
        self.classname = self.__class__.__name__
        self.switch = False
        super(TestNewHouseYhzs, self).setUp()

    def test_goto_map_点击地图(self):
        """
        摇号查询助手页，点击地图
        """
        self.page.get_element('image[class="qcPic3 disflex-flex-shrink-0"]').tap()

        self.verifyPageName('/page/newhouse/mapzf/mapzf')
        self.get_screenshot()

    def test_z_share_分享(self):
        """
        摇号查询助手页，点击分享
        """
        self.page.get_element('view[class="qcTxt"]').tap()

        self.get_screenshot()

    @data(('新领销许', 0), ('正在报名', 1), ('摇号公示', 2), ('摇号查询', 3), ('已经开盘', 4), ('即将开盘', 5))
    @unpack
    def test_click(self, name, num):
        """
        摇号查询助手页，点击“新领销许”
        """
        self.page.get_element('view[data-index="%d"]' % num, inner_text=name).tap()

        self.get_screenshot()

    @data('嘉品美寓2', '苏宁测试11')
    def test_search(self, name='嘉品美寓2'):
        """
        摇号查询助手页，输入楼盘名，选择后进入楼盘详情页
        """
        self.page.get_element('navigator[class="qcSearch disflex-flexgrow-1"]').tap()
        self.delay(1)

        # 进入搜索页
        self.verifyPageName('/page/yaohao/search')
        self.delay(1)

        # 输入关键词搜索
        self.page.get_element('input[class="searchTR-input"]').input(name)
        self.delay(1)

        # 选择第一条联想结果
        try:
            self.page.get_element('view[class="searchBLi tfLine1"]').tap()

            self.verifyPageName('/page/newhouse/detail')
            self.get_screenshot()
        except minium.MiniElementNotFoundError:
            print('没有搜索结果')
            self.get_screenshot('test_search_没有摇号楼盘')

    def test_click_IM_在线咨询(self):
        """
        V6.21.X: 1003947   摇号助手页，点击咨询
        """
        self.page.get_element('view[class="consultEntrance--consultBtn"]').tap()

        self.delay(3)
        self.get_screenshot()

