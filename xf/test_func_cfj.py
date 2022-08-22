# add by zsy
from ddt import ddt, file_data

from base.test_base import TestBase


@ddt
class TestFuncCfj(TestBase):
    """
    查房价页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/checkprices/index?city=nj'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncCfj, self).setUp()

    @file_data('./test_func_cfj.yml')
    def test_fast_evaluation(self, name='测试正式小区2', area='234'):
        """
        查房价页面，搜索小区，面积，点击“快速评估”
        """
        self.goto_search().\
            search_select(name).\
            delay(1).\
            input_value_by_mk(png='xf/cfjarea.png', value=area).\
            submit()

        self.verifyPageName('/page/checkprices/result')
        self.get_screenshot()

    def test_result_goto_esf_detail(self):
        self.goto_search(). \
            search_select('测试正式小区'). \
            delay(1). \
            input_value_by_mk(png='xf/cfjarea.png', value='122'). \
            submit()

        self.delay(1)
        self.click_esf()

        self.get_screenshot()

    # 以下是查房价页面元素点击
    def goto_search(self):
        """
        查房价页面，点击小区名称，进入搜索页面
        """
        self.page.get_element('navigator').tap()
        self.delay(1)
        return self

    def input_area(self, area='123'):
        """
        查房价页面，输入面积
        """
        self.page.get_element('input[class="searchprices_size"]').input(area)
        return self

    def submit(self):
        """
        查房价页面，点击“快速评估”
        """
        self.page.get_element('button').tap()

    # 搜索页面
    def search_select(self, name='测试正式小区2'):
        """
        输入小区名称，并选择
        """
        self.page.get_element('input[class="blur-input"]').input(name)
        self.delay(1)
        # self.page.get_element_by_xpath(f'//*[contains(text(), {name}').tap()
        self.page.get_element('scroll-view').get_element('text').tap()


        return self

    # 评估结果页面
    def click_esf(self):
        """
        点击 小区二手房的 房源列表，第一个房源
        """
        self.page.get_element('image=[class="list-poster"]').click()