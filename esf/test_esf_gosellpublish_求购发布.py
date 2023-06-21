from ddt import ddt, file_data
from base.test_base import TestBase

import pyautogui
import pyperclip

@ddt
class Testesfgosellfb(TestBase):
    """
    求购发布
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/publish/lookRoom/sell?city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfgosellfb, self).setUp()
        print("Testesfgosellfb setup")

    def test_publish_gosell_求购发布(self):
        # 想买的区域
        # self.find_element('view[class="indicator down"]').tap()
        # self.delay(3)

        # 想买的户型
        # self.page.get_element('/view[2]/view[6]/view[3]').tap()
        # self.delay(3)

        # 买房预算
        e = self.page.get_element('//slider[1]')
        e.slide_to(500)
        self.delay(3)

        # 点击立刻找房
        self.page.get_element('view[class="submit"]', inner_text='立刻找房').tap()
        self.delay(1)
        self.get_screenshot()