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

    def test_01_卡片IM咨询(self):
        """
        V6.23.X: 卡片信息模块的“在线咨询”
        """
        self.find_element('view[class="tBtn-im flex tfAlignC tfFlexC"]').tap()

        self.delay(4)
        self.get_screenshot()

    def test_97_bottom_im_底部在线咨询(self):
        """
        V6.23.X: 底部“在线咨询”
        """
        self.find_element('view[class="bBtn-im flex tfAlignC tfFlexC positionRel"]').tap()

        self.delay(4)
        self.get_screenshot()

    def test_03_为我点赞(self):
        """
        V6.23.X: 点击“为我点赞”
        """
        self.find_element('view[class="mBtnBox zanBox flex tfFlexC tfAlignC"]').tap()

        self.get_screenshot()

    def test_04_生成海报(self):
        """
        V6.23.X: 点击“生成海报”
        """
        self.find_element('view[class="mBtnBox flex tfFlexC tfAlignC"]').tap()

        self.delay(2)
        self.get_screenshot()

    def test_05_添加微信(self):
        """
        V6.23.X: 点击“添加微信”
        """
        # 设置跳转到其他置业顾问名片
        self.g['phone'] = self.other_zygw

        self.find_element('view[class="addwx flex tfAlignC tfFlexC"]').tap()

        self.delay(2)
        self.get_screenshot()

    def test_06_为TA点赞(self):
        """
        V6.23.X: 点击“为TA点赞”
        """
        # 设置跳回自己的置业顾问名片
        self.g['phone'] = self.get_phone()

        self.find_element('view[class="mBtnBox zanBox flex tfFlexC tfAlignC"]').tap()

        self.get_screenshot()

    def test_07_查看分享规则(self):
        """
        V6.27.X: 点击 分享页面享加倍曝光
        """
        self.find_element('view[class="house__tt_img"]').tap()

        self.get_screenshot()

    def test_99_分享名片(self):
        """
        V6.23.X: 点击“分享名片”
        """
        self.find_element('button[class="btn-tool bBtn-share"]').tap()

        self.get_screenshot()

    def test_10_卡片IM电话(self):
        """
        V6.23.X: 卡片信息模块的“在线咨询”
        """
        self.find_element('view[class="tBtn-tel flex tfAlignC tfFlexC"]').tap()

        self.get_screenshot()

    def test_11_主营楼盘(self):
        """
        V6.27.X: 查看主营楼盘
        """
        self.find_element('view[class="house__item tfFlex tfFlexSb"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_12_主营楼盘_最新动态(self):
        """
        V6.27.X: 查看主营楼盘_最新动态
        """
        self.find_element('view[class="house_icon"][data-name="最新动态"]').tap()

        self.verifyPageName('/page/newhouse/zxdt/zxdt')
        self.get_screenshot()

    def test_13_主营楼盘_户型解析(self):
        """
        V6.27.X: 查看主营楼盘_户型解析
        """
        self.find_element('view[class="house_icon"][data-name="户型解析"]').tap()

        self.verifyPageName('/page/newhouse/hx/hxlist')
        self.get_screenshot()

    def test_14_主营楼盘_楼盘详情(self):
        """
        V6.27.X: 查看主营楼盘_楼盘详情
        """
        self.find_element('view[class="house_icon"][data-name="楼盘详情"]').tap()

        self.verifyPageName('/page/newhouse/lpxx/lpxx')
        self.get_screenshot()

    def test_15_主营楼盘_一房一价(self):
        """
        V6.27.X: 查看主营楼盘_一房一价
        """
        self.find_element('view[class="house_icon"][data-name="一房一价"]').tap()

        self.verifyPageName('/page/newhouse/fd/xkb')
        self.get_screenshot()

    def test_16_主营楼盘_楼盘点评(self):
        """
        V6.27.X: 查看主营楼盘_楼盘点评
        """
        self.find_element('view[class="house_icon"][data-name="楼盘点评"]').tap()

        self.verifyPageName('/page/taofangquan/lpdp/lpdp')
        self.get_screenshot()

    def test_17_帖子评论TAB切换(self):
        """
        V6.27.X: TA的帖子  TA的评论 TAB切换
        """
        self.find_element('view[class="zygw_messages_tit"][data-type="2"]').tap()
        self.delay(2)
        self.get_screenshot('TA的评论')

        self.find_element('view[class="zygw_messages_tit"][data-type="1"]').tap()
        self.get_screenshot()

    def test_18_点击帖子(self):
        """
        V6.27.X: TA的帖子  点击进入帖子详情页
        """
        self.find_element('view[class="zygw_post"]').tap()
        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_19_点击评论(self):
        """
        V6.27.X: TA的评论 点击进入评论详情页
        """
        self.find_element('view[class="zygw_messages_tit"][data-type="2"]').tap()
        self.delay(3)
        self.find_element('view[class="zygw_comment flex"]').tap()
        self.verifyPageName('/page/taofangquan/commentDetail/commentDetail')
        self.get_screenshot()

    def test_98_bottom_call_底部拨打电话(self):
        """
        V6.23.X: 底部“在线咨询”
        """
        self.find_element('view[class="bBtn-tel flex tfAlignC tfFlexC positionRel"]').tap()

        self.get_screenshot()



