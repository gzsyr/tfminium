# add by zsy
from base.test_base import TestBase


class TestFuncJqkp(TestBase):
    """
    近期开盘页
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/jqkp/jqkp?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncJqkp, self).setUp()
        print('TestFuncJqkp setup test')

    def test_goto_first_newhouse(self):
        """
        近期开盘页面，点击第一个楼盘进入楼盘详情页
        """
        self.page.get_element('navigator[class="xfxq_jqkp_lp"]').click()

        # 验证
        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()
