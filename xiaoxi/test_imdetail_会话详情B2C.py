import pyautogui
import pyperclip
from ddt import ddt, file_data

from tfq.writepost import WritePost

@ddt
class TestImdetailCB(WritePost):
    """
    IM会话详情B2C
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestImdetailCB, cls).setUpClass()
        cls().change_zygw()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/im/pages/chating/chating?chatTo=tf_1127301&city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestImdetailCB, self).setUp()
        print("TestZygwWritePost setup")

    def test_16_发送资料(self):
        """
        V6.48.X: 发送资料
        """
        self.find_element('view[class="gfzlBtn flex tfAlignC"]').tap()
        self.delay(3)
        self.get_screenshot('open')

        self.find_element('image[class="img"]').tap()
        self.delay(2)
        self.get_screenshot('view')

        self.back()

        self.find_element('view[class="tfFlex tfAlignC tfFlexC chat"]').tap()
        self.get_screenshot('send')

    def test_15_点击跟进客户(self):
        """
        V6.42.X: 点击 跟进客户
        """
        self.find_element('view[class="btn"]/view', inner_text='跟进客户').tap()
        self.get_screenshot()
        self.verifyPageName('/page/business/zygwinfomanage/followAdd')

    def test_01_clicktouxiang_用户头像(self):
        # 点击上方C端用户头像
        e = self.page.get_element('image[class="avatar"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_02_clickzdhf_去设置自动回复(self):
        # 点击【去设置自动回复，不错过任何消息】
        try:
            e = self.page.get_element('view[class="chatTips flex tfAlignC tfFlexSb"]')
            e.tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print("设置自动回复已X掉")

    def test_03_clickcyy_常用语(self):
        # 点击常用语
        e = self.page.get_element('view[class="kjhfBtn flex tfAlignC"]')
        e.tap()
        self.delay(2)
        # 点击新增常用语
        self.page.get_element('view[class="addkjhf flex tfAlignC"]').tap()
        self.delay(2)
        # 输入常用语
        pyperclip.copy('哈哈哈哈哈哈哈好好好好')
        self.delay(3)
        self.input_value_by_mk(png='xiaoxi/changyongyu.png', value='哈哈哈哈哈哈哈好好好好', direction=1)
        self.delay(5)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(3)
        # 点击保存
        self.page.get_element('//form/button').tap()
        self.delay(3)
        self.get_screenshot()

    def test_04_clickcyygl_常用语管理新增(self):
        # 点击常用语
        e = self.page.get_element('view[class="kjhfBtn flex tfAlignC"]')
        e.tap()
        self.delay(3)
        # 点击管理
        self.page.get_element('view[class="glkjhf"]').tap()
        self.delay(3)
        # 点击新增常用语
        self.page.get_element('button[class="addBtn zygwBtn"]').tap()
        self.delay(3)
        # 输入常用语
        pyperclip.copy('呜呜呜呜呜呜呜呜无')
        self.delay(3)
        self.input_value_by_mk(png='xiaoxi/changyongyu.png', value='呜呜呜呜呜呜呜呜无', direction=1)
        self.delay(3)
        pyautogui.hotkey('Ctrl', 'V')
        self.delay(3)
        # 点击保存
        self.page.get_element('//form/button').tap()
        self.delay(3)
        self.get_screenshot()

    def test_05_clickcyygl_常用语管理编辑(self):
        # 点击常用语
        e = self.page.get_element('view[class="kjhfBtn flex tfAlignC"]')
        e.tap()
        self.delay(2)
        # 点击管理
        self.page.get_element('view[class="glkjhf"]').tap()
        self.delay(3)
        # 点击编辑常用语
        e = self.page.get_elements('image[class="edit_img"]')
        e[0].tap()
        self.delay(3)
        # 输入常用语
        self.page.get_element('textarea').input('woowowo我我哦我我')
        self.delay(3)
        # 点击保存
        self.page.get_element('//form/button').tap()
        self.delay(3)
        self.get_screenshot()

    def test_06_clickcyydel_常用语删除(self):
        # 点击常用语
        e = self.page.get_element('view[class="kjhfBtn flex tfAlignC"]')
        e.tap()
        self.delay(3)
        # 点击管理
        self.page.get_element('view[class="glkjhf"]').tap()
        self.delay(3)
        # 点击删除常用语
        result = {"confirm": True}
        self.app.mock_wx_method("showModal", result=result)
        e = self.page.get_elements('image[class="delete_img"]')
        e[0].tap()
        self.app.restore_wx_method("showModal")
        self.delay(3)
        self.get_screenshot()

    def test_07_clickcyyfasong_常用语发送(self):
        # 点击常用语
        e = self.page.get_element('view[class="kjhfBtn flex tfAlignC"]')
        e.tap()
        self.delay(2)
        e1 = self.page.get_element('view[class="kjhfList"]').get_element('view')
        e1.tap()
        self.delay(3)
        self.get_screenshot()

    def test_08_clickwytw_点击我要提问(self):
        # 点击我要提问
        self.find_element('image[class="chatinput-img fr"]').tap()
        self.find_element('view[class="more-subcontent-item"]/text', inner_text='我要提问').tap()
        self.delay(2)
        # 选择一条消息
        self.page.get_element('checkbox[class="checkbox"]').tap()
        self.delay(2)
        # 点击去提问
        self.page.get_element('view[class="toask"]').tap()
        self.delay(5)
        # 点击发布
        self.page.get_element('button[class="submit-btn"]').tap()
        self.get_screenshot()

    def test_09_clickwytw_点击我要提问取消(self):
        # 点击我要提问
        self.find_element('image[class="chatinput-img fr"]').tap()
        self.find_element('view[class="more-subcontent-item"]/text', inner_text='我要提问').tap()
        self.delay(2)
        # 选择一条消息
        self.page.get_element('checkbox[class="checkbox"]').tap()
        self.delay(2)
        # 点击取消
        self.page.get_element('view[class="cancel"]').tap()
        self.get_screenshot()

    def test_10_clickkfyq_点击看房邀请(self):
        # 点击看房邀请
        # self.find_element('view[class="kfBtn flex tfAlignC"]').tap()
        self.page.get_element('image[class="chatinput-img fr"]').tap()
        self.delay(2)
        # 点击发送位置
        self.page.get_element('text[class="text"]', inner_text='看房邀请').tap()
        self.delay(2)
        # 选择看房日期
        e = self.page.get_elements('picker')
        e[0].tap()
        e[0].pick('2022-12-10')
        self.delay(2)
        # 选择看房时间
        e1 = self.page.get_elements('picker')
        e1[1].tap()
        e1[1].pick('18:00')
        self.delay(3)
        self.get_screenshot()
        # 点击确定
        self.page.get_element('view[class="confirm"]').tap()
        self.delay(2)
        # 点击确定
        self.page.get_element('view[class="confirm"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_14_clickmap_点击发送位置(self):
        # 点击右下角更多图标
        self.page.get_element('image[class="chatinput-img fr"]').tap()
        self.delay(2)
        # 点击发送位置
        self.page.get_element('text[class="text"]', inner_text='发送位置').tap()
        self.delay(3)
        self.get_screenshot()

    def test_12_clickyqzd_邀请卡片立即致电(self):
        # 邀请卡片中的立即致电
        self.page.get_element('view[class ="content-card-b flex tfAlignC tfFlexC"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_13_addtel_拨打电话(self):
        # 点击拨打电话
        e = self.page.get_elements('view[class="btn"]')
        e[0].tap()
        self.delay(3)
        self.get_screenshot()

    def test_11_clickyqzd_邀请致电(self):
        # 点击邀请致电
        self.page.get_element('view[class="btn"]', inner_text='邀请致电').tap()
        self.delay(3)
        self.page.get_element('view[class="content-card-b flex tfAlignC tfFlexC"]').tap()
        self.delay(3)
        self.get_screenshot()
