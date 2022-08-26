# add by zsy
from ddt import ddt, file_data

from base.test_base import TestBase


@ddt
class TestNewhouseYhcx(TestBase):
    """
    摇号结果查询页
    """
    def setUp(self) -> None:
        self.page_name = '/page/yaohao/result?city=qz&pinyin=quanzhouyingjun&ps_id=72668'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhouseYhcx, self).setUp()

    def test_click_house_name(self):
        """
        摇号结果查询页，点击楼盘名称，进入楼盘详情页
        """
        self.page.get_element('image[class="qcPic2 disflex-flex-shrink-0"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_capture()

    def test_click_yhlc(self):
        """
        摇号结果查询页，点击“摇号流程”
        """
        self.page.get_element('view[class="disflex-flex-shrink-0 qcTxt2"]', inner_text='摇号流程').tap()

        self.verifyPageName('/page/news/detail')
        self.get_capture()

    @file_data('./test_newhouse_yhcx_final.yml')
    def test_result_final_search(self, kw='洪叶', ret=True):
        """
        摇号结果查询页，摇号最终结果tab，输入姓名/证明号查询
        """
        self.page.get_element('view[data-index="0"]', inner_text='摇号最终结果').tap()
        self.page.get_element('input[class="search-int"').input(kw+'\n')

        if ret:
            self.delay(1)
            self.page.get_element('view[class="bdliBR-t arr"]', text_contains='选房序号').tap()
            self.delay(1)
        self.get_capture()

    @file_data('./test_newhouse_yhcx_round.yml')
    def test_result_round_search(self, rn=0, round='第一轮', kw='洪叶', ret=True):
        """
        摇号结果查询页，摇号轮次结果tab，输入姓名查询
        """
        # 切换到 摇号轮次结果 tab
        self.page.get_element('view[data-index="1"]', inner_text='摇号轮次结果').tap()

        # 先切换轮次 第x轮
        self.page.get_element(f'view[data-index="{rn}"]', inner_text=round).tap()

        # 输入关键词
        self.page.get_element('input[class="search-int"').input(kw + '\n')

        if ret:
            self.delay(1)
            self.verifyContainsStr(kw, self.page.get_element('view[class="disflex-flexgrow-1"]').inner_wxml, f'摇号结果 最终结果 {kw}ok')
        self.get_capture()