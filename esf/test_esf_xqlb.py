from minium import ddt_class, ddt_case
from base.common import delay

from base.test_base import TestBase
@ddt_class()
class Testesfxqlb(TestBase):
    """
    小区列表页
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/pages/list/list"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfxqlb, self).setUp()
        print("Testesfxqlb setup")

    def test_click_search(self):
        """
        搜索
        :return:
        """
        e = self.page.get_element('input[class="search--flex_1"]')
        e.tap()
        self.verifyPageName('/esf/village/pages/search/search', '搜索 ok')
        delay(3)

    def test_click_yqtl(self):
        """
        点击一起讨论
        :return:
        """
        e = self.page.get_element('view[class="flex align_center titleText"]')
        e.tap()
        self.get_screenshot()

    def test_click_jhpl(self):
        """
        点击滚动的精华评论
        :return:
        """
        comment_Item = self.page.get_element('swiper-item[class="flex align_center commentItem"]')
       # comment = comment_Item[0]
        comment_Item.tap()
        self.get_screenshot()

    def test_show_wz(self):
        """
        展开位置筛选
        :return:
        """
        e = self.page.get_element("view", inner_text="位置")
        e.tap()
        self.get_screenshot()
        delay(2)

    def test_show_jj(self):
        """
        展开均价筛选
        :return:
        """
        e = self.page.get_element("view", inner_text="均价")
        e.tap()
        self.get_screenshot()
        delay(2)

    def test_show_fl(self):
        """
        展开房龄筛选
        :return:
        """
        e = self.page.get_element("view", inner_text="房龄")
        e.tap()
        self.get_screenshot()
        delay(2)

    def test_show_gd(self):
        """
        展开更多筛选
        :return:
        """
        e = self.page.get_element("view", inner_text="更多")
        e.tap()
        self.get_screenshot()
        delay(2)

    def test_show_px(self):
        """
        展开排序筛选
        :return:
        """
        e = self.page.get_element("view", inner_text="排序")
        e.tap()
        self.get_screenshot()
        delay(2)

    def test_show_delete(self):
        """
        点击删除按钮
        :return:
        """
        e = self.page.get_element('image[class="img"]')
        e.tap()
        self.get_screenshot()
        delay(2)

    def test_select_bx(self):
        """
        筛选不限
        :return:
        """
        e = self.page.get_element("view", inner_text="位置")
        e.tap()
        e1 = self.page.get_element("view", inner_text="不限")
        e1.tap()
        self.get_screenshot()

    def test_select_qy(self):
        """
        筛选位置-区域
        :return:
        """
        e = self.page.get_element("view", inner_text="位置")
        e.tap()
        e1 = self.page.get_element("view", inner_text="区域")
        e1.tap()
        e2 = self.page.get_element("view", inner_text="玄武区")
        e2.tap()
        e3 = self.page.get_element("view", inner_text="丹凤街")
        e3.tap()
        delay(2)
        e4 = self.page.get_element('view[class="pa clear"]')
        e4.tap()
        self.get_screenshot()

    def test_select_jj(self):
        """
        筛选均价
        :return:
        """
        e = self.page.get_element("view", inner_text="均价")
        e.tap()
        e1 = self.page.get_element("view", inner_text="≥3万元/ m²")
        e1.tap()
        delay(2)
        e3 = self.page.get_element('view[class="pa clear"]')
        e3.tap()
        self.get_screenshot()

    def test_select_jjzdy(self):
        """
        筛选均价自定义
        :return:
        """
        e = self.page.get_element("view", inner_text="均价")
        e.tap()
        self.page.get_element("input", inner_text="最低价").input("2000")
        self.page.get_element("input", inner_text="最高价").input("10000")
        e1 = self.page.get_element('view[class="price--text_center price--confirm"]')
        e1.tap()
        delay(2)
        e3 = self.page.get_element('view[class="pa clear"]')
        e3.tap()
        self.get_screenshot()

    def test_select_fl(self):
        """
        筛选房龄
        :return:
        """
        e = self.page.get_element("view", inner_text="房龄")
        e.tap()
        e1 = self.page.get_element("view", inner_text="10年以上")
        e1.tap()
        delay(2)
        e3 = self.page.get_element('view[class="pa clear"]')
        e3.tap()
        self.get_screenshot()


    def test_select_gdqd(self):
        """
        更多筛选确定
        :return:
        """
        self.page.get_element("view", inner_text="更多").tap()
        self.page.get_element('text', inner_text="大型社区").tap()
        self.page.get_element('text', inner_text="确定").tap()
        delay(2)
        self.page.get_element('view[class="pa clear"]').tap()
        self.get_screenshot()

    def test_select_gdcz(self):
        """
        更多筛选重置
        :return:
        """
        self.page.get_element("view", inner_text="更多").tap()
        self.page.get_element('text', inner_text="近地铁").tap()
        self.page.get_element('text', inner_text="重置").tap()
        delay(2)
        self.page.get_element('view[class="pa clear"]').tap()
        self.get_screenshot()

    def test_select_px(self):
        """
        排序
        :return:
        """
        self.page.get_element("view", inner_text="排序").tap()
        self.page.get_element("text", inner_text="涨幅从高到低").tap()
        delay(2)
        self.page.get_element('view[class="pa clear"]').tap()
        self.get_screenshot()


    def test_select_vr(self):
        """
        点击有vr
        :return:
        """
        e = self.page.get_element('view[class="screenQuickItem"][data-index="4"]')
        e.tap()
        delay(2)
        self.page.get_element('view[class="pa clear"]').tap()
        self.get_screenshot()

    def test_select_xqjd(self):
        """
        点击小区解读
        :return:
        """
        e = self.page.get_element('view[class="screenQuickItem"][data-index="3"]')
        e.tap()
        delay(2)
        self.page.get_element('view[class="pa clear"]').tap()
        self.get_screenshot()

    def test_select_dxsq(self):
        """
        点击大型社区
        :return:
        """
        e = self.page.get_element('view[class="screenQuickItem"][data-index="1"]')
        e.tap()
        delay(2)
        self.page.get_element('view[class="pa clear"]').tap()
        self.get_screenshot()

    def test_select_list(self):
        """
        点击小区列表进入详情页页
        :return:
        """
        elm = self.page.get_element('//villageitem/view')
        elm.tap()
        self.get_screenshot()

    def test_select_listim(self):
        """
        点击小区列表的im
        :return:
        """
        elm = self.page.get_element('//villageitem/view/view[3]')
        elm.tap()
        self.get_screenshot()