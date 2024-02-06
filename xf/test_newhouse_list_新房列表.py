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

    def test_click_子榜单信息(self):
        """
        V7.01.X: 找房页面（第三位后）子榜单信息流
        """
        self.page.scroll_to(800, 200)
        self.get_screenshot('show')

        self.find_element('view[class="ranking_more"]').tap()
        self.delay(3)
        self.verifyPageName('/page/newhouse/rankinglist/rankinglist')
        self.get_screenshot()

    def test_click_进入楼盘评测(self):
        """
        V6.47.x: 进入楼盘评测
        """
        self.page.scroll_to(3500, 200)
        self.delay(2)
        self.find_element('navigator[class="grid_lpcp"]').tap()
        self.delay(5)
        self.verifyPageName('/page/newhouse/evaluation/evaluation')
        self.get_screenshot()

    def test_click_findcard_点击找房卡(self):
        """
        V6.32.X: 点击找房卡
        """
        self.find_element('view[class="quick-find"]').tap()

        self.get_screenshot()

    def test_click_zygw_置业顾问头像(self):
        """
        V6.20.X: 点击新房列表项下第五个的置业顾问头像
        """
        self.delay(2)
        self.page.get_element('image[class="kgjavatar"]').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def test_click_zygw_置业顾问咨询(self):
        """
        V6.20.X: 点击新房列表项下第五个的置业顾问咨询
        """
        self.delay(2)
        self.page.get_element('view[class="kgjzixun"]').tap()
        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_click_1_search_and_select_and_clear_搜索并清除(self):
        """
        新房列表页面，点击搜索框，输入关键词，点击搜索结果第一条，展示带关键字的列表，点击搜索框的“清空”按钮
        """
        self.find_element('view[class="hint"]', text_contains='请输入楼盘或小区名称').tap()
        # self.find_element('view[class="search-wrapper"]').tap()
        # 进入搜索页面
        self.app.wait_for_page('/page/search/index')
        # 输入关键词
        self.find_element('input[class="searchTR-input"]').input("泉州万科城")
        self.delay(5)
        # 选择搜索结果
        # self.find_element('view[class="searchBLi-l-wrap tfLine1"]').tap()
        # self.delay(5)

        self.find_element('view[class="cancle"]').tap()

        self.get_screenshot()

    def del_test_click_map_地图(self):
        """
        V6.42.X: DELETE
        新房列表页面，点击地图
        """
        self.page.get_element('view[class="search-map"]').tap()

        self.verifyPageName('/page/newhouse/mapzf/mapzf')
        self.get_screenshot()

    def test_click_ads_联板广告(self):
        """
        新房列表页面，点击联板广告
        """
        self.page.get_element('image[class="ad-img"]').tap()

        self.get_screenshot()

    # @file_data('./test_newhouse_list_func.yml')
    @data(0, 1, 2, 3, 4)
    def test_click_yldc_工具区入口(self, index):
        """
        V6.42.X: 新房列表页面，找房卡下面，点击工具入口
        """
        self.page.get_elements('view[class="tool mr0"]')[index].tap()

        self.get_screenshot()

    def del_test_click_dgmk_导购模块1(self):
        """
        V6.42.x: delete
        V6.30.X: 1005036，UI改版
        """
        self.page.get_element('view[class="guide-item guide-item-left"]').tap()

        self.get_screenshot()

    @data(0, 1, 2, 3, 4, 5, 6)
    def test_click_gffw_购房服务(self, num=6):
        """
        V6.42.x: 购房服务模块
        # 新房列表页面，功能入口下方，点击导购模块
        """
        self.page.get_elements('view[class="service"]')[num].tap()

        self.get_screenshot()

    def test_click_zj_足迹(self):
        """
        V6.21.x：更新 新房列表页面，点击足迹
        """
        self.page.get_element('view[class="footprint"]').tap()
        self.delay(2)

        self.verifyPageName('/page/mine/myFootPrint/myFootPrint')
        # self.verifyByScreenshot('xf/IM.png')
        self.get_screenshot()

    def test_click_housedetail_新房详情(self):
        """
        新房列表页面，进入新房详情页
        """
        self.page.get_element('view[class="tfFlex xflb_lp disflex-flexwrap-nowrap"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_select_bk_筛选地铁(self):
        """
        V6.32.X: 列表页，筛选板块
        """
        self.find_element('view[class="newHouseTabLi-msg"]', inner_text="位置").tap()
        self.delay(3)
        self.find_element('view[class="newHouseMaskLi-oneLi"]', inner_text="地铁").tap()
        self.find_element('view[class="newHouseMaskLi-twoLi tfLine1"]', inner_text='1号线').tap()
        self.find_element('view[class="newHouseMaskLi-threeLi-check"]').tap()
        self.find_element('view[class="newHouseMaskLi-sx-btn-confirm"]').tap()

        self.delay(2)
        self.verifyStr(True, self.element_is_exist('view[class="newHouseTabLi-msg"]'),
                       '筛选区域正确')
        self.get_screenshot()

    def test_select_bk_筛选板块(self, bk='城东板块'):
        """
        V6.32.X: 列表页，筛选板块
        """
        self.find_element('view[class="newHouseTabLi-msg"]', inner_text="位置").tap()
        self.delay(3)
        self.find_element('view[class="newHouseMaskLi-oneLi"]', inner_text="板块").tap()
        self.find_element('view[class="newHouseMaskLi-twoLi tfLine1"]', inner_text=bk).tap()
        self.find_element('view[class="newHouseMaskLi-sx-btn-confirm"]').tap()

        self.verifyStr(True, self.page.element_is_exists('view[class="newHouseTabLi-msg"]'),
                       '筛选区域正确')
        self.get_screenshot()

    @data('洛江')
    def test_select_wz_筛选区域(self, qy='洛江'):
        """
        新房列表页面，筛选区域
        """
        self.find_element('view[class="newHouseTabLi-msg"]', inner_text="位置").tap()
        self.find_element('view[class="newHouseMaskLi-oneLi on"]', inner_text="区域").tap()
        self.find_element('view[class="newHouseMaskLi-twoLi tfLine1"]', inner_text=qy).tap()

        self.find_element('view[class="newHouseMaskLi-sx-btn-confirm"]').tap()
        self.verifyStr(True, self.page.element_is_exists('view[class="newHouseTabLi-msg"]'),
                       '筛选区域正确')
        self.get_screenshot()

    @data('8000-10000元/㎡')
    def test_select_jg_筛选价格(self, jg):
        """
        新房列表页面，筛选价格
        """
        self.page.get_element('view[class="newHouseTabLi-msg"]', inner_text="价格").tap()
        self.page.get_element('view[class="newHouseMaskLi-price-li"]', inner_text=jg).tap()

        self.verifyStr(True, self.page.element_is_exists('view[class="newHouseTabLi-msg"]'),
                       '筛选价格正确')
        self.get_screenshot()

    @data('二室')
    def test_select_hx_筛选户型(self, hx='二室'):
        """
        新房列表页面，筛选户型
        """
        self.page.get_element('view[class="newHouseTabLi-msg"]', inner_text="户型").tap()
        self.page.get_element('view[class="newHouseMaskLi-sx-li"]', inner_text=hx).tap()

        self.verifyStr(True, self.page.element_is_exists('view[class="newHouseTabLi-msg"]'),
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
        self.page.get_element('view[class="newHouseMaskLi-order-li"]', inner_text=px).tap()

        self.get_screenshot()

    def test_select_wz_清空筛选项(self):
        """
        V6.32.X: 新房列表页，选择位置区域，点击筛选条件，点击“清空”
        """
        self.find_element('view[class="newHouseTabLi-msg"]', inner_text="位置").tap()
        self.find_element('view[class="newHouseMaskLi-oneLi on"]', inner_text="区域").tap()
        self.find_element('view[class="newHouseMaskLi-twoLi tfLine1"]', inner_text='洛江').tap()

        self.get_screenshot('select')
        self.find_element('view[class="newHouseMaskLi-sx-btn-cancle"]').tap()
        self.get_screenshot()

    def delete_test_z_click_fx_分享(self):
        """
        新房列表页面，点击分享
        V6.34.X: delete
        """
        self.page.get_element('button[class="newHouseRfixed-share xfxq_fx"]')

        self.get_screenshot()

    def tearDown(self) -> None:
        self.app.go_home()
        super(TestNewsHouseList, self).tearDown()