import time

from base.test_base import TestBase


class TestKFT(TestBase):
    """
    看房团页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/houseteam/list?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestKFT, self).setUp()
        
    def test_01_click_kfxq_看房需求(self):
        """
        前置条件是登录，
        手机号是登录之后自动获取，
        看房团页面，点击看房需求，
        键入当日日期，
        点击楼盘输入框，进入新页面，
        点击输入框，输入‘苏宁’
        点击‘苏宁测试1’，返回，
        点击立即报名
        """
        self.find_element("view[class='kftfixed-r']").tap()
        self.delay(10)

        # 输入日期
        self.set_pick_filter('picker', time.strftime('%Y-%m-%d'))

        # 点击楼盘名称，到搜索页搜索楼盘
        self.find_element('view.kfxqLi-l').tap()
        self.app.wait_for_page('/page/search/index')
        self.find_element('input.searchTR-input').input('苏宁')
        self.delay(5)
        self.find_element('view.searchBLi').tap()
        self.delay(5)

        tap = 'self.page.get_element(\'button.kfxqSub.kgt_tjxq\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '发布看房需求ok')
        self.get_screenshot()

    def test_02_click_route1_看房线路(self):
        """
        点击第一条路线
        """
        self.page.get_element('view[class="kftliLi-l"]', inner_text="测试22").tap()

        self.verifyPageName('/page/houseteam/detail')
        self.get_screenshot()

    def test_05_click_zphone_电话咨询(self):
        """
        点击电话咨询
        """
        self.page.get_element('view[class="kftliBtn-style bg_448bc3 kgt_phone"]').tap()
        # self.delay(1)
        # self.verifyByScreenshot('xf/call.png')
        self.get_screenshot()

    def test_03_click_signup_我要报名(self):
        """
        点击我要报名,点击我已阅读小√，输入手机号，点击获取验证码
        """
        self.page.get_element('view[class="kftliBtn-style bg_ff5500"]').tap()
        self.app.wait_for_page('/page/houseteam/apply')
        self.page.get_element('image.agree-icon').tap()
        self.page.get_element('input', inner_text='请填写11位手机号码').input('15105182846')
        self.page.get_element('input', inner_text='请填写姓名').input('测试人员')
        self.page.get_element('input', inner_text='请填写报名人数').input('11')
        self.page.get_element('input', inner_text='请输入验证码').input('11')
        self.page.get_element('button.btn-submit').tap()

        self.get_screenshot()

    # @unittest.skip("加群图标已删除")
    # def test_click_addgroup(self):
    #     """
    #     点击加群图标
    #     """
    #     self.page.get_element('add-group[is="component/addgroup"]').get_element('image[role="img"]').tap()
    #     self.delay(1)

    def test_04_click_zallroutes_全部线路(self):
        """
        点击全部路线下拉箭头
        """
        # self.page.get_element('view[class="headTR-select"]').tap()
        self.set_pick_filter('picker', 3)

        self.verifyStr(True, self.page.element_is_exists('view[class="headTL-allLine"]', inner_text='线路1'),
                       "选择线路1，ok")
        self.get_screenshot()

