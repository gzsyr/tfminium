# 新首页6.40x
from ddt import ddt, data

from base.test_base import TestBase

@ddt
class TestNewSy(TestBase):
    """
    仅南京站，首页
    """

    def setUp(self) -> None:
        self.page_name = "/page/index/index"
        self.switch = True
        self.classname = self.__class__.__name__
        super(TestNewSy, self).setUp()

    def test_tab_新房详情(self):
        """
        V6.40.X: 切换到新房tab，点击进入房源
        """
        self.page.scroll_to(1200, 200)
        self.delay(2)
        self.find_element('view[data-type="xf"]').tap()
        self.get_screenshot('切换到新房tab')
        self.find_element('view[class="gridNewItem--houseItem"]').tap()
        self.delay(4)
        self.get_screenshot('进入房源详情页')

    def test_tab_新房置业顾问主页(self):
        """
        V6.40.X: 切换到新房tab，点击置业顾问
        """
        self.page.scroll_to(1200, 200)
        self.delay(2)
        self.find_element('view[data-type="xf"]').tap()

        self.get_screenshot('暂为配置置业顾问')

    def test_tab_新房置业顾问咨询(self):
        """
        V6.40.X: 切换到新房tab，点击置业顾问
        """
        self.page.scroll_to(1200, 200)
        self.delay(2)
        self.find_element('view[data-type="xf"]').tap()

        self.get_screenshot('暂为配置置业顾问')

    def test_tab_新房置业顾问电话(self):
        """
        V6.40.X: 切换到新房tab，点击置业顾问
        """
        self.page.scroll_to(1200, 200)
        self.delay(2)
        self.find_element('view[data-type="xf"]').tap()

        self.get_screenshot('暂为配置置业顾问')

    def test_tab_租房房源详情(self):
        """
        V6.40.X: 切换到租房tab，点击进入房源
        """
        self.page.scroll_to(1000, 200)
        self.delay(2)
        self.find_element('view[data-type="zf"]').tap()
        self.get_screenshot('切换到租房tab')

        self.find_element('view[class="gridRentItem--gridRentWrapper"]').tap()
        self.delay(4)
        self.get_screenshot('进入房源详情页')


    def test_z_tab_二手房房源详情(self):
        """
        V6.40.X: 切换到二手房tab，点击二手房进入房源/经纪人/经纪人咨询/经纪人电话
        """
        self.page.scroll_to(1200, 200)
        self.delay(2)
        self.find_element('view[data-type="esf"]').tap()
        self.get_screenshot('切换到二手房tab')
        self.find_element('view[class="gridSellItem--sellFlowWrapper"]').tap()
        self.delay(4)
        self.get_screenshot('进入房源详情页')

    def test_z_tab_二手房经纪人电话(self):
        """
        V6.40.X: 切换到二手房tab，点击二手房进入房源/经纪人/经纪人咨询/经纪人电话
        """
        self.page.scroll_to(1200, 200)
        self.delay(2)
        self.find_element('view[data-type="esf"]').tap()

        self.find_element('view[class="gridSellItem--zixunBtn"]/view', inner_text='电话').tap()
        self.get_screenshot('电话经纪人')

    def test_z_tab_二手房经纪人咨询(self):
        """
        V6.40.X: 切换到二手房tab，点击二手房经纪人咨询/
        """
        self.page.scroll_to(1200, 200)
        self.delay(2)
        self.find_element('view[data-type="esf"]').tap()

        self.find_element('view[class="gridSellItem--zixunBtn"]/view', inner_text='咨询').tap()
        self.delay(4)
        self.get_screenshot('咨询经纪人')

    def test_z_tab_二手房经纪人店铺(self):
        """
        V6.40.X: 切换到二手房tab，点击经纪人
        """
        self.page.scroll_to(1200, 200)
        self.delay(2)
        self.find_element('view[data-type="esf"]').tap()

        self.find_element('image[class="gridSellItem--avatar"]').tap()
        self.delay(4)
        self.get_screenshot('点击经纪人')

    @data(0, 1, 2, 3)
    def test_nav_导航(self, v):
        """
        V6.40.X: 点击 导航区
        """
        self.find_element(f'view[class="newIndexPage--guideItem"][data-index="{v}"]').tap()
        self.delay(2)
        self.get_screenshot()

    def test_click_广告(self):
        """
        V6.40.X: 点击 轮播广告
        """
        self.find_element('image[class="newIndexPage--bannerImg"]').tap()
        self.get_screenshot()

    @data('search-city', 'search-input', 'search-map')
    def test_top_入口(self, value):
        """
        V6.40.x: 点击 城市搜索框 和旁边的地图
        """
        self.find_element(f'view[class="newIndexPage--{value}"]').tap()

        self.delay(2)
        self.get_screenshot()

    @data('新房', '二手房', '租房', '地图找房')
    def test_e_入口(self, value):
        """
        V6.40.X: 点击入口  新房 二手房 租房  地图找房
        """
        self.find_element('view[class="newIndexPage--navItem"]/view', inner_text=value).tap()

        if value == '新房':
            self.verifyPageName('/page/newhouse/newhouseindex/newhouseindex')
        elif value == '二手房':
            self.verifyPageName('/esf/sell/pages/home/home')
        elif value == '租房':
            self.verifyPageName('/esf/sell/rent/home/home')
        elif value == '地图找房':
            self.verifyPageName('/page/newhouse/mapzf/mapzf')

        self.delay(3)
        self.get_screenshot()

    # @data(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    @data({'k': 0, "v": 0},
          {'k': 0, "v": 1},
          {'k': 0, "v": 2},
          {'k': 0, "v": 3},
          {'k': 0, "v": 4},
          {'k': 0, "v": 5},
          {'k': 0, "v": 6},
          {'k': 0, "v": 7},
          {'k': 0, "v": 8},
          {'k': 0, "v": 9},
          {'k': 1, "v": 0},
          {'k': 1, "v": 1},
          {'k': 1, "v": 2}
          )
    def test_f_功能入口(self, vv):
        """
        V6.40.X: 点击功能入口
        """
        self.find_element(f'view[data-index1="{vv["k"]}"][data-index2="{vv["v"]}"]').click()
        self.delay(2)
        self.get_screenshot()

