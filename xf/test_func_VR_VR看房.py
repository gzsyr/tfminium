# add by zsy
from base.test_base import TestBase


class TestFuncVR(TestBase):
    """
    VR 看房页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/vr/vrlist?city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFuncVR, self).setUp()
        print("TestFuncVR setup atest")

    def test_03_filter_area_筛选区域(self):
        """
        VR看房页面，点击筛选项“区域”选择
        """
        self.set_pick_filter('picker[data-bj="0"]', 2)

        ele = self.page.get_elements('view[class= "headBarLi-txt tfLine1 picker"]')
        self.verifyStr(ele[0].inner_text, '丰泽', "VR看房页面，点击筛选项“区域”选择 丰泽 ok")
        self.get_screenshot()

    def test_05_filter_price_筛选价格(self):
        """
        VR看房页面，点击筛选项“价格”选择
        """
        self.set_pick_filter('picker[data-bj="1"]', 3)

        ele = self.page.get_elements('view[class= "headBarLi-txt tfLine1 picker"]')
        self.verifyStr(ele[1].inner_text, '4000-5000元/㎡', "VR看房页面，点击筛选项“价格”选择 4000-5000元/㎡ ok")
        self.get_screenshot()

    def test_04_filter_huxing_筛选户型(self):
        """
        VR看房页面，点击筛选项“户型”选择
        """
        self.set_pick_filter('picker[data-bj="2"]', 3)

        ele = self.page.get_elements('view[class= "headBarLi-txt tfLine1 picker"]')
        self.verifyStr(ele[2].inner_text, '三室', "VR看房页面，点击筛选项“户型”选择 三室 ok")
        self.get_screenshot()

    def test_06_goto_housedetail_进入楼盘(self):
        """
        VR看房页面，点击列表项第一个标题，进入新房详情页
        """
        self.page.get_element('view[class="vrLiT tfLine1"]').click()

        self.verifyPageName("/page/newhouse/detail")
        self.get_screenshot()

    def test_02_VRname_goto_detail_VR名称进入VR(self):
        """
        VR看房页面，点击列表项第一个VR名称
        """
        self.page.get_element('view[class="vrLiB-t tfLine1"]').click()

        self.verifyPageName("/page/vr/vrdetail")
        self.get_screenshot()

    def test_01_VRbtn_goto_detail_看房按钮进入VR(self):
        """
        VR看房页面，点击列表项第一个VR看房 按钮
        """
        self.page.get_element('view[class="vrLiB-vrBtn"]').click()

        self.verifyPageName("/page/vr/vrdetail")
        self.get_screenshot()

