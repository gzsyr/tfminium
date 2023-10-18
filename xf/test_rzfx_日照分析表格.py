# add by zsy
from base.test_base import TestBase


class TestRzfxBg(TestBase):
    """
    日照分析表格页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/rizhaofenxi/rizhaofenxi?city=qz&pinyin=shanhaiguojixzl&tab=1'
        self.switch = False
        self.classname = __class__.__name__
        super(TestRzfxBg, self).setUp()

    def test_goto_噪音分析_3d(self):
        """
        V6.41.X: 噪音分析，点击图片
        """
        self.find_element('view[class="tab"][data-id="2"]').tap()
        self.find_element('view[class="icon tfFlex tfAlignC icon_2"]').tap()

        self.get_screenshot('进入3D页面')
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhao3d')

        self.delay(10)

        self.input_value_by_mk('xf/zy_night.png')
        self.delay(3)
        self.get_screenshot('3D页面黑夜')

        self.find_element('cover-image[class="consultimg"]').tap()
        self.get_screenshot('3D页面咨询')

    def test_goto_噪音分析_切换黑夜(self):
        """
        V6.41.X: 噪音分析，点击黑夜切换
        """
        self.find_element('view[class="tab"][data-id="2"]').tap()
        self.delay(1)

        self.find_element('view[class="jqItem"][data-id="2"]').tap()

        self.get_screenshot()

    def delete_test_goto_噪音分析_底部咨询(self):
        """
        V6.45.x: delete
        V6.41.X: 噪音分析，点击底部咨询
        """
        self.find_element('view[class="tab"][data-id="2"]').tap()
        self.delay(2)

        self.find_element('view[class="consultWrap tfFlex tfAlignC tfFlexC"]').tap()
        # self.find_element('view[class="comBottomBar--link-button comBottomBar--im"]').tap()

        self.get_screenshot()

    def test_goto_户型分析_3d(self):
        """
        V6.40.X: 户型分析，点击图片
        """
        self.find_element('view[class="tab"][data-id="4"]').tap()
        self.find_element('view[class="icon tfFlex tfAlignC icon_4"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhao3d')

    def test_goto_户型分析_切换户型(self):
        """
        V6.40.X: 户型分析，点击户型切换
        """
        self.find_element('view[class="tab"][data-id="4"]').tap()
        self.delay(1)

        self.find_element('view[class="ldItem"][data-id="390"]').tap()

        self.get_screenshot()

    def test_goto_户型分析_底部咨询(self):
        """
        V6.40.X: 户型分析，点击底部咨询
        """
        self.find_element('view[class="tab"][data-id="4"]').tap()
        self.delay(1)

        self.find_element('view[class="consultWrap tfFlex tfAlignC tfFlexC"]').tap()

        self.get_screenshot()

    def test_goto_tab切换(self):
        """
        V6.40.X: 户型分析-点击日照
        """
        # 点击户型分析
        self.find_element('view[class="tab"][data-id="4"]').tap()
        self.delay(1)
        self.get_screenshot('切换到户型分布')
        # 点击日照
        self.find_element('view[class="tab"][data-id="1"]').tap()
        self.delay(1)
        self.get_screenshot('切换到日照')
        # 点击日照
        self.find_element('view[class="tab"][data-id="3"]').tap()
        self.delay(1)
        self.get_screenshot('切换到楼距')

    def test_goto_楼距_切换楼栋(self):
        """
        V6.39.X: 点击“楼距”，进入楼距tab，点击 楼栋“居民楼”
        """
        self.find_element('view[class="tab"][data-id="3"]').tap()
        self.delay(1)

        self.find_element('view[class="ldItem"][data-id="2505"]').tap()

        self.get_screenshot()

    def test_goto_楼距_3d(self):
        """
        V6.39.X: 点击“楼距”，进入楼距tab，点击 3d模型
        """
        self.find_element('view[class="tab"][data-id="3"]').tap()
        self.delay(1)
        self.get_screenshot('切换到楼距分析')
        self.find_element('view[class="tab"][data-id="1"]').tap()
        self.delay(1)
        self.get_screenshot('切换到日照分析')
        self.find_element('view[class="tab"][data-id="3"]').tap()
        self.find_element('view[class="icon tfFlex tfAlignC icon_3"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhao3d')

    def test_goto_3d(self):
        """
        点击 进入3D 模型
        """
        self.find_element('view[class="icon tfFlex tfAlignC icon_1"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhao3d')

    def test_click_节气楼栋(self):
        """
        V6.37.x: 点击 大寒  +  2 栋楼
        """
        self.find_element('view[class="jqItem"][data-id="6"]').tap()
        self.find_element('view[class="ldItem"][data-id="2440"]').tap()

        self.get_screenshot()

    def test_tab_底部控件收起展开(self):
        """
        V6.37.X: 点击 底部控件 展开收起操作
        """
        self.find_element('view[class="lpBottomBar--popup_icon"]').tap()
        self.delay(2)
        self.get_screenshot('展开截图')
        self.find_element('view[class="lpBottomBar--popup_icon lpBottomBar--open_icon"]').tap()
        self.delay(1)
        self.get_screenshot('收起截图')

    def click_hx(self):
        """
        点击 户型
        """
        # 点击主力户型
        self.find_element('view[class="lpBottomBar--tab"][data-index="1"]').tap()

    def test_hx_进入户型详情页(self):
        """
        V6.37.X: 点击 主力户型 选择 二室，选择第一个户型进入户型详情页
        """
        # 点击主力户型
        self.click_hx()
        # 点击 二室
        self.find_element('view[class="lpBottomBar--hxtab"][data-index="1"]').tap()
        # 点击户型进入详情页
        self.find_element('image[class="lpBottomBar--hxImg"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/hx/hxdetail')

    def test_hx_咨询底价(self):
        """
        V6.37.X: 点击 主力户型，点击 咨询底价
        """
        # 点击主力户型
        self.click_hx()
        # 点击咨询底价
        self.find_element('view[class="lpBottomBar--tfFlex lpBottomBar--tfAlignC lpBottomBar--tfFlexC lpBottomBar--consult_hx"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_hx_更多(self):
        """
        V6.37.X: 点击 主力户型，点击 更多
        """
        # 点击主力户型
        self.click_hx()
        # 点击更多
        self.find_element('view[class="lpBottomBar--lpmore"]', inner_text="更多").tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/hx/hxlist')

    def click_yfyj(self):
        """
        点击 一房一价
        """
        self.find_element('view[class="lpBottomBar--tab"][data-index="2"]').tap()

    def test_yfyj_更多(self):
        """
        V6.37.X: 点击 一房一价，点击 更多
        """
        self.click_yfyj()

        self.find_elements('view[class="lpBottomBar--lpmore"]', inner_text='更多')[1].tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/fd/xkb')

    def test_yfyj_咨询(self):
        """
        V6.37.X: 点击 一房一价，点击 更多
        """
        self.click_yfyj()

        self.find_element('view[class="lpBottomBar--consult_imicon_yfyj"]').tap()

        self.get_screenshot()

    def test_yfyj_进入详情(self):
        """
        V6.37.X: 点击  一房一价， 点击 进入详情页
        """
        self.click_yfyj()

        self.find_element('view[class="lpBottomBar--yfyjList"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/fd/fdfydetail')

    def click_lp(self):
        """
        点击 楼盘信息
        """
        self.find_element('view[class="lpBottomBar--tab lpBottomBar--tabActive"][data-index="0"]').tap()

    def test_lp_进入楼盘详情(self):
        """
        V6.37.X: 点击 楼盘信息，进入楼盘详情页
        """
        self.click_lp()

        self.find_element('view[class="lpBottomBar--lpmore"]', inner_text='详情').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/detail')

    def test_z_在线咨询(self):
        """
        V6.37.X: 点击 在线咨询
        """
        self.find_element('view[class="comBottomBar--link-button comBottomBar--im"]').tap()

        self.delay(3)
        self.get_screenshot()

    def test_zz_打电话(self):
        """
        V6.37.X: 点击 拨打电话
        """
        self.find_element('view[class="comBottomBar--link-button comBottomBar--call"]').tap()

        self.get_screenshot()

