from ddt import file_data, ddt
from minium import ddt_class, ddt_case

from base.common import delay
from base.test_base import TestBase

@ddt
class Testrentdetail(TestBase):
    """
    租房详情页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/detail/detail?rentId=106520189&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentdetail, self).setUp()
        print("Testrentdetail setup")

    def test_goto_photo(self):
        """
        点击相册
        """
        elms = self.page.get_element('banner').get_elements('view')
        elms[0].get_element('swiper').get_element('swiper-item').tap()
        delay(3)
        self.get_screenshot()
        delay(3)

    def test_goto_collect(self):
        """
        点击收藏
        :return:
        """
        e = self.page.get_element('view[class="button collect"]')
        e.tap()
        self.get_screenshot()
        delay(3)
        """
        取消收藏
        """
        e1 = self.page.get_element('view[class="button collect"]')
        e1.tap()
        self.get_screenshot()

    def test_goto_share(self):
        """
        点击分享
        :return:
        """
        e = self.page.get_element('button[class="button"]')
        e.tap()
        # self.get_screenshot()
        self.get_screenshot()
        delay(1)

    def test_click_mapadd(self):
        """
        点击标题下坐标地址
        :return:
        """
        m = self.page.element_is_exists('text[class="blockName"]')
        if m == True:
            self.page.get_element('text[class="blockName"]').tap()
            self.get_screenshot()
            delay(1)
        else:
            print('没有该模块')
            self.get_screenshot()
            delay(1)

    def test_click_map(self):
        """
        点击地图图标
        :return:
        """
        m = self.page.element_is_exists('view[class="map"][data-type="0"]')
        if m == True:
            self.page.get_element('view[class="map"][data-type="0"]').tap()
            self.get_screenshot()
            delay(1)
        else:
            print('没有该模块')
            self.get_screenshot()
            delay(1)

    def test_click_xiaoqu(self):
        """
        点击小区
        :return:
        """
        self.page.scroll_to(400, 500)
        delay(1)
        m = self.page.element_is_exists('view[class="flex_1 between"]')
        if m == True:
            self.page.get_element('view[class="flex_1 between"]').tap()
            self.get_screenshot()
            delay(1)
        else:
            print('没有小区')
            self.get_screenshot()
            delay(1)

    def test_click_ditie(self):
        """
        点击地铁地图
        :return:
        """
        self.page.scroll_to(400, 500)
        delay(1)
        m = self.page.element_is_exists('view[class="flex flex_1 justify_between"]')
        if m == True:
            self.page.get_element('view[class="flex flex_1 justify_between"]').tap()
            self.get_screenshot()
            delay(1)
        else:
            print('没有地铁')
            delay(1)

    def test_click_fyim(self):
        """
        点击房源详情咨询
        :return:
        """
        self.page.scroll_to(500, 500)
        delay(1)
        m = self.page.element_is_exists('view[class="center msg"]')
        if m == True:
            self.page.get_element('view[class="center msg"]').tap()
            self.get_screenshot()
            delay(1)
        else:
            print('没有房源详情咨询')
            delay(1)

    def test_click_descmsg(self):
        """
        点击房源描述中的经纪人Im
        :return:
        """
        self.page.scroll_to(800, 500)
        delay(1)
        msg = self.page.element_is_exists('view[class="msg"]')
        if msg == True:
            self.page.get_element('view[class="msg"]').tap()
            self.get_screenshot()
        else:
            print('没有经纪人')

    def test_click_desctel(self):
        """
        点击房源描述中的经纪人电话
        :return:
        """
        self.page.scroll_to(800, 500)
        delay(1)
        tel = self.page.element_is_exists('view[class="tel"]')
        if tel == True:
            self.page.get_element('view[class="tel"]').tap()
            self.get_screenshot()
        else:
            print('没有经纪人')

    def test_click_descShowAll(self):
        """
        点击房源描述-查看全部-收起
        :return:
        """
        self.page.scroll_to(800, 500)
        delay(1)
        des = self.page.element_is_exists('text', inner_text='房源描述')
        if des == True:
            tog = self.page.element_is_exists('text', inner_text='查看全部')
            if tog == True:
                self.page.get_element('text', inner_text='查看全部').tap()
                self.get_screenshot()
                delay(1)
                self.page.get_element('text', inner_text='收起').tap()
                self.get_screenshot()
                delay(1)
            else:
                print('没有查看更多')
        else:
            print('没有房源描述模块')
            self.get_screenshot()
            delay(1)

    def test_click_loupanmore(self):
        """
        所属楼盘-点击查看详情
        :return:
        """
        self.page.scroll_to(800, 500)
        delay(1)
        loupan = self.page.element_is_exists('text', inner_text='所属楼盘')
        if loupan == True:
            self.page.get_element('text', inner_text='查看详情').tap()
            self.get_screenshot()
        else:
            print('没有所属楼盘模块')

    def test_click_loupan(self):
        """
        点击所属楼盘
        :return:
        """
        self.page.scroll_to(800, 500)
        delay(1)
        loupan = self.page.element_is_exists('text', inner_text='所属楼盘')
        if loupan == True:
            self.page.get_element('view[class="flex officeBlockInfo"]').tap()
            self.get_screenshot()
        else:
            print('没有所属楼盘模块!')

    def test_click_prmap(self):
        """
        点击周边配套
        :return:
        """
        self.page.scroll_to(1350, 500)
        delay(1)
        pr = self.page.element_is_exists('text', inner_text='周边配套')
        if pr == True:
            m = self.page.get_element('view[class="pr map"][data-type="0"]')
            m.tap()
            self.get_screenshot()
        else:
            print('没有周边配套模块')

    def test_goto_tongxiaoqu(self):
        """
        同小区房源/附近写字楼，进入房源详情页
        :return:
        """
        # 页面滚动
        self.page.scroll_to(1550, 500)
        delay(1)
        fujin = self.page.element_is_exists('text', inner_text='附近写字楼')
        tognxiaoqu = self.page.element_is_exists('text', inner_text='同小区房源')
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
                    self.get_screenshot()
            else:
                print("无")

    def test_click_tognxiaoqumore(self):
        """
        点击同小区*套房源
        :return:
        """
        self.page.scroll_to(1900, 500)
        delay(1)
        m = self.page.element_is_exists('view[class="center checkSame"]')
        if m == True:
            more = self.page.get_element('view[class="center checkSame"]')
            more.tap()
            self.get_screenshot()
        else:
            print('没有同小区*套房源')

    def test_goto_report(self):
        """
        点击我要举报
        :return:
        """
        self.page.scroll_to(1900, 500)
        delay(1)
        e = self.page.get_element('view[class="flex justify_flex_end report"]')
        e.tap()
        self.get_screenshot()

    @ddt_case(
        0, 1, 2, 3
    )
    def test_goto_asklayer(self, value):
        """
        提问弹层()
        :param value:
        :return:
        """
        self.page.get_element('view[class="center askBtn"]').tap()
        if self.page.wait_for('//view[@class="pa questions"]/view'):
            elms = self.page.get_elements('//view[@class="pa questions"]/view/text')
            if len(elms) > value:
                #print(value)
                elms[value].tap()
                self.get_screenshot()

    def test_goto_broker(self):
        """
        点击经纪人
        :return:
        """
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[1]')
        elm.tap()
        self.get_screenshot()

    def test_goto_zxmsg(self):
        """
        点击在线咨询
        :return:
        """
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[2]/view[1]')
        elm.tap()
        self.get_screenshot()

    def test_goto_tel(self):
        """
        点击拨打电话
        :return:
        """
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[2]/view[2]')
        elm.tap()
        self.get_screenshot()