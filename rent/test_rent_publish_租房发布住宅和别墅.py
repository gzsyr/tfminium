from ddt import ddt, file_data
from base.test_base import TestBase

from rent.rent_content import ZufangContent
import pyautogui
import pyperclip
@ddt
class Testrentfb(ZufangContent):
    """
    租房发布
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/publish/index/index?publishType=rent&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentfb, self).setUp()
        print("Testrentfb setup")

    def set_rentxqmc_小区名称自定义(self):
        """
        小区名称（自定义）
        :return:
        """
        self.page.get_element(f'view[class="between houseType"][data-type="1"]').tap()
        self.delay(3)
        self.page.get_element('/view/view[2]/view').tap()
        self.delay(3)
        self.page.get_element('input[class="flex_1 input"]').input('自定义')
        self.delay(3)
        # 点击去添加
        self.page.get_element('view[class="flex justify_between align_center add-block"]').tap()
        self.delay(3)
        # 添加页
        # 自定义小区名称
        pyperclip.copy('自定义')
        self.delay(5)
        self.input_value_by_mk(png='esf/zdyxqmc.png', value='自定义', direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(3)
        #区属板块
        self.page.get_element('/view[3]/view[2]').tap()
        self.delay(5)
        e = self.page.get_element('picker-view[class="picker-view"]')
        e.trigger("change", {"value": [1, 1]})
        self.delay(3)
        self.page.get_element('view[class="confirm"]' ,inner_text='确定').tap()
        # 地址
        pyperclip.copy('测试勿扰啊')
        self.delay(5)
        self.input_value_by_mk(png='esf/zdydz.png', value='测试勿扰啊', direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(3)
        # 提交
        self.page.get_element('view[class="submit"]', inner_text='提交').tap()
        self.delay(5)
        self.get_screenshot()
        self.delay(3)

    @file_data('./test_rent_publish.yml')
    def test_publish_sell_发布出租(self, **kwargs):
        """
        发布出租
        :param kwargs:
        :return:
        """
        self.page.get_element(f'view[class="between houseType"][data-type="{kwargs["datatype"]}"]').tap()
        self.delay(3)
        # 重置
        self.set_result()
        # 输入内容
        self.rent_content(kwargs)
        self.delay(3)
        self.get_screenshot()

    def rent_content(self, kwargs):
        """
        填写租房发布内容
        :return:
        """
        # 小区名称
        self.set_xqmc(kwargs['xqmc'])
        # 户型
        self.set_huxing(kwargs['huxing'])
        # 朝向
        self.set_chaoxiang(kwargs['chaoxiang'])
        # 楼层
        self.set_louceng(kwargs['louceng'])
        # 楼栋号
        self.set_loudonghao(kwargs['loudong'], ckcwloudong=kwargs['ckcwloudong'])
        # 单元号
        self.set_danyuan(kwargs['danyuan'], ckcwdanyuan=kwargs['ckcwdanyuan'])
        # 室号
        self.set_shihao(kwargs['shi'], ckcwshi=kwargs['ckcwshi'])
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
        # 核验码#delete 2024.4.2
        # self.set_hym(kwargs['heyanma'])
        # 看房时间
        self.set_kanfangtime(kwargs['kanfangtime'])
        # 入住时间
        self.set_ruzhutime(kwargs['ruzhutime'])
        # 联系人
        self.set_name(kwargs['name'])
        # 房屋权属信息-去认证
        self.set_renzheng(kwargs['zjlx'], kwargs['zjhm'], kwargs['qqh'], kwargs['cqrxm'], kwargs['cqrsfzh'])

        # 上传图片
        self.set_img()

        self.get_screenshot()
        self.delay(3)
        # 发布
        self.set_fabu()
        self.get_screenshot()
        # 个人中心
        # self.set_grzx()

    # def test_set_fwpz(self):
    #     self.page.get_element(f'view[class="between houseType"][data-type="1"]').tap()
    #     self.delay(3)
    #     self.set_xiayibu()
    #     # 房屋配置
    #     self.page.get_element('view[class="center option"][data-equipment="床"]').tap()
    #     self.delay(2)
    #     self.page.get_element('view[class="center option"][data-equipment="热水器"]').tap()
    #     self.delay(2)
    #     self.page.get_element('view[class="center option"][data-equipment="可做饭"]').tap()
    #     self.delay(2)
    #     self.page.get_element('view[class="center option"][data-equipment="独立卫生间"]').tap()
    #     return self