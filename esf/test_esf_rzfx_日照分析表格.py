# add by zsy
from base.test_base import TestBase


class TestEsfRzfxBg(TestBase):
    """
    日照分析表格页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/rizhaofenxi/rizhaofenxi?city=nj&esfId=10017892&tab=1'
        self.switch = False
        self.classname = __class__.__name__
        super(TestEsfRzfxBg, self).setUp()


    def test_goto_3d(self):
        """
        点击 进入3D 模型
        """
        self.find_element('view[class="icon tfFlex tfAlignC icon_esf_1"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhao3d')

    def test_click_节气楼栋(self):
        """
        V6.38.x: 点击 大寒  +  5 栋楼
        """
        self.find_element('view[class="jqItem"][data-id="6"]').tap()
        self.find_element('view[class="ldItem"][data-id="2"]').tap()

        self.get_screenshot()

    def test_tab_底部控件收起展开(self):
        """
        V6.38.X: 点击 底部控件 展开收起操作
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

    def test_zzhx_选择两室查看户型图(self):
        """
        V6.38.X: 点击 主力户型 选择 二室 查看户型图
        """
        # 点击主力户型
        self.click_hx()
        self.delay(2)
        # 点击 二室
        self.find_element('view[class="lpBottomBar--hxtab"][data-key="3"]').tap()
        self.get_screenshot('选择san室的截图')

        self.find_element('image[class="lpBottomBar--hxImg"]').tap()
        self.get_screenshot('点击户型图的截图')

    def test_hx_咨询在售(self):
        """
        V6.38.X: 点击 小区户型，点击 咨询底价
        """
        # 点击主力户型
        self.click_hx()
        # 点击咨询底价
        self.find_element('view[class="lpBottomBar--tfFlex lpBottomBar--tfAlignC lpBottomBar--tfFlexC lpBottomBar--consult_hx"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_hx_更多(self):
        """
        V6.37.X: 点击 主力户型，点击 更多
        """
        # 点击小区户型
        self.click_hx()
        # 点击更多
        self.find_element('view[class="lpBottomBar--lpmore"]', inner_text="更多").tap()

        self.get_screenshot()
        self.verifyPageName('/esf/village/pages/detail/detailHxImage/detailHxImage')

    def click_xqfy(self):
        """
        点击 小区房源
        """
        self.find_element('view[class="lpBottomBar--tab"][data-index="2"]').tap()

    def redirect_to_have_house(self):
        """
        切换到有 二手房、租房房源的页面
        """
        self.redirect_to_page('/page/newhouse/rizhaofenxi/rizhaofenxi?city=nj&esfId=10006280&tab=1')
        self.delay(3)

    def test_xqfy_在租更多(self):
        """
        V6.38.X: 点击 小区房源，点击 更多
        """
        self.redirect_to_have_house()
        try:
            self.click_xqfy()

            # 点击 在租
            self.find_element('view[class="lpBottomBar--fytab"][data-type="2"]').tap()

            # 点击 更多
            self.find_element('view[class="lpBottomBar--xq_consult_hx"]').tap()

            self.get_screenshot()
            self.verifyPageName('/esf/sell/rent/list/list')
        except:
            self.get_screenshot('没有房源')

    def test_xqfy_在租房源详情(self):
        """
        V6.38.X: 点击 小区房源，点击 整租
        """
        self.redirect_to_have_house()
        try:
            self.click_xqfy()

            # 点击 在租
            self.find_element('view[class="lpBottomBar--fytab"][data-type="2"]').tap()

            # 点击房源
            self.find_element('view[class="item--line_1 item--title"]').tap()

            self.get_screenshot()
            self.verifyPageName('/esf/sell/rent/r_detail/detail')
        except:
            self.get_screenshot('没有房源')

    def test_xqfy_切换租售进入出售房源详情(self):
        """
        V6.38.X: 点击  小区房源，点击在租  在售，点击房源进入详情
        """
        self.redirect_to_have_house()
        try:
            self.click_xqfy()

            # 点击 在租
            self.find_element('view[class="lpBottomBar--fytab"][data-type="2"]').tap()

            # 点击 在售
            self.find_element('view[class="lpBottomBar--fytab"][data-type="1"]').tap()

            # 点击房源
            self.find_element('image[class="sell-item--img"]').tap()

            self.get_screenshot()
            self.verifyPageName('/esf/sell/pages/detail/detail')
        except:
            self.get_screenshot('没有房源')

    def click_lp(self):
        """
        点击 小区信息
        """
        self.find_element('view[class="lpBottomBar--tab lpBottomBar--tabActive"][data-index="0"]').tap()

    def test_xq_进入小区详情(self):
        """
        V6.38.X: 点击 小区信息，进入小区详情页
        """
        self.click_lp()

        self.find_element('view[class="lpBottomBar--lpmore"]', inner_text='查看详情').tap()

        self.get_screenshot()
        self.verifyPageName('/esf/village/pages/detail/detail')

    def test_xq_咨询近期成交(self):
        """
        V6.38.X: 点击 小区信息，咨询近期成交
        """
        self.click_lp()

        self.find_element('view[class="lpBottomBar--xq_consult_imicon_hx"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_z_在线咨询(self):
        """
        V6.38.X: 点击 在线咨询
        """
        self.find_element('view[class="contact--center contact--pr contact--msg contact--positionRel"]').tap()


        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_zz_打电话(self):
        """
        V6.38.X: 点击 拨打电话
        """
        self.find_element('view[class="contact--center contact--tel contact--positionRel"]').tap()

        self.get_screenshot()

