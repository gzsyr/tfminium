import minium

from base.test_base import TestBase

class TestNewHouseYhqc(TestBase):
    """
    新房详情页摇号清册页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/yaohao/publicity?city=qz&pinyin=quanzhouyingjun&ps_id=72668"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewHouseYhqc, self).setUp()

    def test_03_click_qkboxR_顶部删除按(self):
        """
        摇号清册页面，点击顶部说明栏“删除”按钮
        """
        self.page.get_element('view[class="qkboxR disflex-flex-shrink-0"]').tap()

        self.get_screenshot()

    def test_07_click_yhlc_摇号流程(self):
        """
        摇号清册页面，点击顶部“摇号流程”按钮
        """
        self.page.get_element('view[class="disflex-flex-shrink-0 qcTxt2"]').tap()

        self.get_screenshot()

    def test_02_click_jinqun_进群按钮(self):
        """
        摇号清册页面，点击开盘时间右侧的进群按钮
        """
        try:
            ele = self.page.get_element('image[class="jiaqun"]')
            ele.tap()
        except minium.MiniElementNotFoundError:
            print("没有配置进群广告")
        self.get_screenshot()

    def test_08_search_清册搜索(self,name="岳小勇"):
        """
        摇号清册页面，摇号清册列表，输入姓名搜索
        """
        self.page.get_element('input[class="search-int"]').input(name)
        self.delay(1)
        self.page.get_element("view", inner_text="搜索").tap()

        self.get_screenshot()

    def test_04_click_tab1_清册第一个tab(self):
        """
        摇号清册页面，摇号清册列表，点击第一个tab
        """
        self.page.get_element('view[class="hdli on"][data-index="0"]').tap()

        self.get_screenshot()

    def test_05_click_tab2_清册第二个tab(self):
        """
        摇号清册页面，摇号清册列表，点击第二个tab
        """
        self.page.get_element('view[class="hdli"][data-index="1"]').tap()

        self.get_screenshot()

    def test_06_click_tab3_清册第三个tab(self):
        """
        摇号清册页面，摇号清册列表，点击第三个tab
        """
        self.page.get_element('view[class="hdli"][data-index="2"]').tap()

        self.get_screenshot()

    def test_01_click_add_添加(self):
        """
        摇号清册页面，摇号清册列表。点击“添加”按钮
        """
        result = {"confirm": True}
        self.app.mock_wx_method("showModal", result=result)
        self.page.get_element('button[class="bdliB-r disflex-flex-shrink-0"]').tap()
        self.delay(1)
        self.app.restore_wx_method("showModal")
        self.delay(2)
        self.capture("提示")
        self.native.handle_modal("确定", "提示")

        self.get_screenshot()

    def test_09_z_click_share_分享(self):
        """
        摇号清册页面，摇号清册列表，点击分享按钮
        """
        self.page.get_element('button[class="newHouseRfixed-share xfxq_fx"]').tap()

        self.get_screenshot()

