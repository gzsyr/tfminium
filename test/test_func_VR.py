# add by zsy
from test.test_base import TestBase


class TestFuncVR(TestBase):
    """
    VR 看房页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/vr/vrlist?city=qz'
        self.switch = False
        super(TestFuncVR, self).setUp()
        print("TestFuncVR setup test")

    def set_pick_filter(self, index, value):
        """
        picker选择器的选择
        index: 元素的顺序
        value: 选择的pick数值
        """
        ele = self.page.get_element(f'picker[data-bj="{index}"]')
        ele.click()
        ele.pick(value)

    def test_filter_area(self):
        """
        VR看房页面，点击筛选项“区域”选择
        """
        self.set_pick_filter(0, 2)

        ele = self.page.get_elements('view[class= "headBarLi-txt tfLine1 picker"]')
        self.verifyStr(ele[0].inner_text, '丰泽', "VR看房页面，点击筛选项“区域”选择 丰泽 ok")

    def test_filter_price(self):
        """
        VR看房页面，点击筛选项“价格”选择
        """
        self.set_pick_filter(1, 3)

        ele = self.page.get_elements('view[class= "headBarLi-txt tfLine1 picker"]')
        self.verifyStr(ele[1].inner_text, '4000-5000元/㎡', "VR看房页面，点击筛选项“价格”选择 4000-5000元/㎡ ok")

    def test_filter_huxing(self):
        """
        VR看房页面，点击筛选项“户型”选择
        """
        self.set_pick_filter(2, 3)

        ele = self.page.get_elements('view[class= "headBarLi-txt tfLine1 picker"]')
        self.verifyStr(ele[2].inner_text, '三室', "VR看房页面，点击筛选项“户型”选择 三室 ok")

    def test_goto_housedetail(self):
        """
        VR看房页面，点击列表项第一个标题，进入新房详情页
        """
        self.page.get_element('view[class="vrLiT tfLine1"]').click()

        self.verifyPageName("/page/newhouse/detail")

    def test_VRname_goto_detail(self):
        """
        VR看房页面，点击列表项第一个VR名称
        """
        self.page.get_element('view[class="vrLiB-t tfLine1"]').click()

        self.verifyPageName("/page/vr/vrdetail")

    def test_VRbtn_goto_detail(self):
        """
        VR看房页面，点击列表项第一个VR看房 按钮
        """
        self.page.get_element('view[class="vrLiB-vrBtn"]').click()

        self.verifyPageName("/page/vr/vrdetail")

