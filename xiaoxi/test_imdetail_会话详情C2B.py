from ddt import ddt, file_data

from tfq.writepost import WritePost

@ddt
class TestImdetail(WritePost):
    """
    IM会话详情C2B
    """

    @classmethod
    def setUpClass(cls) -> None:
        super(TestImdetail, cls).setUpClass()
        cls().change_C()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/im/pages/chating/chating?chatTo=slwkgj_6544&city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestImdetail, self).setUp()
        print("TestZygwWritePost setup")

    def test_01_addweixin_添加微信(self):
        # 点击添加微信-复制微信号
        e = self.find_elements('view[class="btn"]')
        e[1].tap()
        self.delay(3)
        # 复制微信号
        self.find_element('view[class="content-card-b-btn copywxnum"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_02_addsaoma_扫码直接添加(self):
        # 点击扫码直接添加
        e = self.find_element('view[class="content-card-b-btn copywxcode"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_03_clickname_点击置业顾问姓名(self):
        # 点击上方置业顾问姓名
        self.page.get_element('view[class="name"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_04_clicklpmc_点击楼盘名称(self):
        # 点击上方楼盘名称
        self.page.get_element('view[class="lpInf flex tfAlignC"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_05_clickhrzx_点击换人咨询(self):
        # 点击换人咨询
        self.page.get_element('view[class="hrzx flex tfAlignC"]').tap()
        self.delay(3)
        try:
            e = self.page.get_elements('button[class="zyList_li_r_im"]')
            e[0].tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有换人咨询列表')

    def test_06_clickwypj_点击我要评价(self):
        # 点击我要评价
        self.page.get_element('view[class="btn pjBtn flex tfAlignC"]').tap()
        self.delay(3)
        self.get_screenshot()
        # 点击一颗心
        try:
            self.page.get_element('view[class="item"][data-index="0"]').tap()
            self.delay(2)
            # 点击提交
            self.page.get_element('view[class="submitpj"]').tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('评价机会已用完')

    def test_07_clickcyy_点击常用语(self):
        # 点击常用语
        self.page.get_element('view[class="btn kjhfBtn flex tfAlignC"]').tap()
        self.delay(2)
        # 点击第一条用语
        self.page.get_element('view[class="kjhfList"]').get_element('view').tap()
        self.delay(3)
        self.get_screenshot()

    def test_08_clickwytw_点击我要提问(self):
        """
        v6.48.x: update
        """
        # 点击我要提问
        self.find_element('image[class="chatinput-img fr"]').tap()
        self.find_element('view[class="more-subcontent-item"]/text', inner_text='我要提问').tap()
        self.delay(2)
        # 选择一条消息
        self.page.get_element('checkbox[class="checkbox"]').tap()
        self.delay(3)
        # 点击去提问
        self.page.get_element('view[class="toask"]').tap()
        self.delay(3)
        # 点击发布
        self.page.get_element('button[class="submit-btn"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_09_clickyuying_点击语音按钮(self):
        # 点击发送语音按钮
        self.page.get_element('image[class="chatinput-img"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_10_clickfzwx_点击复制微信(self):
        # 点击引导联系卡片的【复制微信】
        e = self.page.get_elements('view[class="content-card-b"]')
        e[0].tap()
        self.delay(3)
        self.get_screenshot()

    def test_11_clicktjwx_扫码添加微信(self):
        # 点击引导联系卡片的【扫码添加微信】
        e = self.page.get_element('view[class="content-card-b"][data-kind="auto_addwx"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_12_clickzyhwtel_置业顾问给我回电(self):
        # 点击引导联系卡片的【让置业顾问给我回电】
        e = self.page.get_element('view[class="content-card-b"]', inner_text='让置业顾问给我回电')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_13_clickqunliao_加入群聊链接(self):
        # 点击加入群聊卡片的【加入群聊链接】
        e = self.page.get_element('view[class="content-card-b flex tfAlignC tfFlexC"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_14_clickbqb_表情包按钮(self):
        # 点击表情包按钮
        e = self.page.get_element('image[class="chatinput-emoji"]')
        e.tap()
        self.delay(2)
        e1 = self.page.get_elements('view[class="emojiWrap"]')
        e1[0].tap()
        self.delay(3)
        self.get_screenshot()

    def test_15_clicklsxx_历史消息(self):
        # 点击历史消息按钮
        e = self.find_element('view[class="historychat"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_16_clicktel_拨打电话(self):
        # 点击引导联系卡片的【拨打电话】
        e = self.page.get_element('view[class="content-card-b"]', inner_text='拨打电话')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_17_addtel_拨打电话(self):
        # 点击拨打电话
        e = self.page.get_elements('view[class="btn"]')
        e[0].tap()
        self.delay(3)
        self.get_screenshot()
