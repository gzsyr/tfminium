from ddt import file_data
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt_class()
class Testrentlist(TestBase):
    """
    租房列表页
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/home/home?city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentlist, self).setUp()
        print("Testrentlist setup")

    def test_查看整租房源(self):
        """
        V6.38.X: 点击整租tab下的 查看房源
        """
        self.find_element('view[class="flex_1 center total"]').tap()

        self.get_screenshot()
        self.verifyPageName('/esf/sell/rent/list/list')

    def test_查看合租房源(self):
        """
        V6.38.X: 点击合租tab及 查看房源
        """
        self.find_element('view[class="t_c rentType"][data-index="1"]').tap()
        self.find_element('view[class="flex_1 center total"]').tap()

        self.get_screenshot()
        self.verifyPageName('/esf/sell/rent/list/list')

    def test_去地图看(self):
        """
        V6.38.X: 点击 去地图看
        """
        self.find_element('view[class="flex a_c goMap"]').tap()
        self.delay(3)
        self.get_screenshot()
        self.verifyPageName('/page/publicPages/dtzf/dtzf')

    def test_click_search_搜索(self):
        """
        搜索
        :return:
        """
        self.find_element('view[class="center search"]').tap()
        self.get_screenshot()
        self.verifyPageName('/esf/sell/rent/search/search', '搜索 ok')

    @ddt_case(
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    )
    def test_click_king_点击金刚区10个(self, value=0):
        """
        点击金刚区（整租、合租等）
        :return:
        """
        try:
            self.page.get_element(f'view[class="i_c column tile"][data-index="{value}"]').tap()
            self.delay(1)
            self.get_screenshot()
        except:
            print("无")

    def test_click_rentdetail_进入租房详情页(self):
        """
        进入租房详情页
        :return:
        """
        # 先获取所有item
        self.find_element('view[class="gridRentItem--line_2 gridRentItem--title"]').tap()
        self.delay(2)
        self.get_screenshot()
        # self.verifyPageName('/esf/sell/rent/detail/detail', '房源详情 ok')

    @file_data('./test_rent_list.yml')
    def test_search_租房筛选(self, **kwargs):
        """
        租房筛选
        :return:
        """
        self.tab_class = '//view[@class="flex tab"]/view[@class="tab-text"]'
        self.tab_class_selected = '//view[@class="flex tab selected"]/view[@class="tab-text"]'

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

        # 租金筛选
        if 'price_text' in kwargs.keys():
            price_text = kwargs['price_text']
            min_val = kwargs['min_val']
            max_val = kwargs['max_val']

            self.price_search(price_text, min_val, max_val)
            self.delay(1)

        # 户型筛选
        if 'hx_text' in kwargs.keys():
            hx_text = kwargs['hx_text']

            self.house_type_search(hx_text)
            self.delay(1)

        # 更多筛选
        if 'more_flag' in kwargs.keys():
            ary_more_text = {}
            ary_more_key = ['rent_type_text',
                            'origin_from_text',
                            'info_type_text',
                            'fitment_text',
                            'special_text'
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
        is_selected = False
        verify_text = '位置'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, text_contains=verify_text)
            e.tap()
            self.delay(1)

            e = self.page.get_element("//location/view/view/view", text_contains=text_1)
            e.tap()
            self.delay(1)

            if text_1 != '不限':
                if text_2 != '不限' and text_2 != '':
                    is_selected = True

                    e = self.page.get_element("//location//view/scroll-view[1]/view", text_contains=text_2)
                    e.tap()
                    self.delay(1)

                    if text_3 != '不限' and text_3 != '':
                        ary_text3 = text_3.split("|")

                        i = 0
                        verify_text = ''
                        for k in ary_text3:
                            if k == '不限' or k == '':
                                continue

                            e = self.page.get_element("//location//view/scroll-view[2]/view/text", inner_text=k)
                            e.tap()

                            if verify_text != '':
                                verify_text += ','

                            verify_text += k

                            # 最多只能选 3 个
                            i += 1
                            if i == 3:
                                break
                    else:
                        verify_text = text_2

            e = self.page.get_element('//location/view/view[3]/view[2]', inner_text="确定")
            e.tap()
            self.delay(1)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, text_contains=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)

            print(verify_flag)
        else:
            print("没找到位置按钮")

        return self

    def price_search(self, price_text, min_val, max_val):
        """
        租金筛选
        """
        is_selected = False
        verify_text = '租金'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, text_contains=verify_text)
            e.tap()
            self.delay(1)

            if price_text != '':
                e = self.page.get_element("//price/view/scroll-view/view", text_contains=price_text)
                e.tap()
                self.delay(1)

                if price_text != '不限':
                    is_selected = True
                    verify_text = price_text
            else:
                is_selected = True

                if min_val != '':
                    e = self.page.get_element("//price/view/view/input", inner_text="最低价")
                    e.input(min_val)
                    self.delay(1)

                if max_val != '':
                    e = self.page.get_element("//price/view/view/input", inner_text="最高价")
                    e.input(max_val)
                    self.delay(1)

                e = self.page.get_element('view[class="price--confirm price--enable"]')
                e.tap()
                self.delay(1)

                if min_val == '':
                    verify_text = max_val + '元以下'
                elif max_val == '':
                    verify_text = min_val + '元以上'
                else:
                    verify_text = min_val + '-' + max_val + '元'
                    # 缺 min_val > max_val 情况

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, text_contains=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)

            print(verify_flag)
        else:
            print("没找到租金按钮")

        return self

    def house_type_search(self, hx_text):
        """
        户型筛选
        """
        is_selected = False
        verify_text = '户型'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, text_contains=verify_text)
            e.tap()
            self.delay(1)

            if hx_text != '不限':
                is_selected = True
                verify_text = hx_text

            e = self.page.get_element("//room/scroll-view/view", text_contains=hx_text)
            e.tap()
            self.delay(1)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, text_contains=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)

            print(verify_flag)
        else:
            print("没找到户型按钮")

        return self

    def search_order_by(self, order_by_text):
        """
        筛选排序
        """
        is_selected = False
        verify_text = '排序'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, text_contains=verify_text)
            e.tap()
            self.delay(1)

            if order_by_text != '不限':
                is_selected = True

            e = self.page.get_element("//order/scroll-view/view", text_contains=order_by_text)
            e.tap()
            self.delay(1)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, text_contains=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)

            print(verify_flag)
        else:
            print("没找到排序按钮")

        return self

    def more_search(self, ary_more_text):
        """
        更多筛选
        """
        is_selected = False
        verify_text = '更多'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, text_contains=verify_text)
            e.tap()
            self.delay(1)

            dict_more_height = {'rent_type_text': 0,
                                'origin_from_text': 72,
                                'info_type_text': 144,
                                'fitment_text': 256,
                                'special_text': 368
                                }

            scroll_view = self.page.get_element('//more/view/scroll-view')

            for str_key in ary_more_text:
                more_text = ary_more_text[str_key]
                more_height = dict_more_height[str_key]

                if more_text != '不限' and more_text != '':
                    is_selected = True

                    if more_height != 0:
                        scroll_view.scroll_to(y=more_height)
                        self.delay(1)

                    e = self.page.get_element("//more/view/scroll-view/view/view", text_contains=more_text)
                    e.tap()
                    self.delay(1)

            e = self.page.get_element('//more/view/view/view', inner_text="确定")
            e.tap()
            self.delay(1)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, text_contains=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)

            print(verify_flag)
        else:
            print("没找到更多按钮")

        return self

    def clear_search(self):
        """
        清空筛选条件
        """
        self.delay(1)
        self.page.get_element('image[class="icon-clear-filter"]').tap()
        self.get_screenshot()

        return self
