from ddt import file_data
from minium import ddt_class
from base.test_base import TestBase

@ddt_class()
class Testrenthouseinglist(TestBase):
    """
    找室友列表页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/rent/list/list?houseType=3"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrenthouseinglist, self).setUp()
        print("Testrenthouseinglist setup")

    @file_data('./test_rent_housing_list.yml')
    def test_01_click_search_找室友筛选(self, **kwargs):
        """
        找室友筛选
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

        # 有房无房筛选
        if 'share_type_text' in kwargs.keys():
            share_type_text = kwargs['share_type_text']

            self.share_type_search(share_type_text)
            self.delay(1)

        # 更多筛选
        if 'more_flag' in kwargs.keys():
            ary_more_text = {}
            ary_more_key = ['roommate_sex_text',
                            'publish_sex_text',
                            'special_tag'
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
        verify_text = '全南京'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, text_contains=verify_text)
            e.tap()
            self.delay(3)

            e = self.page.get_element("//location/view/view/view", text_contains=text_1)
            e.tap()
            self.delay(3)

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
            self.delay(3)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, text_contains=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)

            print(verify_flag)
        else:
            print("没找到位置按钮")

        return self

    def share_type_search(self, share_type_text):
        """
        有房无房筛选
        """
        is_selected = False
        verify_text = '有房/无房'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, text_contains=verify_text)
            e.tap()
            self.delay(3)

            if share_type_text != '有房/无房':
                is_selected = True
                verify_text = share_type_text

            e = self.page.get_element("//share-type/scroll-view/view", text_contains=share_type_text)
            e.tap()
            self.delay(3)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, text_contains=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)

            print(verify_flag)
        else:
            print("没找到有房无房按钮")

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
            self.delay(3)

            if order_by_text != '默认':
                is_selected = True

            e = self.page.get_element("//order/scroll-view/view", text_contains=order_by_text)
            e.tap()
            self.delay(3)

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
        verify_text = '筛选'

        self.delay(1)
        flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)
        if flag:
            e = self.page.get_element(self.tab_class, text_contains=verify_text)
            e.tap()
            self.delay(3)

            dict_more_height = {'roommate_sex_text': 0,
                                'publish_sex_text': 72,
                                'special_tag': 144
                                }

            dict_more_no = {'roommate_sex_text': 2,
                            'publish_sex_text': 4,
                            'special_tag': 6
                            }

            scroll_view = self.page.get_element('//roommate/view/scroll-view')

            for str_key in ary_more_text:
                more_text = ary_more_text[str_key]
                more_height = dict_more_height[str_key]

                if more_text != '':
                    is_selected = True

                    if more_height != 0:
                        scroll_view.scroll_to(y=more_height)
                        self.delay(3)

                    ary_texts = more_text.split("|")

                    for k in ary_texts:
                        if k == '':
                            continue

                        e = self.page.get_element(f"//roommate/view/scroll-view/view[{dict_more_no[str_key]}]/view",
                                                  text_contains=k)
                        e.tap()

                    self.delay(3)

            e = self.page.get_element('//roommate/view/view/view', inner_text="确定")
            e.tap()
            self.delay(3)

            if is_selected:
                verify_flag = self.page.element_is_exists(self.tab_class_selected, text_contains=verify_text)
            else:
                verify_flag = self.page.element_is_exists(self.tab_class, text_contains=verify_text)

            print(verify_flag)
        else:
            print("没找到筛选按钮")

        return self

    def clear_search(self):
        """
        清空筛选条件
        """
        self.delay(1)
        self.page.get_element('image[class="icon-clear-filter"]').tap()

        return self

    def test_02_click_homelist_点击列表(self):
        """
        点击列表
        :return:
        """
        elms = self.page.get_elements('//view[@class="rent-home-list grey"]/view/findRoommateItem/view')
        elms[1].tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(1)

    def test_03_click_sc_点击收藏取消收藏(self):
        """
        点击列表-收藏-取消收藏
        :return:
        """
        sc = self.page.get_elements('//view[@class="rent-home-list grey"]/view/findRoommateItem/view/view[5]/view[2]')
        sc[0].tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)

        qxsc = self.page.get_elements('//view[@class="rent-home-list grey"]/view/findRoommateItem/view/view[5]/view[2]')
        qxsc[0].tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)

    def test_04_click_zxim_点击列表在线聊(self):
        """
        点击列表-在线聊
        :return:
        """
        im = self.page.get_elements('//view[@class="rent-home-list grey"]/view/findRoommateItem/view/view[5]/view[3]')
        im[0].tap()
        self.delay(3)
        self.get_screenshot()
        self.delay(3)
