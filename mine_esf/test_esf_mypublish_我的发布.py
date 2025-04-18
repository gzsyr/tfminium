import minium
from ddt import ddt, data, unpack

from base.test_base import TestBase


@ddt
class TestEsfMypublish(TestBase):
    """
    我的发布
    """

    def setUp(self) -> None:
        self.page_name = '/esf/village/myPublish/myPublish?city=nj'
        self.classname = self.__class__.__name__
        self.switch = False
        super(TestEsfMypublish, self).setUp()
        self.delay(6)

    @data(('出售', 1), ('出租', 2), ('求购', 3), ('求租', 4))
    @unpack
    def test_01_click_切换TAB(self, name, num):
        """
        我的发布，切换tab
        """
        self.page.get_element('view[data-index="%d"]' % (num-1), inner_text=name).tap()
        self.delay(2)
        self.get_screenshot()

    # 出售
    def test_02_click_esf_点击出售列表进入详情页(self):
        """
        点击出售列表-进入详情页
        :return:
        """
        self.find_element('view[data-index="0"]', inner_text='出售').tap()
        self.delay(1)
        try:
            self.find_element('view[class="myPublishSellItem--flex_1 myPublishSellItem--w0"]').tap()
            self.delay(3)
        except minium.MiniElementNotFoundError:
            self.find_element('view[class="publish"]').tap()
        self.get_screenshot()

    def test_03_click_esf_点击出售列表修改(self):
        """
        点击出售列表-修改（显示中）
        :return:
        """
        self.page.get_element('view[data-index="0"]', inner_text='出售').tap()
        self.delay(1)
        try:
            e = self.page.get_element('view[class="myPublishSellItem--pr"]/view', inner_text='修改')
            e.tap()
            self.delay(1)
            # 修改价格
            self.page.scroll_to(800, 500)
            self.delay(1)
            self.page.get_element('input[id="price"]').input('150')
            self.delay(2)
            self.page.get_element('view[class="next"]', inner_text='下一步').tap()
            self.delay(2)
            self.page.get_element('view[class="unchecked"]').tap()
            self.delay(2)
            self.page.get_element('view[class="confirm"]', inner_text='确认发布').tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有显示中的房源')

    def test_04_click_esf_点击出售列表下架(self, sxiajia=[1]):
        """
        点击出售列表-下架（显示中）
        :return:
        """
        self.page.get_element('view[data-index="0"]', inner_text='出售').tap()
        self.delay(1)
        try:
            e = self.page.get_element('view[class="myPublishSellItem--pr"]/view', inner_text='下架')
            e.tap()
            self.delay(1)
            # 下架
            e = self.page.get_element('picker-view')
            e.trigger("change", {"value": sxiajia})
            self.delay(3)
            self.page.get_element('view[class="class="confirm"]', inner_text='确定').tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有显示中的房源')

    def test_05_click_esf_点击出售列表重新发布(self):
        """
        点击出售列表-重新发布（个人下架）
        :return:
        """
        self.page.get_element('view[data-index="0"]', inner_text='出售').tap()
        self.delay(1)
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            e = self.page.get_element('view[class="myPublishSellItem--pr"]/view', inner_text='重新发布')
            e.tap()
            self.app.restore_wx_method("showModal")
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有个人下架的房源')

    def test_06_click_esf_点击出售列表个人下架删除(self):
        """
        点击出售列表-删除（个人下架）
        :return:
        """
        self.page.get_element('view[data-index="0"]', inner_text='出售').tap()
        self.delay(1)
        # grxj = self.page.element_is_exists('view[class="center button"]', inner_text='重新发布')
        # if grxj == True:
        try:
            self.page.scroll_to(1000, 500)
            self.delay(1)
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            e = self.page.get_element('view[class="myPublishSellItem--pr"]/view', inner_text='删除')
            e.tap()
            self.app.restore_wx_method("showModal")
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有个人下架的房源')

    def test_07_click_esf_点击出售列表悬浮发布(self):
        """
        点击出售列表-悬浮发布按钮
        :return:
        """
        self.page.get_element('view[data-index="0"]', inner_text='出售').tap()
        self.delay(1)
        self.page.get_element('view[class="pf center column publishType"]').tap()
        self.delay(3)
        self.get_screenshot()

    # 出租
    def test_08_click_rent_点击出租列表进入详情(self):
        """
        点击出租列表-进入详情
        :return:
        """
        self.find_element('view[data-index="1"]', inner_text='出租').tap()
        self.delay(1)
        self.find_element('view[class="myPublishRentItem--flex_1 myPublishRentItem--w0"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_09_click_rent_点击出租列表修改(self):
        """
        点击出租列表-修改（显示中）
        :return:
        """
        self.page.get_element('view[data-index="1"]', inner_text='出租').tap()
        self.delay(1)
        try:
            e = self.page.get_element('view[class="myPublishRentItem--pr"]/view', inner_text='修改')
            e.tap()
            self.delay(1)
            # 修改价格
            self.page.scroll_to(800, 500)
            self.delay(1)
            self.page.get_element('view[class="between infoItem"][data-picker="7"]').tap()
            self.delay(2)
            # self.page.get_element('//priceareapicker/view/view[2]/view/input').input('8000')
            # self.page.get_element('input[id="ipt"]').input('8000')
            self.delay(2)
            self.page.get_element('//priceareapicker/view/view/view/view[2]').tap()
            self.delay(2)
            self.page.get_element('//resetConfirm/view/view/view[2]').tap()
            self.delay(2)
            self.page.get_element('view[class="check"]').tap()
            self.delay(2)
            self.page.get_element('view[flex_1 center confirm]', inner_text='确认发布').tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有显示中的房源')

    def test_10_click_rent_点击出租列表下架(self, zxiajia=[1]):
        """
        点击出租列表-下架（显示中）
        :return:
        """
        self.page.get_element('view[data-index="1"]', inner_text='出租').tap()
        self.delay(1)
        try:
            e = self.page.get_element('view[class="myPublishRentItem--pr"]/view', inner_text='下架')
            e.tap()
            self.delay(1)
            # 下架
            e = self.page.get_element('picker-view')
            e.trigger("change", {"value": zxiajia})
            self.delay(3)
            self.page.get_element('view[class="class="confirm"]', inner_text='确定').tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有显示中的房源')

    def test_11_click_rent_点击出租列表重新发布(self):
        """
        点击出租列表-重新发布（个人下架）
        :return:
        """
        self.page.get_element('view[data-index="1"]', inner_text='出租').tap()
        self.delay(1)
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            e = self.page.get_element('view[class="myPublishRentItem--pr"]/view', inner_text='重新发布')
            e.tap()
            self.app.restore_wx_method("showModal")
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有个人下架的房源')

    def test_12_click_rent_点击出租列表个人下架删除(self):
        """
        点击出租列表-删除（个人下架）
        :return:
        """
        self.page.get_element('view[data-index="1"]', inner_text='出租').tap()
        self.delay(1)
        try:
            self.page.scroll_to(1000, 500)
            self.delay(1)
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            e = self.page.get_element('view[class="myPublishRentItem--pr"]/view', inner_text='删除')
            e.tap()
            self.app.restore_wx_method("showModal")
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有个人下架的房源')

    def test_13_click_rent_点击出租列表悬浮发布(self):
        """
        点击出租列表-悬浮发布按钮
        :return:
        """
        self.page.get_element('view[data-index="1"]', inner_text='出租').tap()
        self.delay(1)
        self.page.get_element('view[class="pf center column publishType"]').tap()
        self.delay(3)
        self.get_screenshot()

    # 求购
    def test_14_click_esf_点击求购列表删除(self):
        """
        点击求购列表-点击删除（审核通过）
        :return:
        """
        self.page.get_element('view[data-index="2"]', inner_text='求购').tap()
        self.delay(1)
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[class="center del"]').tap()
            self.app.restore_wx_method("showModal")
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有审核通过的房源')

    def test_15_click_esf_点击求购列表悬浮发布(self):
        """
        点击求购列表-悬浮发布按钮
        :return:
        """
        self.page.get_element('view[data-index="2"]', inner_text='求购').tap()
        self.delay(1)
        self.page.get_element('view[class="pf center column publishType"]').tap()
        self.delay(3)
        self.get_screenshot()

    # 求租
    def test_16_click_rent_点击求租列表删除(self):
        """
        点击求租列表-点击删除（无需审核）
        :return:
        """
        self.page.get_element('view[data-index="3"]', inner_text='求租').tap()
        self.delay(1)
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[class="center del"]').tap()
            self.app.restore_wx_method("showModal")
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有房源')

    def test_17_click_rent_点击求租列表悬浮发布(self):
        """
        点击求购列表-悬浮发布按钮
        :return:
        """
        self.page.get_element('view[data-index="3"]', inner_text='求租').tap()
        self.delay(1)
        self.page.get_element('view[class="pf center column publishType"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_18_click_esf_点击出售列表查看原因(self):
        """
        点击出售列表-点击查看原因（审核不通过）
        :return:
        """
        self.page.get_element('view[data-index="0"]', inner_text='出售').tap()
        self.delay(1)
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            e = self.page.get_element('view[class="myPublishSellItem--pr"]/view', inner_text='查看原因')
            e.tap()
            self.app.restore_wx_method("showModal")
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有审核不通过的房源')
