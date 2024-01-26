# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestNewhouseLpxx(TestBase):
    """
    楼盘信息详情页(苏宁测试11）
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/lpxx/lpxx?pinyin=sjcs1&city=qz&zygw_id='
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhouseLpxx, self).setUp()

    def click_kpjl(self):
        """
        点击开盘记录
        """
        eles = self.find_elements('view[class="lpxxDetailUl-li-r-link flex tfAlignC tfFlexC"]')
        for e in eles:
            if '开盘记录' in e.inner_wxml:
                e.tap()
                break

    def test_009_楼距分析(self):
        """
        V6.39.X: 容积率字段旁，点击“楼距分析”
        """
        self.find_element('view[class="lpxxDetailUl-li-r-link flex tfAlignC tfFlexC"][data-ysname="楼距分析"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_008_xxxx_点击开盘记录(self):
        """
        V6.24.X: 开盘时间字段旁，点击“开盘记录”按钮
        """
        self.click_kpjl()

        self.get_screenshot()

    def test_001_click_zygw_more_置业顾问更多(self):
        """
        V6.23.X: -置业顾问楼层，点击“查看更多”
        """
        self.find_element('view[class="newHouseTitle-r-sj"]').tap()

        self.verifyPageName('/page/newhouse/zygw/list')
        self.get_screenshot()

    def test_002_click_zygw_im_置业顾问咨询(self):
        """
        V6.23.X: 置业顾问楼层，点击IM按钮
        """
        self.find_element('button[class="zyList_li_r_im"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_003_goto_zygw_进置业顾问名片(self):
        """
        V6.23.X: 置业顾问楼层，点击置业顾问头像，进置业顾问名片页
        """
        self.find_element('image[class="zyList_li_l-img"]').tap()

        self.verifyPageName('/page/newhouse/zygw/detail')
        self.get_screenshot()

    def delete_004_click_申请入驻(self):
        """
        V6.23.X: 置业顾问楼层，点击“申请入驻”
        V6.32.X: 已删除改申请入驻
        """
        self.find_element('navigator[class="notification"]').tap()

        self.verifyPageName('/page/index/mine')
        self.get_screenshot()

    def test_005_xxxx_咨询周边板块(self):
        """
        V6.23.X: 详细信息楼层-板块旁“咨询周边板块”入口
        """
        self.find_element('image[class="lpxxDetailUl-li-r-link-bk"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_006_xxxx_地图找房(self):
        """
        V6.23.X: 详细信息楼层-楼盘区属旁“地图找房”入口
        """
        self.find_element('view[class="lpxxDetailUl-li-r-link-disk"]').tap()

        self.verifyPageName('/page/newhouse/mapzf/mapzf')
        self.get_screenshot()

    def test_007_gjdt_im_公交地铁咨询(self):
        """
        V6.23.X: 公交地铁楼层，点击“咨询周边交通详情”按钮
        """
        self.find_element('image[class="consult_imicon"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_010_click_zygw_call_置业顾问电话(self):
        """
        V6.23.X: 置业顾问楼层，点击电话
        """
        self.find_element('button[class="zyList_li_r_tel"]').tap()

        self.get_screenshot()