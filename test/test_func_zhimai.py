# add by zsy
from test.test_base import TestBase


class TestFuncZhiMai(TestBase):
    """
    直卖频道页
    """
    def setUp(self) -> None:
        self.page_name = "/page/newhouse/zmpd/zmpd?city=qz"
        self.switch = False
        super(TestFuncZhiMai, self).setUp()
        print("TestFuncZhiMai setup test")

    def test_search(self):
        """
        直卖频道页，输入搜索框“苏宁测试11”搜索
        """
        self.page.get_element('input[class="headZmT-input"]').input("苏宁测试11")

        self.verifyStr(True, self.page.element_is_exists('view[class="item"]'))

    def test_filter_area(self):
        """
        直卖频道页，点击筛选项“区域”选择
        """
        self.set_pick_filter('picker[data-bj="0"]', 2)

        ele = self.page.get_elements('view[class="item tfLine1"]')
        self.verifyStr(ele[0].inner_text, '丰泽', "直卖频道页，点击筛选项“区域”选择 丰泽 ok")

    def test_filter_price(self):
        """
        直卖频道页，点击筛选项“价格”选择
        """
        self.set_pick_filter('picker[data-bj="1"]', 3)

        ele = self.page.get_elements('view[class="item tfLine1"]')
        self.verifyStr(ele[1].inner_text, '4000-5000元/㎡', "直卖频道页，点击筛选项“价格”选择 4000-5000元/㎡ ok")

    def test_filter_huxing(self):
        """
        直卖频道页，点击筛选项“户型”选择
        """
        self.set_pick_filter('picker[data-bj="2"]', 3)

        ele = self.page.get_elements('view[class="item tfLine1"]')
        self.verifyStr(ele[2].inner_text, '三室', "直卖频道页，点击筛选项“户型”选择 三室 ok")

    def test_goto_housedetail(self):
        """
        直卖频道页，点击列表项第一个，进入详情页
        """
        self.page.get_element('view[class="relative zmpd_lp"]').click()

        self.verifyPageName('/page/newhouse/detail')

    def test_goto_im(self):
        """
        直卖频道页，点击列表第一个“咨询我”
        """
        self.page.get_element('view[class="im-btn"]').click()

        self.verifyPageName('/im/pages/chating/chating')

    def test_unfold_hxlist(self):
        """
        直卖频道页，点击列表项第一个“展开户型”
        """
        self.page.get_element('view[class="ctr zmpd_zkhx"]').click()

        self.verifyStr(True, self.page.element_is_exists('view[class="arr open"]'))

    def test_goto_hxdetail(self):
        """
        直卖频道页，点击列表项第一个“展开户型”的第一个户型
        """
        self.page.get_element('view[class="house-info"]').click()

        self.verifyPageName('/page/newhouse/hx/hxdetail')

    def test_goto_morehx(self):
        """
        直卖频道页，点击列表项第一个“展开户型”的“更多户型”
        """
        self.page.get_element('view[class="more-btn"]').click()

        self.verifyPageName('/page/newhouse/hx/hxlist')