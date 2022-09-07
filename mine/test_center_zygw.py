# add by zsy
from ddt import ddt, data

from base.test_mine import TestMine


@ddt
class TestCenterZygw(TestMine):
    """
    置业顾问个人中心页面
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestCenterZygw, cls).setUpClass()
        cls().change_zygw()
        print("setupclass change_zygw")

    def setUp(self) -> None:
        self.page_name = '/page/index/mine?city=qz'
        self.switch = True
        self.classname = self.__class__.__name__
        super(TestCenterZygw, self).setUp()

    def test_click_huoyuedu(self):
        """
        置业顾问个人中心页面，点击活跃度
        """
        self.page.get_element('view[class="desc"]', inner_text='活跃度').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def test_click_jifen(self):
        """
        置业顾问个人中心页面，点击积分
        """
        self.page.get_element('view[class="desc"]', inner_text='积分').tap()

        self.verifyPageName('/page/mine/myscores/myscores')
        self.get_screenshot()

    def test_click_quanyiquan(self):
        """
        置业顾问个人中心页面，点击权益券
        """
        self.page.get_element('view[class="desc"]', inner_text='权益券').tap()

        self.verifyPageName('/page/mine/myscores/mycoupons')
        self.get_screenshot()

    def test_click_my_jifen(self):
        """
        置业顾问个人中心页面，点击我的积分
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的积分').tap()

        self.verifyPageName('/page/mine/myscores/myscores')
        self.get_screenshot()

    def test_click_my_customer(self):
        """
        置业顾问个人中心页面，点击我的客户
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的客户').tap()

        self.verifyPageName('/page/business/infoManage/customerList')
        self.get_screenshot()

    def test_click_my_card(self):
        """
        置业顾问个人中心页面，点击我的名片
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的名片').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def test_click_my_house(self):
        """
        置业顾问个人中心页面，点击来电记录
        """
        self.page.get_element('view[class="tab-text"]', inner_text='来电记录').tap()

        self.verifyPageName('/page/message/phoneList')
        self.get_screenshot()

    def test_click_my_fuwuhao(self):
        """
        置业顾问个人中心页面，点击关注服务号
        """
        self.page.get_element('view[class="tab-text"]', inner_text='关注服务号').tap()

        self.verifyPageName('/page/mine/gzService/gzService')
        self.get_screenshot()

    def test_click_my_quanzi(self):
        """
        置业顾问个人中心页面，点击我的圈子
        """
        self.page.get_element('view[class="name"]', inner_text='我的圈子').tap()

        self.verifyPageName('/page/mine/myQuanzi/myQuanzi')
        self.get_screenshot()

    def test_click_my_huati(self):
        """
        置业顾问个人中心页面，点击我的话题
        """
        self.page.get_element('view[class="name"]', inner_text='我的话题').tap()

        self.verifyPageName('/page/mine/myHuati/myHuati')
        self.get_screenshot()

    def test_click_my_tiezi(self):
        """
        置业顾问个人中心页面，点击我的帖子
        """
        self.page.get_element('view[class="name"]', inner_text='我的帖子').tap()

        self.verifyPageName('/page/mine/myTopic/myTopic')
        self.get_screenshot()

    def test_click_my_pinglun(self):
        """
        置业顾问个人中心页面，点击我的评论
        """
        self.page.get_element('view[class="name"]', inner_text='我的评论').tap()

        self.verifyPageName('/page/mine/myComment/myComment')
        self.get_screenshot()

    def test_click_my_draftbox(self):
        """
        置业顾问个人中心页面，点击草稿箱
        """
        self.page.get_element('view[class="name"]', inner_text='草稿箱').tap()

        self.verifyPageName('/page/mine/draftBox/draftBox')
        self.get_screenshot()

    @data(0, 1, 2, 3, 4)
    def test_click_tools(self, index):
        """
        置业顾问个人中心页面，点击常用工具
        """
        self.page.get_element(f'view[class="tab-item"][data-index="{index}"]').tap()

        self.get_screenshot()

    def test_goto_setting(self):
        """
        置业顾问个人中心页面，点击个人设置
        """
        self.page.get_element('view[id="setting"]').tap()

        self.verifyPageName('/page/business/setting')
        self.get_screenshot()

    def test_goto_policy(self):
        """
        置业顾问个人中心页面，点击隐私权政策
        """
        self.page.get_element('view[id="privacyPolicy"]').tap()

        self.verifyPageName('/page/index/notice')
        self.get_screenshot()

    def test_goto_feedback(self):
        """
        置业顾问个人中心页面，点击意见反馈
        """
        self.page.get_element('view[id="yjfk"]').tap()

        self.verifyPageName('/page/mine/wtfk/wtfk')
        self.get_screenshot()

    def test_goto_packet(self):
        """
        置业顾问个人中心页面，点击我的红包
        """
        self.page.get_element('view[id="myHongBao"]').tap()

        self.verifyPageName('/page/mine/wdhb/wdhb')
        self.get_screenshot()

    # @classmethod
    # def tearDownClass(cls):
    #     cls().app.go_home()
    #     super(TestCenterZygw, cls).tearDownClass()