# add by zsy 2023.10.10
from base.test_base import TestBase


class TestesfXxxq(TestBase):
    """
    学校详情页
    """
    def setUp(self) -> None:
        self.page_name = '/esf/sell/pages/schoolDetail/schoolDetail?city=nj&id=90'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestesfXxxq, self).setUp()

    def test_01_点击学校地址(self):
        """
        V6.42.X: 点击学校地址
        """
        self.find_element('view[class="info-info--flex info-info--a_s info-info--p024 info-info--address"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/publicPages/map/map')

    def test_02_点击纠错按钮(self):
        """
        V6.42.X: 点击纠错功能
        """
        self.find_element('view[class="info-info--pa info-info--center info-info--correctError"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/mine/wtfk/wtfk')

    def test_03_咨询学校详细信息(self):
        """
        V6.42.X: 点击咨询学校详细信息
        """
        self.delay(2)
        self.find_element('view[class="info--center info--chat"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_04_学校话题查看(self):
        """
        V6.42.X: 点击学校话题，查看详情
        """
        self.find_element('view[class="schoolTopic--center schoolTopic--check"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')

    def test_05_周边配套查看(self):
        """
        V6.42.X: 点击 周边配套查看
        """
        self.find_element('view[class="zbpt--center zbpt--checkClick"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/publicPages/map/map')

    def test_06_咨询周边配套(self):
        """
        V6.42.X: 点击咨询周边配套
        """
        self.find_element('view[class="zbpt--center zbpt--chat"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_07_热门咨询提问(self):
        """
        V6.42.X: 点击热门咨询快捷提问
        """
        self.find_element('view[class="hotConsult--flex_1 hotConsult--line_1"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_08_点击划片范围(self):
        """
        V6.42.X: 点击划片范围
        """
        self.find_element('view[class="hpfw--p024 hpfw--schoolBlockRange"]').tap()

        self.delay(5)
        self.get_screenshot()
        self.verifyPageName('/page/publicPages/xxdt/xxdt')

    def test_09_咨询划片范围(self):
        """
        V6.42.X: 点击咨询划片范围
        """
        self.find_element('view[class="hpfw--center hpfw--chat"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_10_划片小区更多(self):
        """
        V6.42.X: 点击划片小区更多
        """
        self.find_element('view[class="hpxq--center hpxq--checkClick"]').tap()
        self.delay(5)
        self.get_screenshot('进入划片小区列表页面')
        self.verifyPageName('/esf/sell/pages/schoolBlockList/schoolBlockList')
        
        self.find_elements('view[class="villageItem--pr villageItem--village_item_img"]')[1].tap()
        self.delay(3)
        self.get_screenshot('列表页点击进入小区详情页')
        self.back()

        self.find_elements('view[class="villageItem--center villageItem--chat"]')[1].tap()
        self.get_screenshot('列表页点击进入咨询页面')
        

    def test_11_点击划片小区(self):
        """
        V6.42.X: 点击划片小区进入小区详情页
        """
        self.find_element('view[class="hpxq--pr hpxq--coverPic"]').tap()

        self.get_screenshot()
        self.verifyPageName('/esf/village/pages/detail/detail')

    def test_12_点击划片小区咨询底价(self):
        """
        V6.42.X: 点击划片小区 咨询底价
        """
        self.find_element('view[class="hpxq--center hpxq--consult"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_13_优质在售房源(self):
        """
        V6.42.X: 点击 优质 在售房源，进列表
        """
        self.find_element('view[class="yzfy--center yzfy--chat"]').tap()
        self.get_screenshot()
        self.verifyPageName('/esf/sell/pages/sellList/sellList')

    def test_14_购房资料(self):
        """
        V6.42.X: 点击 购房资料
        """
        self.find_element('view[class="pf advert"]').tap()
        self.get_screenshot()
        self.verifyPageName('/page/tools/ziliaomoban/ziliaomoban')

    def test_15_优质在租房源(self):
        """
        V6.42.X: 点击 优质 在租房源，进列表
        """
        try:
            self.find_element('view[class="yzfy--center yzfy--type"][data-id="rent"]').tap()
            self.find_element('view[class="yzfy--center yzfy--chat"]').tap()
            self.get_screenshot()
            self.verifyPageName('/esf/sell/rent/list/list')
        except:
            self.page.scroll_to(10000, 200)
            self.get_screenshot()

    def test_99_分享(self):
        """
        V6.42.X: 点击 分享
        """
        self.find_element('button[class="pf shareBtn"]').tap()
        self.get_screenshot()