import pyautogui
import pyperclip
from ddt import ddt, file_data

from tfq.writepost import WritePost


class TestJJRImdetailB2C(WritePost):
    """
    IM会话详情B（经纪人）2C
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestJJRImdetailB2C, cls).setUpClass()
        cls().change_jjr()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/im/pages/chating/chating?chatTo=tf_6219430&city=nj"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestJJRImdetailB2C, self).setUp()
        print("TestJJRImdetailB2C setup")

    def test_01_点击用户足迹(self):
        """
        点击上方C端用户昵称旁边的“用户足迹”
        """
        self.find_element('view[class="usertrack"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_02_去设置自动回复(self):
        """
        点击【去设置自动回复，不错过任何消息】
        """
        try:
            self.find_element('view[class="chatTips flex tfAlignC tfFlexSb"]').tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print("设置自动回复已X掉")

    def test_03_快捷发送房源(self):
        """
        通过快捷发送房源
        """
        # 点击“发送房源”
        self.find_element('view[class="fyBtn flex tfAlignC"]').tap()
        self.delay(4)

        # 进入 我的房源  页面，选择房源
        self.find_element('view[class="pa itemPlaceholder"]').tap()

        # 进行发送
        self.find_element('view[class="center send"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

    def test_04_更多发送房源(self):
        """
        通过更多功能发送房源
        """
        # 点击更多功能
        self.find_element('image[class="chatinput-img fr"]').tap()
        self.delay(1)

        # 点击 发送房源
        self.find_element('view[class="more-subcontent-item"][data-kind="fy"]', inner_text='发送房源').tap()
        self.delay(4)

        # 进入 我的房源  页面，选择房源
        self.find_element('view[class="pa itemPlaceholder"]').tap()

        # 进行发送
        self.find_element('view[class="center send"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

