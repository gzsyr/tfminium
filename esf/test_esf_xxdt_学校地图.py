from ddt import file_data, ddt
from minium import ddt_class, ddt_case
from base.test_base import TestBase


class TestesfXXDT(TestBase):
    """
    二手房学校地图
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/page/publicPages/xxdt/xxdt"
        self.switch = true
        self.classname = self.__class__.__name__
        super(TestesfXXDT, self).setUp()
        print("TestesfXXDT setup")

    def goto_search(self, search = 0, search_kw = 'test'):
        """
        进入搜索页
        """
        self.find_element('view[class="flex_1"]').tap()

        if search == 1:
            """输入小区/学校搜索"""
            self.delay(20)
            self.get_screenshot('进入搜索页面')
            self.find_element('input[class="flex_1 ipt"]').input(search_kw)
            self.get_screenshot(search_kw)

            self.find_element('view[class="flex column j_c item"]').tap()
            self.delay(8)
            self.get_screenshot(search_kw)
        elif search == 2:
            """历史关键词搜索"""
            self.delay(20)
            self.find_element('view[class="center item rtItem"][data-index="0"]').tap()
            self.delay(8)
            self.get_screenshot('历史关键词搜索')
        elif search == 3:
            """输入关键词后删除关键词"""
            self.delay(20)
            self.find_element('input[class="flex_1 ipt"]').input('输入关键词')
            self.get_screenshot('输入关键词')
            self.delay(3)
            self.find_element('image[class="close"]').tap()
            self.delay(1)
            self.get_screenshot('删除关键词')
            self.back()
            self.get_screenshot('返回到地图页')
        elif search == 4:
            """删除历史记录"""
            self.delay(20)
            self.find_element('image[class="clearHistory"]').tap()
            self.get_screenshot('删除历史记录')

    def del_test_goto_search(self):
        """
        V6.42.X: 进入搜索页
        """
        self.goto_search()

        self.verifyPageName('/esf/sell/search/search')
        self.get_screenshot()

    def test_001_search_学校(self):
        """
        V6.42.X: 搜索学校
        """
        self.goto_search(search=1, search_kw='雨花台中学')

    def test_002_search_小区(self):
        """
        V6.42.X: 搜索小区
        """
        self.goto_search(search=1, search_kw='万科金域蓝湾')

    def test_003_search_点击搜索历史(self):
        """
        V6.42.X: 点击搜索历史搜索
        """
        self.goto_search(search=2)

    def test_004_search_输入关键词后删除并返回(self):
        """
        V6.42.x: 输入关键词后删除，返回地图页面
        """
        self.goto_search(search=3)

    def test_005_search_删除历史记录(self):
        """
        V6.42.X: 删除历史记录
        """
        self.goto_search(search=4)

    def test_006_点击快捷提问(self):
        """
        V6.42.x：点击快捷提问
        """
        self.find_element('view[class="center shrink0 qs"]').tap()

        self.delay(2)
        self.get_screenshot()

    def test_099_初中小区定位分享(self):
        """
        V6.42.X: 分别点击初中小区定位分享
        """
        self.find_element('view[class="flex_1 center school_type"]').tap()
        self.delay(2)
        self.get_screenshot('切换到初中')

        self.find_element('view[class="flex_1 center school_type"]').tap()
        self.delay(2)
        self.get_screenshot('切换到小学')

        self.find_element('view[class="center column btn"]').tap()
        self.delay(3)
        self.get_screenshot('点击定位')

        self.find_element('button[class="center column btn button"]').tap()
        self.delay(3)
        self.get_screenshot('点击分享')

    def click_school_commit(self, type = 0):
        """
        点击学校  或  小区
        type: 0 -- 学校
              1 -- 小区
              3 -- 周边配套
              4 -- 切换到中学
        """
        self.delay(15)
        # 点击 雨花台区
        self.find_element('cover-view[class="i_c customCallout districtCallout"][marker-id="3"]').tap()
        self.delay(15)
        self.get_screenshot('点击雨花台区')

        self.find_element('cover-view[class="i_c customCallout schoolCallout"][marker-id="217"]').tap()
        self.delay(40)
        self.get_screenshot('点击雨花外国语小学')
        # self.find_element('cover-view[class="t_c"]/conver-view', text_contains='雨花台区').tap()

        if type == 4:
            self.find_element('view[class="flex_1 center school_type"][data-id="3"]/text').tap()
            self.get_screenshot('切换到中学')
            return

        if type == 1:
            self.find_element('cover-view[class="i_c customCallout blockCallout"][marker-id="1727"]').tap()
            self.delay(40)
            self.get_screenshot('点击宏图上水园')

            self.find_element('view[class="support"]').tap()
            self.delay(40)
            self.get_screenshot('进入周边配套')
            self.back()

        self.find_element('view[class="arrow_up"]').tap()
        self.delay(15)
        self.get_screenshot('上拉展示')

        self.find_element('view[class="arrow_down"]').tap()
        self.delay(15)
        self.get_screenshot('向下收起')

        if type == 0:
            self.find_element('view[class="villageItem--flex villageItem--village_item_wrapper"]').tap()
        elif type == 1:
            # self.find_element('view[class="sellItem--sell_item_wrapper"]').tap()
            return
        self.delay(40)
        self.get_screenshot('当前页面')

        self.back()

        if type == 0:
            self.find_element('view[class="support"]').tap()
            self.delay(40)
            self.get_screenshot('进入学校详情页面')
            self.back()

        if type == 1:
            self.find_element('view[class="sellItem--pr sellItem--sell_item_wrapper"]').tap()
            self.delay(15)
            self.get_screenshot('进入二手房详情页')
            self.back()

        self.find_element('view[class="center chat"]').tap()
        self.delay(3)
        self.get_screenshot('咨询')

    def test_007_点击学校(self):
        """
        V6.42.X: 点击学校
        """
        self.click_school_commit(type=0)
        
    def test_008_点击小区(self):
        """
        V6.42.X: 点击小区
        """
        self.click_school_commit(type=1)
        
    def test_009_切换到中学(self):
        """
        V6.42.X: 切换到中学
        """
        self.click_school_commit(type=4)
