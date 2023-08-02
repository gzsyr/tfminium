from base.test_base import TestBase


class TestMap(TestBase):
    """
    地图找房页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/publicPages/dtzf/dtzf?city=nj&zf_type=sell"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestMap, self).setUp()

    def test_esf_filter_筛选(self):
        """
        V6.40.X: 选择“位置”、“价格”、“户型”、“来源”、“类型”、“面积”、“装修”、“房龄、“楼层”、“朝向”、“税费”、“全景看房、“产权”，筛选
        """
        # 选择“位置”
        self.find_element('view[class="filter--center"][data-id="location"]').tap()
        self.find_element('view[class="screen--between screen--l_item"][data-id="1"]').tap()
        self.find_element('view[class="screen--flex_1 screen--center screen--confirm"]').tap()
        self.get_screenshot('选择“位置”')

        # 选择“价格”
        self.find_element('view[class="filter--center"][data-id="price"]').tap()
        self.find_element('view[class="screen--line_1 screen--item"][data-id="8"]').tap()
        self.find_element('view[class="screen--flex_1 screen--center screen--confirm"]').tap()
        self.get_screenshot('选择“价格”')

        # 选择“户型”
        self.find_element('view[class="filter--center"][data-id="room"]').tap()
        self.find_element('view[class="screen--line_1 screen--item"][data-id="3"]').tap()
        self.find_element('view[class="screen--flex_1 screen--center screen--confirm"]').tap()
        self.get_screenshot('选择“户型”')

        # 选择“gengduo”
        self.find_element('view[class="filter--center"][data-id="more"]').tap()
        self.find_element('view[class="screen--line_1 screen--item"][data-id="3"]').tap()
        self.find_element('view[class="screen--line_1 screen--item"][data-id="1"]/text', inner_text='住宅').tap()
        self.find_element('view[class="screen--line_1 screen--item"][data-id="2"]/text', inner_text='50-80㎡').tap()
        self.find_element('view[class="screen--flex_1 screen--center screen--confirm"]').tap()
        self.get_screenshot()

    def test_esf_点击搜索并返回(self):
        """
        V6.40.X: 点击搜索
        """
        self.find_element('view[class="center column btn"]').tap()
        self.delay(5)
        self.get_screenshot('search')
        self.verifyPageName('/page/publicPages/search/search')

        self.back()
        self.get_screenshot()

    def test_esf_清空筛选(self):
        """
        V6.40.X: 选择“位置”筛选，点击“清空”
        """
        # 选择“位置”
        self.find_element('view[class="filter--center"][data-id="location"]').tap()
        self.find_element('view[class="screen--between screen--l_item"][data-id="1"]').tap()
        self.find_element('view[class="screen--flex_1 screen--center screen--confirm"]').tap()
        self.get_screenshot('选择“位置”')

        # 点击“清空”
        self.find_element('view[class="filter--center filter--filterActive"]').tap()
        self.find_element('view[class="screen--center screen--clear"]').tap()
        self.get_screenshot()

    def test_tab切换(self):
        """
        V6.40.X: tab切换
        """
        self.find_element('view[class="pr center zf_type"]/text', inner_text='新房').tap()
        self.delay(15)
        self.get_screenshot('XF')

        self.find_element('view[class="flex tfFlexC tfAlignC zf_type"]/text', inner_text='二手房').tap()
        self.delay(5)
        self.get_screenshot('esf')

    def tabtorent(self):
        """
        V6.40.X: 切换到租房
        """
        self.find_element('view[class="pr center zf_type"]/text', inner_text='租房').tap()
        self.get_screenshot('rent')
        self.delay(2)

    def test_rent_filter_筛选(self):
        """
        V6.40.X: 选择“位置”、“租金”、“户型”、“出租方式”、“来源”、“物业类型”、“装修”、“房源特色”，筛选
        """
        self.tabtorent()

        # 选择“位置”
        self.find_element('view[class="filter--center"][data-id="location"]').tap()
        self.find_element('view[class="screen--between screen--l_item"][data-id="1"]').tap()
        self.find_element('view[class="screen--flex_1 screen--center screen--confirm"]').tap()
        self.get_screenshot('选择“位置”')

        # 选择“价格”
        self.find_element('view[class="filter--center"][data-id="price"]').tap()
        self.find_element('view[class="screen--line_1 screen--item"][data-id="2"]').tap()
        self.find_element('view[class="screen--flex_1 screen--center screen--confirm"]').tap()
        self.get_screenshot('选择“价格”')

        # 选择“户型”
        self.find_element('view[class="filter--center"][data-id="room"]').tap()
        self.find_element('view[class="screen--line_1 screen--item"][data-id="3"]').tap()
        self.find_element('view[class="screen--flex_1 screen--center screen--confirm"]').tap()
        self.get_screenshot('选择“户型”')

        # 选择“gengduo”
        self.find_element('view[class="filter--center"][data-id="more"]').tap()
        self.find_element('view[class="screen--line_1 screen--item"][data-id="3"]').tap()
        self.find_element('view[class="screen--line_1 screen--item"][data-id="1"]/text', inner_text='住宅').tap()
        self.find_element('view[class="screen--line_1 screen--item"][data-id="1"]/text', inner_text='整租').tap()
        self.find_element('view[class="screen--flex_1 screen--center screen--confirm"]').tap()
        self.get_screenshot()

    def test_rent_清空筛选(self):
        """
        V6.40.X:
        """
        self.tabtorent()

        # 选择“位置”
        self.find_element('view[class="filter--center"][data-id="location"]').tap()
        self.find_element('view[class="screen--between screen--l_item"][data-id="1"]').tap()
        self.find_element('view[class="screen--flex_1 screen--center screen--confirm"]').tap()
        self.get_screenshot('选择“位置”')

        # 点击“清空”
        self.find_element('view[class="filter--center filter--filterActive"]').tap()
        self.find_element('view[class="screen--center screen--clear"]').tap()
        self.get_screenshot()

    def test_rent_搜索并返回(self):
        """
        V6.40.x: 点击搜索
        """
        self.tabtorent()

        self.find_element('view[class="center column btn"]').tap()
        self.delay(3)
        self.get_screenshot('search')
        self.verifyPageName('/page/publicPages/search/search')

        self.back()
        self.get_screenshot()

