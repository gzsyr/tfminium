from ddt import ddt, file_data
from base.test_base import TestBase

import pyautogui
import pyperclip

@ddt
class Testesfsellfb(TestBase):
    """
    发布出售
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/publish/sell/first/first?infoType=1&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfsellfb, self).setUp()
        print("Testesfsellfb setup")

    @file_data('./test_esf_fabu.yml')
    def test_publish_sell_发布出售(self, **kwargs):
        """
        发布出售
        :param kwargs:
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
        # 期望价格
        self.set_price(kwargs['price'])
        # 建筑年代
        self.set_year(kwargs['year'])
        # 下一步
        self.set_xiayibu()
        self.delay(5)
        self.get_screenshot()
        self.delay(3)
        # 房源标题
        self.set_title(kwargs['title'])
        # 核验码
        self.set_hym(kwargs['heyanma'])
        # 房源特色
        self.set_fyts()
        # 房源描述
        self.set_desc(kwargs['fyms'])
        # 联系人
        self.set_name(kwargs['name'])
        # 去认证
        self.set_renzheng(kwargs['zjlx'], kwargs['zjhm'], kwargs['cqrxm'], kwargs['cqrsfzh'])
        self.delay(5)
        self.get_screenshot()
        self.delay(3)
        # 发布
        self.set_fabu()
        self.delay(5)
        self.get_screenshot()
        self.delay(3)
        # 个人中心
        self.set_grzx()

    def set_img(self):
        # 上传图片
        self.page.get_element('//step_1head//text', inner_text="上传图片").tap()
        self.delay(2)

        self.page.get_element('view[class="center flex_column upload"]').tap()
        self.delay(3)

        self.input_select_image(png='esf\\123.png')

        self.delay(2)
        self.page.get_element('view[class="center completeBtn"]').tap()

        self.delay(3)
        self.page.get_element('view[class="center noMorePics"]').tap()
        return self

    def test_set_xqmc(self, xqmc='测试'):
        # 小区名称
        self.page.get_element('/view[2]/view[2]/view/view/view[2]').tap()
        self.delay(3)
        self.page.get_element('input[class="flex_1 input"]').input(xqmc)
        self.delay(3)
        item = self.page.get_elements('/view[2]/view/view')
        item[0].tap()
        self.delay(2)
        return self

    def set_huxing(self, huxing=[3, 2, 1]):
        # 户型
        self.page.get_element('//view[@class="basic-info"]/view[2]/view').tap()
        self.delay(2)
        e = self.page.get_element('picker-view[class="picker-view"]')
        e.trigger("change", {"value": huxing})
        self.delay(2)
        self.page.get_element('/view[2]/view[5]/view/view/view[2]').tap()
        return self

    def set_chaoxiang(self, chaoxiang=[1]):
        # 朝向
        self.page.get_element('//view[@class="basic-info"]/view[2]/view[3]/view[2]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view[class="picker-view"]')
        e.trigger("change", {"value": chaoxiang})
        self.delay(2)
        self.page.get_element('/view[2]/view[5]/view/view/view[2]').tap()
        return self

    def set_louceng(self, louceng=[3, 3]):
        # 楼层
        self.page.get_element('//view[@class="basic-info"]/view[2]/view[5]/view[2]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view[class="picker-view"]')
        e.trigger("change", {"value": louceng})
        self.delay(2)
        self.page.get_element('/view[2]/view[5]/view/view/view[2]').tap()
        self.delay(3)
        return self

    def set_loudonghao(self, loudong="4"):
        # 楼栋号
        self.input_value_by_mk(png='esf/loudong.png', value=loudong)
        self.delay(3)
        return self

    def set_danyuan(self, danyuan="2"):
        # 单元号
        self.input_value_by_mk(png='esf/danyuan.png', value=danyuan)
        self.delay(3)
        return self

    def set_shihao(self, shi="6"):
        # 室号
        self.input_value_by_mk(png='esf/shi.png', value=shi)
        self.delay(3)
        return self

    def set_zhuangxiu(self, zhuangxiu=[3]):
        # 装修
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('//view[@class="basic-info"]/view[5]/view[2]/view[2]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view[class="picker-view"]')
        e.trigger("change", {"value": zhuangxiu})
        self.delay(2)
        self.page.get_element('/view[2]/view[5]/view/view/view[2]').tap()
        return self

    def set_area(self, area="90"):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 面积
        self.input_value_by_mk(png='esf/area.png', value=area)
        self.delay(1)
        return self

    def set_price(self, price="300"):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 期望价格
        self.input_value_by_mk(png='esf/price.png', value=price)
        self.delay(1)
        return  self

    def set_year(self, year="300"):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 建筑年代
        self.page.get_element('//view[@class="basic-info"]/view[5]/view[5]/input').input(year)
        #self.input_value_by_mk(png='esf/year.png', value=kwargs['year'])
        self.delay(1)
        return self

    def set_xiayibu(self):
        # 下一步
        self.page.get_element('view[class="next"]').tap()
        self.delay(3)
        return self

    def set_title(self, title='测试小区好房出售'):
        #self.delay(3)
        #self.set_xiayibu()
        # 房源标题
        self.page.get_element('/view[2]/view[2]/input').input(title)
        self.delay(1)
        return self

    def set_hym(self, heyanma="NJS220929123456"):
        # 核验码
        # self.page.get_element('/view[2]/view[2]/view[2]/view[2]')
        self.input_value_by_mk(png='esf/heyanma.png', value=heyanma, direction=1)
        self.delay(1)
        return self

    def set_fyts(self):
        # 房源特色
        self.page.get_element('view[class="feat-item"][data-index="0"]').tap()
        self.delay(1)
        self.page.get_element('view[class="feat-item"][data-index="8"]').tap()
        self.delay(1)
        self.page.get_element('view[class="feat-item"][data-index="15"]').tap()
        self.delay(1)
        return self

    def set_desc(self, fyms='房源描述好房好房好房好房房源描述'):
        # 房源描述
        self.page.get_element('/view[2]/view[2]/view[7]/text').tap()
        self.delay(3)
        pyperclip.copy(fyms)
        self.delay(3)
        self.input_value_by_mk(png='esf/fyms.png', value=fyms, direction=1)
        self.delay(3)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(3)
        self.page.get_element('view[class="center confirm"]').tap()
        return self

    def set_name(self, name='赵赵测试'):
        # 联系人
        self.page.scroll_to(800, 500)
        self.delay(1)
        pyperclip.copy(name)
        self.delay(3)
        self.input_value_by_mk(png='esf/name.png', value=name, direction=1)
        self.delay(3)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(3)
        return self

    def set_renzheng(self, zjlx=[2], zjhm='0000000000', cqrxm='赵赵赵', cqrsfzh='111111111111111'):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 房屋权属信息-去认证
        self.page.get_element('/view[2]/view[5]/view[2]').tap()
        self.delay(3)
        # 证件类型
        self.page.get_element('/view/view[2]').tap()
        self.delay(5)
        e = self.page.get_element('picker-view[class="picker-view"]')
        e.trigger("change", {"value": zjlx})
        self.delay(5)
        self.page.get_element('//view[@class="pa picker"]/view/view[2]').tap()
        # 证件号码
        self.delay(5)
        self.input_value_by_mk(png='esf/zjhm.png', value=zjhm, direction=1)
        self.delay(6)
        # 产权人姓名
        pyperclip.copy(cqrxm)
        self.delay(5)
        self.input_value_by_mk(png='esf/cqrxm.png', value=cqrxm, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(5)
        # 产权人身份证号
        # self.input_value_by_mk(png='esf/cqrsfzh.png', value=cqrsfzh, direction=1)
        # self.delay(5)
        # 证件照上传
        # 房屋证件
        self.page.get_element('view[class="add-pic"][data-type="house_credit_image"]').tap()
        self.delay(5)
        self.input_select_image(png='esf\\123.png')
        self.delay(5)
        # 房主身份证
        self.page.get_element('view[class="add-pic"][data-type="id_card_credit_image"]').tap()
        self.delay(5)
        self.input_select_image(png='esf\\123.png')
        self.delay(5)
        # 其他类型证件
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('view[class="add-pic"][data-type="owner_pics"]').tap()
        self.delay(5)
        self.input_select_image(png='esf\\123.png')
        self.delay(5)
        # self.page.get_element('view[class="resetConfirm--flex_1 resetConfirm--center resetConfirm--confirm"]').tap()

        # 完成
        self.page.get_element('/view[@class="pf bottom"]/view/view[2]').tap()
        self.delay(5)
        return self

    def set_fabu(self):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # self.set_xiayibu()
        #点击我已阅读并同意
        # self.page.get_element('/view[2]/view[6]/view').tap()
        self.page.get_element('view[class="unchecked"]').tap()
        self.delay(3)

        #确认发布
        self.page.get_element('/view[2]/view[8]/view/view[2]').tap()
        return self

    def set_grzx(self):
        # 个人中心
        self.page.get_element('//view[@class="success"]/view[3]/text[2]').tap()
        self.delay(3)
        return self





