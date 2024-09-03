import time

import pytest
from ddt import data, ddt

from base.test_mine import TestMine

@ddt
class TestJJRCustomer(TestMine):
    """
    经纪人身份，我的客户页面
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestJJRCustomer, cls).setUpClass()
        cls().change_jjr()
        print("setupclass TestJJRCustomer")

    def setUp(self) -> None:
        self.page_name = '/page/business/customerManage/myCustomer/myCustomer?tab=1'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestJJRCustomer, self).setUp()

    @data('13182855160', '客户_5160', '测试')
    def test_list_001_搜索(self, kw):
        """
        V6.40.x: 输入手机号搜索
        """
        self.find_element('input[class="flex_1"]').input(kw)

        self.get_screenshot()

    @data('IM咨询', '高', '未跟进', '有效')
    def test_list_002_筛选后重置(self, filter):
        """
        V6.40.X: 选择筛选项 筛选
        """
        self.find_element('view[class="flex a_c filter"]/view', inner_text='筛选').tap()

        self.find_element('view[class="customerFilter--filter-item"]', inner_text=filter).tap()

        self.find_element('view[class="customerFilter--confirm"]').tap()

        self.get_screenshot(filter)

        # 下面进行选项重置
        self.find_element('view[class="flex a_c filter selected"]/view', inner_text='筛选').tap()
        self.find_element('view[class="customerFilter--reset"]').tap()
        self.find_element('view[class="customerFilter--confirm"]').tap()
        self.get_screenshot('取消选项'+filter)

    def test_list_003_排序后重置(self):
        """
        V6.40.x: 排序
        """
        self.find_element('view[class="flex a_c filter"]/view', inner_text='排序').tap()
        self.find_element('view[class="customerOrder--flex customerOrder--a_c customerOrder--between customerOrder--order-item"][data-order="2"]').tap()
        self.find_element('view[class="customerOrder--confirm"]').tap()
        self.get_screenshot("上客时间由远到近")

        self.find_element('view[class="flex a_c filter selected"]/view', inner_text='排序').tap()
        self.find_element(
            'view[class="customerOrder--flex customerOrder--a_c customerOrder--between customerOrder--order-item"][data-order="1"]').tap()
        self.find_element('view[class="customerOrder--confirm"]').tap()
        self.get_screenshot("上客时间由近到远")

        self.find_element('view[class="flex a_c filter"]/view', inner_text='排序').tap()
        self.find_element(
            'view[class="customerOrder--flex customerOrder--a_c customerOrder--between customerOrder--order-item"][data-order="3"]').tap()
        self.find_element('view[class="customerOrder--confirm"]').tap()
        self.get_screenshot("跟进时间由近到远")

        self.find_element('view[class="flex a_c filter selected"]/view', inner_text='排序').tap()
        self.find_element(
            'view[class="customerOrder--flex customerOrder--a_c customerOrder--between customerOrder--order-item"][data-order="4"]').tap()
        self.find_element('view[class="customerOrder--confirm"]').tap()
        self.get_screenshot("跟进时间由远到近")

        self.find_element('view[class="flex a_c filter selected"]/view', inner_text='排序').tap()
        self.find_element('view[class="customerOrder--reset"]').tap()
        self.find_element('view[class="customerOrder--confirm"]').tap()
        self.get_screenshot("重置为默认")

    def test_list_004_切换TAB(self):
        """
        v6.40.X: 切换 全部 未跟进 未标记tab
        """
        self.find_element('view[class="flex column center tab"][data-tab="2"]').tap()
        self.get_screenshot('切换到未跟进')

        self.find_element('view[class="flex column center tab"][data-tab="3"]').tap()
        self.get_screenshot('切换到未标记')

        self.find_element('view[class="flex column center tab"][data-tab="1"]').tap()
        self.get_screenshot('切换到全部')

    def test_list_005_客户操作(self):
        """
        V6.40.X: 点击 5160客户，打电话  发消息 写跟进
        """
        self.find_element('input[class="flex_1"]').input('测试')

        self.find_element('view[class="customerItem--flex customerItem--a_c customerItem--action"][data-index="1"]').tap()
        self.delay(3)
        self.get_screenshot('给客户-发消息')
        self.back()

        self.find_element(
            'view[class="customerItem--flex customerItem--a_c customerItem--action"][data-index="0"]').tap()
        self.get_screenshot('给客户-打电话')

        self.find_element(
            'view[class="customerItem--flex customerItem--a_c customerItem--action"][data-index="2"]').tap()
        self.get_screenshot('给客户-写跟进')

    def test_detail_001_客户操作(self):
        """
        v6.40.X: 客户详情页的 发消息 打电话 写跟进
        """
        self.find_element('input[class="flex_1"]').input('测试')
        self.delay(2)
        self.find_element('view[class="customerItem--item"]').tap()
        self.delay(2)
        self.get_screenshot('查看客户详情')

        # 切换客户跟进
        self.find_element('view[class="flex column a_c category"]').tap()

        self.find_element('view[class="check-all"][data-type="followUp"]').tap()
        self.delay(2)
        self.get_screenshot('客户详情-查看全部跟进记录')
        self.back()

        try:
            self.find_element('view[class="check-all"][data-type="call"]').tap()
            self.delay(2)
            self.get_screenshot('客户详情-查看全部跟进记录')
            self.back()
        except:
            self.get_screenshot('客户详情-无更多通话记录')

        self.find_element(
            'view[class="flex a_c action"][data-index="1"]').tap()
        self.delay(3)
        self.get_screenshot('客户详情-发消息')
        self.back()

        self.find_element(
            'view[class="flex a_c action"][data-index="0"]').tap()
        self.get_screenshot('客户详情-打电话')

        self.find_element('image[class="eye"]').tap()
        self.get_screenshot('客户详情-手机号')

        self.find_element('view[class="flex j_c a_c record"]').tap()
        self.delay(3)
        self.get_screenshot('客户详情-回话记录')
        self.back()

        self.find_element(
            'view[class="flex a_c action"][data-index="2"]').tap()
        self.get_screenshot('客户详情-写跟进')
        self.back()

        self.find_element('image[class="edit"]').tap()
        self.get_screenshot('客户详情-编辑')

    def test_gj_001_写跟进(self):
        """
        V6.40.X: 编辑写跟进 并保存
        """
        url = '/page/business/customerManage/followUp/followUp?id=13679'
        self.redirect_to_page(url=url)
        self.delay(2)
        date = time.strftime('%Y-%m-%d')

        # 跟进阶段
        self.find_element('view[class="filter-item"][data-type="stage"]').tap()
        # 客户意向
        self.find_element('view[class="filter-item"][data-type="intent"]').tap()

        # 备注
        self.find_element('textarea[class="pr remark"]').input(date)

        tap = 'self.find_element(\'view[class="pf save"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '保存成功')
        self.get_screenshot()

    def test_edit_001_编辑(self):
        """
        V6.40.X: 编辑客户信息
        """
        url = '/page/business/customerManage/customerEdit/customerEdit?id=13679'
        self.redirect_to_page(url=url)
        self.delay(2)

        # 选择性别
        self.find_element('view[class="flex a_c sex"]').tap()

        # 输入价格
        self.find_element('input[class="input"][data-type="minPrice"]').input('100')
        self.find_element('input[class="input"][data-type="maxPrice"]').input('500')

        # 输入面积
        self.find_element('input[class="input"][data-type="minArea"]').input('100')
        self.find_element('input[class="input"][data-type="maxArea"]').input('600')

        # 选择 户型
        self.find_element('view[class="tag"][data-type="room"]').tap()

        # 选择装修
        self.find_element('view[class="tag"][data-type="fitment"]').tap()

        # 选择楼层
        self.find_element('view[class="tag"][data-type="floor"]').tap()

        # 选择置业目的
        self.find_element('view[class="tag"][data-type="userTag"]').tap()

        # 选择购房周期
        self.find_element('view[class="tag"][data-type="period"]').tap()

        # 保存
        tap = 'self.find_element(\'view[class="save"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '保存成功')
        self.get_screenshot()

    def test_edit_002_添加删除板块(self):
        """
        v6.40.x: 添加 板块后删除
        """
        url = '/page/business/customerManage/customerEdit/customerEdit?id=13679'
        self.redirect_to_page(url=url)
        self.delay(2)

        # 添加板块
        self.find_element('view[class="tag add"]').tap()
        self.delay(3)
        self.get_screenshot('进入选择板块页面')

        # 选择板块
        self.find_element('view[class="item"]', inner_text='建邺区').tap()
        self.find_element('view[class="flex between a_c item"][data-index="1"]').tap()
        self.get_screenshot('选择建邺区')

        # 重置
        self.find_element('view[class="flex_1 btn"]', inner_text='重置').tap()
        self.get_screenshot('重置')

        # 重新选择板块
        self.find_element('view[class="item"]', inner_text='鼓楼区').tap()
        self.find_element('view[class="flex between a_c item"][data-index="1"]').tap()
        self.find_element('view[class="flex between a_c item"][data-index="2"]').tap()
        self.find_element('view[class="flex between a_c item"][data-index="3"]').tap()
        self.find_element('view[class="flex between a_c item"][data-index="4"]').tap()
        self.find_element('view[class="flex between a_c item"][data-index="5"]').tap()

        self.find_element('view[class="flex_1 btn"]', inner_text='确认').tap()

        self.delay(2)
        self.page.scroll_to(1000, 200)
        self.get_screenshot('选择的板块')

        self.find_element('view[class="pr del"]').tap()
        self.get_screenshot('删除已选择的板块')