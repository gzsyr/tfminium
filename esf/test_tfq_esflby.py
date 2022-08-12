from minium import ddt_class, ddt_case

from test.test_base import TestBase


@ddt_class()
class Testesflby(TestBase):
    """
    二手房首页
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/home/home"
        self.switch = true
        super(Testesflby, self).setUp()
        print("Testesflby setup")

    def test_click_search(self):
        """
        搜索
        :return:
        """
        e = self.page.get_element('input[class="search--flex_1"]')
        e.tap()

    @ddt_case(
        0, 1, 2, 3, 4
    )
    def test_click_func_entry(self, value):
        """
        二手房首页五个banner
        :param value:
        :return:
        """
        # e = self.page.get_element('view[class="text_center tile"][data-index="0"]')
        # e.tap()
        self.page.get_element(f'view[class="text_center tile"][data-index="{value}"]').click()

    @ddt_case(
        0, 1, 2
    )
    def test_click_func_adv(self, value):
        """
        二手房首页广告
        :param value:
        :return:
        """
        self.page.get_element(
            f'view[class="inline_flex flex_column justify_center entrance"][data-index="{value}"]').click()

    def test_show_wz(self):
        """
        展开位置筛选
        :return:
        """
        e = self.page.get_element("view", inner_text="位置")
        e.tap()

    def test_show_zj(self):
        """
        展开总价筛选
        :return:
        """
        e = self.page.get_element("view", inner_text="总价")
        e.tap()

    def test_show_fx(self):
        """
        展开房型筛选
        :return:
        """
        e = self.page.get_element("view", inner_text="房型")
        e.tap()

    def test_show_gd(self):
        """
        展开更多筛选
        :return:
        """
        e = self.page.get_element("view", inner_text="更多")
        e.tap()

    def test_show_px(self):
        """
        展开排序筛选
        :return:
        """
        e = self.page.get_element("view", inner_text="排序")
        e.tap()

    def test_show_delete(self):
        """
        点击删除按钮
        :return:
        """
        e = self.page.get_element('image[class="img"]')
        e.tap()

    def test_select_bx(self):
        """
        筛选不限
        :return:
        """
        e = self.page.get_element("view", inner_text="位置")
        e.tap()
        e1 = self.page.get_element("view", inner_text="不限")
        e1.tap()

    def test_select_qy(self):
        """
        筛选位置-区域
        :return:
        """
        e = self.page.get_element("view", inner_text="位置")
        e.tap()
        e1 = self.page.get_element("view", inner_text="区域")
        e1.tap()
        e2 = self.page.get_element("view", inner_text="鼓楼区")
        e2.tap()
        e3 = self.page.get_element("view", inner_text="华侨路")
        e3.tap()

    def test_select_dt(self):
        """
        筛选位置-地铁
        :return:
        """
        e = self.page.get_element("view", inner_text="位置")
        e.tap()
        e1 = self.page.get_element("view", inner_text="地铁")
        e1.tap()
        e2 = self.page.get_element("view", inner_text="10号线")
        e2.tap()
        e3 = self.page.get_element("view", inner_text="雨山路站")
        e3.tap()

    def test_select_xx(self):
        """
        筛选位置-学校
        :return:
        """
        e = self.page.get_element("view", inner_text="位置")
        e.tap()
        e1 = self.page.get_element("view", inner_text="学校")
        e1.tap()
        e2 = self.page.get_element("view", inner_text="雨花台区")
        e2.tap()
        e3 = self.page.get_element("view", inner_text="雨花台中学")
        e3.tap()

    # def test_click_housedetail(self):
    #   """
    #  进入二手房详情页
    #  :return:
    #  """
    #  ele = self.page.get_elements('view[class="sell_item_wrapper"]')
    # ele.tap()
