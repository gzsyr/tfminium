# add by zsy
import minium
from minium import ddt_class

from base.test_base import TestBase


@ddt_class()
class TestIndexShouye(TestBase):
    """
    淘房小程序首页
    """
    def setUp(self) -> None:
        self.page_name = "/page/index/index"
        self.switch = True
        self.classname = self.__class__.__name__
        super(TestIndexShouye, self).setUp()
        print("TestIndexShouye setup atest")

    def test_30_click_新房列表页子榜单(self):
        """
        V7.01.x:小程序后台榜单排行榜配置了新房列表页（第三位后）子榜单信息流
        """
        self.page.scroll_to(3200, 200)
        self.get_screenshot('show')
        self.find_element('view[class="ranking_more"]').tap()
        self.delay(3)
        self.verifyPageName('/page/newhouse/rankinglist/rankinglist')
        self.get_screenshot()

    def test_29_更多精选主题(self):
        """
        V7.01.X: 点击小程序首页主题找房楼层右侧的更多精选主题
        """
        self.find_element('image[class="more"]').tap()

        self.get_screenshot()
        self.verifyPageName('/page/newhouse/housespecial/housespecail')

        self.find_element('view[class="item flex tfAlignC"]').tap()
        self.delay(2)
        self.get_screenshot('first content')

        self.back()

        self.find_elements('view[class="item flex tfAlignC"]')[1].tap()
        self.get_screenshot('second content')

    def test_28_进入楼盘评测(self):
        """
        V6.47.X: 进入楼盘评测
        """
        self.page.scroll_to(3000, 500)
        self.delay(2)

        i = 0
        while (i < 5):
            self.page.scroll_to(5000, 200)
            self.delay(2)
            try:
                self.find_element('navigator[class="grid_lpcp"]').tap()
                self.delay(5)
                break
            except:
                i = i + 1
        self.verifyPageName('/page/newhouse/evaluation/evaluation')
        self.get_screenshot()

    def test_27_热门插件更多(self):
        """
        V6.30.X: 1005036，互动插件模块，点击 更多
        """
        self.find_element('view[class="hdzj-more"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiList')
        self.get_screenshot()

    def test_26_点击热门插件(self):
        """
        V6.30.X: 1005036，互动插件模块，点击进入详情
        """
        self.find_element('view[class="hdzj-content"]').tap()
        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_23_优选顾问_置业顾问IM(self):
        """
        V6.29.X: 1004933, 优选顾问模块，点击置业顾问在线咨询
        """
        self.page.scroll_to(1500, 100)

        self.find_element('view[class="yxgw-btn"][data-jhtype="1"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_24_优选顾问_房博士IM(self):
        """
        V6.29.X: 1004933, 优选顾问模块，点击房博士在线咨询
        """
        self.page.scroll_to(1500, 100)

        self.find_element('view[class="yxgw-btn"][data-jhtype="2"]').tap()

        self.delay(6)
        self.verifyPageName('/im/pages/chating/chating')
        self.get_screenshot()

    def test_25_优选顾问_更多(self):
        """
        V6.29.X: 1004933, 优选顾问模块，点击更多
        """
        self.page.scroll_to(1500, 100)

        self.find_elements('view[class="gd index_fbsgd"]', inner_text='更多')[1].tap()
        # self.find_element('view[class="indexTitL"][text="优选顾问"]/../view[class="indexTitR index_fbsgd"]').tap()
        self.delay(2)
        self.get_screenshot()

    def test_01_click_banner_one_联板广告(self):
        """
        首页，点击联板广告第一张
        :return:
        """
        self.page.get_element('image[class="bannerTwo-img index_banner"]').click()

        self.get_screenshot()

    @minium.ddt_case(
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    )
    def test_05_click_func_entry_功能入口(self, value):
        """
        首页，点击功能入口,第一页的十项
        :return:
        """
        # self.page.get_element('view[data-index2="0"]').click()
        self.page.get_element(f'view[data-index1="0"][data-index2="{value-1}"]').click()
        self.delay(1)
        self.get_screenshot()

    def test_15_click_toutiao_淘房头条(self):
        """
        首页，点击“淘房头条”
        :return:
        """
        self.page.get_element('view[class="toutiao-swiper-item tfLine1"]').click()
        self.get_screenshot()

    def test_12_click_reyi_more_更多热议(self):
        """
        首页，点击“正在热议”更多按钮
        :return:
        """
        self.page.get_element('view[class="toutiao_more toutiao_r"]').click()
        self.get_screenshot()

    def test_11_click_reyi_first_正在热议(self):
        """
        首页，点击“正在热议”滚动的第一条
        :return:
        """
        self.page.get_element('view[class="toutiao-swiper-item flex tfAlignC tfFlexSb tfLine1"]').click()
        self.get_screenshot()

    def test_09_click_middle_adv_中间横幅广告(self):
        """
        首页，点击正在热议下方的大广告
        :return:
        """
        self.page.get_element('image[class="game-enter-img"]').click()
        self.get_screenshot()

    def test_10_click_qukuai_导购楼层1(self):
        """
        首页，点击导购楼层的4个区块，左边一个大的
        :return:
        """
        self.find_element('view[class="guide-item guide-item-left"]').click()
        self.get_screenshot()

    @minium.ddt_case(
        1, 2, 3
    )
    def test_10_click_qukuai_导购楼层(self, value):
        """
        首页，点击导购楼层的4个区块（摇号查询上方），右边3个小的
        :return:
        """
        self.page.get_element(f'view[class="guide-item"][data-index="{value}"]').click()
        self.get_screenshot()

    def test_19_click_yaohao_loupan_name_摇号楼盘(self):
        """
        首页，点击摇号查询模块的，选择楼盘名称
        :return:
        """
        self.page.scroll_to(1000, 200)
        self.set_pick_filter('picker', 2)
        self.get_screenshot()

    def test_17_click_yaohao_input_摇号输入(self):
        """
        首页，摇号查询模块，输入框输入内容
        :return:
        """
        self.page.get_element('input[type="text"]').input("atest minitest")
        self.get_screenshot()

    def test_18_click_yaohao_inquire_摇号查询(self):
        """
        首页，摇号查询模块，点击“一键查询”
        :return:
        """
        self.page.get_element('view[class="link-btn"]').click()
        self.get_screenshot()

    @minium.ddt_case(
        1, 2
    )
    def test_14_click_sell_yaohao_销售节点楼层(self, value):
        """
        首页，点击销售节点楼层，“1-新领销许、2-最新摇号”
        :return:
        """
        self.page.get_element(f'view[class="yhcx-tab-item"][data-index="{value}"]').click()
        self.get_screenshot()

    def test_13_click_sell_loupan_近期开盘(self):
        """
        首页，点击销售节点楼层，“近期开盘”下的第一个楼盘
        :return:
        """
        self.page.get_element('view[class="name oneline"]').click()
        self.get_screenshot()

    def test_22_click_zhibo_more_更多直播(self):
        """
        首页，点击直播看房模块，右侧“更多”按钮
        :return:
        """
        self.find_element('view[class="gd"]').click()
        self.get_screenshot()

    def test_21_click_zhibo_first_直播(self):
        """
        首页，点击直播看房模块，第一个直播
        :return:
        """
        self.page.get_element('view[class="zhlc-item"]').click()
        self.get_screenshot()

    def test_20_click_zhaofang_帮你找房(self):
        """
        首页，点击找房模块“帮你找房”的“马上找房”按钮
        :return:
        """
        self.page.get_element('view[data-index="0"]', inner_text='帮你找房').click()
        self.page.get_element('view[class="btn"]', inner_text="查询").click()
        self.get_screenshot()

    def test_07_click_maifang_帮你卖房(self):
        """
        首页，点击找房模块“帮你卖房”
        :return:
        """
        self.page.get_element('view[data-index="1"]', inner_text="帮你卖房").click()
        self.get_screenshot()

    def test_08_click_maifang_fabu_帮你卖房发布按钮(self):
        """
        首页，点击找房模块“帮你卖房”的“发布房源”按钮
        :return:
        """
        self.test_07_click_maifang_帮你卖房()
        self.find_element('view[class="btn"]', inner_text="查询").click()
        self.get_screenshot()

    def test_04_click_fbs_zixun_房博士咨询(self):
        """
        首页，点击房博士模块第一个房博士的“立即咨询”
        :return:
        """
        self.page.get_element('view[id="actionToOpenQuestion"]').click()
        self.get_screenshot()

    def test_02_click_fbs_avatar_房博士头像(self):
        """
        首页，点击房博士模块 第一个房博士的头像
        :return:
        """
        self.delay(1)
        self.page.get_element('image[id="actionToOpenFBSDetail"]').click()
        self.get_screenshot()

    def test_03_click_fbs_more_房博士更多(self):
        """
        首页，点击房博士模块“更多”按钮
        :return:
        """
        self.page.get_element('view[id="actionToOpenFBSIndex"]').click()
        self.get_screenshot()

    def test_06_click_icon_右侧悬浮广告(self):
        """
        首页，点击右下角的广告icon
        :return:
        """
        self.page.get_element('add-group').get_element('view').get_element('image').click()
        self.get_screenshot()

    def test_16_click_tuijian_loupan_推荐楼盘(self):
        """
        首页，点击推荐楼盘列表的第一个楼盘
        :return:
        """
        self.page.scroll_to(3000, 200)
        self.delay(2)
        try:
            self.find_element('view[class="commonNewHouseLi-l"]').click()
        except:
            print('没有配置楼盘推荐')
        self.get_screenshot()

    def tearDown(self) -> None:
        self.app.go_home()
        super(TestIndexShouye, self).tearDown()