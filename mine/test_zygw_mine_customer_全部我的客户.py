# -*-coding:utf-8-*-
import time

import minium

from base.test_mine import TestMine


class TestMineAllCustomer(TestMine):
    """
    置业顾问 我的客户 页
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestMineAllCustomer, cls).setUpClass()
        cls().change_zygw()
        print("setupclass change_zygw")

    def setUp(self) -> None:
        self.page_name = '/page/business/zygwinfomanage/customerList?city=qz&optionstype=1'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestMineAllCustomer, self).setUp()

    def search_name(self, name='1122'):
        """
        输入客户姓名，搜索
        """
        self.find_element('input').input(name + '\n')
        self.delay(3)

    def test_01_搜索客户姓名(self):
        """
        V6.27.X: 点击搜索，输入姓名，搜索
        """
        self.search_name('1122')

        self.verifyStr(True, self.element_is_exist('view[class="customerName tfFlex tfAlignC"]', text_contains='1122'), '搜索到客户')
        self.get_screenshot()

    def test_02_切换到未跟进(self):
        """
        V6.27.X: 切换到未跟进TAB
        """
        self.find_element('view[data-idx="1"]', inner_text='未跟进').tap()

        self.get_screenshot()

    def test_03_切换到未接通(self):
        """
        V6.27.X: 切换到未接通
        """
        self.find_element('view[data-idx="2"]', inner_text='未接通').tap()

        self.get_screenshot()

    def test_04_切换到已接通(self):
        """
        V6.27.X: 切换到已接通TAB
        """
        self.find_element('view[data-idx="3"]', inner_text='已接通').tap()

        self.get_screenshot()

    def test_05_切换到未标记(self):
        """
        V6.27.X: 切换到未标记TAB
        """
        self.find_element('view[data-idx="4"]', inner_text='未标记').tap()

        self.get_screenshot()

    def test_06_切换到全部(self):
        """
        V6.27.X: 切换到未跟进TAB
        """
        self.find_element('view[data-idx="4"]', inner_text='未标记').tap()

        self.find_element('view[data-idx="0"]', inner_text='全部').tap()

        self.get_screenshot()

    def click_sort(self, sort_str='老客优先'):
        """
        点击“排序”
        """
        self.find_element('view[class="c-text"]', inner_text='排序').tap()
        self.delay(1)

        self.find_element('view[class="item"][data-value="%s"]'%sort_str).tap()

        self.verifyStr(True, self.element_is_exist('view[class="c-text"]', inner_text=sort_str), '选择%s正确'%sort_str)

    def test_07_排序_老客优先(self):
        """
        V6.27.X: 排序-老客优先
        """
        self.click_sort('老客优先')

        self.get_screenshot()

    def test_08_排序_新客优先(self):
        """
        V6.27.X: 排序-新客优先
        """
        self.click_sort('新客优先')

        self.get_screenshot()

    def test_09_排序_高意向优先(self):
        """
        V6.27.X: 排序_高意向优先
        """
        self.click_sort('高意向优先')

        self.get_screenshot()

    def test_10_排序_近期跟进优先(self):
        """
        V6.27.X: 排序_近期跟进优先
        """
        self.click_sort('近期跟进优先')

        self.get_screenshot()

    def test_11_排序_历史跟进优先(self):
        """
        V6.27.X: 排序_历史跟进优先
        """
        self.click_sort('历史跟进优先')

        self.get_screenshot()

    def test_12_筛选客户并重置(self):
        """
        V6.27.X: 筛选客户
        """
        self.find_element('view[class="c-text"]', inner_text='筛选').tap()

        #     点击筛选项
        self.find_element('view[class="sonMenuCon"]', inner_text='已接通').tap()
        self.find_element('view[class="sonMenuCon"]', inner_text='有效').tap()
        self.find_element('view[class="sonMenuCon"]', inner_text='高').tap()

        self.find_element('view[class="confirm"]').tap()

        self.get_screenshot("筛选（已接通、有效、高）的结果")

        self.find_element('view[class="c-text current"]', inner_text='筛选').tap()
        # 重置筛选项
        self.find_element('view[class="reset"]').tap()
        self.find_element('view[class="confirm"]').tap()

        self.get_screenshot('重置后的筛选结果')

    def test_13_客户列表_查看客户详情(self):
        """
        V6.27.X: 点击客户进入详情
        """
        self.find_element('view[class="customerWrap"]').tap()

        self.verifyPageName('/page/business/zygwinfomanage/customerDetails')
        self.get_screenshot()

    def test_14_客户列表_点击星标(self):
        """
        V6.27.X: 客户列表，点击星标
        """
        self.search_name('1122')
        self.delay(2)

        self.find_element('view[class="customer_sign"]').tap()

        self.get_screenshot("第一条非星标客户，已添加星标")

    def test_15_客户列表_取消星标(self):
        """
        V6.27.X: 客户列表，取消星标
        """
        self.search_name('1122')

        self.find_element('view[class="customer_sign active"]').tap()

        self.get_screenshot('第一条星标客户，取消星标')

    def test_98_客户列表_拨打电话(self):
        """
        V6.27.X: 客户列表，点击电话
        """
        self.find_element('image[class="btnIcon"]').tap()

        self.get_screenshot()

    def test_16_搜客户写跟进(self):
        """
        置业顾问个人中心，我的客户页面，搜索后的第一个结果写跟进记录
        """
        # 搜索客户
        self.search_name('1122')
        # 点击第一个搜索结果
        try:
            self.page.get_element('image[src="http://tfxcx.house365.com/static/tfxcx_img/cust_gj.png"]').tap()
        except minium.MiniElementNotFoundError:
            print('没有搜索到客户数据，用例通过')
            self.get_screenshot('没有搜索到“1122”客户')
            return

        try:
            self.delay(2)
            self.add_comment(bz=time.strftime('%Y-%m-%d %H:%M:%S'))
        except minium.MiniElementNotFoundError as e:
            self.get_screenshot()
            raise e

        self.get_screenshot()

    def add_comment(self, yx='高', jd='到访', zt='有效', bz='test'):
        """
        添加跟进记录页面
        """
        self.delay(2)
        if zt:
            self.page.get_element('view[data-tagindex="0"]', inner_text=zt).tap()

        if yx:
            self.page.get_element('view[data-tagindex="0"]', inner_text=yx).tap()
        if jd:
            lxele = self.page.get_element('view[data-index="2"]', inner_text=jd)
            a = lxele.attribute('class')
            if 'active' not in a[0]:
                lxele.tap()
        if bz:
            self.page.get_element('textarea').input(bz)

        tap = 'self.page.get_element(\'button\').tap()'
        self.getShowToast(tap)

    def test_17_客户列表_回拨记录(self):
        """
        V6.27.X: 客户列表，点击’回拨记录‘
        """
        self.find_element('/page/movable-area/movable-view/view').tap()

        self.verifyPageName('/page/business/zygwinfomanage/callback')
        self.get_screenshot()

    def test_18_客户详情_点击星标(self):
        """
        V6.27.X: 客户详情，点击星标
        """
        self.search_name('1122')
        try:
            self.find_element('view[class="customerWrap"]').tap()
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有搜索到用户')
            return

        self.delay(2)
        try:
            self.find_element('view[class="customer_sign"]').tap()
        except minium.MiniElementNotFoundError:
            self.get_screenshot('已经是星标用户')
            return

        self.get_screenshot()

    def test_19_客户详情_取消星标(self):
        """
        V6.27.X: 客户详情，取消星标
        """
        self.search_name('1122')

        try:
            self.find_element('view[class="customerWrap"]').tap()
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有搜索到用户')
            return

        self.delay(2)
        try:
            self.find_element('view[class="customer_sign active"]').tap()
        except minium.MiniElementNotFoundError:
            self.get_screenshot('已经取消星标')
            return

        self.get_screenshot()

    def test_20_客户详情_编辑客户(self):
        """
        V6.27.X: 客户详情，编辑客户
        """
        self.search_name('1122')

        try:
            self.find_element('view[class="customerWrap"]').tap()
            self.delay(2)
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有搜索到用户')
            return

        self.find_element('image[class="edit_img"]').tap()
        self.delay(2)
        self.verifyPageName('/page/business/zygwinfomanage/editCustomer')
        self.get_screenshot('编辑页面')

        self.find_element('button[class="submitBtn"]').tap()
        self.verifyPageName('/page/business/zygwinfomanage/customerDetails')
        self.get_screenshot()

    def test_99_客户详情_拨打电话(self):
        """
        V6.27.X: 客户详情，拨打电话
        """
        self.search_name('1122')

        try:
            self.find_element('view[class="customerWrap"]').tap()
            self.delay(2)
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有搜索到用户')
            return

        self.find_element('image[class="btnIcon"]').tap()
        self.get_screenshot()

    def test_21_客户详情_IM咨询(self):
        """
        V6.27.X: 客户详情，IM咨询
        """
        self.search_name('5160')

        try:
            self.find_element('view[class="customerWrap"]').tap()
            self.delay(2)
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有搜索到用户')
            return

        try:
            self.find_element('text', inner_text='发消息').tap()
        except minium.MiniElementNotFoundError:
            self.get_screenshot('no-im')
        self.get_screenshot()

    def test_25_客户详情_会话记录进聊天(self):
        """
        V6.42.X: 客户详情，会话记录进聊天
        """
        self.search_name('3806')

        try:
            self.find_element('view[class="customerWrap"]').tap()
            self.delay(3)
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有搜索到用户')
            return

        try:
            self.delay(2)
            self.find_element('view[class="history_chat"]').tap()
        except minium.MiniElementNotFoundError:
            self.get_screenshot('no-im')
        self.get_screenshot()
        self.verifyPageName('/im_pages/historyFromCloud/historyFromCloud')
    def test_24_客户详情_会话记录无响应(self):
        """
        V6.42.X: 客户详情，会话记录无响应
        """
        self.search_name('1122')

        try:
            self.find_element('view[class="customerWrap"]').tap()
            self.delay(2)
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有搜索到用户')
            return

        try:
            self.find_element('view[class="history_chat"]').tap()
        except minium.MiniElementNotFoundError:
            self.get_screenshot('no-im')
        self.get_screenshot()

    def test_22_客户详情_写跟进(self):
        """
        V6.27.X: 客户详情，写跟进
        """
        self.search_name('1122')

        try:
            self.find_element('view[class="customerWrap"]').tap()
            self.delay(4)
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有搜索到用户')
            return

        self.find_element('text', inner_text='写跟进').tap()
        self.verifyPageName('/page/business/zygwinfomanage/followAdd')
        self.get_screenshot('写跟进页面')

        self.add_comment(bz=time.strftime('%Y-%m-%d %H:%M:%S'))

        self.verifyPageName('/page/business/zygwinfomanage/customerDetails')
        self.get_screenshot()

    def test_23_客户详情_TAB切换(self):
        """
        V6.27.X: 客户详情，TAB切换
        """
        self.search_name('1122')

        try:
            self.find_element('view[class="customerWrap"]').tap()
            self.delay(2)
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有搜索到用户')
            return

        self.find_element('text', inner_text='跟进反馈记录').tap()
        self.get_screenshot('切换到“跟进反馈记录”')

        self.find_element('text', inner_text='客户资料').tap()
        self.get_screenshot('切换到“客户资料”')

        self.find_element('text', inner_text='客户画像').tap()
        self.get_screenshot('切换到“客户画像”')

    def del_test_24_客户详情_查看历史跟进(self):
        """
        V6.42.x: delete
        V6.27.X: 客户详情，历史楼盘查看
        """
        self.search_name('1122')

        try:
            self.find_element('view[class="customerWrap"]').tap()
            self.delay(2)
        except minium.MiniElementNotFoundError:
            self.get_screenshot('没有搜索到用户')
            return

        self.find_element('view[class="look_detail"]').tap()
        self.get_screenshot()