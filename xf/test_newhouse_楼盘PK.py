# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestNewhousePK(TestBase):
    """
    楼盘PK页面（南岸万星城市广场 住宅）
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/pkDetail/pkDetail?city=qz&id=68'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhousePK, self).setUp()

    def test_01_点击PK咨询底价(self):
        """
        V6.39.X: 点击PK部分的“咨询底价”按钮
        """
        self.find_element('view[class="im"]').tap()

        self.delay(4)
        self.get_screenshot()

    def test_02_点击支持TA(self):
        """
        V6.39.X: 点击 支持TA
        """
        try:
            self.find_element('view[class="button"][data-type="prj_one"]', inner_text='支持TA').tap()
            self.get_screenshot()
        except:
            self.get_screenshot('已经投过票了')

    def test_03_基本信息咨询底价(self):
        """
        V6.39.X: 点击 基本信息 咨询底价
        """
        self.find_element('view[class="im"]', inner_text='咨询底价').tap()

        self.delay(4)
        self.get_screenshot()

    def test_04_底部咨询底价(self):
        """
        V6.39.X: 点击 底部 咨询底价
        """
        self.page.scroll_to(1000, 300)
        self.delay(2)
        self.find_element('view[class="button"]', inner_text='咨询底价').tap()

        self.delay(4)
        self.get_screenshot()

    def test_05_从楼盘详情页进入PK后返回详情(self):
        """
        V6.39.X: 点击 楼盘进入楼盘详情页，再从楼盘详情页进入pk
        """
        url = '/page/newhouse/detail?pinyin=nananwanxingchengshiguangchang&city=qz'
        self.redirect_to_page(url=url)
        self.delay(3)
        self.find_element('view[class="infoWrap"][id="pk"]').tap()

        self.get_screenshot('进入pk页面')
        self.verifyPageName('/page/newhouse/pkDetail/pkDetail')

        # 返回到楼盘详情页
        self.back()
        self.get_screenshot()
        self.verifyPageName('/page/newhouse/detail')

