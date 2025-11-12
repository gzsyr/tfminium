# -*-coding:utf-8-*-
import pytest

from base.test_base import TestBase


class TestNewhousePKCP(TestBase):
    """
    楼盘PK与测评页面（南岸万星城市广场 住宅）
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/detail?pinyin=nananwanxingchengshiguangchang&city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhousePKCP, self).setUp()

    def goto_pk(self):
        """
        进入PK页面
        """
        self.delay(3)
        self.find_element('view[class="infoWrap"][id="pk"]').tap()
        self.delay(6)

    @pytest.mark.im_consult
    def test_PK_01_点击PK咨询底价(self):
        """
        V6.39.X: 点击PK部分的“咨询底价”按钮
        """
        self.goto_pk()
        self.delay(2)
        self.find_element('view[class="im"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()
        self.verifyPageParams('chatTo', 'slwkgj_9584')

    def test_PK_02_点击支持TA(self):
        """
        V6.39.X: 点击 支持TA
        """
        self.goto_pk()

        try:
            self.find_element('view[class="button"][data-type="prj_one"]', inner_text='支持TA').tap()
            self.get_screenshot()
        except:
            self.get_screenshot('已经投过票了')

    @pytest.mark.im_consult
    def test_PK_03_基本信息咨询底价(self):
        """
        V6.39.X: 点击 基本信息 咨询底价
        """
        self.goto_pk()

        self.find_element('view[class="im"]', inner_text='咨询底价').tap()


        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()
        self.verifyPageParams('chatTo', 'slwkgj_9584')

    @pytest.mark.im_consult
    def test_PK_04_底部咨询底价(self):
        """
        V6.39.X: 点击 底部 咨询底价
        """
        self.goto_pk()
        self.delay(2)
        self.page.scroll_to(1000, 300)
        self.delay(2)
        self.find_element('view[class="button"]', inner_text='咨询底价').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()
        self.verifyPageParams('chatTo', 'slwkgj_9584')

    def test_PK_05_进入PK后返回详情(self):
        """
        V6.39.X: 点击 楼盘进入楼盘详情页，再从楼盘详情页进入pk
        """
        self.find_element('view[class="infoWrap"][id="pk"]').tap()

        self.get_screenshot('进入pk页面')
        self.verifyPageName('/page/newhouse/pkDetail/pkDetail')

        # 返回到楼盘详情页
        self.back()
        self.get_screenshot()
        self.verifyPageName('/page/newhouse/detail')

    def goto_cp(self):
        """
        点击测评，进入测评页面
        """
        self.page.scroll_to(3000, 200)
        self.delay(3)
        self.find_element('view[class="check-more"]').tap()

    def test_CP_01_点击测评后返回详情(self):
        """
        V6.40.X: 点击测评
        """
        self.goto_cp()

        self.get_screenshot('进入测评')
        self.verifyPageName('/page/newhouse/evaluation/evaluation')
        self.back()
        self.get_screenshot()
        self.verifyPageName('/page/newhouse/detail')

    @pytest.mark.im_consult
    def test_CP_02_点击咨询和拨打电话(self):
        """
        V6.40.X: 点击咨询
        """
        self.goto_cp()
        self.delay(7)
        self.find_element('view[class="button positionRel"]', inner_text='在线咨询\n隐私保护').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot('点击咨询')
        self.verifyPageParams('chatTo', 'slwkgj_9584')

        self.back()
        self.find_element('view[class="button positionRel"]', inner_text='拨打电话\n免费').tap()
        self.get_screenshot('拨打电话')

    def test_CP_04_点击户型(self):
        """
        V6.40.x: 点击户型
        """
        self.goto_cp()

        self.get_screenshot()