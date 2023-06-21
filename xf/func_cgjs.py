from base.test_base import TestBase


class Funccgjs(TestBase):
    """
    采光计算器 页面 元素
    """
    def select_city(self):
        # 选择 城市
        self.find_element('picker').trigger("change", {"value": [15, 0]})

    def select_total_floor(self):
        # 选择 6层
        self.set_pick_filter('picker[class="flex-1 t-r"]', 5)

    def input_height(self):
        # 输入 单层高度
        # self.find_element('input').input('9.9')
        self.input_value_by_mk('xf/cg_cg.png', '9.9\n', direction=1)
        self.delay(5)

    def click_next(self):
        # 点击 下一步
        self.find_element('view[class="nextBtn"]').tap()
        self.delay(5)
        if self.element_is_exist('view[class="nextBtn"]'):
            self.input_value_by_mk('xf/cg_next.png')

    def select_floor(self):
        # 选择 居住楼层 3层
        self.set_pick_filter('picker[class="flex-1 t-r"]', 2)

    def input_distance(self):
        # 输入楼距 2米
        # self.find_element('input').input('2')
        self.input_value_by_mk('xf/cg_lj.png', '60')

    def click_back(self):
        # 点击 上一步
        self.find_element('view[class="backBtn"]').tap()

    def click_result(self):
        # 点击 开始计算
        self.find_element('view[class="countResult"]').tap()
        self.delay(6)

    def click_im(self):
        # 点击 咨询采光
        self.find_element('view[class="codezx tfFlex tfAlignC"]').tap()

    def click_repeat(self):
        # 点击 重新计算
        self.find_element('view[class="jsBtn"]', inner_text='重新计算').tap()
        self.delay(3)

