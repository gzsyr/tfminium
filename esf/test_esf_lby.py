from ddt import file_data
from minium import ddt_class, ddt_case

from base.common import delay
from base.test_base import TestBase


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

    def test_click_gg(self):
        """
        广告位
        :return:
        """
        b_l = self.page.element_is_exists('swiper-item[class="img"]')
        if b_l == True:
            e = self.page.get_element('swiper-item[class="img"]')
            e.tap()
        else:
            print("没有配置广告")


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

    @file_data('./test_func_weizhi.yml')
    def test_select_qy(self, **kargs):
        """
        筛选位置-区域
        :return:
        """
        e4 = self.page.get_element('view[class="pa clear"]')
        e4.tap()
        e = self.page.get_element("view", inner_text=kargs['district'])
        e.tap()
        e1 = self.page.get_element("view", inner_text=kargs['searchone'])
        e1.tap()
        e2 = self.page.get_element("view", inner_text=kargs['searchtwo'])
        e2.tap()
        e3 = self.page.get_element("view", inner_text=kargs['searchthree'])
        e3.tap()
        delay(2)

    @file_data('./test_func_zongjia.yml')
    def test_select_zjzdy(self, **kwargs):
        """
        筛选总价自定义
        :return:
        """
        e3 = self.page.get_element('view[class="pa clear"]')
        e3.tap()
        e = self.page.get_element("view", inner_text=kwargs['zdy'])
        e.tap()
        self.page.get_element("input", inner_text="最低价").input(kwargs['nameone'])
        self.page.get_element("input", inner_text="最高价").input(kwargs['nametwo'])
        e1 = self.page.get_element('view[class="price--text_center price--confirm"]')
        e1.tap()
        delay(2)

    @file_data('./test_func_zongjia.yml')
    def test_select_fx(self, **kwargs):
        """
        筛选房型
        :return:
       """
        self.page.get_element('view[class="pa clear"]').tap()
        e = self.page.get_element("view", inner_text=kwargs['fx'])
        e.tap()
        self.page.get_element('text', inner_text=kwargs['namethree']).tap()
        self.page.get_element('text', inner_text=kwargs['namefour']).tap()
        self.page.get_element('text', inner_text="确定").tap()
        delay(2)

    @file_data('./test_func_zongjia.yml')
    def test_select_gdqd(self, **kwargs):
        """
        更多筛选确定
        :return:
        """
        self.page.get_element('view[class="pa clear"]').tap()
        self.page.get_element("view", inner_text=kwargs['more']).tap()
        self.page.get_element('text', inner_text=kwargs['ly']).tap()
        self.page.get_element('text', inner_text=kwargs['lx']).tap()
        self.page.get_element('text', inner_text=kwargs['mj']).tap()
        self.page.scroll_to(348, 500)
        delay(1)
        self.page.get_element('text', inner_text=kwargs['zx']).tap()
        self.page.get_element('text', inner_text=kwargs['fl']).tap()
        self.page.get_element('text', inner_text=kwargs['lc']).tap()
        self.page.scroll_to(648, 500)
        delay(1)
        self.page.get_element('text', inner_text=kwargs['cx']).tap()
        self.page.get_element('text', inner_text=kwargs['sf']).tap()
        self.page.scroll_to(848, 500)
        delay(1)
        self.page.get_element('text', inner_text=kwargs['qjkf']).tap()
        self.page.get_element('text', inner_text=kwargs['cq']).tap()
        self.page.get_element('text', inner_text="确定").tap()
        delay(2)

    @file_data('./test_func_zongjia.yml')
    def test_select_px(self, **kwargs):
        """
        排序
        :return:
        """
        self.page.get_element('view[class="pa clear"]').tap()
        self.page.get_element("view", inner_text=kwargs['paixu']).tap()
        self.page.get_element("text", inner_text=kwargs['paixuone']).tap()
        delay(2)

    @ddt_case(
        0, 1, 2, 3, 4
    )
    def test_click_func_bqsx(self, value):
        """
        标签筛选
        :param value:
        :return:
        """
        self.page.get_element(f'view[class="text_center screenQuickItem"][data-index="{value}"]').tap()


    def test_click_housedetail(self):
        """
        进入二手房详情页
        :return:
        """

        # 先获取所有item
        elm_items = self.page.get_elements('view[class="item"]')

        # 第一个item
        elm_first_item = elm_items[0]

        # 点击
        elms = elm_first_item.get_element('sellitem').get_elements('view')
        elms[0].tap()