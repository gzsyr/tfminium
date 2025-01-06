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

    def click_setting(self):
        """
        V7.17: 点击设置
        """
        self.find_element('image[class="set"]').tap()
        self.delay(3)
    def test_046_点击设置(self):
        """
        V7.17: 点击设置
        """
        self.click_setting()

        self.verifyPageName('/page/mine/brokerSetting/brokerSetting')
        self.get_screenshot()

    def test_047_点击设置_修改资料(self):
        """
        V7.17: 点击设置  修改资料
        """
        self.click_setting()
        self.find_element('view[class="flex a_c key"]/text', inner_text='修改资料').tap()

        self.verifyPageName('/page/mine/brokerEdit/brokerEdit')
        self.get_screenshot()

    def test_048_点击设置_IM咨询配置(self):
        """
        V7.17: 点击设置  IM咨询配置
        """
        self.click_setting()
        self.find_element('view[class="flex a_c key"]/text', inner_text='IM咨询配置').tap()

        self.verifyPageName('/page/business/setting')
        self.get_screenshot()

    def test_049_点击设置_推送配置(self):
        """
        V7.17: 点击设置  推送配置
        """
        self.click_setting()
        self.find_element('view[class="flex a_c key"]/text', inner_text='推送配置').tap()

        self.verifyPageName('/page/mine/pushSetting/pushSetting')
        self.get_screenshot()

    def test_050_点击设置_个人房源帮聊(self):
        """
        V7.17: 点击设置  个人房源帮聊
        """
        self.click_setting()
        self.find_element('view[class="flex a_c key"]/text', inner_text='个人房源帮聊').tap()

        self.verifyPageName('/page/mine/helpChat/helpChat')
        self.get_screenshot()

    def test_051_点击设置_我的套餐(self):
        """
        V7.17: 点击设置  我的套餐
        """
        self.click_setting()
        self.find_element('view[class="flex a_c key"]/text', inner_text='我的套餐').tap()

        self.get_screenshot()

    def test_052_点击设置_修改手机(self):
        """
        V7.17: 点击设置  修改手机
        """
        self.click_setting()
        self.find_element('view[class="flex a_c key"]/text', inner_text='修改手机').tap()

        self.verifyPageName('/page/mine/brokerTelEdit/brokerTelEdit')
        self.get_screenshot()

    def test_024_点击购买套餐(self):
        """
        V7.17: 点击 购买套餐
        """
        self.find_element('view[class="jjr_btn"]', inner_text='购买套餐').tap()

        self.get_screenshot()

    def test_025_点击租售一体激活(self):
        """
        V7.17: 点击 租售一体激活
        """
        self.find_element('view[class="item"][data-index="0"]').tap()

        self.verifyPageName('/zsb/manage/sell')
        self.get_screenshot()

    def test_026_点击纯租激活(self):
        """
        V7.17: 点击 纯租激活
        """
        self.find_element('view[class="item"][data-index="1"]').tap()

        self.verifyPageName('/zsb/manage/rent')
        self.get_screenshot()

    def test_027_点击纯售激活(self):
        """
        V7.17: 点击 纯寿激活
        """
        self.find_element('view[class="item"][data-index="2"]').tap()

        self.verifyPageName('/zsb/manage/sell')
        self.get_screenshot()

    def test_028_点击房豆(self):
        """
        V7.17: 点击 房豆
        """
        self.find_element('view[class="item"][data-index="3"]').tap()

        self.verifyPageName('/zsb/houseBeanLog/houseBeanLog')
        self.get_screenshot()

    def test_029_点击放心看(self):
        """
        V7.17: 点击 放心看
        """
        self.find_element('view[class="item"][data-index="4"]').tap()

        self.verifyPageName('/zsb/manage/sell')
        self.get_screenshot()

    def test_030_点击急推(self):
        """
        V7.17: 点击 急推
        """
        self.find_element('view[class="item"][data-index="6"]').tap()

        self.verifyPageName('/zsb/manage/rent')
        self.get_screenshot()

    def test_031_点击售租新增(self):
        """
        V7.17: 点击 售|租新增
        """
        self.find_element('view[class="item"][data-index="7"]').tap()

        self.verifyPageName('/zsb/manage/sell')
        self.get_screenshot()

    def test_032_点击出售管理(self):
        """
        V7.17: 点击 出售管理
        """
        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV tile"][data-index="0"]').tap()

        self.verifyPageName('/zsb/manage/sell')
        self.get_screenshot()

    def test_033_点击出租管理(self):
        """
        V7.17: 点击 出租管理
        """
        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV tile"][data-index="1"]').tap()

        self.verifyPageName('/zsb/manage/rent')
        self.get_screenshot()

    def test_034_点击发布出售(self):
        """
        V7.17: 点击 发布出售
        """
        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV tile"][data-index="2"]').tap()

        self.verifyPageName('/zsb/publish/sell')
        self.get_screenshot()

    def test_035_点击发布出租(self):
        """
        V7.17: 点击 发布出租
        """
        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV tile"][data-index="3"]').tap()

        self.verifyPageName('/zsb/publish/rent')
        self.get_screenshot()

    def test_036_点击房源优推(self):
        """
        V7.17: 点击 房源优推
        """
        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV tile"][data-index="4"]').tap()

        self.get_screenshot()

    def test_037_点击获客榜单(self):
        """
        V7.17: 点击 获客榜单
        """
        self.find_element('view[class="jjr_btn"]', inner_text='获客榜单').tap()

        self.verifyPageName('/page/business/broker/jjrranklist')
        self.get_screenshot()

    def test_038_点击房豆抢客(self):
        """
        V7.17: 点击 房豆抢客
        """
        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV tile"][data-index="0"]/view', inner_text='房豆抢客').tap()

        self.get_screenshot()

    def delete_test_039_点击积分抢客(self):
        """
        V7.17: 点击 积分抢客
        """
        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV tile"][data-index="1"]/view', inner_text='积分抢客').tap()

        self.get_screenshot()

    def test_040_点击房源点击量(self):
        """
        V7.17: 点击 房源点击量
        """
        self.find_element('view[class="key"]', inner_text='房源点击量').tap()

        self.verifyPageName('/zsb/profileData/profileData')
        self.get_screenshot()

    def test_041_点击优推房源量(self):
        """
        V7.17: 点击 优推房源量
        """
        self.find_element('view[class="key"]', inner_text='优推房源量').tap()

        self.verifyPageName('/zsb/profileData/profileData')
        self.get_screenshot()

    def test_042_点击IM咨询人数(self):
        """
        V7.17: 点击 IM咨询人数
        """
        self.find_element('view[class="key"]', inner_text='IM咨询人数').tap()

        self.verifyPageName('/zsb/profileData/profileData')
        self.get_screenshot()

    def test_043_点击IM1分钟回复率(self):
        """
        V7.17: 点击 IM1分钟回复率
        """
        self.find_element('view[class="key"]', inner_text='IM1分钟回复率').tap()

        self.verifyPageName('/zsb/profileData/profileData')
        self.get_screenshot()

    def test_044_点击房贷计算器(self):
        """
        V7.17: 点击 房贷计算器
        """
        self.find_element('view[class="item"][data-type="1"]/view[class="name"]', inner_text='房贷计算器').tap()

        self.verifyPageName('/page/tools/fdjsq/sd/index')
        self.get_screenshot()

    def test_045_点击采光计算器(self):
        """
        V7.17: 点击 采光计算器
        """
        self.find_element('view[class="item"][data-type="2"]/view[class="name"]', inner_text='采光计算器').tap()

        self.verifyPageName('/page/tools/cgjsq/cgjsq')
        self.get_screenshot()

    def test_039_点击海报获客(self):
        """
        V7.17: 点击 海报获客
        """
        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV tile"][data-index="1"]/view', inner_text='海报获客').tap()

        self.verifyPageName('/page/publicPages/hkhb/hkhbindex')
        self.get_screenshot()

    def test_039_点击发帖获客(self):
        """
        V7.17: 点击 发帖获客
        """
        self.delay(5)
        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV tile"][data-index="2"]/view', inner_text='发帖获客').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def test_023_查看课程(self):
        """
        V6.45.X: 转到课程详情页
        """
        self.delay(3)
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

        self.verifyPageName('/page/mine/myinfo/myinfo')
        self.get_screenshot()

    def delete_test_002_点击淘房圈发帖(self):
        """
        点击“淘房圈发帖”，进入写贴子页面
        """
        self.find_element('view[class="name"]', inner_text='淘房圈发帖').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def test_003_点击我的帖子(self):
        """
        点击“我的帖子”，进入我的帖子页面
        """
        self.find_element('view[class="dp myTfq flex tfAlignC tfFlexC tfFlexV"]').tap()

        self.verifyPageName('/page/business/minetiezi')
        self.get_screenshot()

    def test_004_点击我的店铺(self):
        """
        点击”我的店铺“，进入我的店铺页面
        """
        self.find_element('view[class="dp"]').tap()

        self.verifyPageName('/esf/sell/pages/broker/broker')
        self.get_screenshot()

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

        self.verifyPageName('/page/business/quickReply')
        self.get_screenshot()

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

        self.verifyPageName('/page/business/quickReply')
        self.get_screenshot()

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

        self.verifyPageName('/page/business/autoreplyadd')
        self.get_screenshot()

    def test_010_保存自动回复(self):
        """
        点击“IM咨询配置”，点击“自动回复设置”，进入自动回复设置页面，输入内容保存
        """
        self.delay(2)
        self.goto_im_autoreply()
        self.delay(5)

        self.find_element('textarea').input('您好，现在正忙，稍后回复您！')
        self.find_element('button').tap()

        self.verifyPageName('/page/business/setting')
        self.get_screenshot()

    def test_011_点击系统通知(self):
        """
        点击常用功能：系统通知，进入系统通知页
        """
        self.find_element('view[class="name"]', inner_text='系统通知').tap()

        self.verifyPageName('/page/business/zygwmsglist')
        self.get_screenshot()

    def test_012_点击关注服务号(self):
        """
        点击服务指南：关注服务号，进入关注页面
        """
        self.find_element('view[class="name"]', inner_text='关注服务号').tap()

        self.verifyPageName('/page/mine/gzService/gzService')
        self.get_screenshot()

    def test_013_点击意见反馈(self):
        """
        点击服务指南：完成意见反馈
        """
        self.find_element('view[class="name"]', inner_text='意见反馈').tap()

        self.verifyPageName('/page/mine/wtfk/wtfk')
        self.get_screenshot()

    def test_014_点击隐私权政策(self):
        """
        点击服务指南：隐私权政策
        """
        self.find_element('view[class="name"]', inner_text='隐私权政策').tap()

        self.verifyPageName('/page/index/notice')
        self.get_screenshot()

    def test_015_点击素材库(self):
        """
        V6.38.x: 点击 素材库
        """
        self.find_element('swiper[class="store-swiper"]').tap()
        self.delay(1)
        self.verifyPageName('/page/taofangquan/contentstore/contentstore')
        self.get_screenshot()

    def click_jifen(self):
        """
        点击 我的积分
        """
        self.find_element('view[class="my_points"]').tap()
        self.delay(2)

    def test_016_点击我的积分(self):
        """
        V6.38.x: 点击 我的积分，进入积分页面
        """
        self.click_jifen()

        self.verifyPageName('/page/mine/myscores/alltasks')
        self.get_screenshot()

    def test_017_已兑换商品_待使用_赚积分(self):
        """
        V6.38.x: 点击 积分->积分明细->做任务赚积分
        """
        self.click_jifen()
        self.delay(7)
        self.verifyPageName('/page/mine/myscores/alltasks')

        # 点击 jifen
        self.find_element('view[class="t_score"]').tap()
        self.delay(3)
        self.find_element('view[class="toMyscore flex tfAlignC tfFlexC"]').tap()
        self.get_screenshot('点击做任务赚积分')
        self.verifyPageName('/page/mine/myscores/alltasks')

    def test_018_已兑换商品_已使用_赚积分(self):
        """
        V6.38.X: 点击 积分->积分明细->支出->做任务赚积分
        """
        self.click_jifen()

        self.delay(2)

        # 点击 积分
        self.find_element('view[class="t_score"]').tap()
        self.delay(3)

        self.find_element('view[class="pay"]').tap()
        self.delay(2)
        self.find_element('view[class="toMyscore flex tfAlignC tfFlexC"]').tap()
        self.get_screenshot('点击赚积分到我的积分页面')
        self.verifyPageName('/page/mine/myscores/alltasks')

    def test_019_点击任务1(self):
        """
        V6.38.X: 点击 任务 1
        """
        try:
            self.find_element('view[class="toPublish"]').tap()
        except:
            self.find_element('view[class="toPublish unuse"]').tap()
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

        self.verifyPageName('/page/mine/myscores/alltasks')
        self.get_screenshot()

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

        self.verifyPageName('/page/mine/myscores/goodsdetail')

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

        self.verifyPageName('/page/mine/myscores/goodsdetail')
        self.get_screenshot()

    def test_000_001_进入客户列表(self):
        """
        V6.40.x: 点击  全部客户、未跟进、未标记，分别进入列表页
        """
        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV item"][data-type="1"]').tap()
        self.delay(2)

        self.get_screenshot('全部客户列表页')
        self.verifyPageName('/page/business/customerManage/myCustomer/myCustomer')
        self.back()

        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV item"][data-type="2"]').tap()
        self.delay(2)

        self.get_screenshot('未跟进列表页')
        self.verifyPageName('/page/business/customerManage/myCustomer/myCustomer')
        self.back()

        self.find_element('view[class="tfFlex tfFlexC tfAlignC tfFlexV item"][data-type="3"]').tap()
        self.delay(2)

        self.get_screenshot('未标记列表页')
        self.verifyPageName('/page/business/customerManage/myCustomer/myCustomer')
