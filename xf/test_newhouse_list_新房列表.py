# add by yfl
import minium
from ddt import file_data, ddt, data

from base.test_base import TestBase


@ddt
class TestNewsHouseList(TestBase):
    """
    新房列表页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/newHouseList/newHouseList"
        self.switch = True
        self.classname = self.__class__.__name__
        super(TestNewsHouseList, self).setUp()

        try:
            self.page.get_element('view[class="ads_mask-close"]').tap()
            print("关闭弹窗广告")
        except minium.MiniElementNotFoundError:
            print("无弹窗广告")
        print("TestNewsHouseList setup")

    def test_click_1_search_and_select_and_clear_搜索并清除(self):
        """
        新房列表页面，点击搜索框，输入关键词，点击搜索结果第一条，展示带关键字的列表，点击搜索框的“清空”按钮
        """
        self.page.get_element('navigator', text_contains='请输入楼盘名或区域').tap()
        # 进入搜索页面
        self.app.wait_for_page('/page/search/index')
        # 输入关键词
        self.page.get_element('input[class="searchTR-input"]').input("泉州万科城")
        self.delay(1)
        # 选择搜索结果
        self.page.get_element('view[class="searchBLi tfFlex tfFlexSb tfLine1"]').tap()
        self.delay(1)

        self.page.get_element('view[class="cleanKeyWord"]', inner_text='清空').tap()

        self.get_screenshot()

    def test_click_map_地图(self):
        """
        新房列表页面，点击地图
        """
        self.page.get_element('navigator[class="search-map"]').tap()

        self.verifyPageName('/page/newhouse/mapzf/mapzf')
        self.get_screenshot()

    def test_click_ads_联板广告(self):
        """
        新房列表页面，点击联板广告
        """
        self.page.get_element('image[class="bannerTwo-img index_banner"]').tap()

        self.get_screenshot()

    @file_data('./test_newhouse_list_func.yml')
    def test_click_yldc_功能入口(self, **kwargs):
        """
        新房列表页面，联板广告下面，点击功能入口
        """
        self.page.get_element('view[class="newHouseIconEnterLi-b"]', inner_text=kwargs['funcname']).tap()

        if kwargs['pagename']:
            self.verifyPageName(kwargs['pagename'])
        self.get_screenshot()

    @data(1, 2, 3, 4)
    def test_click_dgmk_导购模块(self, num):
        """
        新房列表页面，功能入口下方，点击导购模块
        """
        self.page.get_element(f'view[class="disflex tfAlignC newHouseDgLi xflb_dg{num}"]').tap()

        self.get_screenshot()

    def test_click_zx_咨询(self):
        """
        新房列表页面，点击咨询
        """
        self.page.get_element('view[class="newHouseRfixed-wyzx xflb_fx"]').tap()
        self.delay(5)

        self.verifyStr(True, self.page.element_is_exists('image[class="historychat"]'),
                       '进入im页面正确')
        # self.verifyByScreenshot('xf/IM.png')
        self.get_screenshot()

    def test_click_housedetail_新房详情(self):
        """
        新房列表页面，进入新房详情页
        """
        self.page.get_element('view[class="tfFlex xflb_lp disflex-flexwrap-nowrap"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    @data('洛江')
    def test_select_wz_筛选区域(self, qy='洛江'):
        """
        新房列表页面，筛选区域
        """
        self.page.get_element('view[class="newHouseTabLi-msg wmax114 tfLine1"]', inner_text="位置").tap()
        self.page.get_element('view[class="maxw175 tfLine1"]', inner_text="区域").tap()
        self.page.get_element('view[class="newHouseMaskLi-twoLi tfLine1"]', inner_text=qy).tap()

        self.verifyStr(True, self.page.element_is_exists('view[class="newHouseTabLi-msg wmax114 tfLine1"]', inner_text=qy),
                       '筛选区域正确')
        self.get_screenshot()

    @data('8000-10000元/㎡')
    def test_select_jg_筛选价格(self, jg):
        """
        新房列表页面，筛选价格
        """
        self.page.get_element('view[class="newHouseTabLi-msg wmax114 tfLine1"]', inner_text="价格").tap()
        self.page.get_element('view[class="newHouseMaskLi-price-li"]', inner_text=jg).tap()

        self.verifyStr(True, self.page.element_is_exists('view[class="newHouseTabLi-msg wmax114 tfLine1"]', inner_text=jg),
                       '筛选价格正确')
        self.get_screenshot()

    @data('二室')
    def test_select_hx_筛选户型(self, hx='二室'):
        """
        新房列表页面，筛选户型
        """
        self.page.get_element('view[class="newHouseTabLi-msg wmax114 tfLine1"]', inner_text="户型").tap()
        self.page.get_element('view[class="newHouseMaskLi-price-li"]', inner_text=hx).tap()

        self.verifyStr(True, self.page.element_is_exists('view[class="newHouseTabLi-msg wmax114 tfLine1"]', inner_text=hx),
                       '筛选户型正确')
        self.get_screenshot()

    @file_data('./test_newhouse_list_sx.yml')
    def test_select_sx_筛选更多(self, **kwargs):
        """
        筛选
        """
        self.page.get_element('view[class="newHouseTabLi-msg"]', inner_text="筛选").tap()
        if kwargs['ts']:
            self.page.get_element('view[class="newHouseMaskLi-sx-li"]', inner_text=kwargs['ts']).tap()
        if kwargs['lx']:
            self.page.get_element('view[class="newHouseMaskLi-sx-li"]', inner_text=kwargs['lx']).tap()
        if kwargs['mj']:
            self.page.get_element('view[class="newHouseMaskLi-sx-li"]', inner_text=kwargs['mj']).tap()
        if kwargs['kpsj']:
            self.page.get_element('view[class="newHouseMaskLi-sx-li"]', inner_text=kwargs['kpsj']).tap()
        if kwargs['zx']:
            self.page.get_element('view[class="newHouseMaskLi-sx-li"]', inner_text=kwargs['zx']).tap()

        self.page.get_element('view[class="newHouseMaskLi-sx-btn-confirm"]').tap()

        self.get_screenshot()

    @data('开盘时间由近到远')
    def test_select_px_筛选排序(self, px):
        """
        新房列表页面，筛选排序
        """
        self.page.get_element('view[class="newHouseTabLi-msg"]', inner_text="排序").tap()
        self.page.get_element('view[class="newHouseMaskLi-price-li"]', inner_text=px).tap()

        self.get_screenshot()

    def test_z_click_fx_分享(self):
        """
        新房列表页面，点击分享
        """
        self.page.get_element('button[class="newHouseRfixed-share xfxq_fx"]')

        self.get_screenshot()

    def tearDown(self) -> None:
        self.app.go_home()
        super(TestNewsHouseList, self).tearDown()