# -*-coding:utf-8-*-
import time

from base.test_mine import TestMine

class TestMineScoreZygw(TestMine):
    """
    置业顾问 我的积分页
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestMineScoreZygw, cls).setUpClass()

        cls.g = globals()
        cls.g['phone'] = cls().get_phone()

        cls().change_zygw()
        print("setupclass TestMineScoreZygw")

    def setUp(self) -> None:
        self.page_name = '/page/mine/myscores/myscores?city=qz&role_id=1005'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestMineScoreZygw, self).setUp()

    def test_01_积分规则(self):
        """
        V6.27.X: 点击积分规则图标
        """
        self.find_element('view[class="flex tfAlignC"]/image').tap()

        self.verifyPageName('/page/mine/myscores/scorerule')
        self.get_screenshot()

    def test_02_联系客服(self):
        """
        V6.27.X: 点击联系客服图标
        """
        self.find_element('view[class="contact_kf flex tfAlignC tfFlexC"]').tap()

        self.get_screenshot()

    def test_03_积分明细TAB切换(self):
        """
        V6.27.X: 点击积分明细，收入支出切换
        """
        self.find_element('view[class="jf_record flex tfAlignC tfFlexC"]').tap()
        self.delay(2)

        self.find_element('view[id="getPayList"]').tap()
        self.get_screenshot('支出列表')
        self.find_element('view[id="getList"]').tap()
        self.get_screenshot()

    def test_04_查看任务规则(self):
        """
        V6.27.X: 做任务赚积分，点击第一个任务
        """
        self.find_element('view[class="taskName itemName"]').tap()

        self.get_screenshot()

    def test_05_去发布(self):
        """
        V6.27.X: 做任务赚积分，点击“去发布”
        """
        self.find_element('view[class="toPublish"]', inner_text='去发布').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

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

    def test_07_去完成(self):
        """
        V6.27.X: 做任务赚积分，点击“去完成”
        """
        self.find_element('view[class="toPublish"]', inner_text='去完成').tap()

        self.verifyPageName('/page/mine/myscores/upload')
        self.delay(1)

        self.find_element('textarea').input(time.strftime('%Y-%m-%d')+'置业顾问楼盘信息上传')

        self.verifyStr(True, self.getShowToast('self.find_element(\'button[class="btnSubmit"]\').tap()'),
                       '提交成功弹框')

    def test_08_查看提交信息(self):
        """
        V6.27.X: 点击上传记录，查看 test_07_去完成 发布的内容
        """
        self.find_element('view[class="jf_upload flex tfAlignC tfFlexC"]').tap()

        self.verifyPageName('/page/mine/myscores/uploadrecord')
        self.delay(1)

        # 点击第一条记录
        self.find_element('view[class="status pending"]').tap()
        self.verifyPageName('/page/mine/myscores/updetail')
        self.get_screenshot()

    def click_alltask(self):
        """
        做任务赚积分，点击“全部任务”
        """
        self.find_element('view[id="toallMask"]').tap()
        self.delay(3)

    def test_09_查看全部任务(self):
        """
        V6.27.X: 做任务赚积分，点击“全部任务”
        """
        self.click_alltask()

        self.verifyPageName('/page/mine/myscores/alltasks')
        self.get_screenshot()

    def test_10_全部任务_去发布(self):
        """
        V6.27.X: 做任务赚积分，点击“全部任务”，点击第一个“去发布”
        """
        self.click_alltask()
        self.find_element('view[id="toPublish"]', inner_text='去发布').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def test_11_全部任务_去分享(self):
        """
        V6.27.X: 做任务赚积分，点击“全部任务”，点击第一个“去分享”
        """
        self.click_alltask()
        try:
            self.find_element('view[id="toPublish"]', inner_text='去分享').tap()

            self.verifyPageName('/page/mine/myscores/share')
        except:
            print('无分享任务')
        self.get_screenshot()

    def test_12_全部任务_去完成(self):
        """
        V6.27.X: 做任务赚积分，点击“全部任务”，点击第一个“去完成”
        """
        self.click_alltask()
        self.find_element('view[id="toPublish"]', inner_text='去完成').tap()

        self.verifyPageName('/page/mine/myscores/upload')
        self.get_screenshot()

    def test_13_全部任务_任务规则(self):
        """
        V6.27.X: 做任务赚积分，点击“全部任务”，点击第一个任务查看规则
        """
        self.click_alltask()
        self.delay(1)
        self.find_element('view[id="showTaskrule"]').tap()

        self.get_screenshot()

    def test_17_全部任务_去邀请(self):
        """
        V6.40.X: 做任务赚积分，点击“全部任务”，点击”去邀请“
        """
        self.click_alltask()
        self.delay(1)
        self.find_element('button[class="btn invitezygw"]').tap()

        self.get_screenshot()

    def delete_test_14_积分兑换_兑换置顶券(self):
        """
        V7.16delete
        V6.27.X: 积分兑换，点击第一个置顶券类型，执行兑换
        """
        self.find_element('view[id="toGoodsdetail"][data-type="1"]').tap()

        self.delay(2)
        self.verifyPageName('/page/mine/myscores/goodsdetail')

        # 点击“立即兑换”
        self.find_element('view[id="toChange"]').tap()
        self.delay(1)
        self.get_screenshot('确认兑换弹框')
        # 点击“确定”
        self.find_element('view[id="confirm"]').tap()
        self.delay(2)
        # 跳转到“我的权益券”页面
        self.verifyPageName('/page/mine/myscores/mycoupons')
        self.get_screenshot()

    def click_jfmall(self):
        """
        积分兑换，点击 积分商城
        """
        self.find_element('view[id="tojfMall"]').tap()
        self.delay(2)

    def delete_test_15_积分兑换_积分商城(self):
        """
        V7.16delete
        V6.27.X: 积分兑换，点击积分商城
        """
        self.click_jfmall()

        self.verifyPageName('/page/mine/myscores/scoremall')
        self.get_screenshot()

    def delete_test_16_积分商城_去兑换(self):
        """
        V7.16delete
        V6.27.X: 积分兑换，点击积分商城
        """
        self.click_jfmall()

        self.find_element('view[id="toGoodsdetail"]').tap()

        self.verifyPageName('/page/mine/myscores/goodsdetail')
        self.get_screenshot()