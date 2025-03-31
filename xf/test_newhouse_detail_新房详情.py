# add by zsy

from base.test_base import TestBase
from xf.func_cgjs import Funccgjs


class TestNewhouseDetail(TestBase):
    """
    新房详情页页面
    """
    def setUp(self) -> None:
        self.page_name = "/page/newhouse/detail?pinyin=shanhaiguojixzl&city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhouseDetail, self).setUp()
        self.delay(4)

    def click_caiguang(self):
        """
        点击 采光计算器
        """
        self.delay(10)
        self.find_element('/page/view/view[2]/scroll-view/view/view[12]/view/image').tap()

        self.delay(25)

    def test_goto_3D_噪音分析_and_订阅(self):
        """
        V7.02.X:add subscribe
        V6.41.X: 点击 3D分析处的 噪音分析
        """
        self.page.scroll_to(3000, 500)
        self.delay(4)
        self.find_element('image[class="btn_3d"][data-ysname="噪音分析"]').tap()

        self.get_screenshot('page')
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

        self.delay(5)
        # subscribe
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('subscribe')
        self.delay(2)
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('cancel')

    def test_goto_xxxx_日照分析_and_订阅(self):
        """
        V7.02.X:add subscribe
        V6.37.X: 点击详细信息的 日照分析
        """
        self.page.scroll_to(2500, 500)
        self.delay(4)

        self.find_element('view[class="newHouseXxxxLirzfx_icon"]').tap()

        self.get_screenshot('page')
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

        self.delay(5)
        # subscribe
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('subscribe')
        self.delay(2)
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('cancel')

    def test_goto_xxxx_more_日照分析(self):
        """
        V6.37.X: 点击 楼盘信息 更多 页面的 “日照分析”
        """
        self.goto_xxxx_more()

        self.find_element('view[class="lpxxDetailUl-li-r-link flex tfAlignC tfFlexC"]/view', inner_text='日照分析').tap()
        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_cg_采光计算器咨询采光(self):
        """
        V6.36.X: 点击采光计算器页面的 咨询采光
        """
        self.click_caiguang()
        self.find_element('picker').trigger("change", {"value": [15, 0]})
        self.set_pick_filter('picker[class="flex-1 t-r"]', 5)
        # self.find_element('input').input('9.9')
        self.input_value_by_mk('xf/cg_cg_im.png', '9.9', direction=1)
        self.delay(2)
        self.find_element('view[class="nextBtn"]').tap()
        self.delay(2)
        self.set_pick_filter('picker[class="flex-1 t-r"]', 2)
        # self.find_element('input').input('2')
        self.input_value_by_mk('xf/cg_lj.png', '2')
        self.find_element('view[class="countResult"]').tap()
        self.delay(6)
        self.find_element('view[class="codezx tfFlex tfAlignC"]').tap()

        # Funccgjs.select_city()
        # Funccgjs().select_total_floor()
        # Funccgjs().input_height()
        # Funccgjs().click_next()
        # Funccgjs().select_floor()
        # Funccgjs().input_distance()
        # Funccgjs().click_result()
        # Funccgjs().click_im()

        # # 选择 6层
        # self.set_pick_filter('picker[class="flex-1 t-r"]', 6)
        #
        # # 输入 单层高度
        # self.find_element('input').input('9.9')
        #
        # # 点击 下一步
        # self.find_element('view[class="nextBtn"]').tap()
        #
        # # 选择 居住楼层 3层
        # self.set_pick_filter('picker[class="flex-1 t-r"]', 2)
        #
        # # 输入楼距 2米
        # self.find_element('input').input('2')
        #
        # # 点击 开始计算
        # self.find_element('view[class="countResult"]').tap()
        #
        # # 点击 咨询采光
        # self.find_element('view[class="codezx tfFlex tfAlignC"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_10858')

    def test_cg_采光计算器咨询层高(self):
        """
        V6.36.X: 点击采光计算器页面的 咨询 按钮
        """
        self.click_caiguang()

        self.find_element('view[class="zxicon"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_10858')

    def test_func_采光计算器(self):
        """
        V6.35.x: 点击采光计算器
        """
        self.click_caiguang()

        self.get_screenshot()
        self.verifyPageName('/page/tools/cgjsq/cgjsq')

    def test_func_日照分析(self):
        """
        V6.37.X: 点击功能入口“日照分析”
        """
        self.find_element('/page/view/view[2]/scroll-view/view/view[1]/view/image').tap()
        self.delay(2)

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_func_周边规划(self):
        """
        V6.37.X: 点击功能入口“周边规划”
        """
        self.find_element('/page/view/view[2]/scroll-view/view/view[2]/view/image').tap()
        self.delay(2)

        self.get_screenshot()
        self.verifyPageName('/page/publicPages/zbgh/zbgh')

    def test_func_噪音分析(self):
        """
        V6.41.X: 点击功能入口“噪音分析”
        """
        self.find_element('/page/view/view[2]/scroll-view/view/view[3]/view/image').tap()
        self.delay(2)

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_click_photo_点击噪音(self):
        """
        V6.41.X: 点击楼盘相册的“噪音”，进入噪音分布表格页
        """
        self.find_element('view[class="newHouseBannerB-li"][data-type="105"]', inner_text='噪音').tap()
        self.delay(2)
        self.find_element('view[class="newHouseBanner-img-wrap"][data-type="105"]/image').tap()
        # self.find_element('swiper-item[data-type="104"]/image').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_click_photo_点击户型(self):
        """
        V6.40.X: 点击楼盘相册的“户型”，进入户型分布表格页
        """
        self.find_element('view[class="newHouseBannerB-li"][data-type="104"]', inner_text='户型').tap()
        self.delay(2)
        self.find_element('view[class="newHouseBanner-img-wrap"][data-type="104"]/image').tap()
        # self.find_element('swiper-item[data-type="104"]/image').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')
    def test_click_photo_点击楼距(self):
        """
        V6.39.X: 点击楼盘相册的“楼距”，进入楼距页面
        """
        self.find_element('view[class="newHouseBannerB-li"][data-type="103"]', inner_text='楼距').tap()
        self.delay(2)
        self.find_element('view[class="newHouseBanner-img-wrap"][data-type="103"]/image').tap()
        # self.find_element('swiper-item[data-type="103"]/image').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_click_photo_点击日照分析(self):
        """
        V6.37.x: 点击楼盘相册的“日照”，进入日照分析页面
        """
        self.find_element('view[class="newHouseBannerB-li"][data-type="102"]', inner_text='日照').tap()
        self.delay(2)
        self.find_element('view[class="newHouseBanner-img-wrap"][data-type="102"]/image').tap()
        # self.find_element('swiper-item[data-type="102"]/image').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_click_photo_点击总平(self):
        """
        V6.32.X: 点击楼盘相册上面显示的“总平”
        """
        self.find_element('view[class="newHouseBannerB-li"][data-type="101"]', inner_text='总平').tap()
        self.delay(2)
        self.find_element('view[class="newHouseBanner-img-wrap"][data-type="101"]/image').tap()
        # self.find_element('swiper-item[data-type="101"]/image').tap()

        self.verifyPageName('/page/newhouse/fd/fdxx')
        self.get_screenshot()

    def goto_fbs_more(self):
        """
        点击“房博士解读”楼层 更多
        """
        self.page.scroll_to(4000, 200)
        self.delay(6)

        self.find_element("view[class='infoTitle']/view", text_contains='房博士解读').tap()
        return self

    def goto_fbs_detail(self):
        """
        房博士问答列表页面，点击回答内容
        """
        self.delay(9)
        self.find_element('view[class="wdLiC-intro tfline2"]').tap()
        return self

    def test_goto_fbs_more_房博士解读更多(self):
        """
        V6.32.X: 点击“房博士解读”楼层 更多
        """
        self.goto_fbs_more()

        self.verifyPageName('/fbs/lpquestionlist/lpquestionlist')
        self.get_screenshot()

    def test_goto_fbs_more_点击回答内容(self):
        """
        V6.32.X: 问答列表，点击问答内容
        """
        self.goto_fbs_more().goto_fbs_detail()

        self.verifyPageName('/fbs/detail/detail')
        self.get_screenshot()

    def test_goto_fbs_点击内容(self):
        """
        V6.32.X: 新房详情页，点击房博士解读楼层，点击内容
        """
        self.page.scroll_to(8000, 200)

        self.delay(6)
        self.find_element('view[class="p-flex-item fbsjdTLi-da-t tfline4"]').tap()

        self.verifyPageName('/fbs/detail/detail')
        self.get_screenshot()

    def test_goto_fbs_more_列表更多问答(self):
        """
        V6.32.X: 问答列表，点击 更多问答
        """
        self.goto_fbs_more()
        self.delay(8)

        self.find_element('view[class="showAllqus tfFlex tfAlignC tfFlexC"]').tap()
        self.get_screenshot()

    def test_goto_fbs_more_更多问答切换TAB(self):
        """
        V6.32.X: 问答列表，点击 更多问答，进入全部回答页面，点击TAB
        """
        self.goto_fbs_more()
        self.delay(6)

        self.find_element('view[class="showAllqus tfFlex tfAlignC tfFlexC"]').tap()
        self.delay(6)
        self.find_element('view[class="selectLi"]').tap()
        self.get_screenshot()

    def test_backtop_展示锚点(self):
        """
        V6.30.X: 滑动至“最新开盘信息”头部，展示锚点
        """
        self.page.scroll_to(2000, 200)
        self.delay(6)

        self.get_screenshot()

    def delete_backtop_楼盘详情TAB(self):
        """
        V6.30.X: 滑动至“最新开盘信息”头部,点击首个“楼盘详情”tab
        6.32.x: 删除该功能
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
        self.find_element('view[class="iwantdpT"]', inner_text='周边学校咨询z').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'fxzj_15')
        self.get_screenshot()

    def test_func_最新动态(self):
        """
        V6.30.X: 功能入口, 最新动态
        """
        self.find_element('view[class="newHouseIconInLi-b"]', inner_text='最新动态').tap()

        self.verifyPageName('/page/newhouse/zxdt/zxdt')
        self.get_screenshot()

    def click_func_yfyj(self):
        """
        功能入口，点击 一房一价
        """
        self.find_element('view[class="newHouseIconInLi-b"]', inner_text='一房一价').tap()

        return self

    def test_func_一房一价(self):
        """
        V6.30.X: 功能入口, 一房一价
        """
        self.click_func_yfyj()

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

        self.get_screenshot()
        self.verifyPageName('/page/taofangquan/lpdp/lpdp')

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
        self.find_element('/page/view/view[2]/scroll-view/view/view[5]/view/image').tap()

        self.verifyPageName('/page/newhouse/fd/fdxx')
        self.get_screenshot()

    def test_func_开盘记录(self):
        """
        V6.30.X: 功能入口, 开盘记录
        """
        self.find_element('/page/view/view[2]/scroll-view/view/view[4]/view/image').tap()

        self.verifyPageName('/page/newhouse/historyLp/historyLp')
        self.get_screenshot()

    def test_func_航拍看房(self):
        """
        V6.30.X: 功能入口, 航拍看房
        """
        self.find_element('/page/view/view[2]/scroll-view/view/view[6]/view/image').tap()

        self.verifyPageName('/page/newhouse/xcny/photoalbum')
        self.get_screenshot()

    def test_func_置业顾问(self):
        """
        V6.30.X: 功能入口, 置业顾问
        """
        self.find_element('/page/view/view[2]/scroll-view/view/view[7]/view/image').tap()

        self.verifyPageName('/page/newhouse/zygw/list')
        self.get_screenshot()

    def test_func_摇号查询(self):
        """
        V6.30.X: 功能入口, 摇号查询
        """
        self.find_element('/page/view/view[2]/scroll-view/view/view[8]/view/image').tap()

        self.get_screenshot()
        self.verifyPageName('/page/yaohao/result')

    def test_func_VR看房(self):
        """
        V6.30.X: 功能入口, VR看房
        """
        self.delay(2)
        self.find_element('/page/view/view[2]/scroll-view/view/view[9]/view/image').click()

        self.verifyPageName('/page/newhouse/xcny/photoalbum')
        self.get_screenshot()

    def test_func_楼盘相册(self):
        """
        V6.30.X: 功能入口, 楼盘相册
        """
        self.find_element('/page/view/view[2]/scroll-view/view/view[10]/view/image').tap()

        self.verifyPageName('/page/newhouse/xcny/xcnylist')
        self.get_screenshot()

    def test_func_房贷计算(self):
        """
        V6.30.X: 功能入口, 房贷计算
        """
        self.find_element('/page/view/view[2]/scroll-view/view/view[11]/view/image').tap()

        self.verifyPageName('/page/tools/fdjsq/sd/index')
        self.get_screenshot()

    def test_func_购房资格(self):
        """
        V6.30.X: 功能入口, 购房资格
        """
        self.find_element('/page/view/view[2]/scroll-view/view/view[13]/view/image').tap()

        self.verifyPageName('/page/tools/goufangzige/goufangzige')
        self.get_screenshot()

    def test_addr_点击区属(self):
        """
        V6.30.X: 点击楼盘价格下方的 行政区属
        """
        self.find_element('view[class="mr10"]').tap()

        self.verifyPageName('/page/publicPages/map/map')
        self.get_screenshot()

    def test_addr_点击楼盘地址(self):
        """
        V6.30.X: 点击楼盘价格下方的 楼盘地址
        """
        self.find_element('view[class="newHouseInfor-add-l tfLine1"]', inner_text='楼盘地址').tap()

        self.verifyPageName('/page/publicPages/map/map')
        self.get_screenshot()

    def test_addr_点击售楼部地址(self):
        """
        V6.30.X: 点击楼盘价格下方的 售楼部地址
        """
        self.find_element('view[class="newHouseInfor-add-l tfLine1"]', inner_text='售楼部地址').tap()

        self.verifyPageName('/page/publicPages/map/map')
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
        self.verifyPageParams('chatTo', 'fxzj_15')
        self.get_screenshot()

    def test_check_baoming_优惠活动一(self):
        """
        V6.19.x: 第一个优惠活动的立即报名按钮
        """
        self.page.scroll_to(800, 200)
        self.delay(3)

        try:
            tap = 'self.page.get_element(\'view[class= "promotions_btn_0"]\').tap()'
        except:
            self.find_elements('view[class="title-im promotions_im"]')[0].tap()

        self.get_screenshot()

    def test_check_baoming_优惠活动二(self):
        """
        V6.19.x: 第二个优惠活动的立即报名按钮
        """
        self.page.scroll_to(800, 200)
        self.delay(3)

        try:
            tap = 'self.page.get_element(\'view[class= "promotions_btn_1"]\').tap()'
        except:
            self.find_elements('view[class="title-im promotions_im"]')[1].tap()

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
        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_10858')
        self.get_screenshot()

    def goto_pk(self):
        """
        新房详情页页面，点击PK
        """
        self.find_element("navigator[class='pk-icon']").tap()
        self.delay(5)

        self.verifyPageName('/page/newhouse/loupanPk/loupanPk')
        return self

    def add_house(self):
        """
        PK页面，点击添加楼盘
        """
        self.find_element('view[class="lpBtn1"]').tap()
        self.delay(4)
        self.verifyPageName('/page/newhouse/loupanPk/loapanAdd')

        return self

    def select_house(self):
        """
        PK页面，输入楼盘搜索并选择
        """
        self.find_element('input[class="searchTR-input"]').input('格林春天')
        self.delay(6)
        # self.find_element('view[class="searchBLi-c disflex-flex-shrink-0"]').tap()

        tap = 'self.find_element(\'view[class="searchBLi-c disflex-flex-shrink-0"]\').tap()'
        if self.getShowToast(tap):
            self.app.navigate_back()

        self.verifyPageName('/page/newhouse/loupanPk/loupanPk')
        
        return self

    def delete_house(self):
        """
        PK页面，删除楼盘
        """
        self.find_element('checkbox[aria-disabled="false"]').tap()
        self.find_element('view[class="lpTxt1"]').tap()
        
        return self

    def select_pk(self):
        """
        选择第一个楼盘，点击“对比”
        """
        self.delay(4)
        self.find_element('checkbox[aria-disabled="false"]').tap()
        self.delay(4)
        self.find_element('view[class="disflex-flex-shrink-0 lpBtn2 lpBtnAct"]').tap()
        self.delay(7)
        self.verifyPageName('/page/newhouse/loupanPk/pkResult')

    def test_goto_pk_PK页面(self):
        self.goto_pk()
        self.get_screenshot()

    def test_PK_01_点击添加楼盘(self):
        """
        V6.32.X: pk页面，点击“添加楼盘”
        """
        self.goto_pk().add_house()

        self.get_screenshot()

    def test_PK_02_加入PK楼盘(self):
        """
        V6.32.X: pk页面，点击“添加楼盘”，输入“格林春天”选择“格林春天2”，加入对比列表
        """
        self.goto_pk().add_house().select_house()

        self.get_screenshot()

    def test_PK_08_删除楼盘(self):
        """
        V6.32.X: pk页面，删除第一个楼盘
        """
        self.goto_pk().delete_house()
        
        self.get_screenshot()

    def test_PK_04_选择楼盘对比(self):
        """
        V6.32.X: pk页面，选择楼盘，点击“对比”
        """
        self.goto_pk().add_house().select_house().select_pk()

        self.get_screenshot()

    def test_PK_05_点击楼盘咨询(self):
        """
        V6.32.X: pk结果页面，点击楼盘的“咨询详情”
        """
        self.goto_pk().add_house().select_house().select_pk()

        self.find_element('view[class="to_im"]').tap()

        self.get_screenshot()

    def test_PK_06_点击热门咨询(self):
        """
        V6.32.X: pk结果页面，点击下面的热门咨询
        """
        self.goto_pk().add_house().select_house().select_pk()

        self.find_element('view[class="tfLine1"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_10858')
        self.get_screenshot()

    def test_PK_07_点击更多内容(self):
        """
        V6.32.X: pk结果页面，点击下面的更多内容
        V6.47.x：pk结果页面，点击楼盘名称
        """
        self.goto_pk().add_house().select_house().select_pk()

        self.find_element('image[class="pkPic1"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_goto_dy_订阅(self):
        """
        新房详情页页面，点击订阅（图片右边的爱心按钮）
        """
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()

        self.get_screenshot()

    def test_goto_dy_订阅楼盘(self):
        """
        新房详情页页面，点击楼盘名称旁边的闹铃 订阅楼盘
        """
        self.find_elements('view[class="subscribe--pa subscribe--subscribe"]')[1].tap()

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
        self.page.scroll_to(3550, 200)
        self.delay(10)
        try:
            self.find_element('view[class="avator"]').tap()
            self.delay(3)
            self.get_screenshot()
        except:
            self.get_screenshot()

    def test_goto_zxdt_点击置业顾问正文(self):
        """
        V6.29.X: 1004932，点击置业顾问头像
        """
        self.page.scroll_to(3550, 200)
        self.delay(10)
        try:
            self.find_element('view[class="contentWrap"]').tap()
            self.delay(3)
            self.get_screenshot()
        except:
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

    def test_goto_hxjx_户型解析_and_订阅(self):
        """
        V7.02.X:add subscribe
        新房详情页页面，点击户型解析
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="户型解析").tap()

        self.verifyPageName('/page/newhouse/hx/hxlist')
        self.get_screenshot('list')

        # 到户型解析页面
        self.delay(10)

        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('subscribe')
        self.delay(2)
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('cancel')

    def test_goto_hxjx_点击户型分布图(self):
        """
        V6.40.x: 新房详情页页面，点击户型解析，点击顶部缩图
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="户型解析").tap()

        # 到户型解析页面
        self.delay(10)

        self.find_element('view[class="imgwrap"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

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

    def test_goto_yfyj_一房一价_and_订阅(self):
        """
        V7.02.X:add subscribe
        新房详情页页面，点击一房一价
        """
        self.find_element("view[class='newHouseIconInLi-b']", inner_text="一房一价").tap()
        self.delay(5)

        self.get_screenshot('page')

        # subscribe
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('subscribe')
        self.delay(2)
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('cancel')

    def test_goto_yfyj_一房一价咨询价格(self):
        """
        新房详情页页面，点击一房一价下方的’咨询房源价格‘
        """
        self.find_element("view[class='iwantdpT']", inner_text="一房一价咨询z").tap()
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

    def yfyj_select(self, type='loudong', select=None):
        """
        一房一价页面，切换至“列表”，对楼栋、户型、楼层、状态进行筛选
        """
        self.delay(9)
        self.find_element('view[class="fixedR-icon"]').tap()
        self.delay(9)
        if type == 'loudong':
            self.find_element(f'view[class="p-flex-item p-28 z-select"][data-type="{type}"]').tap()
        else:
            self.find_element(f'view[class="p-flex-item p-28"][data-type="{type}"]').tap()
        self.delay(6)
        # 选择第一个选项
        try:
            self.find_element('view[class="popup_select_icon"]').tap()
        except:
            print('已勾选')
        # 点击“确定”
        self.find_element('view[class="popup_btn_confirm"]').tap()

    def test_goto_yfyj_筛选楼栋(self):
        """
        V6.32.X: 新房详情页-一房一价，点击列表，切换至列表页，选择楼栋筛选
        """
        self.click_func_yfyj().yfyj_select(type='loudong')

        self.get_screenshot()

    def test_goto_yfyj_筛选户型(self):
        """
        V6.32.X: 新房详情页-一房一价，点击列表，切换至列表页，选择户型筛选
        """
        self.click_func_yfyj().yfyj_select(type='hx')

        self.get_screenshot()

    def test_goto_yfyj_筛选楼层(self):
        """
        V6.32.X: 新房详情页-一房一价，点击列表，切换至列表页，选择楼层筛选
        """
        self.click_func_yfyj().yfyj_select(type='floor')

        self.get_screenshot()

    def test_goto_yfyj_筛选状态(self):
        """
        V6.32.X: 新房详情页-一房一价，点击列表，切换至列表页，选择状态筛选
        """
        self.click_func_yfyj().yfyj_select(type='state')

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

        self.delay(4)
        self.find_element("view[class='left-icon disflex tfAlignC tfFlexC']").tap()
        self.delay(4)

        self.verifyPageName('/page/yaohao/publicity')
        self.get_screenshot()

    def test_goto_bmxh_摇号报名序号(self):
        """
        新房详情页页面，点击报名序号
        """
        self.delay(4)
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


    def test_goto_xxxx_楼距分析(self):
        """
        V6.39.X: 点击 详细信息 “楼距分析”，进入楼距页面
        """
        self.page.scroll_to(2500, 500)
        self.delay(4)

        self.find_element('view[class="newHouseXxxxLimap flex tfAlignC tfFlexC"][data-ysposition="详细信息"][data-ysname="楼距分析"]').tap()
        self.delay(2)
        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

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

        self.verifyPageName('/page/publicPages/map/map')
        self.get_screenshot()

    def goto_xxxx_more(self):
        """
        点击楼盘详细信息 更多
        """
        self.find_element("view[class='infoTitle']/view", inner_text='详细信息\n更多').tap()

        self.verifyPageName('/page/newhouse/lpxx/lpxx')

    def test_goto_xxxx_more_楼盘详细信息(self):
        """
        新房详情页页面，点击楼盘详细信息 更多
        """
        self.goto_xxxx_more()

        self.get_screenshot()

    def test_goto_xxxx_more_滑动显示锚点(self):
        """
        V6.32.X: 楼盘详细信息页面，滑动页面，显示锚点
        """
        self.goto_xxxx_more()

        self.page.scroll_to(800, 200)

        self.delay(2)
        self.verifyStr(True, self.element_is_exist('view[class="anchor_scroll_item"]'),
                       '显示锚点')

        self.get_screenshot()

    def test_goto_xxxx_more_点击详情(self):
        """
        V6.32.X: 楼盘详细信息页面，点击楼盘名旁边的“详情”
        """
        self.goto_xxxx_more()
        self.find_element('view[class="tolpdetail"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_goto_xxxx_more_点击楼盘地址(self):
        """
        V6.32.X: 楼盘详细信息页面，点击楼盘地址
        """
        self.goto_xxxx_more()

        self.find_element('view[class="jt_icon jt_icon_lpdz"]').tap()

        self.verifyPageName('/page/publicPages/map/map')
        self.get_screenshot()

    def test_goto_xxxx_more_IM_详细信息咨询(self):
        """
        V6.21.X: 1003947   新房详情页页面，详情详细信息位置，点击【咨询更多楼盘信息】按钮
        """
        self.find_element("view[class='iwantdpT']", inner_text="楼盘详情咨询z").tap()


        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'fxzj_15')
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


        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'fxzj_15')
        self.get_screenshot()

    def test_goto_ldxq_点击户型分布_and_订阅(self):
        """
        V7.02.X:add subscribe
        V6.39.X: 新房详情页页面，分栋鸟瞰图点，点击【户型分布】按钮
        """
        self.page.scroll_to(6000, 500)
        self.delay(12)

        self.find_element('view[class="newHouseFdnkt_hxfx_short newHouseFdnkt_fx"]').tap()

        self.get_screenshot('page')
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

        self.delay(5)
        # subscribe
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('subscribe')
        self.delay(2)
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('cancel')

    def test_goto_ldxq_点击楼距分析_and_订阅(self):
        """
        V7.02.X:add subscribe
        V6.39.X: 新房详情页页面，分栋鸟瞰图点，点击【楼距分析】按钮
        """
        self.page.scroll_to(6000, 500)
        self.delay(12)

        self.find_element('view[class="newHouseFdnkt_ljfx_short newHouseFdnkt_fx"]').tap()

        self.get_screenshot('page')
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

        self.delay(5)
        # subscribe
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('subscribe')
        self.delay(2)
        self.find_element('view[class="subscribe--pa subscribe--subscribe"]').tap()
        self.get_screenshot('cancel')

    def test_goto_ldxq_楼栋详情_户型分布(self):
        """
        V6.39.X: 新房详情页页面，分栋鸟瞰图点，点击【户型分布】按钮
        """
        self.page.scroll_to(6000, 500)
        self.delay(12)
        self.find_element("view[class='infoTitle']/view", inner_text='分栋鸟瞰图\n更多').tap()

        # 进入分栋页面
        self.delay(10)
        self.find_element('view[class="z-map-icon"]').tap()
        self.delay(5)
        self.find_element('view[class="ljfx_wrap flex tfAlignC tfFlexC"]/view', inner_text='户型分布').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_goto_ldxq_楼栋详情_楼距分析(self):
        """
        V6.39.X: 新房详情页页面，分栋鸟瞰图点，点击【楼距分析】按钮
        """
        self.page.scroll_to(6000, 500)
        self.delay(12)
        self.find_element("view[class='infoTitle']/view", inner_text='分栋鸟瞰图\n更多').tap()

        # 进入分栋页面
        self.delay(10)
        self.find_element('view[class="ljfx_wrap flex tfAlignC tfFlexC"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_goto_ldxq_楼栋详情提问(self):
        """
        V6.21.X: 1003947   新房详情页页面，分栋鸟瞰图点击更多，点击【提问】按钮
        """
        self.page.scroll_to(6000, 500)
        self.delay(12)
        self.find_element("view[class='infoTitle']/view", inner_text='分栋鸟瞰图\n更多').tap()

        # 进入分栋页面
        self.delay(10)
        self.find_element('image[class="consultQuestion--askquestion_icon"]').tap()

        self.get_screenshot()

    def test_goto_ldxq_IM_楼栋详情咨询(self):
        """
        V6.21.X: 1003947   新房详情页页面，分栋鸟瞰图位置，点击【咨询楼栋详情】按钮
        """
        self.page.scroll_to(6000, 500)
        self.delay(10)
        self.find_element("view[class='iwantdpT']", inner_text="鸟瞰图咨询z").tap()

        self.delay(3)
        self.get_screenshot()

    def test_goto_wzzb_点击位置周边(self):
        """
        新房详情页页面，点击位置周边标题
        """
        self.page.scroll_to(3500, 500)
        self.delay(4)

        # self.page.get_element('view[class="newHouseTitle-r xfxq_qbhx"][data-eventid="2648"]').tap()
        self.find_element('view[data-eventid="2648"]').tap()
        self.delay(3)
        self.get_screenshot()
        # self.input_value_by_mk('xf/mapreturn.png')   # del V6.22.x

    def test_goto_wzzb_点击楼盘地址(self):
        """
        V6.30.X: 新房详情页，位置及周边楼层，点击“楼盘地址”
        """
        self.page.scroll_to(4500, 500)
        self.delay(4)

        self.find_element('view[class="label"]', inner_text='楼盘地址').tap()

        self.verifyPageName('/page/publicPages/map/map')
        self.get_screenshot()

    def test_goto_wzzb_点击地图(self):
        """
        V6.30.X: 新房详情页，位置及周边楼层，点击地图
        """
        self.page.scroll_to(4500, 500)
        self.delay(15)

        # self.find_element('//*[@id="map"]').tap()
        # self.find_element('view[class="mapNearDes"]').click()
        # self.find_element('map[class="newHouseMap-map-img"]').tap()
        self.input_value_by_mk('xf/click_map.png')
        self.delay(3)

        self.get_screenshot()
        self.verifyPageName('/page/publicPages/map/map')

    def test_goto_wzzb_点击教育的文字(self):
        """
        V6.30.X: 新房详情页，位置及周边楼层，点击教育下的文字
        """
        self.page.scroll_to(4800, 500)
        self.delay(15)

        # self.find_element('//*[@id="map"]').tap()
        # self.find_element('view[class="mapNearDes"]').click()
        # self.find_element('view[class="newHouseMap-map"]').tap()
        self.input_value_by_mk('xf/click_map_text.png')
        self.delay(3)

        self.get_screenshot()
        self.verifyPageName('/page/publicPages/map/map')

    def test_goto_wzzb_和切换(self):
        """
        V6.36.X: 新房详情页，位置及周边，tab切换
        """
        self.page.scroll_to(4800, 500)
        self.delay(4)

        self.get_screenshot('位置及周边当前页面')

        self.find_element('view[class="mapNearTab-t"]', inner_text='休闲').tap()
        self.get_screenshot()


    def test_goto_wzzb_售楼部地址(self):
        """
        V6.30.X: 新房详情页，位置及周边楼层，点击“售楼部地址”
        """
        self.page.scroll_to(3500, 500)
        self.delay(4)

        self.find_element('view[class="label"]', inner_text='售楼部地址').tap()

        self.verifyPageName('/page/publicPages/map/map')
        self.get_screenshot()

    def delete_test_goto_wzzb_zbpt_周边配套导航(self):
        """
        V6.22.X: 1004113 新房楼盘详情页下的位置及周边下的地图  进入周边配套地图，点击页面底部的【导航】按钮
        V6.36.X:点击打开app
        """
        self.page.scroll_to(4800, 500)
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
        self.page.scroll_to(4800, 500)
        self.delay(6)

        # self.page.get_element('view[class="newHouseTitle-r xfxq_qbhx"][data-eventid="2648"]').tap()
        self.find_element('view[data-eventid="2648"]').tap()
        self.delay(10)

        self.find_element('view[class="center chat"]').tap()

        self.delay(8)
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_10858')
        self.get_screenshot()

    def test_goto_wzzb_zbpt_周边配套切换(self):
        """
        V6.36.X: 1004113 新房楼盘详情页下的位置及周边下的地图  进入周边配套地图，切换tab
        """
        self.page.scroll_to(4800, 500)
        self.delay(6)

        # self.page.get_element('view[class="newHouseTitle-r xfxq_qbhx"][data-eventid="2648"]').tap()
        self.find_element('view[data-eventid="2648"]').tap()
        self.delay(10)

        self.find_element('view[class="i_c column poiType"]', inner_text='休闲').tap()
        self.get_screenshot()

    def test_goto_wzzb_zbpt_周边配套点击高亮(self):
        """
        V6.36.X: 1004113 新房楼盘详情页下的位置及周边下的地图  进入周边配套地图，点击tab下内容高亮
        """
        self.page.scroll_to(4800, 500)
        self.delay(6)

        # self.page.get_element('view[class="newHouseTitle-r xfxq_qbhx"][data-eventid="2648"]').tap()
        self.find_element('view[data-eventid="2648"]').tap()
        self.delay(10)

        self.find_element('view[class="line_1 address"]').tap()
        self.delay(1)
        self.get_screenshot('高亮')

        self.find_element('view[class="line_1 address"]').tap()
        self.delay(1)
        self.get_screenshot('取消高亮')

    def test_goto_wzzb_zbpt_周边配套点击箭头(self):
        """
        V6.36.X: 1004113 新房楼盘详情页下的位置及周边下的地图  进入周边配套地图，点击tab下内容高亮
        """
        self.page.scroll_to(4800, 500)
        self.delay(6)

        # self.page.get_element('view[class="newHouseTitle-r xfxq_qbhx"][data-eventid="2648"]').tap()
        self.find_element('view[data-eventid="2648"]').tap()
        self.delay(10)

        self.find_element('view[class="arrowOpen"]').tap()
        self.delay(3)
        self.get_screenshot('展开更多')

        self.find_element('view[class="arrowClose"]').tap()
        self.delay(3)
        self.get_screenshot('收起')

    def test_goto_wzzb_dt_地图页咨询(self):
        """
        V6.22.X: 1004113  新房楼盘详情页下的位置及周边 点击【咨询周边配套及规划】按钮
        """
        self.page.scroll_to(3500, 500)
        self.delay(6)

        self.find_element("view[class='iwantdpT']", inner_text="位置周边咨询z").tap()


        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'fxzj_15')
        self.get_screenshot()

    def test_goto_jgfx_价格分析(self):
        """
        新房详情页，点击价格分析
        """
        self.page.scroll_to(3500, 500)
        self.delay(12)
        self.find_element('view[class="infoTitle"]/view', inner_text='价格分析\n更多').tap()

        self.verifyPageName('/page/newhouse/priceAnalyse/priceAnalyse')
        self.get_screenshot()

    def test_goto_kpxx_户型分布(self):
        """
        V6.40.x: 点击最新开盘信息模块户型分布
        """
        self.find_element('view[class="newHouseXxxxLimap flex tfAlignC tfFlexC"][data-ysposition="最新开盘信息"][data-ysname="户型分布"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_goto_kpxx_楼距分析(self):
        """
        V6.40.X: 点击最新开盘信息模块楼距分析
        """
        self.find_element(
            'view[class="newHouseXxxxLimap flex tfAlignC tfFlexC"][data-ysposition="最新开盘信息"][data-ysname="楼距分析"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

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

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_10858')
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