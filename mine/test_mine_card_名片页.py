# -*-coding:utf-8-*-
from base.test_mine import TestMine


class TestMineCard(TestMine):
    """
    置业顾问名片页
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestMineCard, cls).setUpClass()

        cls.g = globals()
        cls.g['phone'] = cls().get_phone()

        cls().change_zygw()
        print("setupclass change_zygw")

    def setUp(self) -> None:
        self.page_name = '/page/newhouse/zygw/detail?phone=%s'%self.g['phone']
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestMineCard, self).setUp()

    def test_01_card_im_卡片信息咨询(self):
        """
        V6.23.X: 卡片信息模块的“在线咨询”
        """
        self.find_element('view[class="tBtn-im flex tfAlignC tfFlexC"]').tap()

        self.delay(4)
        self.get_screenshot()

    def test_02_bottom_im_底部在线咨询(self):
        """
        V6.23.X: 底部“在线咨询”
        """
        self.find_element('view[class="bBtn-im flex tfAlignC tfFlexC"]').tap()

        self.delay(4)
        self.get_screenshot()

    def test_03_为我点赞(self):
        """
        V6.23.X: 点击“为我点赞”
        """
        self.find_element('view[class="mBtnBox zanBox flex tfFlexV tfFlexC"]').tap()

        self.get_screenshot()

    def test_04_生成海报(self):
        """
        V6.23.X: 点击“生成海报”
        """
        self.find_element('view[class="mBtnBox flex tfFlexV tfFlexC"]').tap()

        self.delay(2)
        self.get_screenshot()

    def test_05_添加微信(self):
        """
        V6.23.X: 点击“添加微信”
        """
        self.find_element('view[class="addwx flex tfAlignC tfFlexC"]').tap()

        self.delay(2)
        self.get_screenshot()

        # 设置跳转到其他置业顾问名片
        self.g['phone'] = self.other_zygw

    def test_06_为TA点赞(self):
        """
        V6.23.X: 点击“为TA点赞”
        """
        self.find_element('view[class="mBtnBox zanBox flex tfFlexV tfFlexC"]').tap()

        self.get_screenshot()

        # 设置跳回自己的置业顾问名片
        self.g['phone'] = self.get_phone()

    def test_12_分享名片(self):
        """
        V6.23.X: 点击“分享名片”
        """
        self.find_element('button[class="btn-tool bBtn-share"]').tap()

        self.get_screenshot()

    def test_10_card_call_卡片信息电话(self):
        """
        V6.23.X: 卡片信息模块的“在线咨询”
        """
        self.find_element('view[class="tBtn-tel flex tfAlignC tfFlexC"]').tap()

        self.get_screenshot()

    def test_11_bottom_call_底部拨打电话(self):
        """
        V6.23.X: 底部“在线咨询”
        """
        self.find_element('view[class="bBtn-tel flex tfAlignC tfFlexC"]').tap()

        self.get_screenshot()



