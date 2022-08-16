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
        delay(2)
        e4 = self.page.get_element('view[class="pa clear"]')
        e4.tap()

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
        delay(2)
        e4 = self.page.get_element('view[class="pa clear"]')
        e4.tap()

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
        delay(2)
        e4 = self.page.get_element('view[class="pa clear"]')
        e4.tap()

    def test_select_zj(self):
        """
        筛选总价
        :return:
        """
        e = self.page.get_element("view", inner_text="总价")
        e.tap()
        e1 = self.page.get_element("view", inner_text="150-200万")
        e1.tap()
        delay(2)
        e3 = self.page.get_element('view[class="pa clear"]')
        e3.tap()

    def test_select_zjzdy(self):
        """
        筛选总价自定义
        :return:
        """
        e = self.page.get_element("view", inner_text="总价")
        e.tap()
        self.page.get_element("input", inner_text="最低价").input("500")
        self.page.get_element("input", inner_text="最高价").input("1000")
        e1 = self.page.get_element('view[class="price--text_center price--confirm"]')
        e1.tap()
        delay(2)
        e3 = self.page.get_element('view[class="pa clear"]')
        e3.tap()

    def test_select_fx(self):
        """
        筛选房型
        :return:
        """
        e = self.page.get_element("view", inner_text="房型")
        e.tap()
        self.page.get_element('view[class="room--flex room--align_center room--justify_between room--screen_item room--roomOption"][data-index="3"]').tap()
        self.page.get_element('view[class="room--flex room--align_center room--justify_between room--screen_item room--roomOption"][data-index="4"]').tap()
        self.page.get_element('text', inner_text="确定").tap()
        delay(2)
        self.page.get_element('view[class="pa clear"]').tap()

    def test_select_gdqd(self):
        """
        更多筛选确定
        :return:
        """
        self.page.get_element("view", inner_text="更多").tap()
        self.page.get_element('text', inner_text="个人").tap()
        self.page.get_element('text', inner_text="住宅").tap()
        self.page.get_element('text', inner_text="100-120㎡").tap()
        self.page.get_element('text', inner_text="确定").tap()
        delay(2)
        self.page.get_element('view[class="pa clear"]').tap()

    def test_select_gdcz(self):
        """
        更多筛选重置
        :return:
        """
        self.page.get_element("view", inner_text="更多").tap()
        self.page.get_element('text', inner_text="中介").tap()
        self.page.get_element('text', inner_text="别墅").tap()
        self.page.get_element('text', inner_text="300㎡以上").tap()
        self.page.get_element('text', inner_text="重置").tap()
        delay(2)
        self.page.get_element('view[class="pa clear"]').tap()

    def test_select_px(self):
        """
        排序
        :return:
        """
        self.page.get_element("view", inner_text="排序").tap()
        self.page.get_element("text", inner_text="总价由低到高").tap()
        delay(2)
        self.page.get_element('view[class="pa clear"]').tap()

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