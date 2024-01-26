# add by zsy
from base.test_base import TestBase


class TestFuncZhiMai(TestBase):
    """
    直卖频道页
    """
    def setUp(self) -> None:
        self.page_name = "/page/newhouse/zmpd/zmpd?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncZhiMai, self).setUp()
        print("TestFuncZhiMai setup atest")

    def test_08_search_搜索(self):
        """
        直卖频道页，输入搜索框“苏宁测试11”搜索
        """
        self.page.get_element('input[class="headZmT-input"]').input("苏宁测试11")

        self.verifyStr(True, self.page.element_is_exists('view[class="item"]'))
        self.get_screenshot()

    def test_01_filter_area_选择区域(self):
        """
        直卖频道页，点击筛选项“区域”选择
        """
        self.set_pick_filter('picker[data-bj="0"]', 2)

        ele = self.page.get_elements('view[class="item tfLine1"]')
        self.verifyStr(ele[0].inner_text, '丰泽', "直卖频道页，点击筛选项“区域”选择 丰泽 ok")
        self.get_screenshot()

    def test_03_filter_price_选择价格(self):
        """
        直卖频道页，点击筛选项“价格”选择
        """
        self.set_pick_filter('picker[data-bj="1"]', 3)

        ele = self.page.get_elements('view[class="item tfLine1"]')
        self.verifyStr(ele[1].inner_text, '4000-5000元/㎡', "直卖频道页，点击筛选项“价格”选择 4000-5000元/㎡ ok")
        self.get_screenshot()

    def test_02_filter_huxing_选择户型(self):
        """
        直卖频道页，点击筛选项“户型”选择
        """
        self.set_pick_filter('picker[data-bj="2"]', 3)

        ele = self.page.get_elements('view[class="item tfLine1"]')
        self.verifyStr(ele[2].inner_text, '三室', "直卖频道页，点击筛选项“户型”选择 三室 ok")
        self.get_screenshot()

    def test_04_goto_housedetail_进入新房详情(self):
        """
        直卖频道页，点击列表项第一个，进入详情页
        """
        self.page.get_element('view[class="relative zmpd_lp"]').click()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_06_goto_im_在线咨询(self):
        """
        直卖频道页，点击列表第一个“咨询我”
        """
        self.page.get_element('view[class="im-btn"]').click()


        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_09_unfold_hxlist_展开户型(self):
        """
        直卖频道页，点击列表项第一个“展开户型”
        """
        self.page.get_element('view[class="ctr zmpd_zkhx"]').click()

        self.verifyStr(True, self.page.element_is_exists('view[class="arr open"]'))
        self.get_screenshot()

    def test_05_goto_hxdetail_进入户型(self):
        """
        直卖频道页，点击列表项第一个“展开户型”的第一个户型
        """
        self.page.get_element('view[class="house-info"]').click()

        self.verifyPageName('/page/newhouse/hx/hxdetail')
        self.get_screenshot()

    def test_07_goto_morehx_更多户型(self):
        """
        直卖频道页，点击列表项第一个“展开户型”的“更多户型”
        """
        self.page.get_element('view[class="more-btn"]').click()

        self.verifyPageName('/page/newhouse/hx/hxlist')
        self.get_screenshot()

