from minium import ddt_class, ddt_case
from base.test_base import TestBase
@ddt_class()
class Testesffjpg(TestBase):
    """
    房价评估
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/pages/evaluate/evaluate?blockId=3223&blockName=长营村小区&buildArea=45&orientation=南北&room=2&hall=2&totalFloor=6"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesffjpg, self).setUp()
        print("Testesffjpg setup")

    def test_input_flo_输入楼层大于总楼层(self):
        """
        输入楼层大于总楼层
        :return:
        """
        e = self.page.get_element("input", inner_text="请输入").input('10')
        e_butt = self.page.get_element('view[class="center submit"]')
        e_butt.tap()
        self.delay(3)
        self.get_screenshot()

    def test_input_floor_输入楼层(self):
        """
        输入楼层
        :return:
        """
        e = self.page.get_element("input", inner_text="请输入").input('5')
        e_butt = self.page.get_element('view[class="center submit"]')
        e_butt.tap()
        self.delay(3)
        self.get_screenshot()





