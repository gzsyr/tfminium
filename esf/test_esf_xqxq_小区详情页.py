from minium import ddt_class, ddt_case
from base.test_base import TestBase
@ddt_class()
class Testesfxqxq(TestBase):
    """
    小区详情页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/pages/detail/detail?blockId=3982&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfxqxq, self).setUp()
        print("Testesfxqxq setup")

    @ddt_case(
        0, 1, 2, 3
    )
    def test_goto_tag_房源相册标签(self, value):
        """
        点击房源相册标签
        :param value:
        :return:
        """
        img_tag = self.page.element_is_exists('//banner/view/view/view')
        if img_tag == True:
            elms = self.page.get_elements('//banner/view/view/view')

            if len(elms) > value:
                elms[value].tap()
                self.delay(3)
                self.get_screenshot()
        else:
            print("没有标签")

    def test_goto_pic_点击相册(self):
        """
        点击相册
        :return:
        """
        e = self.page.get_element('//banner/view/swiper/swiper-item')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_collec_点击收藏(self):
        """
        点击收藏
        :return:
        """
        e = self.page.get_element('view[class="button collect"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_share_点击分享(self):
        """
        点击分享
        :return:
        """
        e = self.page.get_element('button[class="button"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_zsell_点击在售房源(self):
        """
        点击在售房源
        :return:
        """
        e = self.page.get_element('view[class="onSell"][data-type="1"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_zrent_点击在租房源(self):
        """
        点击在租房源
        :return:
        """
        e = self.page.get_element('view[class="onRent"][data-mark="1"][data-type="2"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_jgzs_点击价格走势图(self):
        """
        点击价格走势图
        :return:
        """
        e = self.page.get_element('view[class="flex_1 priceCharts"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_zxxq_点击咨询详情(self):
        """
        点击咨询详情
        :return:
        """
        e = self.page.get_element('view[class="consult"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_qpg_点击去评估(self):
        """
        点击去评估
        :return:
        """
        e = self.page.get_element('view[class="center appraised"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_wx_点击复制微信(self):
        """
        点击复制微信
        :return:
        """
        e = self.page.get_element('view[class="copy copyWX"][data-type="wechat"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_qq_点击复制QQ(self):
        """
        点击复制QQ
        :return:
        """
        e = self.page.get_element('view[class="copy copyQQ"][data-type="qq"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_jcxx_点击基础信息(self):
        """
        点击基础信息
        :return:
        """
        # 页面滚动到同基础详情
        self.page.scroll_to(595, 500)
        self.delay(1)

        e_base = self.page.element_is_exists('view[class="baseInfo"]')
        if e_base == True:
           self.page.get_element('view[class="baseInfo"]').tap()
           self.delay(3)
           self.get_screenshot()
        else:
            print("没有基础信息模块")

    def test_goto_zbpt_点击周边配套(self):
        """
        点击周边配套
        :return:
        """
        self.page.scroll_to(750, 500)
        self.delay(1)
        e_map = self.page.element_is_exists('view[class="pr map"][data-type="0"]')
        if e_map == True:
            self.page.get_element('view[class="pr map"][data-type="0"]').tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有周边配套模块")

    def test_goto_xqhx_点击小区户型(self):
        """
        点击小区户型
        :return:
        """
        self.page.scroll_to(980, 500)
        self.delay(1)

        houseTypes = self.page.element_is_exists('view[class="houseTypes"]')
        if houseTypes == True:
            self.page.get_element('view[class="houseTypes"]').tap()
            self.delay(1)
            self.get_screenshot()
        else:
            print("没有小区户型模块")

    def test_goto_xqhximg_点击小区户型图片(self):
        """
        点击小区户型图片
        :return:
        """
        self.page.scroll_to(900, 500)
        self.delay(1)

        house_img = self.page.element_is_exists('view[class="typeImg"]')
        if house_img == True:
            #img = self.page.get_element('//view/view[7]/scroll-view/view/view')
            imgs = self.page.get_elements('view[class="typeImg"]')
            imgs[0].tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有小区户型模块")

    def test_goto_xqhxmsg_小区户型咨询在售(self):
        """
        点击小区户型-咨询在售
        :return:
        """
        self.page.scroll_to(900, 500)
        self.delay(1)

        house_msg = self.page.element_is_exists('view[class="typeMsg"]')
        if house_msg == True:
            msg = self.page.get_element('//view[@class="typeMsg"]/view[@class="msg"]')
            msg.tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有小区户型模块")

    def test_goto_housecomment_小区评论全部评论(self):
        """
        点击小区评论-全部评论
        :return:
        """
        self.page.scroll_to(1180, 500)
        self.delay(1)

        house_com = self.page.element_is_exists('view[class="center check"]', inner_text="全部评论")
        if house_com == True:
            comment = self.page.get_element('view[class="center check"]', inner_text="全部评论")
            comment.tap()
            self.delay(2)
            self.get_screenshot()
        else:
            print("没有小区评论模块")

    def test_goto_comxq_小区评论全部评论(self):
        """
        点击小区评论-全部评论
        :return:
        """
        self.page.scroll_to(1350, 500)
        self.delay(1)

        comxq = self.page.element_is_exists('view[class="commentItem"]')
        if comxq == True:
            xq = self.page.get_elements('view[class="commentItem"]')
            xq[0].tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有小区评论模块")

    def test_goto_plimg_点击评论图片(self):
        """
        点击评论图片
        :return:
        """
        self.page.scroll_to(1400, 500)
        self.delay(1)

        plcom = self.page.element_is_exists('view[class="commentItem"]')
        if plcom == True:
            plimg = self.page.get_elements('//view[@class="commentItem"][1]//view[@class="flex pr commentImages"]/view')

            if len(plimg) > 0:
                plimg[0].tap()
                self.delay(3)
                self.get_screenshot()
            else:
                print("没有评论图片")
        else:
            print("没有评论")

    def test_goto_pldz_评论点赞(self):
        """
        评论点赞
        :return:
        """
        self.page.scroll_to(1400, 500)
        self.delay(1)
        pldz = self.page.element_is_exists('view[class="center"][data-index="0"][data-level="1"]')
        if pldz == True:
            dz = self.page.get_elements('view[class="center"][data-index="0"][data-level="1"]')
            dz[0].tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有评论")

    def test_goto_qxdz_取消点赞(self):
        """
        取消点赞
        :return:
        """
        self.page.scroll_to(1400, 500)
        self.delay(1)

        #有点问题
        qxdz = self.page.element_is_exists('view[class="center like"][data-index="0"][data-level="1"]')
        if qxdz == True:
            qx = self.page.get_elements('view[class="center like"][data-index="0"][data-level="1"]')
            qx[0].tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有点赞")

    def test_goto_wypl_点击我要评论(self):
        """
        点击我要评论（有评论时）
        :return:
        """
        self.page.scroll_to(1400, 500)
        self.delay(1)
        iwant = self.page.element_is_exists('view[class="center iWant"]')
        if iwant == True:
            e = self.page.get_element('view[class="center iWant"]')
            e.tap()
            self.delay(3)
            self.get_screenshot()
        else:
            """
            点击抢沙发我要评论(没有评论时)
            :return:
            """
            self.page.scroll_to(1000, 500)
            self.delay(1)
            nocomment = self.page.element_is_exists('//noComment/view/view[3]')
            if nocomment == True:
                e = self.page.get_element('//noComment/view/view[3]')
                e.tap()
                self.delay(3)
                self.get_screenshot()
            else:
                print("没有抢沙发我要评论")


    def test_goto_xqzj_点击小区专家(self):
        """
        点击小区专家
        :return:
        """
        self.page.scroll_to(1490, 500)
        self.delay(3)

        elms = self.page.get_elements('view[class="between expert"]')
        if len(elms) > 0:
            elms[0].tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有小区专家")

    def test_goto_zjim_点击小区专家im(self):
        """
        点击小区专家im
        :return:
        """
        self.page.scroll_to(1490, 500)
        self.delay(1)

        elms = self.page.get_elements('view[class="msg"]')
        if len(elms) > 0:
            elms[0].tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有小区专家IM")

    def test_goto_zjtel_点击小区专家tel(self):
        """
        点击小区专家tel
        :return:
        """
        self.page.scroll_to(1490, 500)
        self.delay(1)

        elms = self.page.get_elements('view[class="tel"]')
        if len(elms) > 0:
            elms[0].tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有小区专家")

    def test_goto_housetab_在售房源和在租房源tab切换(self):
        """
        在售房源和在租房源tab切换
        :return:
        """
        self.page.scroll_to(1300, 500)
        self.delay(1)

        e = self.page.get_element('view[class="pr typeI"][data-type="2"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(2)

        e = self.page.get_element('view[class="pr typeI"][data-type="1"]')
        e.tap()
        self.get_screenshot()

    def test_goto_selltab_在售房源tab(self):
        """
        在售房源tab
        :return:
        """
        self.page.scroll_to(1300, 500)
        self.delay(1)

        selltab = self.page.element_is_exists('view[class="pr typeI active"][data-type="1"]')
        if selltab == True:
            # 先获取所有item
            elm_items = self.page.get_elements('view[class="item"]')
            #print(len(elm_items))
            # 第一个item
            elm_first_item = elm_items[0]
            # 点击
            elms = elm_first_item.get_element('sell_item').get_elements('view')
            elms[0].tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有在售房源")

    def test_goto_renttab_在租房源tab(self):
        """
        在租房源tab
        :return:
        """
        self.page.scroll_to(1300, 500)
        self.delay(1)

        e = self.page.get_element('view[class="pr typeI"][data-type="2"]')
        e.tap()
        self.delay(2)
        self.get_screenshot()
        renttab = self.page.element_is_exists('view[class="pr typeI active"][data-type="2"]')
        if renttab == True:
            # 先获取所有item
            elm_items = self.page.get_elements('view[class="item"]')
            # 第一个item
            elm_first_item = elm_items[0]
            # 点击
            elms = elm_first_item.get_element('rent_item').get_elements('view')
            elms[7].tap()
            self.delay(2)
            self.get_screenshot()
        else:
            print("没有在租房源")

    def test_goto_zbxq_周边小区(self):
        """
        周边小区
        :return:
        """
        self.page.scroll_to(2000, 500)
        self.delay(1)

        view_zbxq = self.page.element_is_exists('view[class="villageList"]')
        if view_zbxq == True:
            # 先获取所有item
            elm_items = self.page.get_elements('//view[@class="villageList"]/view[@class="item"]')
            print(len(elm_items))
            # 第一个item
            elm_first_item = elm_items[0]
            # 点击
            elms = elm_first_item.get_element('villageitem').get_elements('view')
            print(len(elms))
            elms[0].tap()
            self.delay(2)
            self.get_screenshot()
        else:
            print("没有周边小区")

    def test_goto_broker_点击经纪人(self):
        """
        点击经纪人
        :return:
        """
        self.page.scroll_to(2000, 500)
        self.delay(1)
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[1]')
        elm.tap()
        self.delay(1)
        self.get_screenshot()

    def test_goto_zxmsg_点击在线咨询(self):
        """
        点击在线咨询
        :return:
        """
        self.page.scroll_to(2000, 500)
        self.delay(1)
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
        self.page.scroll_to(2000, 500)
        self.delay(1)
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[2]/view[2]')
        elm.tap()
        self.delay(2)
        self.get_screenshot()