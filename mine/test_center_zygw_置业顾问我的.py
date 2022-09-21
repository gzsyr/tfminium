# add by zsy
import time

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

    def test_01_click_huoyuedu_活跃度(self):
        """
        置业顾问个人中心页面，点击活跃度
        """
        self.page.get_element('view[class="desc"]', inner_text='活跃度').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def test_02_click_jifen_积分(self):
        """
        置业顾问个人中心页面，点击积分
        """
        self.page.get_element('view[class="desc"]', inner_text='积分').tap()

        self.verifyPageName('/page/mine/myscores/myscores')
        self.get_screenshot()

    def test_13_click_quanyiquan_权益券(self):
        """
        置业顾问个人中心页面，点击权益券
        """
        self.page.get_element('view[class="desc"]', inner_text='权益券').tap()

        self.verifyPageName('/page/mine/myscores/mycoupons')
        self.get_screenshot()

    def test_09_click_my_jifen_我的积分(self):
        """
        置业顾问个人中心页面，点击我的积分
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的积分').tap()

        self.verifyPageName('/page/mine/myscores/myscores')
        self.get_screenshot()

    def test_04_click_my_customer_我的客户(self):
        """
        置业顾问个人中心页面，点击我的客户
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的客户').tap()

        self.verifyPageName('/page/business/infoManage/customerList')
        self.get_screenshot()

    def test_03_click_my_card_我的名片(self):
        """
        置业顾问个人中心页面，点击我的名片
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的名片').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def test_07_click_my_house_来电记录(self):
        """
        置业顾问个人中心页面，点击来电记录
        """
        self.page.get_element('view[class="tab-text"]', inner_text='来电记录').tap()

        self.verifyPageName('/page/message/phoneList')
        self.get_screenshot()

    def test_06_click_my_fuwuhao_关注服务号(self):
        """
        置业顾问个人中心页面，点击关注服务号
        """
        self.page.get_element('view[class="tab-text"]', inner_text='关注服务号').tap()

        self.verifyPageName('/page/mine/gzService/gzService')
        self.get_screenshot()

    def test_11_click_my_quanzi_我的圈子(self):
        """
        置业顾问个人中心页面，点击我的圈子
        """
        self.page.get_element('view[class="name"]', inner_text='我的圈子').tap()

        self.verifyPageName('/page/mine/myQuanzi/myQuanzi')
        self.get_screenshot()

    def test_08_click_my_huati_我的话题(self):
        """
        置业顾问个人中心页面，点击我的话题
        """
        self.page.get_element('view[class="name"]', inner_text='我的话题').tap()

        self.verifyPageName('/page/mine/myHuati/myHuati')
        self.get_screenshot()

    def test_12_click_my_tiezi_我的帖子(self):
        """
        置业顾问个人中心页面，点击我的帖子
        """
        self.page.get_element('view[class="name"]', inner_text='我的帖子').tap()

        self.verifyPageName('/page/mine/myTopic/myTopic')
        self.get_screenshot()

    def test_10_click_my_pinglun_我的评论(self):
        """
        置业顾问个人中心页面，点击我的评论
        """
        self.page.get_element('view[class="name"]', inner_text='我的评论').tap()

        self.verifyPageName('/page/mine/myComment/myComment')
        self.get_screenshot()

    def test_05_click_my_draftbox_草稿箱(self):
        """
        置业顾问个人中心页面，点击草稿箱
        """
        self.page.get_element('view[class="name"]', inner_text='草稿箱').tap()

        self.verifyPageName('/page/mine/draftBox/draftBox')
        self.get_screenshot()

    @data(0, 1, 2, 3, 4)
    def test_14_click_tools_常用工具(self, index):
        """
        置业顾问个人中心页面，点击常用工具
        """
        self.page.get_element(f'view[class="tab-item"][data-index="{index}"]').tap()

        self.get_screenshot()

    def test_22_goto_setting_个人设置(self):
        """
        置业顾问个人中心页面，点击个人设置
        """
        self.page.get_element('view[id="setting"]').tap()

        self.verifyPageName('/page/business/setting')
        self.get_screenshot()

    def test_21_goto_policy_隐私政策(self):
        """
        置业顾问个人中心页面，点击隐私权政策
        """
        self.page.get_element('view[id="privacyPolicy"]').tap()

        self.verifyPageName('/page/index/notice')
        self.get_screenshot()

    def test_19_goto_feedback_意见反馈(self):
        """
        置业顾问个人中心页面，点击意见反馈
        """
        self.page.get_element('view[id="yjfk"]').tap()

        self.verifyPageName('/page/mine/wtfk/wtfk')
        self.get_screenshot()

    def test_20_goto_packet_我的红包(self):
        """
        置业顾问个人中心页面，点击我的红包
        """
        self.page.get_element('view[id="myHongBao"]').tap()

        self.verifyPageName('/page/mine/wdhb/wdhb')
        self.get_screenshot()

    def test_23_mycustomer_search_comment_搜客户写跟进(self):
        """
        置业顾问个人中心，我的客户页面，搜索后的第一个结果写跟进记录
        """
        self.page.get_element('view[class="tab-text"]', inner_text='我的客户').tap()
        self.delay(3)
        # 我的客户页面
        # 搜索客户
        self.page.get_element('input[class="search-input"]').input('1122'+'\n')
        self.delay(3)
        # 点击第一个搜索结果
        try:
            # self.page.get_element('image[class="btnIcon"]').tap()
            self.page.get_element('text', inner_text='写跟进').tap()
        except:
            print('没有搜索到客户数据，用例通过')
            self.get_screenshot()
            return

        self.add_comment(bz=time.strftime('%Y-%m-%d %H:%M:%S'))

        self.get_screenshot()

    def add_comment(self, yx='高', lx='普通跟进', zt='联系不上', bz='test'):
        """
        添加跟进记录页面
        """
        self.delay(1)
        if yx:
            self.page.get_element('view[class="tagitem"][data-index="0"]', inner_text=yx).tap()
        if lx:
            lxele = self.page.get_element('view[data-index="1"]', inner_text=lx)
            a = lxele.attribute('class')
            if 'active' not in a[0]:
                lxele.tap()
        if zt:
            self.page.get_element('view[class="tagitem"][data-index="2"]', inner_text=zt).tap()
        if bz:
            self.page.get_element('textarea').input(bz)

        tap = 'self.page.get_element(\'button\').tap()'
        self.getShowToast(tap)


    # @classmethod
    # def tearDownClass(cls):
    #     cls().app.go_home()
    #     super(TestCenterZygw, cls).tearDownClass()
