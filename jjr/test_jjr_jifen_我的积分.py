# -*-coding:utf-8-*-
import time

from base.test_mine import TestMine

class TestMineScoreJJR(TestMine):
    """
    经纪人 我的积分页
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestMineScoreJJR, cls).setUpClass()

        cls.g = globals()
        cls.g['phone'] = cls().get_phone()

        cls().change_jjr()
        print("setupclass TestMineScoreZygw")

    def setUp(self) -> None:
        self.page_name = '/page/mine/myscores/myscores?city=nj'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestMineScoreJJR, self).setUp()

    def test_01_积分规则(self):
        """
        V6.27.X: 点击积分规则图标
        """
        self.find_element('view[class="flex tfAlignC"]/image').tap()

        self.verifyPageName('/page/mine/myscores/scorerule')
        self.get_screenshot()

    def test_02_积分明细_去兑换(self):
        """
        V6.38.X: 点击积分明细 点击做任务赚积分 点击积分兑好物
        """
        # 点击 积分明细
        self.find_element('view[class="jf_record flex tfAlignC tfFlexC"]').tap()
        self.delay(3)

        # 点击 做任务赚积分
        self.find_element('view[class="toMyscore flex tfAlignC tfFlexC"]').tap()
        self.delay(3)

        # 点击 积分兑好物
        self.find_element('image[class="dhGoods"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/mine/myscores/scoremall')

    def test_03_已兑换商品(self):
        """
        V6.38.x: 点击已兑换商品
        """
        self.find_element('view[class="jf_ydhgoods flex tfAlignC tfFlexC"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/mine/myscores/mycoupons')

    def test_04_去标记(self):
        """
        v6.38.x: 点击 去标记
        """
        self.find_element('view[class="toPublish"]', inner_text='去标记').tap()

        self.get_screenshot()
        self.verifyPageName('/page/business/customerManage/myCustomer/myCustomer')

    def test_05_去回复(self):
        """
        v6.38.x: 点击 去回复
        """
        self.find_element('view[class="toPublish"]', inner_text='去回复').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/recentchat/recentchat')

    def test_07_去兑换(self):
        """
        V6.38.X: 点击 去兑换
        """
        self.find_element('view[class="toDh"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/mine/myscores/goodsdetail')

    def test_06_去分享(self):
        """
        V6.27.X: 做任务赚积分，点击“去分享”
        """
        try:
            self.find_element('view[class="toPublish"]', inner_text='去分享').tap()

            self.verifyPageName('/page/mine/myscores/share')
        except:
            print('无分享任务')
        self.get_screenshot()

    def test_08_点击全部任务_标记客户(self):
        """
        V6.38.X: 点击全部任务 并且 V6.42.x:点击标记客户
        """
        self.find_element('view[class="toAll"]', inner_text='全部任务 ').tap()
        self.get_screenshot('进入全部任务')
        self.verifyPageName('/page/mine/myscores/alltasks')
        self.delay(3)

        self.find_element('view[class="btn"]', inner_text='去标记').tap()
        self.get_screenshot('点击去标记')
        self.verifyPageName('/page/business/customerManage/myCustomer/myCustomer')

    def test_09_点击积分商城(self):
        """
        V6.38.X: 点击 积分商城
        """
        self.page.scroll_to(500, 200)
        try:
            self.find_element('view[class="toAll"]', inner_text='积分商城  ').tap()
        except:
            print('只有两个商品')

        self.get_screenshot()