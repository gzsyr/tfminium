from ddt import file_data, ddt
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt
class Testrentoffice(TestBase):
    """
    写字楼首页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/office/index/index"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentoffice, self).setUp()
        print("Testrentoffice setup")

    def test_click_search_点击搜索框(self):
        """
        点击搜索框
        :return:
        """
        e = self.page.get_element('//view/search/view/view')
        e.tap()
        self.verifyPageName('/esf/sell/rent/office/search/search', '搜索 ok')
        self.get_screenshot()
        self.delay(3)

    @ddt_case(
        1, 2, 3, 4, 5
    )
    def test_click_tileJump_点击金刚区(self, value):
        """
        点击金刚区
        :param value:
        :return:
        """
        tile = self.page.get_element(f'view[class="t_c tile"][data-type = "{value}"]')
        tile.tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)

    @ddt_case(
        0, 1, 2, 3, 4
    )
    def test_click_hotarea_点击大家都在搜(self, value):
        """
        点击大家都在搜
        :param value:
        :return:
        """
        elms = self.page.get_elements('//view[@class="hotArea"]//view[contains(@class, "item")]')
        if len(elms) > value:
            elms[value].tap()
            self.delay(2)
            self.get_screenshot()
            self.delay(2)

    def test_click_rmlp_热门楼盘查看全部(self):
        """
        点击热门楼盘-查看全部
        :return:
        """
        rmlp = self.page.element_is_exists('text', inner_text='热门楼盘')
        if rmlp == True:
            gd = self.page.get_element('view[class="center check"][data-type="2"]')
            gd.tap()
            self.delay(2)
            self.get_screenshot()
        else:
            print('没有热门楼盘模块')

    def test_click_tjxzl_推荐写字楼查看全部(self):
        """
        点击推荐写字楼-查看全部
        :return:
        """
        rmlp = self.page.element_is_exists('text', inner_text='推荐写字楼')
        if rmlp == True:
            gd = self.page.get_element('view[class="center check"][data-type="1"]')
            gd.tap()
            self.delay(2)
            self.get_screenshot()
        else:
            print('没有推荐写字楼模块')

    def test_click_xzldetail_推荐写字楼进入详情页(self):
        """
        点击推荐写字楼进入详情页
        :return:
        """
        self.page.scroll_to(700, 500)
        self.delay(1)
        rmlp = self.page.element_is_exists('text', inner_text='推荐写字楼')
        if rmlp == True:
            elm_items = self.page.get_elements('//view[@class="list"]')
            if len(elm_items) == 0:
                print("没有附近写字楼")
            else:
                # 第一个item
                elm_first_item = elm_items[0]
                # 点击第一条房源
                elms = elm_first_item.get_element('officeItem').get_elements('view')
                elms[0].tap()
                self.delay(3)
                self.get_screenshot()
                self.delay(2)
        else:
            print('没有推荐写字楼模块')


