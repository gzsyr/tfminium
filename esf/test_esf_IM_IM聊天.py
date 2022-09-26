from ddt import file_data
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt_class()
class Testesfim(TestBase):
    """
    IM聊天页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/im/pages/chating/chating?chatTo=zsb_nj_912407&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfim, self).setUp()
        print("Testesfim setup")

    def test_click_history_点击历史消息(self):
        """
        点击历史消息
        :return:
        """
        self.page.get_element('//view[@class="chat-top flex tfAlignC"]/image').tap()
        self.delay(3)
        self.get_screenshot()

    def test_send_发送消息(self):
        """
        发送消息(输入和语音切换)
        :return:
        """
        chat = self.page.element_is_exists('input[class="chatinput-input"]')
        if chat == True:
            self.page.get_element('input[class="chatinput-input"]').input('你好ya')
            self.delay(1)
            fasong = self.page.get_element('button[class="chatinput-sendbtn fr"]')
            fasong.tap()
            self.delay(2)
            voice = self.page.get_element('image[class="chatinput-img"]')
            voice.tap()
            self.delay(2)
            mask = self.page.get_element('button[class="chatinput-voice-mask"]')
            mask.tap()
            self.delay(2)
            keyboard = self.page.get_element('image[class="chatinput-img"]')
            keyboard.tap()
            self.delay(2)
            self.get_screenshot()
        else:
            mask = self.page.get_element('button[class="chatinput-voice-mask"]')
            mask.tap()
            self.delay(2)
            keyboard = self.page.get_element('image[class="chatinput-img"]')
            keyboard.tap()
            self.delay(2)
            self.page.get_element('input[class="chatinput-input"]').input('你好ya')
            self.delay(1)
            fasong = self.page.get_element('button[class="chatinput-sendbtn fr"]')
            fasong.tap()
            self.delay(2)
            voice = self.page.get_element('image[class="chatinput-img"]')
            voice.tap()
            self.delay(2)
            self.get_screenshot()

    def test_inputimg_点击上传图片(self):
        """
        点击上传图片
        :return:
        """
        self.page.get_element('image[class="chatinput-img fr"]').tap()
        self.get_screenshot()





