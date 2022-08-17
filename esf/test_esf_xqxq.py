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
        1, 2, 3, 4
    )
    def test_goto_tag(self, value):
        """
        点击房源相册标签
        :param value:
        :return:
        """
        #img_tag = self.page.element_is_exists(f'//swiper/view[class="center categoryTab active"][data-index="{value}"]')

        img_tag = self.page.element_is_exists('//banner/view/view/view["{value}"]')

        if img_tag == True:
            self.page.get_element('//banner/view/view/view["{value}"]').tap()
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
        self.page.scroll_to(749, 500)
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
        self.page.scroll_to(982, 500)
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
        self.page.scroll_to(982, 500)
        delay(1)

        house_img = self.page.element_is_exists('view[class="typeImg"]')
        if house_img == True:
            img = self.page.get_element('//view/view[7]/scroll-view/view/view')
            img.tap()
        else:
            print("没有小区户型模块")

    def test_goto_xqhxmsg(self):
        """
        点击小区户型-咨询在售
        :return:
        """
        self.page.scroll_to(982, 500)
        delay(1)

        house_msg = self.page.element_is_exists('view[class="typeImg"]')
        if house_msg == True:
            msg = self.page.get_element('//view/view[7]/scroll-view/view/view[2]/view')
            msg.tap()
        else:
            print("没有小区户型模块")

    def test_goto_housecomment(self):
        """
        点击小区评论-全部评论
        :return:
        """
        self.page.scroll_to(1188, 500)
        delay(1)

        house_com = self.page.element_is_exists('/view[2]/view/view/view/view')
        if house_com == True:
            comment = self.page.get_element('/view[2]/view/view/view/view')
            comment.tap()
        else:
            print("没有小区评论模块")

    def test_goto_comxq(self):
        """
        点击小区评论-全部评论
        :return:
        """
        self.page.scroll_to(1413, 500)
        delay(1)

        comxq = self.page.element_is_exists('view[class="commentItem"][data-id="329"]')
        if comxq == True:
            xq = self.page.get_element('view[class="commentItem"][data-id="329"]')
            xq.tap()
        else:
            print("没有小区评论模块")

    def test_goto_plimg(self):
        """
        点击评论图片
        :return:
        """
        self.page.scroll_to(1413, 500)
        delay(1)

        plcom = self.page.element_is_exists('view[class="commentItem"][data-id="329"]')
        if plcom == True:
            plimg = self.page.element_is_exists('/view[2]/')

        e = self.page.get_element('view[class="center iWant"]')
        e.tap()


    def test_goto_wypl(self):
        """
        点击我要评论
        :return:
        """
        self.page.scroll_to(1413, 500)
        delay(1)
        e = self.page.get_element('view[class="center iWant"]')
        e.tap()