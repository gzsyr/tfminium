import minium

from base.test_base import TestBase

class TestNewHouseYhqc(TestBase):
    """
    新房详情页摇号清册页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/yaohao/publicity?city=qz&pinyin=quanzhouyingjun&ps_id=72668"
        self.switch = False
        super(TestNewHouseYhqc, self).setUp()

    def test_click_qkboxR(self):
        """
        点击顶部说明栏“删除”按钮
        """
        self.page.get_element('view[class="qkboxR disflex-flex-shrink-0"]').tap()

    def test_click_yhlc(self):
        """
        点击顶部“摇号流程”按钮
        """
        self.page.get_element('view[class="disflex-flex-shrink-0 qcTxt2"]').tap()

    def test_click_jinqun(self):
        """
        点击开盘时间右侧的进群按钮
        """
        try:
            ele = self.page.get_element('image[class="jiaqun"]')
            ele.tap()
        except minium.MiniElementNotFoundError:
            print("没有配置进群广告")

    def test_search(self,name="洪叶"):
        """
        摇号清册列表，输入姓名搜索
        """
        ele = self.page.get_element('input[class="search-int"]')
        ele.input(name)
        self.delay(1)
        self.page.get_element("view", inner_text="搜索").tap()

    def test_click_tab1(self):
        """
        摇号清册列表，点击第一个tab
        """
        self.page.get_element('view[class="hdli on"][data-index="0"]').tap()

    def test_click_tab2(self):
        """
        摇号清册列表，点击第二个tab
        """
        self.page.get_element('view[class="hdli"][data-index="1"]').tap()

    def test_click_tab3(self):
        """
        摇号清册列表，点击第三个tab
        """
        self.page.get_element('view[class="hdli"][data-index="2"]').tap()

    def test_click_add(self):
        """
        摇号清册列表。点击“添加”按钮
        """
        result = {"confirm": True}
        self.app.mock_wx_method("showModal", result=result)
        self.page.get_element('button[class="bdliB-r disflex-flex-shrink-0"]').tap()
        self.delay(1)
        self.app.restore_wx_method("showModal")
        self.delay(2)
        self.capture("提示")
        self.native.handle_modal("确定", "提示")

    def test_click_share(self):
        """
        摇号清册列表，点击分享按钮
        """
        self.page.get_element('button[class="newHouseRfixed-share xfxq_fx"]').tap()











