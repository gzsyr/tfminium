from minium import ddt_class, ddt_case
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

    def test_click_小区测评分数(self):
        """
        V6.47.X: 点击小区测评分数
        """
        self.delay(3)
        i = 0
        while(i < 5):
            self.page.scroll_to(2000, 200)
            try:
                self.find_element('image[class="villageItem--ic_cp"]').tap()
                self.delay(2)
                break
            except:
                i = i+1
        self.get_screenshot()

    def search_village(self, name='测试'):
        """
        搜索小区
        """
        self.find_element('input[class="search--flex_1"]').tap()
        self.verifyPageName('/esf/village/pages/search/search', '搜索 ok')
        self.delay(1)

        self.find_element('input[class="search--flex_1"]').input(name)
        self.delay(4)

    def test_搜索小区点击测评分数(self):
        """
        V6.47.X: 搜索小区点击测评分数
        :return:
        """
        self.search_village('保利梧桐语\t\n')
        self.find_element('image[class="villageItem--pa villageItem--icon"]').tap()
        self.delay(2)
        self.get_screenshot()

    def del_test_click_yqtl_点击一起讨论(self):
        """
        V6.42.x: delete
        点击一起讨论
        :return:
        """
        e = self.find_element('view[class="flex a_c titleText"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def delete_test_click_jhpl_点击滚动的精华评论(self):
        """
        V7.05: DELETE
        点击滚动的精华评论
        :return:
        """
        comment_Item = self.page.get_element('swiper-item[class="flex a_c commentItem"]')
       # comment = comment_Item[0]
        comment_Item.tap()
        self.delay(5)
        self.get_screenshot()

    def test_show_wz_展开位置筛选(self):
        """
        展开位置筛选
        :return:
        """
        self.find_element('view[class="flex a_c screenTab"][data-id="0"]', inner_text="位置").tap()
        self.get_screenshot()

    def test_show_jj_展开均价筛选(self):
        """
        展开均价筛选
        :return:
        """
        self.find_element('view[class="flex a_c screenTab"][data-id="1"]', inner_text="均价").tap()
        self.get_screenshot()

    def test_show_fl_展开房龄筛选(self):
        """
        展开房龄筛选
        :return:
        """
        self.find_element('view[class="flex a_c screenTab"][data-id="2"]', inner_text="房龄").tap()
        self.get_screenshot()

    def test_show_gd_展开更多筛选(self):
        """
        展开更多筛选
        :return:
        """
        self.find_element('view[class="flex a_c screenTab"][data-id="3"]', inner_text="更多").tap()
        self.get_screenshot()

    def test_show_px_展开排序筛选(self):
        """
        展开排序筛选
        :return:
        """
        self.find_element('view[class="flex a_c screenTab"][data-id="4"]', inner_text="排序").tap()
        self.get_screenshot()

    def test_show_delete_点击删除(self):
        """
        点击删除按钮
        :return:
        """
        e = self.page.get_element('image[class="img"]')
        e.tap()
        self.get_screenshot()

    def test_select_bx_筛选不限(self):
        """
        筛选不限
        :return:
        """
        e = self.page.get_element('view[class="flex a_c screenTab"][data-id="0"]', inner_text="位置")
        e.tap()
        e1 = self.page.get_element('//location/view/view/view')
        e1.tap()
        self.delay(3)
        self.get_screenshot()

    def test_select_qy_筛选位置区域(self):
        """
        筛选位置-区域
        :return:
        """
        e = self.page.get_element('view[class="line_1 screenTabText"]', inner_text="位置")
        e.tap()
        self.delay(3)
        e1 = self.page.get_element('//location/view/view/view[3]')
        e1.tap()
        self.delay(3)
        e2 = self.page.get_element('//location/view/scroll-view/view[3]')
        e2.tap()
        self.delay(3)
        e3 = self.page.get_element('//location/view/scroll-view[2]/view[3]')
        e3.tap()
        self.delay(3)
        self.get_screenshot()
        e4 = self.page.get_element('view[class="pa clear"]')
        e4.tap()

    def test_select_jj_筛选均价(self):
        """
        筛选均价
        :return:
        """
        e = self.page.get_element('view[class="flex a_c screenTab"][data-id="1"]')
        e.tap()
        e1 = self.page.get_element('//price/view/scroll-view/view[6]')
        e1.tap()
        self.delay(3)
        self.get_screenshot()
        e3 = self.page.get_element('view[class="pa clear"]')
        e3.tap()

    def test_select_jjzdy_筛选均价自定义(self):
        """
        筛选均价自定义
        :return:
        """
        e = self.find_element('view[class="flex a_c screenTab"][data-id="1"]')
        e.tap()
        self.page.get_element('//price/view/view/view/input[1]').input("2000")
        self.page.get_element('//price/view/view/view/input[2]').input("10000")
        e1 = self.find_element('view[class="price--t_c price--confirm"]')
        e1.tap()
        self.delay(3)
        self.get_screenshot()
        e3 = self.page.get_element('view[class="pa clear"]')
        e3.tap()

    def test_select_fl_筛选房龄(self):
        """
        筛选房龄
        :return:
        """
        e = self.page.get_element('view[class="flex a_c screenTab"][data-id="2"]', inner_text="房龄")
        e.tap()
        e1 = self.page.get_element('//age/view/scroll-view/view[4]')
        e1.tap()
        self.delay(3)
        self.get_screenshot()
        e3 = self.page.get_element('view[class="pa clear"]')
        e3.tap()

    def test_select_gdqd_更多筛选确定(self):
        """
        更多筛选确定
        :return:
        """
        self.page.get_element('view[class="flex a_c screenTab"][data-id="3"]', inner_text="更多").tap()
        self.page.get_element('//more/view/scroll-view/view/view[2]/view[2]').tap()
        self.page.get_element('//more/view/view/view[2]').tap()
        self.delay(3)
        self.get_screenshot()
        self.page.get_element('view[class="pa clear"]').tap()

    def test_select_gdcz_更多筛选重置(self):
        """
        更多筛选重置
        :return:
        """
        self.page.get_element('view[class="flex a_c screenTab"][data-id="3"]', inner_text="更多").tap()
        self.page.get_element('//more/view/scroll-view/view/view[2]/view[1]').tap()
        self.page.get_element('//more/view/view/view[1]').tap()
        self.delay(3)
        self.get_screenshot()
        self.page.get_element('view[class="pa clear"]').tap()

    def test_select_px_排序(self):
        """
        排序
        :return:
        """
        self.page.get_element('view[class="flex a_c screenTab"][data-id="4"]', inner_text="排序").tap()
        self.page.get_element('//sort/view/view/view[4]').tap()
        self.delay(3)
        self.get_screenshot()
        self.page.get_element('view[class="pa clear"]').tap()

    def test_select_vr_点击有vr(self):
        """
        点击有vr
        :return:
        """
        e = self.page.get_element('view[class="screenQuickItem"][data-index="4"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()
        self.page.get_element('view[class="pa clear"]').tap()

    def test_select_xqjd_点击小区解读(self):
        """
        点击小区解读
        :return:
        """
        e = self.page.get_element('view[class="screenQuickItem"][data-index="3"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()
        self.page.get_element('view[class="pa clear"]').tap()

    def test_select_dxsq_点击大型社区(self):
        """
        点击大型社区
        :return:
        """
        e = self.page.get_element('view[class="screenQuickItem"][data-index="1"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()
        self.page.get_element('view[class="pa clear"]').tap()

    def test_select_list_小区列表进入详情页(self):
        """
        点击小区列表进入详情页
        :return:
        """
        self.delay(3)
        self.find_element('view[class="villageItem--flex villageItem--village_item_wrapper"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_select_listim_小区列表的im(self):
        """
        点击小区列表的im
        :return:
        """
        self.search_village('测试\t\n')
        self.find_element('image[class="villageItem--icon"]').tap()
        self.delay(6)

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')