from minium import ddt_class, ddt_case
from base.test_base import TestBase
@ddt_class()
class Testesfdetail(TestBase):
    """
    二手房详情页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/detail/detail?sellId=329209949"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfdetail, self).setUp()
        print("Testesfdetail setup")

    def test_goto_photo_点击相册(self):
        """
        点击相册
        """
        elms = self.page.get_element('view[id="banner"]').get_element('banner').get_elements('view')
        elms[0].get_element('swiper').get_element('swiper-item').tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(5)

    def test_goto_fxk_点击放心看(self):
        """
        点击放心看
        :return:
        """
        e = self.page.get_element('view[class="pr between fangXinKan"]')
        e.tap()
        self.delay(2)
        self.get_screenshot()
        self.delay(1)

    def test_goto_collect_点击取消收藏(self):
        """
        点击收藏
        :return:
        """
        e = self.page.get_element('view[class="button collect"]')
        e.tap()
        self.get_screenshot()
        """
        取消收藏
        """
        e1 = self.page.get_element('view[class="button collect"]')
        e1.tap()
        self.get_screenshot()

    def test_goto_share_点击分享(self):
        """
        点击分享
        :return:
        """
        e = self.page.get_element('button[class="button"]')
        e.tap()
        self.delay(5)
        #self.get_capture()
        self.get_screenshot()
        self.delay(3)

    def test_goto_ckxq_点击查看详情(self):
        """
        点击查看详情
        :return:
        """
        e = self.page.get_element('view[class="flex align_center check"]')
        e.tap()
        self.get_screenshot()

    def test_goto_ygim_首付和月供咨询(self):
        """
        点击首付和月供咨询
        :return:
        """
        e = self.page.get_element('text', inner_text="首付和月供咨询")
        e.tap()
        self.get_screenshot()

    def test_goto_lcim_点击楼层咨询(self):
        """
        点击楼层咨询
        :return:
        """
        e = self.page.get_element('text', inner_text="楼层咨询")
        e.tap()
        self.get_screenshot()

    def test_goto_sfim_点击税费咨询(self):
        """
        点击税费咨询
        :return:
        """
        e = self.page.get_element('text', inner_text="税费咨询")
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_qcj_点击去出价(self):
        """
        点击去出价
        :return:
        """
        e = self.page.get_element('text', inner_text="去出价")
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_xqzx_房源详情咨询(self):
        """
        点击房源详情咨询
        :return:
        """
        e = self.page.get_element('text', inner_text="房源详情咨询")
        e.tap()
        self.get_screenshot()

    def test_goto_ckall_房源描述查看详情(self):
        """
        房源描述-查看详情
        :return:
        """
        des = self.page.element_is_exists('text', inner_text='房源描述')
        if des == True:
            tog = self.page.element_is_exists('text', inner_text='查看全部')
            if tog == True:
                self.page.get_element('text', inner_text='查看全部').tap()
                self.delay(3)
                self.get_screenshot()
                self.delay(3)
                self.page.get_element('text', inner_text='收起').tap()
                self.delay(3)
                self.get_screenshot()
                self.delay(3)
            else:
                print('没有查看更多')
        else:
            print('没有房源描述模块')

    @ddt_case(
        1, 2, 3, 4
    )
    def test_goto_rmim_点击热门咨询tab(self, value):
        """
        热门咨询(小区有停车位吗？,小区楼间距如何？,价格可以再优惠吗？,房子满五唯一吗？)
        :param value:
        :return:
        """
        align_msg = self.page.get_elements('view[class="flex align_center msg"]')
        msg_list = align_msg[value]
        msg_list.tap()
        self.delay(2)
        self.get_screenshot()
        self.delay(2)

    def test_goto_xqckxq_小区查看详情(self):
        """
        点击小区-查看详情
        :return:
        """
        e = self.page.get_element('view[class="flex align_center checkDetail"]')
        e.tap()
        self.delay(5)
        self.get_screenshot()
        self.delay(5)

    def test_goto_xqxq_点击小区进入详情页(self):
        """
        点击小区，进入小区详情页
        :return:
        """
        e = self.page.get_element('view[class="village"]')
        e.tap()
        self.delay(5)
        self.get_screenshot()
        self.delay(5)

    def test_goto_cjmsg_咨询近期成交数据(self):
        """
        点击咨询近期成交数据
        :return:
        """
        e = self.page.get_element('text', inner_text="咨询近期成交数据")
        e.tap()
        self.get_screenshot()

    def test_goto_fjpg_点击房价评估(self):
        """
        点击房价评估
        :return:
        """
        e = self.page.get_element('text', inner_text="房价评估")
        e.tap()
        self.get_screenshot()

    def test_goto_fjzs_点击房价走势图(self):
        """
        点击房价走势图
        :return:
        """
        e = self.page.get_element('view[class="trendCharts"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)

    def test_goto_txqfy_点击同小区房源详情页(self):
        """
        点击同小区房源，进入房源详情页
        :return:
        """
        # 页面滚动到同小区房源区域
        self.page.scroll_to(1400, 500)
        self.delay(1)

        # 先获取所有item
        elm_items = self.page.get_elements('//view[@id="anchor_4"]/view[@class="list"]/view[@class="item"]')

        if len(elm_items) == 0:
            print("没有同小区房源")
        else:
            # 第一个item
            elm_first_item = elm_items[0]
            # 点击第一条房源
            elms = elm_first_item.get_element('sell_item').get_elements('view')
            elms[0].tap()
            self.get_screenshot()

    def test_click_prmap_点击周边配套(self):
        """
        点击周边配套
        :return:
        """
        self.page.scroll_to(1350, 500)
        self.delay(1)
        pr = self.page.element_is_exists('text', inner_text='周边配套')
        if pr == True:
            m = self.page.get_element('view[class="pr map"][data-type="0"]')
            m.tap()
            self.delay(5)
            self.get_screenshot()
        else:
            print('没有周边配套模块')

    def test_goto_txq_全部同小区房源(self):
        """
        点击全部同小区房源
        :return:
        """
        e = self.page.get_element('view[class="center moreHouses"][data-type="1"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_cnxh_猜你喜欢进入房源详情页(self):
        """
        猜你喜欢，进入房源详情页
        :return:
        """
        # 页面滚动到猜你喜欢区域
        self.page.scroll_to(1750, 500)
        self.delay(1)

        # 先获取所有item
        elm_items = self.page.get_elements('//view[@class="guessLike"]/view[@class="list"]/view[@class="item"]')

        if len(elm_items) == 0:
            print("没有猜你喜欢房源")
        else:
            # 第一个item
            elm_first_item = elm_items[0]
            # 点击第一条房源
            elms = elm_first_item.get_element('sell_item').get_elements('view')
            elms[0].tap()
            self.delay(3)
            self.get_screenshot()
            self.delay(3)

    def test_goto_moreesf_点击更多二手房(self):
        """
        点击更多二手房
        :return:
        """
        e = self.page.get_element('view[class="center moreHouses"][data-type="2"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)

    def test_goto_report_点击我要举报(self):
        """
        点击我要举报
        :return:
        """
        self.page.scroll_to(1900, 500)
        self.delay(1)
        e = self.page.get_element('view[class="flex justify_flex_end report"]')
        e.tap()
        self.get_screenshot()

    @ddt_case(
        0, 1, 2, 3
    )
    def test_goto_asklayer_点击提问弹层及tab(self, value):
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
                self.delay(3)
                self.get_screenshot()

    def test_goto_broker_点击经纪人(self):
        """
        点击经纪人
        :return:
        """
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[1]')
        elm.tap()
        self.delay(5)
        self.get_screenshot()

    def test_goto_zxmsg_点击在线咨询(self):
        """
        点击在线咨询
        :return:
        """
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[2]/view[1]')
        elm.tap()
        self.delay(2)
        self.get_screenshot()

    def test_goto_tel_点击拨打电话(self):
        """
        点击拨打电话
        :return:
        """
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[2]/view[2]')
        elm.tap()
        self.get_screenshot()