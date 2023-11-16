from ddt import ddt, file_data

from tfq.writepost import WritePost


class TestJJRImdetailC2B(WritePost):
    """
    IM会话详情C2B（经纪人）
    """

    @classmethod
    def setUpClass(cls) -> None:
        super(TestJJRImdetailC2B, cls).setUpClass()
        cls().change_C()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/im/pages/chating/chating?chatTo=zsb_nj_1000947&city=nj"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestJJRImdetailC2B, self).setUp()
        print("TestJJRImdetailC2B setup")

    def test_01_点击头像(self):
        """
        点击经纪人头像
        """
        self.find_element('image[class="avatar"]').tap()
        self.delay(3)
        self.get_screenshot()
        self.verifyPageName('/esf/sell/pages/broker/broker')

    def test_02_点击主推房源发送(self):
        """
        点击悬浮层的“主推房源”，进入房源页，选择房源发送
        """
        # 点击 悬浮层的“主推房源”
        self.delay(2)
        self.find_element('view[class="mainFybtn"]').tap()
        self.delay(20)

        # 进入 主推房源  页面，选择房源
        self.find_element('view[class="pa itemPlaceholder"]').tap()

        # 进行发送
        self.find_element('view[class="center send"]').tap()
        self.delay(2)

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

    def test_03_更多发送房源(self):
        """
        点击更多功能-发送房源，进入我的收藏页面，选择楼盘进行发送
        """
        # 点击更多功能
        self.find_element('image[class="chatinput-img fr"]').tap()
        self.delay(2)

        # 点击 发送房源
        self.find_element('view[class="more-subcontent-item"][data-kind="fy"]', inner_text='发送房源').tap()
        self.delay(4)
        # 进入 我的收藏 页面
        self.verifyPageName('/esf/sell/pages/myCollect/myCollect')

        # 切换到 楼盘 tab
        self.find_element('view[class="pr center tab"][data-id="4"]').tap()
        self.delay(2)
        # 选择第一个楼盘
        self.find_element('view[class="pa itemPlaceholder"]').tap()

        # 进行发送
        self.find_element('view[class="center send"]').tap()
        self.delay(2)

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')