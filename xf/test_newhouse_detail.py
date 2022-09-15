# add by zsy

from base.test_base import TestBase


class TestNewhouseDetail(TestBase):
    """
    新房详情页页面
    """
    def setUp(self) -> None:
        self.page_name = "/page/newhouse/detail?pinyin=shanhaiguojixzl&city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhouseDetail, self).setUp()
        self.delay(2)

    def test_goto_photo(self):
        """
        新房详情页页面，点击相册
        """
        self.page.get_element("image[class='newHouseBanner-img xfxq_xc']").tap()

        self.verifyPageName('/page/newhouse/xcny/xcnylist')
        self.get_screenshot()

    def test_goto_pk(self):
        """
        新房详情页页面，点击PK
        """
        self.page.get_element("navigator[class='pk-icon']").tap()

        self.verifyPageName('/page/newhouse/loupanPk/loupanPk')
        self.get_screenshot()

    def test_goto_dy(self):
        """
        新房详情页页面，点击订阅（爱心按钮）
        """
        if self.page.element_is_exists('view[class="dy-icon is_sub"]'):
            self.page.get_element('view[class="dy-icon is_sub"]').tap()

            self.verifyStr(True, self.page.element_is_exists('view[class="dy-icon"]'),
                           '取消订阅 ok')
        else:
            self.page.get_element('view[class="dy-icon"]').tap()

            self.verifyStr(True, self.page.element_is_exists('view[class="dy-icon is_sub"]'),
                           '订阅 ok')

        self.get_screenshot()

    def test_goto_fdjsq(self):
        """
        新房详情页页面，点击房贷计算器
        """
        self.page.get_element("view[class='newHouseInfor-price-r xfxq_jsq']").tap()

        self.verifyPageName('/page/tools/fdjsq/sd/index')
        self.get_screenshot()

    def test_goto_addr(self):
        """
        新房详情页页面，点击地址右箭头
        """
        self.page.get_element("view[class='newHouseInfor-add-r']").tap()

        self.get_screenshot()

        # 退出地图页面
        self.input_value_by_mk(png='xf/mapreturn.png')

    def test_goto_lpdp_gd(self):
        """
        新房详情页页面，点击楼盘点评滚动处，进入楼盘点评页面，点击第一条点评，进入点评详情页
        """
        self.page.get_element("view[class='tfFlex tfFlexSb tfAlignC dpEntry']").tap()
        self.verifyPageName('/page/taofangquan/lpdp/lpdp')

        #
        # # 返回到楼盘点评页
        # self.app.navigate_back()
        # self.verifyPageName('/page/taofangquan/lpdp/lpdp')
        #
        # # 点击中部的圈子，进入圈子详情页
        # self.page.get_element('view[class="qzwrap"]').tap()
        # self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        # # 返回到楼盘点评页
        # self.app.navigate_back()
        # self.verifyPageName('/page/taofangquan/lpdp/lpdp')

        self.verifyPageName('/page/taofangquan/lpdp/lpdp')
        self.get_screenshot()

    def test_goto_zxdt(self):
        """
        新房详情页页面，点击最新动态
        """
        self.page.get_element("view[class='newHouseIconInLi-b']", inner_text="最新动态").tap()

        self.verifyPageName('/page/newhouse/zxdt/zxdt')
        self.get_screenshot()

    def test_goto_hxjx(self):
        """
        新房详情页页面，点击户型解析
        """
        self.page.get_element("view[class='newHouseIconInLi-b']", inner_text="户型解析").tap()

        self.verifyPageName('/page/newhouse/hx/hxlist')
        self.get_screenshot()

    def test_goto_lpxq(self):
        """
        新房详情页页面，点击楼盘详情
        """
        self.page.get_element("view[class='newHouseIconInLi-b']", inner_text="楼盘详情").tap()

        self.verifyPageName('/page/newhouse/lpxx/lpxx')
        self.get_screenshot()

    def test_goto_yfyj(self):
        """
        新房详情页页面，点击一房一价
        """
        self.page.get_element("view[class='newHouseIconInLi-b']", inner_text="一房一价").tap()

        self.verifyPageName('/page/newhouse/fd/xkb')
        self.get_screenshot()

    def test_goto_lpdp(self):
        """
        新房详情页页面，点击楼盘点评
        """
        self.page.get_element("view[class='newHouseIconInLi-b']", inner_text="楼盘点评").tap()

        self.verifyPageName('/page/taofangquan/lpdp/lpdp')
        self.get_screenshot()

    def test_goto_msbm(self):
        """
        新房详情页页面，点击马上报名(后台配置的）
        """
        self.page.get_element("view[class='ggweiR']", inner_text="马上报名").tap()

        self.get_screenshot()

    def test_goto_bmqc(self):
        """
        新房详情页页面，点击报名清册
        """
        self.page.get_element("view[class='left-icon disflex tfAlignC tfFlexC']").tap()

        self.verifyPageName('/page/yaohao/publicity')
        self.get_screenshot()

    def test_goto_bmxh(self):
        """
        新房详情页页面，点击报名序号
        """
        self.page.get_element("view[class='disflex tfAlignC xf_xh_title']").tap()

        self.verifyPageName('/page/mine/myLottery/myLottery')
        self.get_screenshot()

    def test_goto_bmyfyj(self):
        """
        新房详情页页面，点击最新摇号下方的一房一价
        """
        self.page.get_element("view[class='yifangyijia']").tap()

        self.verifyPageName('/page/newhouse/fd/xkb')
        self.get_screenshot()

    def test_goto_bmgfzl(self):
        """
        新房详情页页面，点击最新摇号下方的购房资料
        """
        self.page.get_element("view[class='goufangziliao']").tap()

        self.get_screenshot()

    def test_goto_lpdt_more(self):
        """
        新房详情页页面，点击楼盘动态更多
        """
        self.page.get_element("view[class='tfFlex tfFlexSb newHouseTitle-line xfxq_lpdt disflex-alignitems-center']").tap()

        self.verifyPageName('/page/newhouse/zxdt/zxdt')
        self.get_screenshot()

    def test_goto_xxxx_more(self):
        """
        新房详情页页面，点击楼盘详细信息
        """
        self.page.get_element("view[class='tfFlex tfFlexSb newHouseTitle-line xfxq_lpdt']").tap()

        self.verifyPageName('/page/newhouse/lpxx/lpxx')
        self.get_screenshot()

    def test_goto_wzzb_dt(self):
        """
        新房详情页页面，点击位置周边下的地图
        """
        self.page.scroll_to(3000, 500)
        self.delay(2)

        # self.page.get_element('view[class="newHouseTitle-r xfxq_qbhx"][data-eventid="2648"]').tap()
        self.page.get_element('view[data-eventid="2648"]').tap()
        self.get_screenshot()
        self.input_value_by_mk('xf/mapreturn.png')

    def test_goto_jgfx(self):
        """
        新房详情页，点击价格分析
        """
        self.page.scroll_to(3000, 500)
        self.delay(2)
        self.page.get_element('view[class="newHouseTitle-l"]', inner_text='价格分析').tap()

        self.verifyPageName('/page/newhouse/priceAnalyse/priceAnalyse')
        self.get_screenshot()

    def test_goto_kpjl(self):
        """
        新房详情页，点击开盘记录
        """
        self.page.scroll_to(3000, 500)
        self.delay(2)
        self.page.get_element('view[class="newHouseTitle-l"]', inner_text='开盘记录').tap()

        self.verifyPageName('/page/newhouse/historyLp/historyLp')
        self.get_screenshot()

    def test_goto_dianping(self):
        """
        新房详情页，点击楼盘评论楼层的“全部点评”
        """
        self.page.scroll_to(3000, 500)
        self.delay(2)
        self.page.get_element('view[class="more newHouseTitle-r-sj"]', inner_text='全部点评').tap()

        self.verifyPageName('/page/taofangquan/lpdp/lpdp')
        self.get_screenshot()

    def test_goto_dianping_and_pinglun(self):
        """
        新房详情页，点击楼盘评论楼层的“我要评论”，并且发布评论
        """
        self.page.scroll_to(3000, 500)
        self.delay(2)
        self.page.get_element('view[class="iwantdpT"]', inner_text='我要评论').tap()

        self.verifyPageName('/page/taofangquan/writePingjia/writePingjia')
        self.get_screenshot()

    def test_goto_commenthouse(self):
        """
        新房详情页，点击热门楼盘楼层的第一个楼盘，进新房详情页
        """
        self.page.scroll_to(3000, 500)
        self.delay(2)
        self.page.get_element('image[class="commonNewHouseLi-l-img"]').tap()

        self.get_screenshot()

    def test_goto_buttom_im(self):
        """
        新房详情页面，点击底部的“在线咨询”
        """
        self.page.get_element('view[class="comBottomBar--link-button comBottomBar--im"]').tap()
        self.delay(3)

        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_z_click_buttom_call(self):
        """
        新房详情页面，点击底部的“拨打电话”
        """
        self.page.get_element('view[class="comBottomBar--link-button comBottomBar--call"]').tap()
        self.delay(1)
        self.verifyByScreenshot('xf/call.png')

    def test_click_buttom_yaohao(self):
        """
        新房详情页面，点击底部的“摇号”
        """
        self.page.get_element('navigator[class="comBottomBar--link-button comBottomBar--yaohao"]').tap()

        self.verifyPageName('/page/newhouse/historyLp/historyLp')
        self.get_screenshot()