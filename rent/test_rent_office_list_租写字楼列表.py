from ddt import file_data
from minium import ddt_class
from base.test_base import TestBase

@ddt_class()
class Testrentofficelist(TestBase):
    """
    租写字楼列表
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/office/list/list?listType=1"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentofficelist, self).setUp()
        print("Testrentofficelist setup")

    def test_click_keyword_searc_关键词搜索(self):
        """
        关键词搜索
        :return:
        """
        e = self.page.get_element('//search/view/view')
        e.tap()
        self.verifyPageName('/esf/sell/rent/office/search/search', '搜索 ok')
        self.delay(3)

    @file_data('./test_rent_office_list.yml')
    def test_click_search_租写字楼筛选(self, **kwargs):
        """
        租写字楼筛选
        :return:
        """
        self.tab_class = '//view[@class="flex align_center screenTab screenTab_1"]/text'
        self.tab_class_selected = '//view[@class="flex align_center screenTab screenTab_1 active"]/text'

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

            self.price_search(price_text)
            self.delay(1)

        # 面积筛选
        if 'area_text' in kwargs.keys():
            area_text = kwargs['area_text']

            self.area_search(area_text)
            self.delay(1)

        # 更多筛选
        if 'more_flag' in kwargs.keys():
            ary_more_text = {}
            ary_more_key = ['office_type_text',
                            'source_text',
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
        flag = self.page.element_is_exists(self.tab_class, inner_text=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, inner_text=verify_text)
            e.tap()
            self.delay(1)

            e = self.page.get_element("//location/view/view/view/view/text", inner_text=text_1)
            e.tap()
            self.delay(1)

            if text_1 != '不限':
                if text_2 != '不限' and text_2 != '':
                    is_selected = True
                    verify_text = text_2

                    e = self.page.get_element("//location//view/scroll-view[1]/view/text", inner_text=text_2)
                    e.tap()
                    self.delay(1)

                    if text_3 != '不限' and text_3 != '':
                        ary_text3 = text_3.split("|")

                        i = 0
                        for k in ary_text3:
                            if k == '不限' or k == '':
                                continue

                            e = self.page.get_element("//location//view/scroll-view[2]/view/text", inner_text=k)
                            e.tap()

                            # 最多只能选 3 个
                            i += 1
                            if i == 3:
                                break

                        if i == 1:
                            verify_text = text_3

            e = self.page.get_element('//location/view/view[2]/view/text', inner_text="确定")
            e.tap()
            self.delay(1)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, inner_text=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, inner_text=verify_text)

            print(verify_flag)
        else:
            print("没找到位置按钮")

        return self

    def area_search(self, area_text):
        """
        面积筛选
        """
        is_selected = False
        verify_text = '面积'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, inner_text=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, inner_text=verify_text)
            e.tap()
            self.delay(1)

            if area_text != '不限':
                is_selected = True
                verify_text = area_text

            e = self.page.get_element("//buildarea/view/scroll-view/view/text", inner_text=area_text)
            e.tap()
            self.delay(1)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, inner_text=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, inner_text=verify_text)

            print(verify_flag)
        else:
            print("没找到类别按钮")

        return self

    def price_search(self, price_text):
        """
        租金筛选
        """
        is_selected = False
        verify_text = '租金'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, inner_text=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, inner_text=verify_text)
            e.tap()
            self.delay(1)

            if price_text != '不限':
                is_selected = True
                verify_text = price_text

            e = self.page.get_element("//price/view/scroll-view/view/text", inner_text=price_text)
            e.tap()
            self.delay(1)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, inner_text=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, inner_text=verify_text)

            print(verify_flag)
        else:
            print("没找到租金按钮")

        return self

    def more_search(self, ary_more_text):
        """
        更多筛选
        """
        is_selected = False
        verify_text = '更多'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, inner_text=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, inner_text=verify_text)
            e.tap()
            self.delay(1)

            dict_more_height = {'office_type_text': 0,
                                'source_text': 72,
                                'fitment_text': 144,
                                'special_text': 256
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

                    e = self.page.get_element("//more/view/scroll-view/view/view/view/text", inner_text=more_text)
                    e.tap()
                    self.delay(1)

            e = self.page.get_element('//more/view/view/view/text', inner_text="确定")
            e.tap()
            self.delay(1)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, inner_text=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, inner_text=verify_text)

            print(verify_flag)
        else:
            print("没找到更多按钮")

        return self

    def search_order_by(self, order_by_text):
        """
        筛选排序
        """
        is_selected = False
        verify_text = '排序'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, inner_text=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, inner_text=verify_text)
            e.tap()
            self.delay(1)

            if order_by_text != '默认':
                is_selected = True

            e = self.page.get_element("//sort/view/view/view/text", inner_text=order_by_text)
            e.tap()
            self.delay(1)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, inner_text=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, inner_text=verify_text)

            print(verify_flag)
        else:
            print("没找到排序按钮")

        return self

    def test_click_office_detail_写字楼列表进入详情页(self):
        """
        点击租写字楼列表进入详情页
        :return:
        """
        elm_items = self.page.get_elements('//view[@class="list"]')
        # 第一个item
        elm_first_item = elm_items[0]
        # 点击第一条房源
        elms = elm_first_item.get_element('officeItem').get_elements('view')
        elms[0].tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)
