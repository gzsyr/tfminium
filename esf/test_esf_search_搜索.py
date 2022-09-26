from ddt import file_data
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt_class()
class Testesfsearch(TestBase):
    """
    搜索页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/search/search?city=nj&keyword="
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfsearch, self).setUp()
        print("Testesfsearch setup")

    def test_01_click_input_输入关键字搜索(self):
        """
        输入关键字
        :return:
        """
        self.page.get_element('//search/view/input').input('金地')
        self.delay(3)
        self.get_screenshot()
        self.delay(3)
        keys = self.page.element_is_exists('//view[@class="flex flex_column justify_center listItem"]')
        if keys == True:
            k = self.page.get_elements('//view[@class="flex flex_column justify_center listItem"]')
            k[0].tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print('没有查找到相关内容')
            self.get_screenshot()

    @ddt_case(
        0, 1, 2
    )
    def test_02_click_hotSearch_点击热门搜索(self, value):
        """
        点击热门搜索
        :return:
        """
        hot = self.page.element_is_exists('view[class="hotSearches"]')
        if hot == True:
            self.page.get_element(f'view[class="flex align_center hotSearch"][data-index="{value}"]').tap()
            self.delay(3)
            self.get_screenshot()
            self.delay(3)
        else:
            print("没有热门搜索")

    def test_03_click_hissearch_点击历史记录(self):
        """
        点击历史记录
        :return:
        """
        his = self.page.element_is_exists('view[class="searchHistories"]')
        if his == True:
            h = self.page.get_elements('view[class="flex align_center searchHistory"]')
            self.delay(3)
            h[0].tap()
            self.get_screenshot()
        else:
            print('没有历史记录')
            self.get_screenshot()

    def test_04_click_clearHistory_点击历史记录删除按钮(self):
        """
        点击历史记录删除按钮
        :return:
        """
        hit = self.page.element_is_exists('view[class="searchHistories"]')
        if hit == True:
            h = self.page.get_element('view[class="clear"]')
            h.tap()
            self.get_screenshot()
        else:
            print('没有历史记录')
            self.get_screenshot()