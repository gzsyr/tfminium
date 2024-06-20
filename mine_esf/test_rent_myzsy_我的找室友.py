from ddt import ddt, data, unpack

from base.test_base import TestBase


@ddt
class TestrentMyzsy(TestBase):
    """
    我的找室友
    """
    def setUp(self) -> None:
        self.page_name = '/esf/village/myRoommate/myRoommate?city=nj'
        self.classname = self.__class__.__name__
        self.switch = False
        super(TestrentMyzsy, self).setUp()

    @data(('我的发布', 1), ('我的收藏', 2), ('我的浏览', 3))
    @unpack
    def test_01_click_找室友切换TAB(self, name, num):
        """
        我的找室友，切换tab
        """
        self.page.get_element('view[data-id="%d"]' % num, inner_text=name).tap()
        self.delay(2)
        self.get_screenshot()

    def test_02_click_shangxiao_我的发布失效点击上架(self):
        """
        我的发布，状态为失效，点击上架
        :return:
        """
        self.page.get_element('view[data-id="1"]', inner_text='我的发布').tap()
        self.delay(2)
        # 上架
        try:
            self.page.get_element('view[class="center operation"]', inner_text='上架').tap()
            self.delay(1)
            self.get_screenshot()
        except:
            print('没有失效房源')

    def test_03_click_xq_我的发布显示中点击进入详情(self):
        """
        我的发布，状态为显示中，点击进入房源详情页
        :return:
        """
        self.page.get_element('view[data-id="1"]', inner_text='我的发布').tap()
        self.delay(2)
        # 进入房源详情页
        try:
            self.page.get_element('view[class="houseInfo"][data-status="1"]').tap()
            self.delay(1)
            self.get_screenshot()
        except:
            print('没有显示中的房源')

    def test_04_click_xiajia_我的发布显示中点击下架(self):
        """
        我的发布，状态为显示中，点击下架
        :return:
        """
        self.page.get_element('view[data-id="1"]', inner_text='我的发布').tap()
        self.delay(2)
        # 下架
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[class="center operation"]', inner_text='下架').tap()
            self.app.restore_wx_method("showModal")
            self.delay(1)
            self.get_screenshot()
        except:
            print('没有显示中的房源')

    def test_05_click_xiugai_我的发布显示中点击修改(self):
        """
        我的发布，状态为显示中，点击修改
        :return:
        """
        self.page.get_element('view[data-id="1"]', inner_text='我的发布').tap()
        self.delay(2)
        # 修改
        try:
            self.page.get_element('view[class="center operation"]', inner_text='修改').tap()
            self.delay(1)
            self.page.get_element('view[class="center option"]', inner_text='有阳台').tap()
            self.delay(1)
            self.page.get_element('//resetConfirm/view/view/view[2]').tap()
            self.delay(1)
            self.get_screenshot()
        except:
            print('没有显示中的房源')

    def test_06_click_yy_我的发布审核不通过点击原因(self):
        """
        我的发布，状态为审核不通过，点击查看原因
        :return:
        """
        self.page.get_element('view[data-id="1"]', inner_text='我的发布').tap()
        self.delay(2)
        # 查看原因
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[class="center operation"]', inner_text='查看原因').tap()
            self.app.restore_wx_method("showModal")
            self.delay(1)
            self.get_screenshot()
        except:
            print('没有审核不通过的房源')

    def test_07_click_tel_我的发布审核中点击电话(self):
        """
        我的发布，状态为审核中，点击电话咨询
        :return:
        """
        self.page.get_element('view[data-id="1"]', inner_text='我的发布').tap()
        self.delay(2)
        # 点击电话
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[class="center operation"]', inner_text='电话咨询').tap()
            self.app.restore_wx_method("showModal")
            self.delay(2)
            self.get_screenshot()
        except:
            print('没有审核中的房源')

    def test_08_click_del_我的发布列表点删除(self):
        """
        我的发布列表，点击删除
        :return:
        """
        self.page.get_element('view[data-id="1"]', inner_text='我的发布').tap()
        self.delay(2)
        # 点击删除
        dels = self.find_elements('view[class="item"]')
        self.delay(1)
        if len(dels) > 0:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.delay(1)
            self.find_element('view[class="center operation"]', inner_text='删除').tap()
            self.app.restore_wx_method("showModal")
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有房源')

    # 我的收藏
    def test_09_click_sc_我的收藏列表进详情(self):
        """
        我的收藏列表，点击进入详情页
        :return:
        """
        self.page.get_element('view[data-id="2"]', inner_text='我的收藏').tap()
        self.delay(2)
        # 点击进入详情页
        sc = self.page.get_elements('view[class="flex_1 line_1"]')
        if len(sc) > 0:
            sc[0].tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有房源')

    def test_10_click_scdel_我的收藏删除(self):
        """
        我的收藏列表，点击删除
        :return:
        """
        self.page.get_element('view[data-id="2"]', inner_text='我的收藏').tap()
        self.delay(2)
        # 点击删除
        sc = self.page.get_elements('view[class="flex_1 line_1"]')
        self.delay(1)
        if len(sc) > 0:
            e = self.page.get_elements('//slidedelete/view/view/view/text')
            e[0].tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有房源')

    def test_11_click_clear_一键清除失效房源(self):
        """
        我的收藏列表，点击一键清除失效房源
        :return:
        """
        self.page.get_element('view[data-id="2"]', inner_text='我的收藏').tap()
        self.delay(2)
        # 点击一键清除失效房源
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.delay(1)
            e = self.page.get_element('view[class="center clearAllInvalidBtn"]')
            e.tap()
            self.app.restore_wx_method("showModal")
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有房源')

    # 我的浏览
    def test_12_click_ll_我的浏览列表进详情(self):
        """
        我的浏览列表，点击进入详情页
        :return:
        """
        self.page.get_element('view[data-id="3"]', inner_text='我的浏览').tap()
        self.delay(2)
        # 点击进入详情页
        sc = self.page.get_elements('view[class="flex_1 line_1"]')
        if len(sc) > 0:
            sc[0].tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有房源')

    def test_13_click_lldel_我的浏览删除(self):
        """
        我的浏览列表，点击删除
        :return:
        """
        self.page.get_element('view[data-id="3"]', inner_text='我的浏览').tap()
        self.delay(2)
        # 点击删除
        sc = self.page.get_elements('view[class="flex_1 line_1"]')
        self.delay(1)
        if len(sc) > 0:
            e = self.page.get_elements('//slidedelete/view/view/view/text')
            e[0].tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有房源')

    def test_14_click_clear_一键清除失效房源(self):
        """
        我的浏览列表，点击一键清除失效房源
        :return:
        """
        self.page.get_element('view[data-id="3"]', inner_text='我的浏览').tap()
        self.delay(2)
        # 点击一键清除失效房源
        try:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.delay(1)
            e = self.page.get_element('view[class="center clearAllInvalidBtn"]')
            e.tap()
            self.app.restore_wx_method("showModal")
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有房源')
