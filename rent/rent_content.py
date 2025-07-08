from base.test_base import TestBase
import pyautogui
import pyperclip

class ZufangContent(TestBase):
    def set_img(self):
        self.find_element('image[class="ic_camera"]').tap()
        self.delay(5)

        # self.page.get_element('view[class="center column upload"]', inner_text='上传视频').tap()
        # self.delay(3)

        self.find_element('view[class="center column upload"]/text', inner_text='上传图片').tap()
        self.delay(3)

        self.input_select_image(png='esf\\123.png')

        self.delay(2)
        self.find_element('view[class="center completeBtn"]').tap()

        self.delay(3)
        self.find_element('view[class="center noMorePics"]').tap()
        self.delay(3)
        return self

    def set_xqmc(self, xqmc='测试'):
        # 小区名称
        self.page.get_element('view[class="center column part"]/view').tap()
        self.delay(3)
        self.page.get_element('input[class="flex_1 input"]').input(xqmc)
        self.delay(3)
        item = self.page.get_elements('/view[2]/view/view')
        item[0].tap()
        self.delay(2)
        return self

    def set_huxing(self, huxing=[3, 2, 1]):
        # 户型
        self.find_element('view[class="center column partItem"][data-picker="1"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": huxing})
        self.delay(2)
        self.page.get_element('view[class="houseTypePicker--center houseTypePicker--confirm"]').tap()
        return self

    def set_chaoxiang(self, chaoxiang=[1]):
        # 朝向
        cfck = self.page.element_is_exists('view[class="center column partItem"][data-picker="2"]')
        if cfck == True:
            self.find_element('view[class="center column partItem"][data-picker="2"]').tap()
            self.delay(2)
            e = self.page.get_element('picker-view')
            self.delay(1)
            e.trigger("change", {"value": chaoxiang})
            self.delay(2)
            self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        else:
            ckcw = self.page.element_is_exists('view[class="flex_1 center column partItem"][data-picker="2"]')
            if ckcw == True:
                self.find_element('view[class="flex_1 center column partItem"][data-picker="2"]').tap()
                self.delay(2)
                e = self.page.get_element('picker-view')
                self.delay(1)
                e.trigger("change", {"value": chaoxiang})
                self.delay(2)
                self.page.get_element('view[class="selector--center selector--confirm"]').tap()
            else:
                print('没有朝向')
        return self

    def set_xzlxz(self, xzlxz=[1]):
        # 性质-写字楼
        self.find_element('view[class="center column partItem"][data-picker="15"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": xzlxz})
        self.delay(2)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        return self

    def set_spxz(self, spxz=[1]):
        # 商铺性质
        self.find_element('view[class="center column partItem"][data-picker="16"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": spxz})
        self.delay(2)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        return self

    def set_splx(self, splx=[2]):
        # 商铺类型
        self.find_element('view[class="center column partItem"][data-picker="17"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": splx})
        self.delay(2)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        return self

    def set_leibie(self, leibie=[1]):
        # 类别-写字楼
        self.page.get_element('view[class="between infoItem"][data-picker="11"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": leibie})
        self.delay(2)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        return self

    def set_louceng(self, louceng=[3, 3]):
        # 楼层
        cfcklc = self.page.element_is_exists('view[class="center column partItem"][data-picker="4"]')
        if cfcklc == True:
            self.find_element('view[class="center column partItem"][data-picker="4"]').tap()
            self.delay(2)
            e = self.page.get_element('picker-view')
            self.delay(1)
            e.trigger("change", {"value": louceng})
            self.delay(2)
            self.page.get_element('view[class="floorPicker--center floorPicker--confirm"]').tap()
            self.delay(3)
        else:
            ckcwlc = self.page.element_is_exists('view[class="flex_1 center column partItem"][data-picker="4"]')
            if ckcwlc == True:
                self.find_element('view[class="flex_1 center column partItem"][data-picker="4"]').tap()
                self.delay(2)
                e = self.page.get_element('picker-view')
                self.delay(1)
                e.trigger("change", {"value": louceng})
                self.delay(2)
                self.page.get_element('view[class="floorPicker--center floorPicker--confirm"]').tap()
                self.delay(3)
            else:
                print('没有楼层')
        return self

    def set_loudonghao(self, loudong="4", ckcwloudong='1'):
        # 楼栋号
        if ckcwloudong == '1':
            self.input_value_by_mk(png='rent/ckcwloudonghao.png', value=loudong)
        else:
            self.input_value_by_mk(png='rent/loudong.png', value=loudong)
        self.delay(5)
        return self

    def set_danyuan(self, danyuan="2", ckcwdanyuan='1'):
        # 单元号
        if ckcwdanyuan == '1':
            self.input_value_by_mk(png='rent/ckcwdanyuan.png', value=danyuan)
        else:
            self.input_value_by_mk(png='rent/danyuan.png', value=danyuan)
        self.delay(5)
        return self

    def set_shihao(self, shi="6", ckcwshi='1'):
        # 室号
        if ckcwshi == '1':
            self.input_value_by_mk(png='rent/ckcwshi.png', value=shi)
        else:
            self.input_value_by_mk(png='rent/shi.png', value=shi)
        self.delay(5)
        return self

    def set_zhuangxiu(self, zhuangxiu=[3]):
        # 装修
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('view[class="between infoItem"][data-picker="3"]').tap()
        self.delay(3)
        e = self.page.get_element('picker-view')
        e.trigger("change", {"value": zhuangxiu})
        self.delay(3)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        return self

    def set_area(self, area="90"):
        # 面积(整租）
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.find_element('view[class="between infoItem"][data-picker="6"]').tap()
        self.delay(5)
        self.input_value_by_mk(png='rent/area.png', value=area)
        self.delay(5)
        self.find_element('view[class="areaPicker--center areaPicker--confirm"]').tap()
        self.delay(5)
        return self

    def set_price(self, price="3000"):
        # 租金
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.find_element('view[class="between infoItem"][data-picker="7"]').tap()
        self.delay(5)
        self.input_value_by_mk(png='rent/price.png', value=price)
        self.delay(5)
        self.find_element('view[class="pricePicker--center pricePicker--type_map"]', inner_text='年付').tap()
        self.delay(5)
        self.find_element('view[class="pricePicker--center pricePicker--confirm"]').tap()
        self.delay(5)
        return self

    def set_qizuqi(self, qizuqi="1"):
        # 起租期
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.input_value_by_mk(png='rent/qizuqi.png', value=qizuqi)
        self.delay(5)
        return self

    def set_mianzuqi(self, mianzuqi="1"):
        # 面租期
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.input_value_by_mk(png='rent/mianzuqi.png', value=mianzuqi)
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
        # self.page.get_element('//scroll-view/view[3]/text').tap()
        # self.delay(3)
        self.page.get_element('view[class="rentItems--center rentItems--confirm"]').tap()
        self.delay(1)
        return self

    def set_zhuanrangfei(self, zhuanrangfei="5000"):
        # 转让费
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.input_value_by_mk(png='rent/zhuanrangfei.png', value=zhuanrangfei)
        self.delay(5)
        return self

    def set_wuyefei(self, wuyefei="1.9"):
        # 物业费
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.input_value_by_mk(png='rent/wuyefei.png', value=wuyefei)
        self.delay(5)
        return self

    def set_zhucegongnsi(self, zhucegongnsi=[1]):
        # 可注册公司-写字楼
        self.page.get_element('view[class="between infoItem"][data-picker="12"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": zhucegongnsi})
        self.delay(2)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()

    def set_kefenge(self, kefenge=[1]):
        # 可分割-写字楼
        self.page.get_element('view[class="between infoItem"][data-picker="13"]').tap()
        self.delay(2)
        e = self.page.get_element('picker-view')
        self.delay(1)
        e.trigger("change", {"value": kefenge})
        self.delay(2)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()

    def set_linjie(self, linjie=[1]):
        # 临街
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('view[class="between infoItem"][data-picker="14"]').tap()
        self.delay(5)
        e = self.page.get_element('picker-view')
        e.trigger("change", {"value": linjie})
        self.delay(5)
        self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        return self

    def set_xiayibu(self):
        # 下一步
        self.delay(3)
        self.page.get_element('//resetConfirm/view/view/view[2]').tap()
        self.delay(3)
        # 重置
        self.set_result()
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
        return self

    def set_spfwpz(self):
        # 房屋配置-商铺
        self.page.get_element('view[class="center option"][data-equipment="客梯"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-equipment="空调"]').tap()
        return self

    def set_fwld(self):
        # 房屋亮点
        self.page.get_element('view[class="center option"][data-special="电梯房"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-special="南北通透"]').tap()
        # self.delay(2)
        # self.page.get_element('view[class="center option"][data-special="交通便利"]').tap()
        # self.delay(2)
        # self.page.get_element('view[class="center option"][data-special="拎包入住"]').tap()
        return self

    def set_czyq(self):
        # 出租要求
        self.page.get_element('view[class="center option"][data-condition="一家人"]').tap()
        self.delay(2)
        self.page.get_element('view[class="center option"][data-condition="一年起租"]').tap()
        # self.delay(2)
        # self.page.get_element('view[class="center option"][data-condition="租户稳定"]').tap()
        # self.delay(2)
        # self.page.get_element('view[class="center option"][data-condition="禁止养宠物"]').tap()
        return self

    def set_desc(self, fyms='房源描述好房好房好房好房房源描述'):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 房源描述
        self.page.get_element('view[class="pr desc"]').tap()
        self.delay(3)
        pyperclip.copy(fyms)
        self.delay(3)
        self.input_value_by_mk(png='rent/fyms.png', value=fyms, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(3)
        self.page.get_element('view[class="center confirm"]').tap()
        return self

    def set_hym(self, heyanma="NJZ220929123456"):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 核验码
        # self.page.get_element('//view[@class="between hyCode"]/input')
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
        self.page.scroll_to(1200, 500)
        self.delay(1)
        # 联系人
        pyperclip.copy(name)
        self.delay(3)
        try:
            self.input_value_by_mk(png='rent/name.png', value=name, direction=1)
        except:
            self.input_value_by_mk(png='rent/name-zz.png', value=name, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        return self

    def set_cfckname(self, name='赵测试厂房仓库'):
        self.page.scroll_to(800, 500)
        self.delay(1)
        # 联系人
        pyperclip.copy(name)
        self.delay(3)
        self.input_value_by_mk(png='rent/cfckname.png', value=name, direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        return self

    def set_renzheng(self, zjlx=[2], zjhm='0000000000', qqh='1111111111', cqrxm='赵赵赵', cqrsfzh='320520199001021111'):
        # 房屋权属信息-去认证
        # delete
        return
        self.page.get_element('view[class="center ownershipCertificate"]', inner_text='去认证').tap()
        self.delay(5)
        self.set_result()
        # # 证件类型 delete 2024.4.1
        # self.page.get_element('/view/view/view[2]').tap()
        # self.delay(5)
        # e = self.page.get_element('picker-view')
        # e.trigger("change", {"value": zjlx})
        # self.delay(5)
        # self.page.get_element('view[class="selector--center selector--confirm"]').tap()
        # self.delay(10)
        # # 证件号码
        # self.input_value_by_mk(png='rent/zjhm.png', value=zjhm, direction=1)
        # self.delay(5)

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
        self.input_value_by_mk(png='rent/cqrsfzh.png', value=cqrsfzh, direction=1)
        self.delay(5)
        # 证件照上传
        self.page.get_element('view[class="center column uploadBtn"]', inner_text="添加照片").tap()
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
        self.page.get_element('view[class="resetConfirm--flex_1 resetConfirm--center resetConfirm--confirm"]',
                              inner_text='确认发布').tap()

    def set_grzx(self):
        # 个人中心
        self.page.get_element('//view[@class="success"]/view[3]/text[2]').tap()
        self.delay(3)
        return self

    def set_result(self):
        # 重置
        result = {"confirm": True}
        self.app.mock_wx_method("showModal", result=result)
        self.page.get_element('//resetconfirm/view/view/view').tap()
        self.app.restore_wx_method("showModal")
        self.delay(3)
        return self