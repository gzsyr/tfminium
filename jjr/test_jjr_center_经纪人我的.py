# -*-coding:utf-8-*-
import minium

from base.test_mine import TestMine


class TestCenterJJR(TestMine):
    """
    经纪人身份，我的页面
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestCenterJJR, cls).setUpClass()
        cls().change_jjr()
        print("setupclass testcenterjjr")

    def setUp(self) -> None:
        self.page_name = '/page/index/mine?city=nj'
        self.switch = True
        self.classname = self.__class__.__name__
        super(TestCenterJJR, self).setUp()

    def test_023_查看课程(self):
        """
        V6.45.X: 转到课程详情页
        """
        self.find_element('view[class="name"]', inner_text='操作指南').tap()
        self.get_screenshot('跳转到课程中心页')
        self.verifyPageName('/page/business/classguide/classguide')

        self.delay(1)
        self.find_element('view[class="content_title"]').tap()
        self.get_screenshot('跳转到课程详情页')
        self.verifyPageName('/page/business/classguide/classguidedetail')

    def test_001_点击头像(self):
        """
        点击头像，进入用户信息页
        """
        self.find_element('image[class="avatar"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/mine/myinfo/myinfo')

    def delete_test_002_点击淘房圈发帖(self):
        """
        点击“淘房圈发帖”，进入写贴子页面
        """
        self.find_element('view[class="name"]', inner_text='淘房圈发帖').tap()

        self.get_screenshot()
        self.verifyPageName('/page/taofangquan/writePost/writePost')

    def test_003_点击我的帖子(self):
        """
        点击“我的帖子”，进入我的帖子页面
        """
        self.find_element('view[class="dp myTfq flex tfAlignC tfFlexC tfFlexV"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/business/minetiezi')

    def test_004_点击我的店铺(self):
        """
        点击”我的店铺“，进入我的店铺页面
        """
        self.find_element('view[class="dp"]').tap()

        self.get_screenshot()
        self.verifyPageName('/esf/sell/pages/broker/broker')

    def goto_im_setting(self):

        # 点击 IM咨询配置
        self.find_element('view[class="name"]', inner_text='IM咨询配置').tap()

        self.delay(8)

        # 点击 常用语设置
        self.find_element('view[class="inner disflex tfAlignC tfFlexSb"]/view', inner_text='常用语设置').tap()

        return self

    def test_005_进入常用语设置页(self):
        """
        点击“IM咨询配置”，点击“常用语设置”，进入常用语设置页面
        """
        self.goto_im_setting()

        self.get_screenshot()
        self.verifyPageName('/page/business/quickReply')

    def test_006_新增常用语(self):
        """
        点击“IM咨询配置”，点击“常用语设置”，进入常用语设置页面，新增一条常用语
        """
        self.goto_im_setting()
        self.delay(3)

        # 点击“新增常用语”按钮
        self.find_element('button[class="addBtn zygwBtn"]').tap()
        self.delay(2)

        # 输入内容，点击保存
        self.find_element('textarea').input('经纪人录入常用语设置：test_006_新增常用语！')

        # 点击“保存”按钮
        self.find_element('button').tap()

        self.get_screenshot()
        self.verifyPageName('/page/business/quickReply')

    def test_007_编辑常用语(self):
        """
        点击“IM咨询配置”，点击“常用语设置”，进入常用语设置页面，编辑新增的一条常用语
        """
        self.goto_im_setting()
        self.delay(3)

        # 选择  test_006_新增常用语  新增的常用语
        if self.element_is_exist('view[class="cyyList_content"]', inner_text='经纪人录入常用语设置：test_006_新增常用语！'):
            self.find_element('image[class="edit_img"]').tap()
            self.delay(2)
            self.find_element('textarea').input('test_007_编辑常用语')
            self.find_element('button').tap()

    def test_008_删除常用语(self):
        """
        点击“IM咨询配置”，点击“常用语设置”，进入常用语设置页面，删除新增编辑的一条常用语
        """
        self.goto_im_setting()
        self.delay(3)

        # 选择  test_006_新增常用语  新增的常用语
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.find_element('image[class="delete_img"]').tap()
            self.app.restore_wx_method("showModal")
        except:
            print('无可删除的常用语配置，直接通过')
            self.get_screenshot('无可删除的常用语配置')

        self.get_screenshot()

    def goto_im_autoreply(self):
        # 点击 IM咨询配置
        self.find_element('view[class="name"]', inner_text='IM咨询配置').tap()

        self.delay(3)

        # 点击 常用语设置
        self.find_element('view[class="inner disflex tfAlignC tfFlexSb"]/view', inner_text='自动回复设置').tap()

        return self

    def test_009_进入自动回复设置页(self):
        """
        点击“IM咨询配置”，点击“自动回复设置”，进入自动回复设置页面
        """
        self.goto_im_autoreply()

        self.get_screenshot()
        self.verifyPageName('/page/business/autoreplyadd')

    def test_010_保存自动回复(self):
        """
        点击“IM咨询配置”，点击“自动回复设置”，进入自动回复设置页面，输入内容保存
        """
        self.goto_im_autoreply()
        self.delay(2)

        self.find_element('textarea').input('您好，现在正忙，稍后回复您！')
        self.find_element('button').tap()

        self.get_screenshot()
        self.verifyPageName('/page/business/setting')

    def test_011_点击系统通知(self):
        """
        点击常用功能：系统通知，进入系统通知页
        """
        self.find_element('view[class="name"]', inner_text='系统通知').tap()

        self.get_screenshot()
        self.verifyPageName('/page/business/zygwmsglist')

    def test_012_点击关注服务号(self):
        """
        点击服务指南：关注服务号，进入关注页面
        """
        self.find_element('view[class="name"]', inner_text='关注服务号').tap()

        self.get_screenshot()
        self.verifyPageName('/page/mine/gzService/gzService')

    def test_013_点击意见反馈(self):
        """
        点击服务指南：完成意见反馈
        """
        self.find_element('view[class="name"]', inner_text='意见反馈').tap()

        self.get_screenshot()
        self.verifyPageName('/page/mine/wtfk/wtfk')

    def test_014_点击隐私权政策(self):
        """
        点击服务指南：隐私权政策
        """
        self.find_element('view[class="name"]', inner_text='隐私权政策').tap()

        self.get_screenshot()
        self.verifyPageName('/page/index/notice')

    def test_015_点击素材库(self):
        """
        V6.38.x: 点击 素材库
        """
        self.find_element('swiper[class="store-swiper"]').tap()
        self.delay(1)
        self.get_screenshot()
        self.verifyPageName('/page/taofangquan/contentstore/contentstore')

    def click_jifen(self, desc='我的积分'):
        """
        点击 我的积分 ，已兑换商品
        """
        self.find_element('view[class="desc"]', inner_text=desc).tap()
        self.delay(2)

    def test_016_点击我的积分(self):
        """
        V6.38.x: 点击 我的积分，进入积分页面
        """
        self.click_jifen(desc='我的积分')

        self.get_screenshot()
        self.verifyPageName('/page/mine/myscores/myscores')

    def test_017_已兑换商品_待使用_赚积分(self):
        """
        V6.38.x: 点击 已兑换商品，待使用  赚积分
        """
        self.click_jifen(desc='已兑换商品')
        self.get_screenshot('已兑换商品')
        self.verifyPageName('/page/mine/myscores/mycoupons')

        self.find_element('view[class="getJf"]').tap()
        self.get_screenshot('点击赚积分到我的积分页面')
        self.verifyPageName('/page/mine/myscores/myscores')

    def test_018_已兑换商品_已使用_赚积分(self):
        """
        V6.38.X: 点击 已兑换商品，已使用  赚积分
        """
        self.click_jifen(desc='已兑换商品')

        self.find_element('view[class="used"]').tap()
        self.delay(2)
        self.find_element('view[class="getJf"]').tap()
        self.get_screenshot('点击赚积分到我的积分页面')
        self.verifyPageName('/page/mine/myscores/myscores')

    def test_019_点击任务1(self):
        """
        V6.38.X: 点击 任务 1
        """
        self.find_element('view[class="toPublish"]').tap()

        self.get_screenshot()

    def test_019_点击任务2(self):
        """
        V6.38.X: 点击 任务2
        """
        try:
            self.find_elements('view[class="toPublish"]')[1].tap()
        except:
            print('没有两个任务')

        self.get_screenshot()

    def test_020_点击全部任务(self):
        """
        V6.38.X: 点击 全部任务
        """
        self.find_element('view[class="tomore"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/mine/myscores/alltasks')

    def test_021_积分兑换(self):
        """
        V6.38.X: 点击 积分抢兑，去兑换商品
        """
        # 点击“积分抢兑”
        try:
            self.find_element('view[class="used"]').tap()
        except minium.MiniElementNotFoundError:
            print('已经在‘积分抢兑’tab下')
        # 点击“去兑换”
        self.find_element('view[class="toDh"]').tap()
        self.delay(3)

        # 商品页面点击兑换
        self.find_element('view[class="btnSubmit"]').tap()

        self.get_screenshot()

    def test_022_积分抢兑_全部商品_查看商品(self):
        """
        V6.38.X: 点击积分抢兑  点击全部商品 点击去兑换
        """
        try:
            self.find_element('view[class="used"]').tap()
        except minium.MiniElementNotFoundError:
            print('已经在‘积分抢兑’tab下')
        # 点击“更多”
        # self.find_element('view[class="more"]').tap()
        # 点击“全部商品”
        self.find_element('view[class="tomore"]', inner_text='全部商品').tap()
        self.delay(4)

        self.find_element('view[class="btn"]').tap()

    def test_kh_001_进入客户列表(self):
        """
        V6.40.x: 点击  全部客户、未跟进、未标记，分别进入列表页
        """
        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"][data-type="1"]').tap()
        self.delay(2)

        self.get_screenshot('全部客户列表页')
        self.verifyPageName('/page/business/customerManage/myCustomer/myCustomer')
        self.back()

        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"][data-type="2"]').tap()
        self.delay(2)

        self.get_screenshot('未跟进列表页')
        self.verifyPageName('/page/business/customerManage/myCustomer/myCustomer')
        self.back()

        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"][data-type="3"]').tap()
        self.delay(2)

        self.get_screenshot('未标记列表页')
        self.verifyPageName('/page/business/customerManage/myCustomer/myCustomer')
