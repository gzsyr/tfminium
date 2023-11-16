from minium import ddt_class, ddt_case
from base.test_base import TestBase
@ddt_class()
class Testesfxqxq(TestBase):
    """
    小区详情页
    """
    def setUp(self, true=None) -> None:
        self.page_name = f"/esf/village/pages/detail/detail?city=nj&blockId={self.blockid}"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfxqxq, self).setUp()
        print("Testesfxqxq setup")

    def test_楼盘测评(self):
        """
        V6.43.x: 楼盘测试用例  中冶钟鼎山庄
        同步未登录用例，在logout/test_xq_未登录_小区详情.py中
        """
        self.redirect_to_page('/esf/village/pages/detail/detail?blockId=1401&city=nj')
        self.delay(10)

        # 点击 进入楼盘测评详情页
        self.find_element('view[class="evaluation--check-more"]').tap()
        self.delay(5)
        self.get_screenshot('进入楼盘测评详情页')

        # 在楼盘测评详情页，点击 在线咨询
        self.find_element('view[class="button"]', inner_text='在线咨询').tap()
        self.delay(5)
        self.get_screenshot('进入咨询页面')
        self.back()

        # 在楼盘测评详情页，点击拨打电话
        self.find_element('view[class="button"]', inner_text='拨打电话').tap()
        self.get_screenshot('点击拨打电话')

        # 在楼盘测评详情页，点击图片
        self.find_element('image[class="single-pic"]').tap()
        self.get_screenshot('查看大图')
        self.back()

        self.verifyPageName('/esf/village/pages/detail/detail')

    def test_001_rizhao_banner(self):
        """
        V6.39.X: 1.点击日照; 2.点击动图
        """
        self.find_element('swiper-item[class="banner--pr banner--bannerItem"][data-id="sunlight"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_001_rizhao_点击日照图(self):
        """
        V6.39.X: 点击日照gif图
        """
        self.find_element('image[class="sunlight--img"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/rizhaofenxi/rizhaofenxi')

    def test_001_rizhao_IM(self):
        """
        V6.42.X: 点击咨房源采光详情
        V6.39.X: 点击咨询楼栋详情
        """
        self.find_element('view[class="sunlight--center sunlight--chat"]').tap()
        self.delay(3)
        self.get_screenshot()

        # self.blockId=3982

    def test_帖子_点击头像(self):
        """
        V6.38.X: 点击 加精帖子 的头像
        """
        self.delay(5)
        self.page.scroll_to(1580, 500)
        self.delay(2)
        try:
            self.find_element('image[class="postComponent--avatar"]').tap()

            self.verifyPageName('/esf/sell/pages/broker/broker')
        except:
            print('没有对应的加精帖子')

        self.get_screenshot()

    def test_帖子_点击咨询(self):
        """
        V6.38.X: 点击 加精帖子的咨询按钮
        """
        self.delay(5)
        self.page.scroll_to(1580, 500)
        self.delay(2)
        try:
            self.find_element('view[class="postComponent--connect postComponent--fbs_contact_tap"]').tap()
        except:
            print('没有对应的加精帖子')

        self.get_screenshot()

    def test_帖子_点击门店(self):
        """
        V6.38.X: 点击 加精帖子的 经纪人门店
        """
        self.delay(5)
        self.page.scroll_to(1580, 500)
        self.delay(2)
        try:
            self.find_element('view[class="postComponent--jjr_shop"]').tap()

            self.verifyPageName('/esf/sell/pages/broker/broker')
        except:
            print('没有对应的加精帖子')

        self.get_screenshot()

    def test_帖子_点击标题(self):
        """
        V6.38.X: 点击 加精帖子的 标题
        """
        self.delay(5)
        self.page.scroll_to(1580, 500)
        self.delay(2)
        try:
            self.find_element('view[class="postComponent--list-desc postComponent--postTitle"]').tap()

            self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        except:
            print('没有对应的加精帖子')

        self.get_screenshot()

    def test_帖子_点击正文(self):
        """
        V6.38.X: 点击 加精帖子的 正文
        """
        self.delay(5)
        self.page.scroll_to(1580, 500)
        self.delay(2)
        try:
            self.find_element('view[class="postComponent--post_cont"]').tap()

            self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        except:
            print('没有对应的加精帖子')

        self.get_screenshot()

    def test_帖子_点击图片(self):
        """
        V6.38.X: 点击 加精帖子的 图片
        """
        self.delay(5)
        self.page.scroll_to(1580, 500)
        self.delay(2)
        try:
            self.find_element('image[class="postComponent--plist-item postComponent--plist-item2-2"]').tap()

        except:
            print('没有对应的加精帖子')

        self.get_screenshot()

    def test_帖子_点击标签(self):
        """
        V6.38.X: 点击 加精帖子的 标签
        """
        self.delay(5)
        self.page.scroll_to(1580, 500)
        self.delay(2)
        try:
            self.find_element('view[class="postComponent--posttag postComponent--flex postComponent--tfAlignC"]').tap()
            self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        except:
            print('没有对应的加精帖子')

        self.get_screenshot()

    def test_帖子_点击分享(self):
        """
        V6.38.X: 点击 加精帖子的 分享
        """
        self.delay(5)
        self.page.scroll_to(1580, 500)
        self.delay(2)
        try:
            self.find_element('image[class="postComponent--shareDetail_img"]').tap()
        except:
            print('没有对应的加精帖子')

        self.get_screenshot()

    def test_帖子_点击点赞(self):
        """
        V6.38.X: 点击 加精帖子的 点赞
        """
        self.delay(5)
        self.page.scroll_to(1580, 500)
        self.delay(2)
        try:
            self.find_element('view[class="postComponent--laud-btn"]').tap()
        except:
            print('没有对应的加精帖子')

        self.get_screenshot()

    def test_帖子_点击评论(self):
        """
        V6.38.X: 点击 加精帖子的 评论
        """
        self.delay(5)
        self.page.scroll_to(1580, 500)
        self.delay(2)
        try:
            self.find_element('view[class="postComponent--replyBtn"]').tap()
            self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        except:
            print('没有对应的加精帖子')

        self.get_screenshot()

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
        self.get_screenshot()

    def test_goto_collect_点击收藏(self):
        """
        点击收藏
        :return:
        """
        self.page.get_element('image[class="image"]').tap()
        self.get_screenshot()

    def del_test_z_goto_share_点击分享(self):
        """
        V6.42.X: DELETE
        点击分享
        :return:
        """
        e = self.page.get_element('button[class="button"]')
        e.tap()
        self.get_screenshot()

    def test_goto_zsell_点击在售房源(self):
        """
        点击在售房源
        :return:
        """
        self.find_element('view[class="price--w33"][data-type="1"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_znew_点击新上房源(self):
        """
        V6.42.x: 点击新上房源
        :return:
        """
        self.find_element('view[class="price--w33"][data-type="3"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_zrent_点击在租房源(self):
        """
        V6.42.X: UPDATE
        点击在租房源
        :return:
        """
        self.find_element('view[class="price--w33"][data-type="2"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_jgzs_点击价格走势图(self):
        """
        点击价格走势图
        :return:
        """
        self.page.get_element('view[class="price--trend"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_dkjs_点击贷款计算(self):
        """
        V6.42.x: 点击贷款计算
        """
        self.find_element('view[class="price--tool"]/text', inner_text='房贷计算').tap()
        self.delay(3)
        self.get_screenshot()

    def test_goto_qpg_点击采光计算(self):
        """
        V6.42.X: 点击采光计算
        """
        self.find_element('view[class="price--tool"]/text', inner_text='采光计算').tap()
        self.delay(3)
        self.get_screenshot()

    def del_test_goto_wx_点击复制微信(self):
        """
        V6.42.X: DELETE
        点击复制微信
        :return:
        """
        try:
            self.find_element('view[class="copy copyWX"][data-type="wechat"]').tap()
        except:
            print('没有复制微信')
        self.get_screenshot()

    def test_goto_信息旁地图(self):
        """
        V6.42.X: 点击基础信息处的地图
        """
        try:
            self.find_element('image[class="price--map"]').tap()
        except:
            print('没有地图')
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
            self.page.get_element('map[class="pr map"][data-type="0"]').tap()
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
        self.page.scroll_to(1280, 500)
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
            self.get_screenshot()
        else:
            print("没有小区专家")

    def test_goto_housetab_在售房源和在租房源tab切换(self):
        """
        在售房源和在租房源tab切换
        :return:
        """
        self.redirect_to_page("/esf/village/pages/detail/detail?blockId=10020371&city=nj")
        self.delay(5)
        self.page.scroll_to(3500, 500)
        self.delay(5)

        e = self.page.get_element('view[class="blockHouses--center blockHouses--sell_rent_type"][data-id="2"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(2)

        e = self.page.get_element('view[class="blockHouses--center blockHouses--sell_rent_type"][data-id="1"]')
        e.tap()
        self.get_screenshot()

    def test_goto_selltab_在售房源(self):
        """
        在售房源tab
        :return:
        """
        self.redirect_to_page("/esf/village/pages/detail/detail?blockId=10020371&city=nj")
        self.delay(5)
        self.page.scroll_to(3500, 500)
        self.delay(5)

        self.find_element('image[class="sellItem--img"]').tap()

        self.delay(2)
        self.get_screenshot()

    def test_goto_renttab_在租房源(self):
        """
        在租房源tab
        :return:
        """
        self.redirect_to_page("/esf/village/pages/detail/detail?blockId=10020371&city=nj")
        self.delay(5)
        self.page.scroll_to(3500, 500)
        self.delay(5)

        self.page.get_element('view[class="blockHouses--center blockHouses--sell_rent_type"][data-id="2"]').tap()
        self.delay(3)
        self.find_element('image[class="rentItem--img"]').tap()

        self.delay(2)
        self.get_screenshot()

    def test_goto_zbxq_周边小区(self):
        """
        周边小区
        :return:
        """
        self.page.scroll_to(2000, 500)
        self.delay(1)

        self.find_element('image[class="villageItem--img"]').tap()

        self.delay(2)
        self.get_screenshot()

    def test_goto_zbpt_咨询周边配套(self):
        """
        V6.42.x: 点击周边配套模块下的“咨询周边配套”
        """
        self.find_element('image[class="zbpt--icon"]').tap()
        self.get_screenshot()

    def test_goto_zxmsg_咨询详情(self):
        """
        V6.42.X: 点击价格走势下方的“咨询详情”
        """

        self.find_element('view[class="price--center price--consult"]').tap()
        self.get_screenshot()

    def test_z_goto_tel_点击底部IM(self):
        """
        V6.42.x: 点击拨打电话
        :return:
        """
        self.find_element('view[class="bottomContact--center bottomContact--chat"]').tap()
        self.get_screenshot()

    def test_z_goto_tel_点击底部拨打电话(self):
        """
        V6.42.x: 点击拨打电话
        :return:
        """

        self.find_element('view[class="bottomContact--center bottomContact--call"]').tap()
        self.get_screenshot()