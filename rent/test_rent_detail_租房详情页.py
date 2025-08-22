from ddt import file_data, ddt
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt
class Testrentdetail(TestBase):
    """
    租房详情页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/r_detail/detail?rentId=104329493&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentdetail, self).setUp()
        print("Testrentdetail setup")

    def checkSendCard(self):
        """
        是不是发送到了咨询卡片
        """
        self.verifyByScreenshot('rent/rentdetailchecksendcard.png')

    def test_20_goto_photo_点击相册(self):
        """
        点击相册
        """
        elms = self.page.get_element('banner').get_elements('view')
        elms[0].get_element('swiper').get_element('swiper-item').tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)

    def test_01_goto_collect_点击收藏取消收藏(self):
        """
        点击收藏
        :return:
        """
        e = self.page.get_element('view[class="pa center collect"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)
        """
        取消收藏
        """
        e1 = self.page.get_element('view[class="pa center collect"]')
        e1.tap()
        self.delay(3)
        self.get_screenshot()

    def test_99_goto_share_点击分享(self):
        """
        点击分享
        :return:
        """
        e = self.page.get_element('button[class="pa center share"]')
        e.tap()
        # self.get_screenshot()
        self.delay(2)
        self.get_screenshot()
        self.delay(1)

    def test_02_click_mapadd_标题下坐标地址(self):
        """
        点击标题下坐标地址
        :return:
        """
        m = self.page.element_is_exists('text[class="blockName"]')
        if m == True:
            self.page.get_element('text[class="blockName"]').tap()
            self.delay(2)
            self.get_screenshot()
        else:
            print('没有该模块')

    def test_03_click_map_地图坐标(self):
        """
        点击地图图标
        :return:
        """
        m = self.page.element_is_exists('view[class="map"][data-type="0"]')
        if m == True:
            self.page.get_element('view[class="map"][data-type="0"]').tap()
            self.delay(2)
            self.get_screenshot()
            self.delay(1)
        else:
            print('没有该模块')

    def test_04_click_xiaoqu_点击小区位置(self):
        """
        点击小区位置
        :return:
        """
        self.find_element('image[class="houseInfo--img"]').tap()
        self.get_screenshot()

    def test_05_click_ditie_点击地铁地图(self):
        """
        点击地铁地图
        :return:
        """
        self.page.scroll_to(400, 500)
        self.delay(1)
        m = self.page.element_is_exists('view[class="flex flex_1 justify_between"]')
        if m == True:
            self.page.get_element('view[class="flex flex_1 justify_between"]').tap()
            self.delay(2)
            self.get_screenshot()
            self.delay(1)
        else:
            print('没有地铁')

    def test_06_click_fyim_点击房源详情咨询(self):
        """
        点击房源详情咨询
        :return:
        """
        self.page.scroll_to(500, 500)
        self.delay(1)

        self.find_element('view[class="houseDesc--center houseDesc--chat"]').tap()
        self.delay(12)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()
        self.checkSendCard()

    def test_22_click_zjim_点击租金详情咨询(self):
        """
        点击房源详情咨询
        :return:
        """
        self.page.scroll_to(550, 500)
        self.delay(1)

        self.find_element('view[class="checkInDetail--center checkInDetail--chat"]').tap()
        self.delay(12)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()
        self.checkSendCard()

    def test_23_click_zbim_点击周边配套咨询(self):
        """
        点击房源详情咨询
        :return:
        """
        self.page.scroll_to(750, 500)
        self.delay(1)

        self.find_element('view[class="zbpt--center zbpt--chat"]').tap()
        self.delay(12)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()
        self.checkSendCard()

    def test_24_click_hotim_点击热门咨询(self):
        """
        点击热门咨询
        :return:
        """
        self.page.scroll_to(650, 500)
        self.delay(1)

        self.find_element('view[class="hotQs--center hotQs--qs"]').tap()
        self.delay(12)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()
        self.checkSendCard()
        
    def test_07_click_descmsg_点击房源描述中的经纪人Im(self):
        """
        点击房源描述中的经纪人Im
        :return:
        """
        self.page.scroll_to(800, 500)
        self.delay(1)
        msg = self.page.element_is_exists('image[class="houseDesc--im_chat"]')
        if msg == True:
            self.page.get_element('image[class="houseDesc--im_chat"]').tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有经纪人')

    def test_18_click_desctel_点击房源描述中的经纪人电话(self):
        """
        点击房源描述中的经纪人电话
        :return:
        """
        self.page.scroll_to(800, 500)
        self.delay(1)
        tel = self.page.element_is_exists('image[class="houseDesc--tel"]')
        if tel == True:
            self.page.get_element('image[class="houseDesc--tel"]').tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有经纪人')

    def test_08_click_descShowAll_点击房源描述查看全部收起(self):
        """
        点击房源描述-查看全部-收起
        :return:
        """
        self.page.scroll_to(800, 500)
        self.delay(1)
        des = self.page.element_is_exists('text[class="moduleName"]', inner_text='房源描述')
        if des == True:
            tog = self.page.element_is_exists('view[class="center toggle"]', inner_text='查看全部')
            if tog == True:
                self.page.get_element('view[class="center toggle"]', inner_text='查看全部').tap()
                self.delay(1)
                self.get_screenshot()
                self.delay(1)
                self.page.get_element('view[class="center toggle"]', inner_text='收起').tap()
                self.delay(1)
                self.get_screenshot()
                self.delay(1)
            else:
                print('没有查看更多')
        else:
            print('没有房源描述模块')

    def test_09_click_loupanmore_所属楼盘点击查看详情(self):
        """
        所属楼盘-点击查看详情
        :return:
        """
        self.page.scroll_to(800, 500)
        self.delay(1)
        loupan = self.page.element_is_exists('text[class="moduleName"]', inner_text='所属楼盘')
        if loupan == True:
            self.page.get_element('text', inner_text='查看详情').tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有所属楼盘模块')

    def test_10_click_loupan_点击所属楼盘(self):
        """
        点击所属楼盘
        :return:
        """
        self.page.scroll_to(800, 500)
        self.delay(1)
        loupan = self.page.element_is_exists('text[class="moduleName"]', inner_text='所属楼盘')
        if loupan == True:
            self.page.get_element('view[class="flex officeBlockInfo"]').tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有所属楼盘模块!')

    def test_11_click_prmap_点击周边配套(self):
        """
        点击周边配套
        :return:
        """
        self.page.scroll_to(1350, 500)
        self.delay(1)
        pr = self.page.element_is_exists('text[class="moduleName"]', inner_text='周边配套')
        if pr == True:
            m = self.page.get_element('map[class="pr map"][data-type="0"]')
            m.tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print('没有周边配套模块')

    def test_12_goto_tongxiaoqu_同小区房源附近写字楼进入房源详情页(self):
        """
        同小区房源/附近写字楼，进入房源详情页
        :return:
        """
        # 页面滚动
        self.page.scroll_to(1550, 500)
        self.delay(1)
        fujin = self.page.element_is_exists('text[class="moduleName"]', inner_text='附近写字楼')
        tognxiaoqu = self.page.element_is_exists('text[class="moduleName"]', inner_text='同小区房源')
        if tognxiaoqu == True:
            elm_items = self.page.get_elements('//view[@class="houses"]/view[@class="house"]')
            if len(elm_items) == 0:
                print("没有同小区房源")
            else:
                # 第一个item
                elm_first_item = elm_items[0]
                # 点击第一条房源
                elms = elm_first_item.get_element('rentitem').get_elements('view')
                elms[0].tap()
                self.delay(3)
                self.get_screenshot()
        else:
            if fujin == True:
                elm_items = self.page.get_elements('//view[@class="houses"]/view[@class="house"]')
                if len(elm_items) == 0:
                    print("没有附近写字楼")
                else:
                    # 第一个item
                    elm_first_item = elm_items[0]
                    # 点击第一条房源
                    elms = elm_first_item.get_element('officeItem').get_elements('view')
                    elms[0].tap()
                    self.delay(3)
                    self.get_screenshot()
            else:
                print("无")

    def test_13_click_tognxiaoqumore_点击同小区套房源(self):
        """
        点击同小区*套房源
        :return:
        """
        self.page.scroll_to(1900, 500)
        self.delay(1)
        m = self.page.element_is_exists('view[class="center checkSame"]')
        if m == True:
            more = self.page.get_element('view[class="center checkSame"]')
            more.tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print('没有同小区*套房源')

    def test_14_goto_report_点击我要举报(self):
        """
        点击我要举报
        :return:
        """
        self.page.scroll_to(1900, 500)
        self.delay(1)
        e = self.page.get_element('view[class="report"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    @ddt_case(
        0, 1, 2, 3
    )
    def test_15_goto_asklayer(self, value=0):
        """
        提问弹层()
        :param value:
        :return:
        """
        self.page.get_element('view[class="questionCst--center questionCst--toggleBtn"]').tap()
        if self.page.wait_for('//view[@class="questionCst--flex questionCst--column questionCst--a_e questionCst--questionList"]/view'):
            # print('+++++a+++++')
            elms = self.page.get_elements('//view[@class="questionCst--flex_1 questionCst--line_1"]')
            if len(elms) > value:
                # print('+++++value+++++')
                elms[value].tap()
                self.delay(3)
                self.get_screenshot()

    def test_16_goto_broker_点击经纪人(self):
        """
        点击经纪人
        :return:
        """
        # xpath定位
        elm = self.find_element('//view[@class="pf contact"]/contact/view/view/view[1]')
        elm.tap()
        self.delay(2)
        self.get_screenshot()

    def test_17_goto_zxmsg_点击在线咨询(self):
        """
        点击在线咨询
        :return:
        """
        # xpath定位
        elm = self.find_element('view[class="contact--center contact--pr contact--msg"]')
        elm.tap()

        self.delay(12)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()
        self.checkSendCard()

    def test_99_goto_tel_点击拨打电话(self):
        """
        点击拨打电话
        :return:
        """
        # xpath定位
        elm = self.find_element('//view[@class="pf contact"]/contact/view/view/view[2]/view[2]')
        elm.tap()
        self.delay(2)
        self.get_screenshot()