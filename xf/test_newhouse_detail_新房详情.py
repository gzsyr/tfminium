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

    def test_backtop_展示锚点(self):
        """
        V6.30.X: 滑动至“最新开盘信息”头部，展示锚点
        """
        self.page.scroll_to(2000, 200)
        self.delay(6)

        self.get_screenshot()

    def test_backtop_楼盘详情TAB(self):
        """
        V6.30.X: 滑动至“最新开盘信息”头部,点击首个“楼盘详情”tab
        """
        self.page.scroll_to(2000, 200)
        self.delay(6)

        self.find_element('view[class="backtop_icon"]').tap()

    def test_goto_yfyj_点击房源(self):
        """
        V6.30.X: 点击一房一价的’第一个房源‘
        """
        self.find_element('view[class="yfyjList_cont"]').tap()

        self.verifyPageName('/page/newhouse/fd/fdfydetail')
        self.get_screenshot()

    def test_zbxx_周边学校_咨询(self):
        """
        V6.30.X: 点击周边学校的’咨询周边学校情况‘
        """
        self.page.scroll_to(3000, 200)
        self.delay(3)
        self.find_element('view[class="iwantdpT"]', inner_text='咨询周边学校情况').tap()

        self.get_screenshot()

    def test_func_最新动态(self):
        """
        V6.30.X: 功能入口, 最新动态
        """
        self.find_element('view[class="newHouseIconInLi-b"]', inner_text='最新动态').tap()

        self.verifyPageName('/page/newhouse/zxdt/zxdt')
        self.get_screenshot()

    def test_func_一房一价(self):
        """
        V6.30.X: 功能入口, 一房一价
        """
        self.find_element('view[class="newHouseIconInLi-b"]', inner_text='一房一价').tap()

        self.verifyPageName('/page/newhouse/fd/xkb')
        self.get_screenshot()

    def test_func_户型解析(self):
        """
        V6.30.X: 功能入口, 户型解析
        """
        self.find_element('view[class="newHouseIconInLi-b"]', inner_text='户型解析').tap()

        self.verifyPageName('/page/newhouse/hx/hxlist')
        self.get_screenshot()

    def test_func_楼盘点评(self):
        """
        V6.30.X: 功能入口, 楼盘点评
        """
        self.find_element('view[class="newHouseIconInLi-b"]', inner_text='楼盘点评').tap()

        self.verifyPageName('/page/taofangquan/lpdp/lpdp')
        self.get_screenshot()

    def test_func_楼盘详情(self):
        """
        V6.30.X: 功能入口, 楼盘详情
        """
        self.find_element('view[class="newHouseIconInLi-b"]', inner_text='楼盘详情').tap()

        self.verifyPageName('/page/newhouse/lpxx/lpxx')
        self.get_screenshot()

    def test_func_楼盘总平(self):
        """
        V6.30.X: 功能入口, 楼盘总平
        """
        self.find_element('view[class="iconList"]/view', inner_text='楼盘总平').tap()

        self.verifyPageName('/page/newhouse/fd/fdxx')
        self.get_screenshot()

    def test_func_开盘记录(self):
        """
        V6.30.X: 功能入口, 开盘记录
        """
        self.find_element('view[class="iconList"]/view', inner_text='开盘记录').tap()

        self.verifyPageName('/page/newhouse/historyLp/historyLp')
        self.get_screenshot()

    def test_func_航拍看房(self):
        """
        V6.30.X: 功能入口, 航拍看房
        """
        self.find_element('view[class="iconList"]/view', inner_text='航拍看房').tap()

        self.verifyPageName('/page/newhouse/xcny/photoalbum')
        self.get_screenshot()

    def test_func_置业顾问(self):
        """
        V6.30.X: 功能入口, 置业顾问
        """
        self.find_element('view[class="iconList"]/view', inner_text='置业顾问').tap()

        self.verifyPageName('/page/newhouse/zygw/list')
        self.get_screenshot()

    def test_func_摇号查询(self):
        """
        V6.30.X: 功能入口, 摇号查询
        """
        self.find_element('view[class="iconList"]/view', inner_text='摇号查询').tap()

        self.verifyPageName('/page/yaohao/result')
        self.get_screenshot()

    def test_func_VR看房(self):
        """
        V6.30.X: 功能入口, VR看房
        """
        self.find_element('view[class="iconList"]/view', inner_text='VR看房').tap()

        self.verifyPageName('/page/newhouse/xcny/photoalbum')
        self.get_screenshot()

    def test_func_楼盘相册(self):
        """
        V6.30.X: 功能入口, 楼盘相册
        """
        self.find_element('view[class="iconList"]/view', inner_text='楼盘相册').tap()

        self.verifyPageName('/page/newhouse/xcny/xcnylist')
        self.get_screenshot()

    def test_func_房贷计算(self):
        """
        V6.30.X: 功能入口, 房贷计算
        """
        self.find_element('view[class="iconList"]/view', inner_text='房贷计算').tap()

        self.verifyPageName('/page/tools/fdjsq/sd/index')
        self.get_screenshot()

    def test_func_购房资格(self):
        """
        V6.30.X: 功能入口, 购房资格
        """
        self.find_element('view[class="iconList"]/view', inner_text='购房资格').tap()

        self.verifyPageName('/page/tools/goufangzige/goufangzige')
        self.get_screenshot()

    def test_addr_点击区属(self):
        """
        V6.30.X: 点击楼盘价格下方的 行政区属
        """
        self.find_element('view[class="mr10"]').tap()

        self.verifyPageName('/page/newhouse/map/map')
        self.get_screenshot()

    def test_addr_点击楼盘地址(self):
        """
        V6.30.X: 点击楼盘价格下方的 楼盘地址
        """
        self.find_element('view[class="newHouseInfor-add-l tfLine1"]', inner_text='楼盘地址').tap()

        self.verifyPageName('/page/newhouse/map/map')
        self.get_screenshot()

    def test_addr_点击售楼部地址(self):
        """
        V6.30.X: 点击楼盘价格下方的 售楼部地址
        """
        self.find_element('view[class="newHouseInfor-add-l tfLine1"]', inner_text='售楼部地址').tap()

        self.verifyPageName('/page/newhouse/map/map')
        self.get_screenshot()

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

    def test_goto_xxxx_楼盘地址(self):
        """
        V6.30.X: 1005036, 新房详情页，详细信息楼层，点击 楼盘地址
        """
        self.find_element('view[class="jt_icon jt_icon_lpdz"]').tap()

        self.verifyPageName('/page/newhouse/map/map')
        self.get_screenshot()

    def test_check_baoming_优惠活动一(self):
        """
        V6.19.x: 第一个优惠活动的立即报名按钮
        """
        self.page.scroll_to(800, 200)

        tap = 'self.page.get_element(\'view[class= "promotions_btn_0"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '报名成功')

        self.get_screenshot()

    def test_check_baoming_优惠活动二(self):
        """
        V6.19.x: 第二个优惠活动的立即报名按钮
        """
        self.page.scroll_to(800, 200)

        tap = 'self.page.get_element(\'view[class= "promotions_btn_1"]\').tap()'

        self.verifyStr(True, self.getShowToast(tap), '报名成功')

        self.get_screenshot()

    def test_goto_photo_相册(self):
        """
        新房详情页页面，点击相册
        """
        self.find_element("view[class='newHouseBanner-more']").tap()

        self.verifyPageName('/page/newhouse/xcny/photoalbum')
        self.get_screenshot()

    def test_goto_photo_相册咨询(self):
        """
        V6.22.X: 1004113 新房楼盘详情页下  进入楼盘相册，点击页面底部的【咨询】按钮
        """
        self.find_element("view[class='newHouseBanner-more']").tap()
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
        新房详情页页面，点击订阅（图片右边的爱心按钮）
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

    def test_goto_dy_订阅楼盘(self):
        """
        新房详情页页面，点击楼盘名称旁边的闹铃 订阅楼盘
        """
        if self.page.element_is_exists('view[class="dy"]', inner_text='订阅楼盘'):
            self.find_element('view[class="dy"]', inner_text='订阅楼盘').tap()

            self.verifyStr(True, self.page.element_is_exists('view[class="dy removeDy"]'),
                           '取消订阅 ok')
        else:
            self.find_element('view[class="dy removeDy"]').tap()

            self.verifyStr(True, self.page.element_is_exists('view[class="dy"]', inner_text='订阅楼盘'),
                           '订阅 ok')

        self.get_screenshot()

    def delete_goto_fdjsq_房贷计算器(self):
        """
        V6.30.X: DELETE
        新房详情页页面，点击房贷计算器
        """
        self.find_element("view[class='newHouseInfor-price-r xfxq_jsq']").tap()

        self.verifyPageName('/page/tools/fdjsq/sd/index')
        self.get_screenshot()

    def delete_goto_addr_地址(self):
        """
        V6.30.X: DELETE, 由test_addr_点击楼盘地址 替代
        新房详情页页面，点击地址右箭头
        """
        self.find_element("view[class='newHouseInfor-add-r']").tap()

        self.get_screenshot()

        # 退出地图页面
        # self.input_value_by_mk(png='xf/mapreturn.png')   # del V6.22.X

    def test_goto_lpdp_gd_热评滚动(self):
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

        self.get_screenshot()

    def test_goto_zxdt_最新动态(self):
        """
        新房详情页页面，点击最新动态
        """
        self.find_element("view[class='infoTitle']/view", text_contains="楼盘动态").tap()

        self.verifyPageName('/page/newhouse/zxdt/zxdt')
        self.get_screenshot()

    def test_goto_zxdt_点击置业顾头像(self):
        """
        V6.29.X: 1004932，点击置业顾问头像
        """
        self.find_element('view[class="avator"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_zxdt_点击置业顾问正文(self):
        """
        V6.29.X: 1004932，点击置业顾问头像
        """
        self.find_element('view[class="contentWrap"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_zxdt_click_最新动态提问(self):
        """
        V6.21.X: 1003947   新房详情页页面，点击最新动态，点击提问
        """
        self.find_element("view[class='infoTitle']/view", text_contains="楼盘动态").tap()

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
        self.delay(3)

        self.get_screenshot()

    def test_goto_yfyj_一房一价咨询价格(self):
        """
        新房详情页页面，点击一房一价下方的’咨询房源价格‘
        """
        self.find_element("view[class='iwantdpT']", inner_text="咨询房源价格").tap()
        self.delay(3)

        self.get_screenshot()

    def test_goto_yfyj_click_一房一价提问(self):
        """
        V6.21.X: 1003947   新房详情页页面，点击一房一价，点击提问
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="一房一价").tap()

        # 到一房一价页面
        self.delay(8)
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
        self.delay(4)

        self.verifyPageName('/page/yaohao/publicity')
        self.get_screenshot()

    def test_goto_bmxh_摇号报名序号(self):
        """
        新房详情页页面，点击报名序号
        """
        self.find_element("view[class='disflex tfAlignC xf_xh_title']").tap()
        self.delay(4)
        self.get_screenshot()

    def delete_goto_bmyfyj_摇号一房一价(self):
        """
        V6.30.X: 删除
        新房详情页页面，点击最新摇号下方的一房一价
        """
        self.find_element("view[class='yifangyijia']").tap()

        self.verifyPageName('/page/newhouse/fd/xkb')
        self.get_screenshot()

    def test_goto_bmgfzl_摇号购房资料(self):
        """
        新房详情页页面，点击最新摇号下方的购房资料
        """
        self.find_element("view[class='latest-gfzl-btn']").tap()

        self.get_screenshot()

    def test_goto_lpdt_more_更多楼盘动态(self):
        """
        新房详情页页面，点击楼盘动态更多
        """
        self.find_element("view[class='infoTitle']/view", text_contains='楼盘动态').tap()

        self.verifyPageName('/page/newhouse/zxdt/zxdt')
        self.get_screenshot()

    def test_goto_xxxx_more_楼盘详细信息(self):
        """
        新房详情页页面，点击楼盘详细信息 更多
        """
        self.find_element("view[class='infoTitle']/view", inner_text='详细信息\n更多').tap()

        self.verifyPageName('/page/newhouse/lpxx/lpxx')
        self.get_screenshot()

    def test_goto_xxxx_more_IM_详细信息咨询(self):
        """
        V6.21.X: 1003947   新房详情页页面，详情详细信息位置，点击【咨询更多楼盘信息】按钮
        """
        self.find_element("view[class='iwantdpT']", inner_text="咨询更多楼盘信息").tap()

        self.delay(3)
        self.get_screenshot()

    def test_goto_zlhx_切换TAB(self):
        """
        V6.30.X:
        """
        self.page.scroll_to(2500, 200)
        self.delay(4)
        self.find_element('view[class="hxTab"]').tap()

        self.get_screenshot()

    def test_goto_zlhx_IM_主力户型咨询(self):
        """
        V6.21.X: 1003947   新房详情页页面，主力户型位置，点击【咨询低价】按钮
        """
        self.page.scroll_to(3000, 500)
        self.delay(4)
        self.find_element('view[class="consult_imicon_hx"]').tap()

        self.delay(3)
        self.get_screenshot()

    def test_goto_ldxq_楼栋详情提问(self):
        """
        V6.21.X: 1003947   新房详情页页面，分栋鸟瞰图点击更多，点击【提问】按钮
        """
        self.page.scroll_to(3000, 500)
        self.delay(10)
        self.find_element("view[class='infoTitle']/view", inner_text='分栋鸟瞰图\n更多').tap()

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
        self.delay(3)
        self.get_screenshot()
        # self.input_value_by_mk('xf/mapreturn.png')   # del V6.22.x

    def test_goto_wzzb_楼盘地址(self):
        """
        V6.30.X: 新房详情页，位置及周边楼层，点击“楼盘地址”
        """
        self.page.scroll_to(3500, 500)
        self.delay(4)

        self.find_element('view[class="label"]', inner_text='楼盘地址').tap()

        self.verifyPageName('/page/newhouse/map/map')
        self.get_screenshot()

    def test_goto_wzzb_售楼部地址(self):
        """
        V6.30.X: 新房详情页，位置及周边楼层，点击“售楼部地址”
        """
        self.page.scroll_to(3500, 500)
        self.delay(4)

        self.find_element('view[class="label"]', inner_text='售楼部地址').tap()

        self.verifyPageName('/page/newhouse/map/map')
        self.get_screenshot()

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
        self.delay(11)
        self.find_element('view[class="infoTitle"]/view', inner_text='价格分析\n更多').tap()

        self.verifyPageName('/page/newhouse/priceAnalyse/priceAnalyse')
        self.get_screenshot()

    def test_goto_kpjl_开盘记录(self):
        """
        新房详情页，点击开盘记录
        """
        self.page.scroll_to(3500, 500)
        self.delay(6)
        self.find_element('view[class="infoTitle"]/view', inner_text='开盘记录\n更多').tap()

        self.verifyPageName('/page/newhouse/historyLp/historyLp')
        self.get_screenshot()

    def test_goto_dianping_全部点评(self):
        """
        新房详情页，点击楼盘评论楼层的“更多”
        """
        self.page.scroll_to(3500, 500)
        self.delay(6)
        self.find_element('view[class="infoTitle_more"][data-eventid="2774"]').tap()

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
        self.page.scroll_to(6500, 500)
        self.delay(11)
        self.find_element('image[class="commonNewHouseLi-l-img"]').tap()
        self.delay(2)
        self.get_screenshot()

    def test_goto_buttom_im_在线咨询(self):
        """
        新房详情页面，点击底部的“在线咨询”
        """
        self.find_element('view[class="comBottomBar--link-button comBottomBar--im"]').tap()
        self.delay(3)

        self.get_screenshot()

    def test_zz_click_buttom_call_拨打电话(self):
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