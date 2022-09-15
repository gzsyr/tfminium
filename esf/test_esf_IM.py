from ddt import file_data
from minium import ddt_class, ddt_case

from base.common import delay
from base.test_base import TestBase


@ddt_class()
class Testesfim(TestBase):
    """
    IM聊天页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/im/pages/chating/chating?chatTo=slwkgj_9021&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfim, self).setUp()
        print("Testesfim setup")

    def test_click_history(self):
        """
        点击历史消息
        :return:
        """
        self.page.get_element('view[class="chating-history"]').tap()
        self.get_capture()

    def test_send(self):
        """
        发送消息(输入和语音切换)
        :return:
        """
        chat = self.page.element_is_exists('input[class="chatinput-input w500"]')
        if chat == True:
            self.page.get_element('input[class="chatinput-input w500"]').input('你好ya')
            delay(1)
            fasong = self.page.get_element('button[class="chatinput-sendbtn fr"]')
            fasong.tap()
            delay(2)
            voice = self.page.get_element('image[class="chatinput-img"]')
            voice.tap()
            delay(2)
            mask = self.page.get_element('button[class="chatinput-voice-mask"]')
            mask.tap()
            delay(2)
            keyboard = self.page.get_element('image[class="chatinput-img"]')
            keyboard.tap()
            delay(2)
            self.get_capture()
        else:
            mask = self.page.get_element('button[class="chatinput-voice-mask"]')
            mask.tap()
            delay(2)
            keyboard = self.page.get_element('image[class="chatinput-img"]')
            keyboard.tap()
            delay(2)
            self.page.get_element('input[class="chatinput-input w500"]').input('你好ya')
            delay(1)
            fasong = self.page.get_element('button[class="chatinput-sendbtn fr"]')
            fasong.tap()
            delay(2)
            voice = self.page.get_element('image[class="chatinput-img"]')
            voice.tap()
            self.get_capture()

    def test_inputimg(self):
        """
        点击上传图片
        :return:
        """
        self.page.get_element('image[class="chatinput-img fr"]').tap()
        self.get_capture()




