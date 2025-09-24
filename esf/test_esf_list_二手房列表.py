from ddt import file_data
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt_class()
class Testesflist(TestBase):
    """
    二手房列表页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/home/home?shareCity=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesflist, self).setUp()
        print("Testesflist setup")

    def test_click_search_搜索(self):
        """
        搜索
        V6.44.x: 搜索发现关键词、小区人气榜、房源推荐榜、经纪人榜分别进入对应页面
        """
        self.redirect_to_page('/esf/sell/pages/search/search')
        # self.delay(3)
        # self.find_element('input[class="flex a_c hotKeyword"]').tap()
        # self.get_screenshot()
        # self.verifyPageName('/esf/sell/pages/search/search', '搜索 ok')
        self.delay(8)

        # 点击发现关键词
        self.find_element('view[class="flex a_c item"]').tap()
        self.delay(8)
        self.get_screenshot('点击发现关键词的第一个')
        self.back()
        #
        # 点击小区人气榜第一个
        self.find_element('view[class="flex a_c rank-item"][data-type="xq"]').tap()
        self.delay(10)
        self.get_screenshot('点击小区人气榜的第一个')
        self.back()

        # 点击房源推荐榜第一个
        self.find_element('view[class="flex a_c rank-item"][data-type="special"]').tap()
        self.delay(8)
        self.get_screenshot('点击房源推荐榜的第一个')
        self.back()

        # 点击经纪人榜第一个
        self.find_element('view[class="flex a_c rank-item"][data-type="jjr"]').tap()
        self.delay(5)
        self.get_screenshot('点击经纪人榜的第一个')

    @ddt_case(
        0, 1, 2, 3, 4
    )
    def test_func_entry_五个banner(self, value):
        """
        二手房首页五个banner
        :param value:
        :return:
        """
        self.page.get_element(f'view[class="t_c tile"][data-index="{value}"]').tap()
        self.get_screenshot()

    @ddt_case(
        0, 1, 2
    )
    def delete_test_func_adv_首页广告(self, value):
        """
        V6.3.X: 删除该入口
        二手房首页广告
        :param value:
        :return:
        """
        self.find_element(f'view[class="inline_flex column j_c entrance"]'
                              f'[data-index="{value}"]').tap()
        # self.get_capture()
        self.get_screenshot()

    def test_click_gg_广告位(self):
        """
        广告位
        :return:
        """
        b_l = self.page.element_is_exists('swiper-item[class="img"]')
        if b_l:
            e = self.page.get_element('swiper-item[class="img"]')
            e.tap()
            self.delay(3)
            self.get_screenshot()
        else:
            print("没有配置广告")

    @file_data('./test_esf_list.yml')
    def test_search_筛选(self, **kwargs):
        """
        二手房筛选
        :return:
        """

        # 清空筛选条件
        self.clear_search()
        self.delay(1)

        # 位置筛选
        if 'pos_text_1' in kwargs.keys():
            pos_text_1 = kwargs['pos_text_1']
            pos_text_2 = kwargs['pos_text_2']
            pos_text_3 = kwargs['pos_text_3']

            if pos_text_1 != '':
                self.pos_search(pos_text_1, pos_text_2, pos_text_3)
                self.delay(1)

        # 总价筛选
        if 'price_text' in kwargs.keys():
            price_text = kwargs['price_text']
            min_val = kwargs['min_val']
            max_val = kwargs['max_val']

            self.price_search(price_text, min_val, max_val)
            self.delay(1)

        # 房型筛选
        if 'hx_text' in kwargs.keys():
            hx_text = kwargs['hx_text']

            self.house_type_search(hx_text)
            self.delay(1)

        # 更多筛选
        if 'more_flag' in kwargs.keys():
            ary_more_text = {}
            ary_more_key = ['infofrom',
                            'infotype',
                            'buildarea',
                            'fitment',
                            'years',
                            'floor',
                            'forward',
                            'taxonlytype',
                            'is360',
                            'mright'
                            ]

            for str_key in ary_more_key:
                if str_key in kwargs.keys():
                    ary_more_text[str_key] = kwargs[str_key]
                else:
                    ary_more_text[str_key] = ''

            self.more_search(ary_more_text)
            self.delay(1)

        # 筛选排序
        if 'order_by_text' in kwargs.keys():
            order_by_text = kwargs['order_by_text']

            self.search_order_by(order_by_text)
            self.delay(1)

        # 截图
        self.get_screenshot()

    def pos_search(self, text_1, text_2, text_3):
        """
        位置筛选
        """

        self.delay(1)
        self.find_element('view[class="flex a_c screenTab"]', inner_text="位置").tap()
        self.delay(1)

        if text_1 != '附近':
            self.find_element('view[class="sellScreen--flex sellScreen--a_c sellScreen--locItem"]', inner_text=text_1).tap()
        self.delay(1)

        if text_1 != '不限':
            self.find_element('view[class="sellScreen--flex sellScreen--a_c sellScreen--locItem"]', inner_text=text_2).tap()
            self.delay(1)

            if text_3 != '':
                self.find_element('view[class="sellScreen--flex sellScreen--a_c sellScreen--locItem"]', inner_text=text_3).tap()
                self.delay(1)

        self.find_element('view[class="sellScreen--center sellScreen--confirm"]').tap()
        self.delay(2)

        self.verifyContainsStr('(1)', self.page.get_element('view[class="flex a_c screenTab screenTabA"]').inner_text, '没有筛选到选项')

        return self

    def price_search(self, price_text, min_val, max_val):
        """
        总价筛选
        """

        self.delay(1)
        self.find_element('view[class="flex a_c screenTab"]', inner_text="总价").tap()
        self.delay(1)

        if price_text != '':
            self.find_element('view[class="sellScreen--center sellScreen--item"]', inner_text=price_text).tap()
            self.delay(1)
        else:
            if min_val != '':
                self.find_element('input[class="sellScreen--ipt"]', inner_text="最低价格(万)").input(min_val)

            if max_val != '':
                self.find_element('input[class="sellScreen--ipt"]', inner_text="最高价格(万)").input(max_val)

        self.find_element('view[class="sellScreen--center sellScreen--confirm"]').tap()
        self.delay(1)

        self.verifyContainsStr('(1)', self.page.get_element('view[class="flex a_c screenTab screenTabA"]').inner_text, '没有筛选到选项')

        return self

    def house_type_search(self, hx_text='三室'):
        """
        房型筛选
        """

        self.delay(1)
        self.find_element('view[class="flex a_c screenTab"]', inner_text="房型").tap()
        self.delay(1)

        ary_hx = hx_text.split("|")
        for hx in ary_hx:
            self.find_element('view[class="sellScreen--center sellScreen--item"]', inner_text=hx).tap()

        self.find_element('view[class="sellScreen--center sellScreen--confirm"]').tap()
        self.delay(2)

        self.verifyContainsStr(f'({len(ary_hx)})', self.find_element('view[class="flex a_c screenTab screenTabA"]').inner_text, '没有筛选到选项')

        return self

    def search_order_by(self, order_by_text='总价由高到低'):
        """
        筛选排序
        """

        self.delay(1)
        self.find_element('view[class="flex a_c screenTab"]', inner_text='排序').tap()
        self.delay(1)

        self.find_element('view[class="sellScreen--center sellScreen--sortItem"]', inner_text=order_by_text).tap()
        self.delay(1)
        self.find_element('view[class="sellScreen--center sellScreen--confirm"]').tap()
        self.delay(2)

        self.verifyContainsStr('排序(1)', self.find_element('view[class="flex a_c screenTab screenTabA"]').inner_text, '没有筛选到选项')

        return self

    def more_search(self, ary_more_text):
        """
        更多筛选
        """
        # ary_more_text= {"infofrom":"放心看",
        #                 "infotype": "住宅",
        #                 "buildarea": "50-80㎡",
        #                 "fitment": "毛坯",
        #                 "years": "2015年后",
        #                 "floor": "2-5层",
        #                 "forward": "南北通透",
        #                 "taxonlytype": "无增值税无个税",
        #                 "is360": "AI讲房",
        #                 "mright": "产权房"}
        self.delay(1)
        self.find_element('view[class="flex a_c screenTab"]', inner_text='更多').tap()
        self.delay(1)

        dict_more_height = {'infofrom': 0,
                            'infotype': 70,
                            'buildarea': 180,
                            'fitment': 290,
                            'years': 360,
                            'floor': 470,
                            'forward': 540,
                            'taxonlytype': 650,
                            'is360': 720,
                            'mright': 790
                            }

        scroll_view = self.find_element('scroll-view[class="sellScreen--screen sellScreen--more"]')

        for str_key in ary_more_text:
            more_text = ary_more_text[str_key]
            more_height = dict_more_height[str_key]

            if more_text != '':
                if more_height != 0:
                    scroll_view.scroll_to(y=more_height)
                    self.delay(1)

                self.find_element(f'view[class="sellScreen--center sellScreen--item"][data-type="{str_key}"]', inner_text=more_text).tap()
                self.delay(1)

        self.find_element('view[class="sellScreen--center sellScreen--confirm"]').tap()
        self.delay(1)

        self.verifyContainsStr('(10)', self.page.get_element('view[class="flex a_c screenTab screenTabA"]').inner_text, '没有筛选到选项')

        return self

    def clear_search(self):
        """
        清空筛选条件
        """
        self.delay(1)
        self.page.get_element('view[class="pa clearScreen"]').tap()

        return self

    @ddt_case(
        'VR看房', '放心看', '个人', '写字楼', '商铺'
    )
    def test_click_func_bqsx_标签筛选(self, value):
        """
        标签筛选
        :param value:
        :return:
        """
        self.find_element('view[class="pa clearScreen"]').tap()
        self.find_element(f'view[class="inline_flex a_c j_c screenQuickI"][data-name="{value}"]').tap()
        self.get_screenshot()

    def test_click_housedetail_点击列表进入详情页(self):
        """
        进入二手房详情页
        :return:
        """

        # 先获取所有item
        elm_items = self.find_element('image[class="gridSellItem--img"]').tap()

        # # 第一个item
        # elm_first_item = elm_items[0]
        #
        # # 点击
        # elms = elm_first_item.get_element('sellitem').get_elements('view')
        # elms[0].tap()
        self.get_screenshot()
        self.verifyPageName('/esf/sell/pages/detail/detail', '房源详情 ok')
