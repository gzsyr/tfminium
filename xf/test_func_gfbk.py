# add by zsy
from ddt import ddt, file_data

from base.test_base import TestBase


@ddt
class TestFuncGfbk(TestBase):
    """
    购房百科页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/tools/goufangbaike/goufangbaike?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncGfbk, self).setUp()
        print('TestFuncGfbk setup test')

    @file_data('./test_func_gfbk.yml')
    def test_click_icon(self, **kwargs):
        """
        购房百科页面，点击功能入口
        """
        self.page.get_element('view[class="bkTxt1"]', inner_text=kwargs['name']).click()

        # 验证
        self.verifyPageName(kwargs['targetp'])
        self.get_screenshot()

    def test_click_first_hot(self):
        """
        购房百科页面，点击第一条热门百科
        """
        self.page.get_element('view[class="bkTxt4"]').click()

        # 验证
        self.verifyPageName('/page/tools/goufangbaike/bkDetail')
        self.get_screenshot()