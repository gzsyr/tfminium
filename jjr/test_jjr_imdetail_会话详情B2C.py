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
        self.page_name = "/im/pages/chating/chating?chatTo=tf_6255336&city=nj"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestJJRImdetailB2C, self).setUp()
        print("TestJJRImdetailB2C setup")

    def test_08_发送资料(self):
        """
        V6.48.X: 发送资料
        """
        self.find_element('view[class="btn gfzlBtn flex tfAlignC"]').tap()
        self.delay(3)
        self.get_screenshot('open')

        self.find_element('image[class="img"]').tap()
        self.delay(2)
        self.get_screenshot('view')

        self.back()

        self.find_element('view[class="tfFlex tfAlignC tfFlexC chat"]').tap()
        self.get_screenshot('send')

    def test_07_点击头像无响应(self):
        """
        V6.42.X: 点击头像无响应
        """
        self.redirect_to_page('/im/pages/chating/chating?chatTo=tf_6219430&city=nj')
        self.find_element('image[class="avatar"]').tap()
        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')
    def test_06_点击头像进详情(self):
        """
        V6.42.X: 点击用户头像进详情
        """
        self.find_element('image[class="avatar"]').tap()
        self.get_screenshot()
        self.verifyPageName('/page/business/customerManage/customerDetail/customerDetail')
    def test_05_点击标记客户(self):
        """
        V6.42.x: 点击 标记客户
        """
        self.find_element('view[class="btn"]/view', inner_text='标记客户').tap()
        self.verifyPageName('/page/business/customerManage/followUp/followUp')
        self.get_screenshot()

    def delete_test_01_点击用户足迹(self):
        """
        点击上方C端用户昵称旁边的“用户足迹”
        delete v7.02.x
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
        self.delay(5)
        self.find_element('view[class="btn fyBtn flex tfAlignC"]').tap()
        self.delay(5)

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
        self.delay(2)

        # 点击 发送房源
        self.find_element('view[class="more-subcontent-item"][data-kind="fy"]', inner_text='发送房源').tap()
        self.delay(4)

        # 进入 我的房源  页面，选择房源
        self.find_element('view[class="pa itemPlaceholder"]').tap()

        # 进行发送
        self.find_element('view[class="center send"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

