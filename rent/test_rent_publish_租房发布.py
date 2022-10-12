from ddt import ddt, file_data
from base.test_base import TestBase

import pyautogui
import pyperclip

@ddt
class Testrentfb(TestBase):
    """
    租房发布
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/publish/rent/step_1?infoType=1&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentfb, self).setUp()
        print("Testrentfb setup")

    @file_data('./test_rent_publish.yml')
    def test_publish_rent_租房发布(self, **kwargs):
        """
        租房发布
        :return:
        """
        # 上传图片
        self.set_img()
        # 小区名称
        self.set_xqmc(kwargs['xqmc'])
        # 户型
        self.set_huxing(kwargs['huxing'])
        # 朝向
        self.set_chaoxiang(kwargs['chaoxiang'])
        # 楼层
        self.set_louceng(kwargs['louceng'])
        # 楼栋号
        self.set_loudonghao(kwargs['loudong'])
        # 单元号
        self.set_danyuan(kwargs['danyuan'])
        # 室号
        self.set_shihao(kwargs['shi'])
        # 装修
        self.set_zhuangxiu(kwargs['zhuangxiu'])
        # 面积
        self.set_area(kwargs['area'])
        # 租金
        self.set_price(kwargs['price'])
        # 租金包含
        self.set_zujinbaohan()
        self.get_screenshot()
        self.delay(3)
        # 下一步
        self.set_xiayibu()
        # 房源标题
        self.set_title(kwargs['title'])
        # 房屋配置
        self.set_fwpz()
        # 房屋亮点
        self.set_fwld()
        # 出租要求
        self.set_czyq()
        # 房源描述
        self.set_desc(kwargs['fyms'])
        # 核验码
        self.set_hym(kwargs['heyanma'])
        # 看房时间
        self.set_kanfangtime(kwargs['kanfangtime'])
        # 入住时间
        self.set_ruzhutime(kwargs['ruzhutime'])
        # 联系人
        self.set_name(kwargs['name'])
        # 房屋权属信息-去认证
        self.set_renzheng(kwargs['zjlx'], kwargs['zjhm'], kwargs['qqh'], kwargs['cqrxm'], kwargs['cqrsfzh'])
        self.get_screenshot()
        self.delay(3)
        # 发布
        self.set_fabu()
        self.get_screenshot()
        self.delay(3)
        # 个人中心
        self.set_grzx()

    def set_img(self):
        self.page.get_element('//step_1head//text', inner_text="图片或视频").tap()
        self.delay(2)

        # self.page.get_element('view[class="center flex_column upload"]', inner_text='上传视频').tap()
        # self.delay(3)

        self.page.get_element('view[class="center flex_column upload"]', inner_text='上传图片').tap()
        self.delay(3)

        self.input_select_image(png='esf\\123.png')

        self.delay(2)
        self.page.get_element('view[class="center completeBtn"]').tap()

        self.delay(3)
        self.page.get_element('view[class="center noMorePics"]').tap()
        return self

    def set_xqmc(self, xqmc='测试'):
        # 小区名称
        self.page.get_element('view[class="center flex_column part"]/view').tap()
        self.delay(3)
        self.page.get_element('input[class="flex_1 input"]').input(xqmc)
        self.delay(3)
        item = self.page.get_elements('/view[2]/view/view')
        item[0].tap()
        self.delay(2)
        return self

    def set_huxing(self, huxing=[3, 2, 1]):
        # 户型
        self.page.get_element('view[class="center flex_column partItem"][data-picker="1"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": huxing})
        self.delay(2)
        self.page.get_element('view[class="houseTypePicker--center houseTypePicker--confirm"]').tap()
        return self

    def set_chaoxiang(self, chaoxiang=[1]):
        # 朝向
        self.page.get_element('view[class="center flex_column partItem"][data-picker="2"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": chaoxiang})
        self.delay(2)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        return self

    def set_louceng(self, louceng=[3, 3]):
        # 楼层
        self.page.get_element('view[class="center flex_column partItem"][data-picker="4"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": louceng})
        self.delay(2)
        self.page.get_element('view[class="floorPicker--center floorPicker--confirm"]').tap()
        self.delay(3)
        return self

    def set_loudonghao(self, loudong="4"):
        # 楼栋号
        self.input_value_by_mk(png='rent/loudong.png', value=loudong)
        self.delay(5)
        return self

    def set_danyuan(self, danyuan="2"):
        # 单元号
        self.input_value_by_mk(png='rent/danyuan.png', value=danyuan)
        self.delay(5)
        return self

    def set_shihao(self, shi="6"):
        # 室号
        self.input_value_by_mk(png='rent/shi.png', value=shi)
        self.delay(5)
        return self

    def set_zhuangxiu(self, zhuangxiu=[3]):
        # 装修
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('view[class="between infoItem"][data-picker="3"]').tap()
        self.delay(5)
        e = self.page.get_element('picker-view')
        e.trigger("change", {"value": zhuangxiu})
        self.delay(5)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        return self

    def set_area(self, area="90"):
        # 面积(整租）
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('view[class="between infoItem"][data-picker="6"]').tap()
        self.delay(5)
        self.input_value_by_mk(png='rent/area.png', value=area)
        self.delay(5)
        self.page.get_element('view[class="priceAreaPicker--center priceAreaPicker--confirm"]').tap()
        self.delay(5)
        return self

    def set_price(self, price="3000"):
        # 租金
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('view[class="between infoItem"][data-picker="7"]').tap()
        self.delay(5)
        self.input_value_by_mk(png='rent/price.png', value=price)
        self.delay(5)
        self.page.get_element('//priceareapicker//text', inner_text = '年付').tap()
        self.delay(5)
        self.page.get_element('view[class="priceAreaPicker--center priceAreaPicker--confirm"]').tap()
        self.delay(5)
        return self

    def set_zujinbaohan(self):
        # 租金包含
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('view[class="between infoItem"][data-picker="8"]').tap()
        self.page.get_element('//scroll-view/view/text').tap()
        self.delay(1)
        self.page.get_element('//scroll-view/view[2]/text').tap()
        self.delay(1)
        self.page.get_element('//scroll-view/view[3]/text').tap()
        self.delay(3)
        self.page.get_element('view[class="rentItems--center rentItems--confirm"]').tap()
        self.delay(1)
        return self

    def set_xiayibu(self):
        # 下一步
        self.delay(3)
        self.page.get_element('//resetConfirm/view/view/view[2]').tap()
        self.delay(3)
        return self

    def set_title(self, title='测试小区好房出租'):
        # self.set_xiayibu()
        # 房源标题
        self.page.get_element('//view[@class="pr"]/view[2]/view/input').input(title)
        self.delay(3)
        return self

    def set_fwpz(self):
        # 房屋配置
        self.page.get_element('view[class="center option"][data-equipment="床"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-equipment="热水器"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-equipment="可做饭"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-equipment="独立卫生间"]').tap()
        return self

    def set_fwld(self):
        # 房屋亮点
        self.page.get_element('view[class="center option"][data-special="电梯房"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-special="南北通透"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-special="交通便利"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-special="拎包入住"]').tap()
        return self

    def set_czyq(self):
        # 出租要求
        self.page.get_element('view[class="center option"][data-condition="一家人"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-condition="一年起租"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-condition="租户稳定"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-condition="禁止养宠物"]').tap()
        return self

    def set_desc(self, fyms= '房源描述好房好房好房好房房源描述'):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 房源描述
        self.page.get_element('view[class="pr desc"]').tap()
        self.delay(3)
        pyperclip.copy(fyms)
        self.delay(3)
        self.input_value_by_mk(png='esf/fyms.png', value=fyms, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(3)
        self.page.get_element('view[class="center confirm"]').tap()
        return self

    def set_hym(self, heyanma= "NJZ220929123456"):
        # 核验码
        self.page.get_element('//view[@class="between hyCode"]/input')
        self.input_value_by_mk(png='rent/heyanma.png', value=heyanma, direction=1)
        self.delay(3)
        return self

    def set_kanfangtime(self, kanfangtime=[2]):
        # 看房时间
        self.page.get_element('view[class="between item"][data-picker="9"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(3)
        e.trigger("change", {"value": kanfangtime})
        self.delay(5)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        return self

    def set_ruzhutime(self, ruzhutime=[1, 2, 3]):
        # 入住时间
        self.page.get_element('view[class="between item"][data-picker="10"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(3)
        e.trigger("change", {"value": ruzhutime})
        self.delay(3)
        self.page.get_element('view[class="yearPicker--center yearPicker--confirm"]').tap()
        return self

    def set_name(self, name='赵赵测试'):
        # 联系人
        pyperclip.copy(name)
        self.delay(3)
        self.input_value_by_mk(png='rent/name.png', value=name, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        return self

    def set_renzheng(self, zjlx=[2], zjhm='0000000000', qqh='1111111111', cqrxm='赵赵赵', cqrsfzh='111111111111111'):
        # 房屋权属信息-去认证
        self.page.get_element('view[class="center ownershipCertificate"]', inner_text='去认证').tap()
        self.delay(5)
        # 证件类型
        self.page.get_element('/view/view/view[2]').tap()
        self.delay(5)
        e = self.page.get_element('picker-view')
        e.trigger("change", {"value": zjlx})
        self.delay(5)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        self.delay(10)
        # 证件号码
        self.input_value_by_mk(png='rent/zjhm.png', value=zjhm, direction=1)
        self.delay(5)
        # 丘权号
        self.input_value_by_mk(png='rent/qqh.png', value=qqh, direction=1)
        self.delay(5)
        # 产权人姓名
        pyperclip.copy(cqrxm)
        self.delay(5)
        self.input_value_by_mk(png='rent/cqrxm.png', value=cqrxm, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(5)
        # 产权人身份证号
        # self.input_value_by_mk(png='rent/cqrsfzh.png', value=cqrsfzh, direction=1)
        # self.delay(5)
        # 证件照上传
        self.page.get_element('view[class="center flex_column uploadBtn"]', inner_text="添加照片").tap()
        self.delay(5)
        self.input_select_image(png='esf\\123.png')
        self.delay(5)
        self.page.get_element('view[class="resetConfirm--flex_1 resetConfirm--center resetConfirm--confirm"]').tap()

    def set_fabu(self):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 点击我已阅读并同意
        self.page.get_element('view[class="check"]').tap()
        self.delay(3)

        # 确认发布
        self.page.get_element('view[class="resetConfirm--flex_1 resetConfirm--center resetConfirm--confirm"]', inner_text='确认发布').tap()

    def set_grzx(self):
        #个人中心
        self.page.get_element('//view[@class="success"]/view[3]/text[2]').tap()
        self.delay(3)
        return self