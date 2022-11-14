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

    def test_goto_hotim_点击热门咨询(self):
        """
        V6.23.X: 点击“热门咨询”模块提问
        """
        self.page.scroll_to(2500, 500)
        self.delay(4)

        ele = self.find_element('view[class="hotConsult_content flex tfAlignC mb20"]')

        question = ele.attribute('data-question')
        ele.tap()

        self.delay(4)
        self.verifyPageName('/im/pages/chating/chating')
        imquestion = self.find_elements('view[class="record-chatting-item self"]')[-1].inner_wxml
        self.verifyContainsStr(question[0], imquestion)
        self.get_screenshot()

    def test_goto_xxxx_map_详细信息地图(self):
        """
        V6.23.X: 详细信息-楼盘区属点击“地图找房”
        """
        self.page.scroll_to(2500, 500)
        self.delay(4)

        self.find_element('view[class="newHouseXxxxLimap_icon"]').tap()

        self.verifyPageName('/page/newhouse/mapzf/mapzf')
        self.get_screenshot()

    def test_check_baoming_优惠活动一(self):
        """
        V6.19.x: 第一个优惠活动的立即报名按钮
        """
        self.page.scroll_to(1400, 500)

        tap = 'self.page.get_elements(\'image[class= "promotions_btn"]\')[0].tap()'
        self.verifyStr(True, self.getShowToast(tap), '报名成功')

        self.get_screenshot()

    def test_check_baoming_优惠活动二(self):
        """
        V6.19.x: 第二个优惠活动的立即报名按钮
        """
        self.page.scroll_to(1400, 500)

        tap = 'self.page.get_elements(\'image[class= "promotions_btn"]\')[1].tap()'

        self.verifyStr(True, self.getShowToast(tap), '报名成功')

        self.get_screenshot()

    def test_goto_photo_相册(self):
        """
        新房详情页页面，点击相册
        """
        self.find_element("image[class='newHouseBanner-img xfxq_xc']").tap()

        self.verifyPageName('/page/newhouse/xcny/photoalbum')
        self.get_screenshot()

    def test_goto_photo_相册咨询(self):
        """
        V6.22.X: 1004113 新房楼盘详情页下  进入楼盘相册，点击页面底部的【咨询】按钮
        """
        self.find_element("image[class='newHouseBanner-img xfxq_xc']").tap()
        self.delay(10)

        self.find_element('view[class="consultEntrance--consultIcon"]').tap()
        self.get_screenshot()

    def test_goto_pk_PK页面(self):
        """
        新房详情页页面，点击PK
        """
        self.find_element("navigator[class='pk-icon']").tap()

        self.verifyPageName('/page/newhouse/loupanPk/loupanPk')
        self.get_screenshot()

    def test_goto_dy_订阅(self):
        """
        新房详情页页面，点击订阅（爱心按钮）
        """
        if self.page.element_is_exists('view[class="dy-icon is_sub"]'):
            self.find_element('view[class="dy-icon is_sub"]').tap()

            self.verifyStr(True, self.page.element_is_exists('view[class="dy-icon"]'),
                           '取消订阅 ok')
        else:
            self.find_element('view[class="dy-icon"]').tap()

            self.verifyStr(True, self.page.element_is_exists('view[class="dy-icon is_sub"]'),
                           '订阅 ok')

        self.get_screenshot()

    def test_goto_fdjsq_房贷计算器(self):
        """
        新房详情页页面，点击房贷计算器
        """
        self.find_element("view[class='newHouseInfor-price-r xfxq_jsq']").tap()

        self.verifyPageName('/page/tools/fdjsq/sd/index')
        self.get_screenshot()

    def test_goto_addr_地址(self):
        """
        新房详情页页面，点击地址右箭头
        """
        self.find_element("view[class='newHouseInfor-add-r']").tap()

        self.get_screenshot()

        # 退出地图页面
        # self.input_value_by_mk(png='xf/mapreturn.png')   # del V6.22.X

    def test_goto_lpdp_gd(self):
        """
        新房详情页页面，点击楼盘点评滚动处，进入楼盘点评页面，点击第一条点评，进入点评详情页
        """
        self.find_element("view[class='tfFlex tfFlexSb tfAlignC dpEntry']").tap()
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

    def test_goto_zxdt_最新动态(self):
        """
        新房详情页页面，点击最新动态
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="最新动态").tap()

        self.verifyPageName('/page/newhouse/zxdt/zxdt')
        self.get_screenshot()

    def test_goto_zxdt_click_最新动态提问(self):
        """
        V6.21.X: 1003947   新房详情页页面，点击最新动态，点击提问
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="最新动态").tap()

        # 到最新动态页面
        self.delay(10)
        self.find_element('image[class="consultQuestion--askquestion_icon"]').tap()
        self.get_screenshot()

    def test_goto_hxjx_户型解析(self):
        """
        新房详情页页面，点击户型解析
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="户型解析").tap()

        self.verifyPageName('/page/newhouse/hx/hxlist')
        self.get_screenshot()

    def test_goto_hxjx_click_IM_户型解析咨询(self):
        """
        V6.21.X: 1003947   新房详情页页面，点击户型解析，点击咨询
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="户型解析").tap()

        # 到户型解析页面
        self.delay(10)
        self.find_element('view[class="consult_txt"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_lpxq_更多楼盘详情(self):
        """
        新房详情页页面，点击楼盘详情
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="楼盘详情").tap()

        self.verifyPageName('/page/newhouse/lpxx/lpxx')
        self.get_screenshot()

    def test_goto_yfyj_一房一价(self):
        """
        新房详情页页面，点击一房一价
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="一房一价").tap()

        self.verifyPageName('/page/newhouse/fd/xkb')
        self.get_screenshot()

    def test_goto_yfyj_click_一房一价提问(self):
        """
        V6.21.X: 1003947   新房详情页页面，点击一房一价，点击提问
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="一房一价").tap()

        # 到一房一价页面
        self.delay(6)
        self.find_element('image[class="consultQuestion--askquestion_icon"]').tap()
        self.get_screenshot()


    def test_goto_lpdp_楼盘点评(self):
        """
        新房详情页页面，点击楼盘点评
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="楼盘点评").tap()

        self.verifyPageName('/page/taofangquan/lpdp/lpdp')
        self.get_screenshot()

    def test_goto_msbm_马上报名(self):
        """
        新房详情页页面，点击马上报名(后台配置的）
        """
        self.find_element("view[class='ggweiR']", inner_text="马上报名").tap()

        self.get_screenshot()

    def test_goto_bmqc_摇号报名清册(self):
        """
        新房详情页页面，点击报名清册
        """
        self.find_element("view[class='left-icon disflex tfAlignC tfFlexC']").tap()

        self.verifyPageName('/page/yaohao/publicity')
        self.get_screenshot()

    def test_goto_bmxh_摇号报名序号(self):
        """
        新房详情页页面，点击报名序号
        """
        self.find_element("view[class='disflex tfAlignC xf_xh_title']").tap()

        self.get_screenshot()

    def test_goto_bmyfyj_摇号一房一价(self):
        """
        新房详情页页面，点击最新摇号下方的一房一价
        """
        self.find_element("view[class='yifangyijia']").tap()

        self.verifyPageName('/page/newhouse/fd/xkb')
        self.get_screenshot()

    def test_goto_bmgfzl_摇号购房资料(self):
        """
        新房详情页页面，点击最新摇号下方的购房资料
        """
        self.find_element("view[class='goufangziliao']").tap()

        self.get_screenshot()

    def test_goto_lpdt_more_更多楼盘动态(self):
        """
        新房详情页页面，点击楼盘动态更多
        """
        self.find_element("view[class='tfFlex tfFlexSb newHouseTitle-line xfxq_lpdt disflex-alignitems-center']").tap()

        self.verifyPageName('/page/newhouse/zxdt/zxdt')
        self.get_screenshot()

    def test_goto_xxxx_more_楼盘详细信息(self):
        """
        新房详情页页面，点击楼盘详细信息
        """
        self.find_element("view[class='tfFlex tfFlexSb newHouseTitle-line xfxq_lpdt']").tap()

        self.verifyPageName('/page/newhouse/lpxx/lpxx')
        self.get_screenshot()

    def test_goto_xxxx_more_IM_详细信息咨询(self):
        """
        V6.21.X: 1003947   新房详情页页面，详情详细信息位置，点击【咨询更多楼盘信息】按钮
        """
        self.find_element("view[class='iwantdpT']", inner_text="咨询更多楼盘信息").tap()

        self.delay(3)
        self.get_screenshot()

    def test_goto_zlhx_IM_主力户型咨询(self):
        """
        V6.21.X: 1003947   新房详情页页面，主力户型位置，点击【咨询低价】按钮
        """
        self.page.scroll_to(3000, 500)
        self.delay(4)
        self.find_element('view[class="consult_txt_hx"]', inner_text="咨询底价").tap()

        self.delay(3)
        self.get_screenshot()

    def test_goto_ldxq_楼栋详情提问(self):
        """
        V6.21.X: 1003947   新房详情页页面，分栋鸟瞰图点击更多，点击【提问】按钮
        """
        self.page.scroll_to(3000, 500)
        self.delay(10)
        self.find_element("view[class='newHouseTitle-l']", inner_text='分栋鸟瞰图').tap()

        # 进入分栋页面
        self.delay(5)
        self.find_element('image[class="consultQuestion--askquestion_icon"]').tap()

        self.get_screenshot()

    def test_goto_ldxq_IM_楼栋详情咨询(self):
        """
        V6.21.X: 1003947   新房详情页页面，分栋鸟瞰图位置，点击【咨询楼栋详情】按钮
        """
        self.page.scroll_to(3000, 500)
        self.delay(10)
        self.find_element("view[class='iwantdpT']", inner_text="咨询楼栋详情").tap()

        self.delay(3)
        self.get_screenshot()

    def test_goto_wzzb_dt_地图页(self):
        """
        新房详情页页面，点击位置周边下的地图
        """
        self.page.scroll_to(3500, 500)
        self.delay(4)

        # self.page.get_element('view[class="newHouseTitle-r xfxq_qbhx"][data-eventid="2648"]').tap()
        self.find_element('view[data-eventid="2648"]').tap()
        self.get_screenshot()
        # self.input_value_by_mk('xf/mapreturn.png')   # del V6.22.x

    def test_goto_wzzb_zbpt_周边配套导航(self):
        """
        V6.22.X: 1004113 新房楼盘详情页下的位置及周边下的地图  进入周边配套地图，点击页面底部的【导航】按钮
        """
        self.page.scroll_to(3500, 500)
        self.delay(6)

        # self.page.get_element('view[class="newHouseTitle-r xfxq_qbhx"][data-eventid="2648"]').tap()
        self.find_element('view[data-eventid="2648"]').tap()
        self.delay(10)

        self.find_element('view[class="mapnav"]').tap()
        self.get_screenshot()
        self.input_value_by_mk('xf/mapreturn.png')

    def test_goto_wzzb_zbpt_周边配套咨询(self):
        """
        V6.22.X: 1004113 新房楼盘详情页下的位置及周边下的地图  进入周边配套地图，点击页面底部的【咨询】按钮
        """
        self.page.scroll_to(3500, 500)
        self.delay(6)

        # self.page.get_element('view[class="newHouseTitle-r xfxq_qbhx"][data-eventid="2648"]').tap()
        self.find_element('view[data-eventid="2648"]').tap()
        self.delay(10)

        self.find_element('view[class="consultEntrance--consultBtn consultEntrance--'
                              'consultBtn2"]').tap()
        self.delay(2)
        self.get_screenshot()

    def test_goto_wzzb_dt_地图页咨询(self):
        """
        V6.22.X: 1004113  新房楼盘详情页下的位置及周边 点击【咨询周边配套及规划】按钮
        """
        self.page.scroll_to(3500, 500)
        self.delay(6)

        self.find_element("view[class='iwantdpT']", inner_text="咨询周边配套及规划").tap()

        self.delay(3)
        self.get_screenshot()

    def test_goto_jgfx_价格分析(self):
        """
        新房详情页，点击价格分析
        """
        self.page.scroll_to(3500, 500)
        self.delay(10)
        self.find_element('view[class="newHouseTitle-l"]', inner_text='价格分析').tap()

        self.verifyPageName('/page/newhouse/priceAnalyse/priceAnalyse')
        self.get_screenshot()

    def test_goto_kpjl_开盘记录(self):
        """
        新房详情页，点击开盘记录
        """
        self.page.scroll_to(3500, 500)
        self.delay(6)
        self.find_element('view[class="newHouseTitle-l"]', inner_text='开盘记录').tap()

        self.verifyPageName('/page/newhouse/historyLp/historyLp')
        self.get_screenshot()

    def test_goto_dianping_全部点评(self):
        """
        新房详情页，点击楼盘评论楼层的“全部点评”
        """
        self.page.scroll_to(3500, 500)
        self.delay(6)
        self.find_element('view[class="more newHouseTitle-r-sj"]', inner_text='全部点评').tap()

        self.verifyPageName('/page/taofangquan/lpdp/lpdp')
        self.get_screenshot()

    def test_goto_dianping_and_pinglun_我要评论(self):
        """
        新房详情页，点击楼盘评论楼层的“我要评论”，并且发布评论
        """
        self.page.scroll_to(3500, 500)
        self.delay(6)
        self.find_element('view[class="iwantdpT"]', inner_text='我要评论').tap()

        self.verifyPageName('/page/taofangquan/writePingjia/writePingjia')
        self.get_screenshot()

    def test_goto_commenthouse_热门楼盘(self):
        """
        新房详情页，点击热门楼盘楼层的第一个楼盘，进新房详情页
        """
        self.page.scroll_to(3500, 500)
        self.delay(6)
        self.find_element('image[class="commonNewHouseLi-l-img"]').tap()

        self.get_screenshot()

    def test_goto_buttom_im_在线咨询(self):
        """
        新房详情页面，点击底部的“在线咨询”
        """
        self.find_element('view[class="comBottomBar--link-button comBottomBar--im"]').tap()
        self.delay(3)

        self.get_screenshot()

    def test_z_click_buttom_call_拨打电话(self):
        """
        新房详情页面，点击底部的“拨打电话”
        """
        self.find_element('view[class="comBottomBar--link-button comBottomBar--call"]').tap()
        self.delay(1)
        self.verifyByScreenshot('xf/call.png')

    def test_click_buttom_yaohao_底部摇号按钮(self):
        """
        新房详情页面，点击底部的“摇号”
        """
        self.find_element('navigator[class="comBottomBar--link-button comBottomBar--yaohao"]').tap()

        self.verifyPageName('/page/newhouse/historyLp/historyLp')
        self.get_screenshot()