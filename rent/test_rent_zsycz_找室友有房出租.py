from ddt import ddt, file_data
from base.test_base import TestBase

import pyautogui
import pyperclip

@ddt
class Testrentzsycz(TestBase):
    """
    找室友有房出租
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/publish/roommate/step_1?city=nj"

        # self.page_name = "/esf/village/publish/roommate/roommateType&city=nj"

        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentzsycz, self).setUp()
        print("Testrentzsycz setup")

    @file_data('./test_rent_zsycz.yml')
    def test_rent_zsycz_找室友有房出租(self, **kwargs):
        """
        有房出租发布
        :param kwargs:
        :return:
        """
        # 上传图片
        self.set_img()
        # 标题
        self.set_zsytitle(kwargs['zsytitle'])
        # 小区名称
        self.set_xqmc(kwargs['xqmc'])
        # 月租金
        self.set_price(kwargs['price'])
        # 户型
        self.set_huxing(kwargs['huxing'])
        # 出租类型
        self.set_chuzutpye(kwargs['chuzutpye'])
        # 入住时间
        self.set_ruzhutime(kwargs['ruzhutime'])
        # 已入住情况
        self.set_ruzhuqk(kwargs['ruzhuqk'])
        # 室友性别
        self.set_roomsex()
        # 室友期望
        self.set_roomexpect()
        # 房屋亮点
        self.set_fwld()
        # 下一步
        self.set_xiayibu()
        # 家具
        self.set_jiaju()
        # 家电
        self.set_jiadian()
        # 其他
        self.set_qita()
        # 房源描述
        self.set_desc(kwargs['fyms'])
        # 您的身份
        self.set_identity()
        # 联系人
        self.set_name(kwargs['name'])
        # 发布
        self.set_fabu()
        # 个人中心
        self.set_grzx()

    def set_img(self):
        # 上传图片
        self.page.get_element('//step_1head/view/view/view[2]').tap()
        self.delay(3)
        # 第一张
        self.page.get_element('view[class="center flex_column upload"]').tap()
        self.delay(5)
        self.input_select_image(png='esf\\123.png')
        self.delay(3)
        # 第二张
        self.page.get_element('view[class="center flex_column upload"]').tap()
        self.delay(5)
        self.input_select_image(png='rent\\2.png')
        self.delay(3)
        # 第三张
        self.page.get_element('view[class="center flex_column upload"]').tap()
        self.delay(5)
        self.input_select_image(png='rent\\3.png')
        self.delay(3)
        self.page.get_element('view[class="center completeBtn"]', inner_text='完成').tap()
        self.delay(3)
        # self.page.get_element('view[class="center noMorePics"]', inner_text='不需要').tap()
        # self.delay(3)
        return self

    def set_zsytitle(self, zsytitle='找室友标题啊啊啊'):
        # 标题
        pyperclip.copy(zsytitle)
        self.delay(8)
        self.input_value_by_mk(png='rent/zsytitle.png', value=zsytitle)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(5)
        return self

    def set_xqmc(self, xqmc='测试'):
        # 小区名称
        self.delay(8)
        self.page.get_element('view[class="flex_1 center flex_column partItem"]/view[2]').tap()
        self.delay(8)
        self.page.get_element('input[class="flex_1 input"]').input(xqmc)
        self.delay(5)
        item = self.page.get_elements('/view[2]/view/view')
        item[0].tap()
        self.delay(2)
        return self

    def set_price(self, price='3500'):
        # 月租金
        self.page.get_element('view[class="flex_1 center flex_column partItem"][data-picker="1"]').tap()
        self.delay(5)
        self.input_value_by_mk(png='rent/zsyprice.png', value=price)
        self.delay(5)
        self.page.get_element('//roommateprice//text', inner_text = '年付').tap()
        self.delay(5)
        self.page.get_element('view[class="roommatePrice--center roommatePrice--confirm"]').tap()
        self.delay(1)
        return self

    def set_huxing(self, huxing=[3, 2, 1]):
        # 户型
        self.page.get_element('view[class="flex_1 center flex_column partItem"][data-picker="2"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": huxing})
        self.delay(2)
        self.page.get_element('view[class="houseTypePicker--center houseTypePicker--confirm"]').tap()
        return self

    def set_chuzutpye(self, chuzutpye=[1]):
        # 出租类型
        self.page.get_element('view[class="flex_1 center flex_column partItem"][data-picker="18"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": chuzutpye})
        self.delay(2)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
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

    def set_ruzhuqk(self, ruzhuqk=[1, 2]):
        # 已入住情况
        self.page.get_element('view[class="flex_1 center flex_column partItem"][data-picker="4"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": ruzhuqk})
        self.delay(2)
        self.page.get_element('view[class="multiSelector--center multiSelector--confirm"]').tap()
        return self

    def set_roomsex(self):
        # 室友性别
        self.page.get_element('view[class="center option"][data-id="2"]', inner_text='限女生').tap()
        self.delay(3)

    def set_roomexpect(self):
        # 室友期望
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('view[class="center option"][data-id="2"]', inner_text='不吸烟').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-id="3"]', inner_text='不养宠物').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-id="6"]', inner_text='爱干净').tap()
        self.delay(2)

    def set_fwld(self):
        # 房屋亮点
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('view[class="center option"][data-id="1"]', inner_text='有电梯').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-id="5"]', inner_text='拎包入住').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-id="7"]', inner_text='可短租').tap()
        self.delay(2)

    def set_xiayibu(self):
        # 下一步
        self.page.get_element('//resetconfirm/view/view/view[2]').tap()
        self.delay(3)

    def set_jiaju(self):
        # self.set_xiayibu()
        # 家具
        self.delay(3)
        self.page.get_element('view[class="center option"][data-id="1"]', inner_text='床').tap()
        self.delay(3)
        self.page.get_element('view[class="center option"][data-id="2"]', inner_text='衣柜').tap()
        self.delay(3)

    def set_jiadian(self):
        # self.set_xiayibu()
        # 家电
        self.delay(3)
        self.page.get_element('view[class="center option"][data-id="7"]', inner_text='洗衣机').tap()
        self.delay(3)
        self.page.get_element('view[class="center option"][data-id="9"]', inner_text='热水器').tap()
        self.delay(3)
        self.page.get_element('view[class="center option"][data-id="13"]', inner_text='微波炉').tap()
        self.delay(3)

    def set_qita(self):
        # self.set_xiayibu()
        # 其他
        self.delay(3)
        self.page.get_element('view[class="center option"][data-id="14"]', inner_text='宽带').tap()
        self.delay(3)
        self.page.get_element('view[class="center option"][data-id="16"]', inner_text='独立卫生间').tap()
        self.delay(3)

    def set_desc(self, fyms= '找室友房源描述好房好房好房好房房源描述'):
        # self.set_xiayibu()
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 房源描述
        self.delay(3)
        self.page.get_element('view[class="pr desc"]').tap()
        self.delay(3)
        pyperclip.copy(fyms)
        self.delay(3)
        self.input_value_by_mk(png='rent/zsyfyms.png', value=fyms, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(3)
        self.page.get_element('view[class="center confirm"]').tap()
        return self

    def set_identity(self):
        # self.set_xiayibu()
        # self.page.scroll_to(800, 500)
        # self.delay(1)
        # 您的身份
        self.delay(3)
        self.page.get_element('view[class="center identity"][data-id="1"]').tap()
        self.delay(3)

    def set_name(self, name='赵赵赵测试'):
        # self.set_xiayibu()
        # self.page.scroll_to(800, 500)
        # self.delay(1)
        # 联系人
        pyperclip.copy(name)
        self.delay(3)
        self.input_value_by_mk(png='rent/zsyname.png', value=name, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        return self

    def set_fabu(self):
        # self.set_xiayibu()
        # self.page.scroll_to(800, 500)
        # self.delay(1)
        # 点击我已阅读并同意
        self.page.get_element('view[class="center checkTap"]').tap()
        self.delay(3)

        # 确认发布
        self.page.get_element('view[class="resetConfirm--flex_1 resetConfirm--center resetConfirm--confirm"]').tap()
        self.delay(3)
        return self

    def set_grzx(self):
        #个人中心
        self.page.get_element('//view[@class="success"]/view[3]/text[2]').tap()
        self.delay(3)
        return self
