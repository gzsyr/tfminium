from minium import ddt_class, ddt_case
from base.common import delay

from base.test_base import TestBase
@ddt_class()
class Testesfxqxq(TestBase):
    """
    小区详情页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/pages/detail/detail?blockId=216416&city=nj"
        self.switch = true
        super(Testesfxqxq, self).setUp()
        print("Testesfxqxq setup")

    @ddt_case(
        0, 1, 2, 3
    )
    def test_goto_tag(self, value):
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
        else:
            print("没有标签")

    def test_goto_pic(self):
        """
        点击相册
        :return:
        """
        e = self.page.get_element('//banner/view/swiper/swiper-item')
        e.tap()

    def test_goto_collect(self):
        """
        点击收藏
        :return:
        """
        e = self.page.get_element('view[class="button collect"]')
        e.tap()

    def test_goto_share(self):
        """
        点击分享
        :return:
        """
        e = self.page.get_element('button[class="button"]')
        e.tap()

    def test_goto_zsell(self):
        """
        点击在售房源
        :return:
        """
        e = self.page.get_element('view[class="onSell"][data-type="1"]')
        e.tap()

    def test_goto_zrent(self):
        """
        点击在租房源
        :return:
        """
        e = self.page.get_element('view[class="onRent"][data-mark="1"][data-type="2"]')
        e.tap()

    def test_goto_jgzs(self):
        """
        点击价格走势图
        :return:
        """
        e = self.page.get_element('view[class="flex_1 priceCharts"]')
        e.tap()

    def test_goto_zxxq(self):
        """
        点击咨询详情
        :return:
        """
        e = self.page.get_element('view[class="consult"]')
        e.tap()

    def test_goto_qpg(self):
        """
        点击去评估
        :return:
        """
        e = self.page.get_element('view[class="center appraised"]')
        e.tap()

    def test_goto_wx(self):
        """
        点击复制微信
        :return:
        """
        e = self.page.get_element('view[class="copy copyWX"][data-type="wechat"]')
        e.tap()

    def test_goto_qq(self):
        """
        点击复制QQ
        :return:
        """
        e = self.page.get_element('view[class="copy copyQQ"][data-type="qq"]')
        e.tap()

    def test_goto_jcxx(self):
        """
        点击基础信息
        :return:
        """
        # 页面滚动到同基础详情
        self.page.scroll_to(595, 500)
        delay(1)

        e_base = self.page.element_is_exists('view[class="baseInfo"]')
        if e_base == True:
           self.page.get_element('view[class="baseInfo"]').tap()
        else:
            print("没有基础信息模块")

    def test_goto_zbpt(self):
        """
        点击周边配套
        :return:
        """
        self.page.scroll_to(750, 500)
        delay(1)
        e_map = self.page.element_is_exists('view[class="pr map"][data-type="0"]')
        if e_map == True:
            self.page.get_element('view[class="pr map"][data-type="0"]').tap()
        else:
            print("没有周边配套模块")

    def test_goto_xqhx(self):
        """
        点击小区户型
        :return:
        """
        self.page.scroll_to(980, 500)
        delay(1)

        houseTypes = self.page.element_is_exists('view[class="houseTypes"]')
        if houseTypes == True:
            self.page.get_element('view[class="houseTypes"]').tap()
        else:
            print("没有小区户型模块")

    def test_goto_xqhximg(self):
        """
        点击小区户型图片
        :return:
        """
        self.page.scroll_to(900, 500)
        delay(1)

        house_img = self.page.element_is_exists('view[class="typeImg"]')
        if house_img == True:
            #img = self.page.get_element('//view/view[7]/scroll-view/view/view')
            imgs = self.page.get_elements('view[class="typeImg"]')
            imgs[0].tap()
        else:
            print("没有小区户型模块")

    def test_goto_xqhxmsg(self):
        """
        点击小区户型-咨询在售
        :return:
        """
        self.page.scroll_to(900, 500)
        delay(1)

        house_msg = self.page.element_is_exists('view[class="typeMsg"]')
        if house_msg == True:
            msg = self.page.get_element('//view[@class="typeMsg"]/view[@class="msg"]')
            msg.tap()
        else:
            print("没有小区户型模块")

    def test_goto_housecomment(self):
        """
        点击小区评论-全部评论
        :return:
        """
        self.page.scroll_to(1180, 500)
        delay(1)

        house_com = self.page.element_is_exists('text', inner_text="全部评论")
        if house_com == True:
            comment = self.page.get_element('text', inner_text="全部评论")
            comment.tap()
        else:
            print("没有小区评论模块")

    def test_goto_comxq(self):
        """
        点击小区评论-全部评论
        :return:
        """
        self.page.scroll_to(1350, 500)
        delay(1)

        comxq = self.page.element_is_exists('view[class="commentItem"]')
        if comxq == True:
            xq = self.page.get_elements('view[class="commentItem"]')
            xq[0].tap()
        else:
            print("没有小区评论模块")

    def test_goto_plimg(self):
        """
        点击评论图片
        :return:
        """
        self.page.scroll_to(1400, 500)
        delay(1)

        plcom = self.page.element_is_exists('view[class="commentItem"]')
        if plcom == True:
            plimg = self.page.get_elements('//view[@class="commentItem"][1]//view[@class="flex pr commentImages"]/view')

            if len(plimg) > 0:
                plimg[0].tap()
            else:
                print("没有评论图片")
        else:
            print("没有评论")

    def test_goto_pldz(self):
        """
        评论点赞
        :return:
        """
        self.page.scroll_to(1400, 500)
        delay(1)

        #有点问题
        pldz = self.page.element_is_exists('view[class="center"][data-index="0"][data-level="1"]')
        if pldz == True:
            dz = self.page.get_elements('view[class="center"][data-index="0"][data-level="1"]')
            dz[0].tap()
        else:
            print("没有评论")

    def test_goto_qxdz(self):
        """
        取消点赞
        :return:
        """
        self.page.scroll_to(1400, 500)
        delay(1)

        #有点问题
        qxdz = self.page.element_is_exists('view[class="center like"][data-index="0"][data-level="1"]')
        if qxdz == True:
            qx = self.page.get_elements('view[class="center like"][data-index="0"][data-level="1"]')
            qx[0].tap()
        else:
            print("没有点赞")

    def test_goto_wypl(self):
        """
        点击我要评论
        :return:
        """
        self.page.scroll_to(1400, 500)
        delay(1)

        e = self.page.get_element('view[class="center iWant"]')
        e.tap()

    def test_goto_xqzj(self):
        """
        点击小区专家
        :return:
        """
        self.page.scroll_to(1490, 500)
        delay(1)

        elms = self.page.get_elements('view[class="between expert"]')
        if len(elms) > 0:
            elms[0].tap()
        else:
            print("没有小区专家")

    def test_goto_zjim(self):
        """
        点击小区专家im
        :return:
        """
        self.page.scroll_to(1490, 500)
        delay(1)

        #e = self.page.get_element('view[class="msg"][data-accid="zsb_nj_902867"]')
        #e.tap()

        elms = self.page.get_elements('view[class="msg"]')
        if len(elms) > 0:
            elms[0].tap()
        else:
            print("没有小区专家")

    def test_goto_zjtel(self):
        """
        点击小区专家tel
        :return:
        """
        self.page.scroll_to(1490, 500)
        delay(1)

        #e = self.page.get_element('view[class="tel"][data-phone="15895958458"]')
        #e.tap()

        elms = self.page.get_elements('view[class="tel"]')
        if len(elms) > 0:
            elms[0].tap()
        else:
            print("没有小区专家")

    def test_goto_housetab(self):
        """
        在售房源和在租房源tab切换
        :return:
        """
        self.page.scroll_to(1700, 500)
        delay(1)

        e = self.page.get_element('view[class="pr typeI"][data-type="2"]')
        e.tap()
        delay(2)

        e = self.page.get_element('view[class="pr typeI"][data-type="1"]')
        e.tap()

    def test_goto_selltab(self):
        """
        在售房源tab
        :return:
        """
        self.page.scroll_to(1700, 500)
        delay(1)

        selltab = self.page.element_is_exists('view[class="pr typeI active"][data-type="1"]')
        if selltab == True:
            # 先获取所有item
            elm_items = self.page.get_elements('view[class="item"]')
            print(len(elm_items))
            # 第一个item
            elm_first_item = elm_items[0]
            # 点击
            elms = elm_first_item.get_element('sell_item').get_elements('view')
            elms[0].tap()
        else:
            print(0)

    def test_goto_renttab(self):
        """
        在租房源tab
        :return:
        """
        self.page.scroll_to(1700, 500)
        delay(1)

        e = self.page.get_element('view[class="pr typeI"][data-type="2"]')
        e.tap()
        delay(2)

        renttab = self.page.element_is_exists('view[class="pr typeI active"][data-type="2"]')
        if renttab == True:
            # 先获取所有item
            elm_items = self.page.get_elements('view[class="item"]')
            # 第一个item
            elm_first_item = elm_items[0]
            # 点击
            elms = elm_first_item.get_element('rent_item').get_elements('view')
            elms[0].tap()
        else:
            print(0)

    def test_goto_zbxq(self):
        """
        周边小区
        :return:
        """
        self.page.scroll_to(2000, 500)
        delay(1)

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
        else:
            print("没有周边小区")

    def test_goto_broker(self):
        """
        点击经纪人
        :return:
        """
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[1]')
        elm.tap()

    def test_goto_zxmsg(self):
        """
        点击在线咨询
        :return:
        """
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[2]/view[1]')
        elm.tap()

    def test_goto_tel(self):
        """
        点击拨打电话
        :return:
        """
        # xpath定位
        elm = self.page.get_element('//view[@class="pf contact"]/contact/view/view/view[2]/view[2]')
        elm.tap()