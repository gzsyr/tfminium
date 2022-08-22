from ddt import file_data
from minium import ddt_class, ddt_case
from minium.miniprogram.base_driver import page

from base.common import delay
from base.test_base import TestBase


@ddt_class()
class Testesfwd(TestBase):
    """
    二手房首页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/home/home"
        self.switch = true
        super(Testesfwd, self).setUp()
        print("Testesfwd setup")

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
        el = self.page.get_element("//more/view/view")
        el.scroll_to(0, 348)
        delay(1)
        self.page.get_element('text', inner_text=kwargs['zx']).tap()
        self.page.get_element('text', inner_text=kwargs['fl']).tap()
        self.page.get_element('text', inner_text=kwargs['lc']).tap()
        e2 = self.page.get_element("//more/view/view")
        e2.scroll_to(0, 648)
        delay(1)
        self.page.get_element('text', inner_text=kwargs['cx']).tap()
        self.page.get_element('text', inner_text=kwargs['sf']).tap()
        e3 = self.page.get_element("//more/view/view")
        e3.scroll_to(0, 948)
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
