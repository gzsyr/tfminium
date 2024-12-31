# add by zsy
import time

import minium
from ddt import ddt, data

from base.test_mine import TestMine


@ddt
class TestCenterFxzj(TestMine):
    """
    分销中介个人中心页面
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestCenterFxzj, cls).setUpClass()
        cls().change_fxzj()
        print("setupclass change_fxzj")

    def setUp(self) -> None:
        self.page_name = '/page/index/mine?city=qz'
        self.switch = True
        self.classname = self.__class__.__name__
        super(TestCenterFxzj, self).setUp()

    def test_44_复制身份ID(self):
        """
        V6.40.X: 点击 复制身份id
        """
        self.find_element('view[class="roleid"]/text').click()

        self.get_screenshot()

    def test_98_服务指南_邀请入驻(self):
        """
        V6.40.X: 点击邀请入驻
        """
        self.find_element('view[class="name"]', inner_text='邀请入驻').tap()

        self.get_screenshot()

    def click_huoyuedu(self):
        """
        分销中介个人中心页面，点击活跃度
        """
        self.find_element('view[class="desc"]', inner_text='服务分').tap()
        self.delay(2)

        return self

    def test_27_活跃度IM咨询(self):
        """
        V6.27.X: 点击活跃度，点击IM等待时长
        """
        self.click_huoyuedu()

        self.find_element('view[class="pointProgress-name"]', inner_text='IM咨询').tap()

        self.verifyPageName('/im/pages/recentchat/recentchat')
        self.get_screenshot()

    def test_28_活跃度线索转化(self):
        """
        V6.27.X: 点击活跃度，点击IM回复率
        """
        self.click_huoyuedu()

        self.find_element('view[class="pointProgress-name"]', inner_text='线索转化').tap()

        self.verifyPageName('/page/business/fxzjmanage/customerlist')
        self.get_screenshot()

    def test_29_活跃度400电话(self):
        """
        V6.27.X: 点击活跃度，点击400会话时长
        """
        self.click_huoyuedu()

        self.find_element('view[class="pointProgress-name"]', inner_text='400电话').tap()

        self.verifyPageName('/page/message/phoneList')
        self.get_screenshot()

    def test_30_活跃度线索反馈(self):
        """
        V6.27.X: 点击活跃度，点击400通话接通率
        """
        self.click_huoyuedu()

        self.find_element('view[class="pointProgress-name"]', inner_text='线索反馈').tap()

        self.verifyPageName('/page/business/fxzjmanage/customerlist')
        self.get_screenshot()

    def test_31_活跃度线索回拨(self):
        """
        V6.27.X: 点击活跃度，点击客户跟进
        """
        self.click_huoyuedu()

        self.find_element('view[class="pointProgress-name"]', inner_text='线索回拨').tap()

        self.verifyPageName('/page/business/fxzjmanage/customerlist')
        self.get_screenshot()

    def test_32_活跃度关注服务号(self):
        """
        V6.27.X: 点击活跃度，点击关注服务号
        """
        self.click_huoyuedu()

        self.find_element('view[class="btn"][data-type="1"]').tap()

        self.verifyPageName('/page/mine/gzService/gzService')
        self.get_screenshot()

    def test_33_活跃度来电记录(self):
        """
        V6.27.X: 点击活跃度，点击来电记录
        """
        self.click_huoyuedu()

        self.find_element('view[class="btn"][data-type="2"]').tap()

        self.verifyPageName('/page/message/phoneList')
        self.get_screenshot()

    def test_34_活跃度做任务得线索(self):
        """
        V6.27.X: 点击活跃度，点击做任务得线索
        """
        self.click_huoyuedu()

        self.find_element('view[class="btn"][data-type="3"]').tap()

        self.verifyPageName('/page/mine/myscores/myscores')
        self.get_screenshot()

    def test_01_click_帖子(self):
        """
        V6.27.X: 分销中介个人中心页面，点击帖子
        """
        self.find_element('view[class="mp myTfq flex tfAlignC tfFlexC tfFlexV"]').tap()

        self.verifyPageName('/page/business/minetiezi')
        self.get_screenshot()

    def test_02_click_jifen_积分(self):
        """
        V6.27.X: 分销中介个人中心页面，点击积分
        """
        self.find_element('view[class="desc"]', inner_text='积分').tap()

        self.verifyPageName('/page/mine/myscores/alltasks')
        self.get_screenshot()

    def click_quanyiquan(self):
        """
        点击“权益券”
        """
        self.find_element('view[class="desc"]', inner_text='已兑换商品').tap()
        self.delay(3)

    def test_04_click_quanyiquan_权益券(self):
        """
        V6.27.X: 分销中介个人中心页面，点击积分
        """
        self.find_element('view[class="desc"]', inner_text='积分').tap()

        self.verifyPageName('/page/mine/myscores/alltasks')
        self.get_screenshot()

    def test_05_click_my_customer_我的客户全部(self):
        """
        V6.27.X: 分销中介个人中心页面，点击我的客户
        """
        self.find_element('view[class="tfFlex tfAlignC key"]/view', inner_text='全部').tap()

        self.verifyPageName('/page/business/fxzjmanage/customerlist')
        self.get_screenshot()

    def test_06_click_my_customer_我的客户星标(self):
        """
        V6.27.X: 分销中介个人中心页面，点击我的客户
        """
        self.find_element('view[class="tfFlex tfAlignC key"]/view', inner_text='星标').tap()

        self.verifyPageName('/page/business/fxzjmanage/customerlist')
        self.get_screenshot()

    def test_07_click_my_customer_我的客户未跟进(self):
        """
        V6.27.X: 分销中介个人中心页面，点击我的客户
        """
        self.find_element('view[class="tfFlex tfAlignC key"]/view', inner_text='未跟进').tap()

        self.verifyPageName('/page/business/fxzjmanage/customerlist')
        self.get_screenshot()

    def test_08_click_my_customer_我的客户未标记(self):
        """
        V6.27.X: 分销中介个人中心页面，点击我的客户
        """
        self.find_element('view[class="tfFlex tfAlignC key"]/view', inner_text='未标记').tap()

        self.verifyPageName('/page/business/fxzjmanage/customerlist')
        self.get_screenshot()

    def delete_test_09_积分TAB切换(self):
        """
        V6.27.X: 积分抢兑 和 做任务赚积分 tab切换
        """
        self.find_element('view[class="used"]').tap()
        self.find_element('view[class="task"]').tap()

        self.get_screenshot()

    def test_10_做任务去发布(self):
        """
        V6.27.X: 做任务赚积分，点击去发布
        """
        self.find_element('view[class="toPublish"]', inner_text='去发布').tap()

        self.get_screenshot()

    def test_99_做任务去分享(self):
        """
        V6.27.X: 做任务赚积分，点击去分享
        """
        try:
            self.find_element('view[class="task"]', inner_text='做任务赚积分').tap()
        except minium.MiniElementNotFoundError:
            print('当前已经在‘做任务赚积分’的tab下')

        try:
            self.find_element('view[class="toPublish"]', inner_text='去分享').tap()
            self.delay(3)
            self.find_element('button').tap()
        except minium.MiniElementNotFoundError:
            print('无首页分享')
        self.get_screenshot()

    def test_12_查看任务规则(self):
        """
        V6.27.X: 做任务赚积分，点击任务名称
        """
        self.find_element('view[id="showTaskrule"][data-idx="0"]').tap()

        self.get_screenshot()

    def test_13_任务查看更多(self):
        """
        V6.30.X: 更换“点击更多”为“全部任务”
        V6.27.X: 做任务赚积分，点击查看更多
        """
        # self.find_element('view[class="more"]').tap()
        # 点击“全部任务”
        self.find_element('view[class="tomore"]', inner_text='全部任务').tap()

        self.verifyPageName('/page/mine/myscores/alltasks')
        self.get_screenshot()

    def delete_test_14_积分去兑换(self):
        """
        V6.27.X: 积分抢兑TAB, 点击去兑换
        """
        # 点击“积分抢兑”
        try:
            self.find_element('view[class="used"]').tap()
        except minium.MiniElementNotFoundError:
            print('已经在‘积分抢兑’tab下')
        # 点击“去兑换”
        self.find_element('view[class="toDh"]').tap()

        # self.verifyPageName('/page/mine/myscores/goodsdetail')
        self.get_screenshot()

    def delete_test_15_积分抢兑_全部商品(self):
        """
        V6.30.X: 更换“点击更多”为“全部商品”
        V6.27.X: 积分抢兑TAB, 点击查看更多
        """
        # 点击“积分抢兑”
        try:
            self.find_element('view[class="used"]').tap()
        except minium.MiniElementNotFoundError:
            print('已经在‘积分抢兑’tab下')
        # 点击“更多”
        # self.find_element('view[class="more"]').tap()
        # 点击“全部商品”
        self.find_element('view[class="tomore"]', inner_text='全部商品').tap()

        # self.verifyPageName('/page/mine/myscores/scoremall')
        self.get_screenshot()

    def test_03_click_my_card_我的名片(self):
        """
        分销中介个人中心页面，点击我的名片
        """
        self.page.get_element('view[class="mp"]').tap()

        self.verifyPageName('/page/business/fxzjmanage/detail')
        self.get_screenshot()

    def test_97_常用功能_来电记录(self):
        """
        V6.27.X: 常用功能，点击来电记录，点击‘回拨’
        """
        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"]/view', inner_text='来电记录').tap()

        self.verifyPageName('/page/message/phoneList')
        self.get_screenshot('来电记录页面展示')

        try:
            self.find_element('view[class="callBack"]', inner_text='回拨').tap()
            self.get_screenshot()
        except minium.MiniElementNotFoundError:
            self.get_screenshot('无来电记录')

    def test_16_常用功能_回拨记录(self):
        """
        V7.17: 常用功能_回拨记录
        """
        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"]/view', inner_text='回拨记录').tap()

        self.verifyPageName('/page/business/fxzjmanage/callback')
        self.get_screenshot()

    def test_20_常用功能_回拨记录(self):
        """
        V7.17: 常用功能_回拨记录
        """
        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"]/view', inner_text='回拨记录').tap()
        self.delay(2)
        self.verifyPageName('/page/business/fxzjmanage/callback')
        self.get_screenshot()

    def test_23_常用功能_房贷计算器(self):
        """
        V7.17: 常用功能_房贷计算器
        """
        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"]/view', inner_text='房贷计算器').tap()

        self.verifyPageName('/page/tools/fdjsq/sd/index')
        self.get_screenshot()

    def test_25_常用功能_采光计算器(self):
        """
        V7.17: 常用功能_采光计算器
        """
        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"]/view', inner_text='采光计算器').tap()

        self.verifyPageName('/page/tools/cgjsq/cgjsq')
        self.get_screenshot()

    def test_35_常用功能_积分商城(self):
        """
        V7.17: 常用功能_积分商城
        """
        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"]/view', inner_text='积分商城').tap()

        self.get_screenshot()

    def test_17_常用功能_消息线索查看(self):
        """
        V6.27.X: 常用功能，点击’消息‘，线索派发的消息，点击“查看更多”
        """
        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"]//view', text_contains='消息').tap()

        self.verifyPageName('/page/business/zygwmsglist')
        self.get_screenshot('消息页面展示')
        self.delay(1)

        try:
            self.find_element('view[class="todetail flex tfAlignC tfFlexSb"]').tap()

            # self.verifyPageName('/page/business/infoManage/customerList')
            self.get_screenshot()
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有线索消息')

    def click_callrecord(self):
        """
        客户消息，点击“回拨记录”
        """
        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"]/view', inner_text='回拨记录').tap()
        self.delay(2)

    def test_39_回拨记录_日期切换(self):
        """
        V6.27.X: 客户消息，点击“回拨记录”，切换回拨日期
        """
        self.click_callrecord()
        self.delay(2)

        self.find_element('view[data-idx="1"]', inner_text='昨日回拨').tap()
        self.get_screenshot('昨日回拨')

        self.find_element('view[data-idx="2"]', inner_text='近七日回拨').tap()
        self.get_screenshot('近七日回拨')

        self.find_element('view[data-idx="0"]', inner_text='今日回拨').tap()
        self.get_screenshot('今日回拨')

    def click_imset(self):
        """
        客户消息，点击“IM咨询配置”
        """
        self.find_element('view[class="item flex tfAlignC tfFlexV tfFlexC"]/view', inner_text='IM咨询配置').tap()
        self.delay(2)

    def test_40_IM_常用语设置(self):
        """
        V6.27.X: 客户消息，点击“IM咨询配置”，点击“常用语设置”
        """
        self.click_imset()

        self.find_element('view[class="inner disflex tfAlignC tfFlexSb"]/view', inner_text='常用语设置').tap()

        self.verifyPageName('/page/business/quickReply')
        self.get_screenshot()

    def test_41_IM_自动回复设置(self):
        """
        V6.27.X: 客户消息，点击“IM咨询配置”，点击“自动回复设置”
        """
        self.click_imset()

        self.find_element('view[class="inner disflex tfAlignC tfFlexSb"]/view', inner_text='自动回复设置').tap()

        self.verifyPageName('/page/business/autoreplyadd')
        self.get_screenshot()

    def test_42_IM_邀请致电设置(self):
        """
        V6.27.X: 客户消息，点击“IM咨询配置”，点击“邀请致电设置”
        """
        self.click_imset()

        self.find_element('view[class="inner disflex tfAlignC tfFlexSb"]/view', inner_text='邀请致电设置').tap()

        self.verifyPageName('/page/business/autoreplyadd')
        self.get_screenshot()

    def test_18_点击横幅广告(self):
        """
        V6.27.X: 点击“横幅广告”
        """
        self.find_element('image[class="ad"]').tap()

        self.get_screenshot()

    def test_19_服务指南_关注服务号(self):
        """
        分销中介个人中心页面，点击关注服务号
        """
        self.find_element('view[class="name"]', inner_text='关注服务号').tap()

        self.verifyPageName('/page/mine/gzService/gzService')
        self.get_screenshot()

    def click_set_icon(self):
        self.find_element('view[class="set"]').tap()
        self.delay(2)
        return self

    def test_24_设置修改资料(self):
        """
        V6.27.X: 分销中介个人中心页面，点击设置，点击修改资料
        """
        self.click_set_icon()

        self.find_element('view[class="inner disflex tfAlignC tfFlexSb"]/view', inner_text='修改资料').tap()

        self.verifyPageName('/page/business/fxzjmanage/updateinfo')
        self.get_screenshot()

    def test_26_设置我的红包(self):
        """
        V6.27.X: 分销中介个人中心页面，点击设置，点击我的红包
        """
        self.click_set_icon()

        self.find_element('view[class="inner disflex tfAlignC tfFlexSb"]/view', inner_text='我的红包').tap()

        self.verifyPageName('/page/mine/wdhb/wdhb')
        self.get_screenshot()

    def test_22_服务指南_隐私政策(self):
        """
        分销中介个人中心页面，点击隐私权政策
        """
        self.find_element('view[class="name"]', inner_text='隐私权政策').tap()

        self.verifyPageName('/page/index/notice')
        self.get_screenshot()

    def test_21_服务指南_意见反馈(self):
        """
        分销中介个人中心页面，点击意见反馈
        """
        self.find_element('view[class="name"]', inner_text='意见反馈').tap()

        self.verifyPageName('/page/mine/wtfk/wtfk')
        self.get_screenshot()


    # @classmethod
    # def tearDownClass(cls):
    #     cls().app.go_home()
    #     super(TestCenterZygw, cls).tearDownClass()
