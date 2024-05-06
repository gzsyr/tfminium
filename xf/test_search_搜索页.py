# add by zsy
from base.test_base import TestBase


class TestSearch(TestBase):
    """
    搜索页面
    """
    def setUp(self) -> None:
        self.page_name = "/page/search/index?type=1&city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestSearch, self).setUp()

    def click_search_button(self):
        """
        点击”搜索“ 按钮
        """
        self.find_element('view[class="search_txt"]').tap()

    def input_keyword(self, keyword='test'):
        """
        输入关键词
        """
        self.find_element('input[class="searchTR-input"]').input(keyword)

    def test_007_click_关注度榜单(self):
        """"
        V7.01.X: click_关注度榜单
        """
        self.get_screenshot('show')
        self.find_element('view[class="item tfFlex tfAlignC listNum"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_006_进入楼盘评测(self):
        """
        V6.47.X: 进入楼盘评测
        """
        # 搜索关键词 ‘苏宁测试11’，搜索
        self.input_keyword('苏宁测试11')
        self.click_search_button()

        self.delay(2)
        self.find_element('navigator[class="grid_lpcp"]').tap()
        self.delay(3)
        self.verifyPageName('/page/newhouse/evaluation/evaluation')
        self.get_screenshot()

    def test_001_无搜索词搜索(self):
        """
        V7.08: update no toast
        V6.38.X: 无搜索词，点击 搜索按钮
        """
        self.find_element('view[class="search_txt"]').tap()

        self.get_screenshot()

    def test_002_关键词搜索(self):
        """
        V7.08: update no toast
        V6.38.X: 输入关键词搜索，进入搜索结果页
        """
        self.input_keyword('test')

        # 进入 搜索结果页
        self.click_search_button()
        self.get_screenshot('关键搜索进入搜索结果页')

        # 取消关键词
        self.find_element('view[class="cancle"]').tap()
        self.get_screenshot('搜索结果页取消关键词')

        # 搜索关键为空，点击搜索
        self.find_element('view[class="search_txt"]').tap()
        self.get_screenshot('关键词为空点击搜索')

        # 搜索关键词 ‘泉州万科城’，搜索
        self.input_keyword('泉州万科城')
        self.click_search_button()
        self.get_screenshot('搜索“泉州万科城”的结果')

        self.delay(2)
        # 点击 楼盘 进入楼盘详情页
        self.find_element('view[class="commonNewHouseLi-r"]').tap()
        self.get_screenshot()
        self.verifyPageName('/page/newhouse/detail')

    def test_004_点击历史搜索(self):
        """
        V6.38.X: 点击 搜索历史 关键词搜索
        """
        try:
            self.find_element('text[class="item"]').tap()

            self.get_screenshot()
            self.verifyPageName('/page/search/result')
        except:
            print('无搜索词')

    def test_003_点击联想结果(self):
        """
        V6.38.X: 输入关键词，点击联想结果，进入楼盘详情页
        """
        self.input_keyword('泉州万科城')
        self.delay(2)

        self.find_element('view[class="searchBLi-l-wrap tfLine1"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/detail')

    def click_filter(self, tab='位置', cont='丰泽'):
        """
        点击筛选项和对应内容，后，点击确定
        """
        # 筛选项
        self.find_element('view[class="newHouseTabLi-msg"]', inner_text=tab).tap()
        # 点击 丰泽
        if tab == '位置':
            self.find_element('view[class="newHouseMaskLi-twoLi tfLine1"]', inner_text=cont).tap()
        elif tab == '价格':
            self.find_element('view[class="newHouseMaskLi-price-li"]', text_contains=cont).tap()
        elif tab == '筛选' or tab == '户型':
            self.find_element('view[class="newHouseMaskLi-sx-li"]', text_contains=cont).tap()
        elif tab == '排序':
            self.find_element('view[class="newHouseMaskLi-order-li"]', text_contains=cont).tap()
        self.find_element('view[class="newHouseMaskLi-sx-btn-confirm"]').tap()

    def test_005_结果页筛选(self):
        """
        V6.38.X: 在结果页筛选
        """
        self.input_keyword('泉州万科城')
        # 点击搜索
        self.click_search_button()

        self.delay(2)

        self.click_filter(tab='位置', cont='丰泽')
        self.get_screenshot('筛选位置-丰泽的结果')

        self.click_filter(tab='价格', cont='8000-10000元')
        self.get_screenshot('筛选价格-8000-10000的结果')

        self.click_filter(tab='筛选', cont='房企')
        self.get_screenshot('筛选 房企 的结果')

        self.click_filter(tab='排序', cont='开盘时间由近到远')
        self.get_screenshot('筛选排序-开盘时间由近到远的结果')

        self.click_filter(tab='户型', cont='三室')
        self.get_screenshot('筛选排序-开盘时间由近到远的结果')