from ddt import ddt, file_data
from base.test_base import TestBase

import pyautogui
import pyperclip

@ddt
class Testrentzsywfcz(TestBase):
    """
    找室友无房出租
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/publish/roommate/noHouse?city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentzsywfcz, self).setUp()
        print("Testrentzsywfcz setup")

    def test_rent_zsywfcz_找室友无房出租(self):
        """
        找室友无房出租
        :return:
        """
        # 重置
        self.set_result()
        # 标题
        self.set_zsytitle()
        # 期望地点
        self.set_qwaddr()
        # 租金预算
        self.set_zjys()
        # 入住时间
        self.set_ruzhutime()
        # 我是几个人住
        self.set_jrz()
        # 室友性别
        self.set_roomsex()
        # 室友期望
        self.set_roomexpect()
        # 对房子的期望
        self.set_houseexpect()
        # 描述
        self.set_desc()
        # 联系人
        self.set_name()
        # 发布
        self.set_fabu()
        # 点击个人中心
        self.set_grzx()

    def set_zsytitle(self, zsytitle='无房找室友标题啊啊啊'):
        # 标题
        pyperclip.copy(zsytitle)
        self.delay(8)
        self.input_value_by_mk(png='rent/wfzsytitle.png', value=zsytitle)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(5)
        return self

    def set_qwaddr(self):
        # 期望地点
        self.page.get_element('view[class="flex_1 center flex_column partItem"][data-picker="1"]').tap()
        self.delay(2)
        self.delay(2)
        self.page.get_element('//locpicker/view/view/view[2]/scroll-view/view[6]').tap()
        self.delay(2)
        self.page.get_element('//locpicker/view/view/view[2]/scroll-view[2]/view[2]').tap()
        self.delay(2)
        self.page.get_element('view[class="locPicker--center locPicker--confirm"]').tap()
        return self

    def set_zjys(self):
        # 租金预算
        self.page.get_element('view[class="flex_1 center flex_column partItem"][data-picker="2"]').tap()
        self.delay(2)
        e = self.page.get_element('//slider/view/view/view[2]/view[2]/slider')
        self.delay(2)
        e.slide_to(5800)
        self.delay(3)
        self.page.get_element('view[class="slider--center slider--confirm"]').tap()
        return self

    def set_ruzhutime(self, ruzhutime=[1, 2, 3]):
        # 入住时间
        self.page.get_element('view[class="flex_1 center flex_column partItem"][data-picker="3"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": ruzhutime})
        self.delay(2)
        self.page.get_element('view[class="yearPicker--center yearPicker--confirm"]').tap()
        return self

    def set_jrz(self, jrz=[1]):
        # 我是几个人住
        self.page.get_element('view[class="flex_1 center flex_column partItem"][data-picker="4"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": jrz})
        self.delay(2)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        return self

    def set_roomsex(self):
        # 室友性别
        self.page.get_element('view[class="center option"][data-id="2"]', inner_text='限女生').tap()
        self.delay(3)
        return self

    def set_roomexpect(self):
        # 室友期望
        self.page.get_element('view[class="center option"][data-id="2"]', inner_text='不吸烟').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-id="3"]', inner_text='不养宠物').tap()
        self.delay(2)
        # self.page.get_element('view[class="center option"][data-id="6"]', inner_text='爱干净').tap()
        # self.delay(2)
        return self

    def set_houseexpect(self):
        # 对房子的期望
        self.page.get_element('view[class="center option"][data-id="1"]', inner_text='有独卫').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-id="4"]', inner_text='临地铁').tap()
        self.delay(2)
        # self.page.get_element('view[class="center option"][data-id="6"]', inner_text='有阳台').tap()
        # self.delay(2)
        return self

    def set_desc(self, desc='描述描述描述啊啊啊'):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 描述
        self.page.get_element('view[class="pr desc"]').tap()
        self.delay(3)
        pyperclip.copy(desc)
        self.delay(3)
        self.input_value_by_mk(png='rent/wfzsydesc.png', value=desc, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(3)
        self.page.get_element('view[class="center confirm"]', inner_text='完成').tap()
        return self

    def set_name(self, name='赵赵赵测试'):
        # 联系人
        pyperclip.copy(name)
        self.delay(3)
        self.input_value_by_mk(png='rent/wfzsyname.png', value=name, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        return self

    def set_fabu(self):
        # 确认发布
        self.page.get_element('//resetconfirm/view/view/view[2]').tap()
        self.delay(3)
        self.get_screenshot()
        return self

    def set_result(self):
        # 重置
        result = {"confirm": True}
        self.app.mock_wx_method("showModal", result=result)
        self.page.get_element('//resetconfirm/view/view/view').tap()
        self.app.restore_wx_method("showModal")
        self.delay(3)
        return self

    def set_grzx(self):
        # 点击个人中心
        self.page.get_element('text[class="color"]').tap()
        self.delay(1)
        self.get_screenshot()
        return self
