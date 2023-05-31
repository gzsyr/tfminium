from xf.func_cgjs import Funccgjs


class TestFuncCGJS(Funccgjs):
    """
    采光计算器页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/tools/cgjsq/cgjsq?city=nj'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncCGJS, self).setUp()

    def test_计算结果(self):
        """
        V6.35.X: 进入计算结果页
        """
        self.delay(2)
        # self.select_city()
        self.select_total_floor()
        self.input_height()
        self.click_next()
        self.select_floor()
        self.input_distance()
        self.click_result()

        self.get_screenshot()
        self.verifyPageName('/page/tools/cgjsq/cgjsqresult')

    def test_重新计算(self):
        """
        V6.35.x: 结果页 点击 重新计算
        """
        # self.select_city()
        self.select_total_floor()
        self.input_height()
        self.click_next()
        self.select_floor()
        self.input_distance()
        self.click_back()
        self.click_next()
        self.click_result()
        self.click_repeat()

        self.get_screenshot()
        self.verifyStr(True, self.element_is_exist('view[class="tfFlex tfAlignC zyallHeight"]/view', inner_text='59.4米'), 'right')
        self.verifyStr(True, self.element_is_exist('view[class="loujuIcon"]/view', inner_text='60米'), 'right')
        self.verifyStr(True, self.element_is_exist('view[class="liveHeight tfFlex tfAlignC"]/view', inner_text='19.8米'), 'right')

