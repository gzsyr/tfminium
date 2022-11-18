# add by zsy
from ddt import ddt, file_data

from base.test_base import TestBase

@ddt
class TestXfMap(TestBase):
    """
    新房地图页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/newhouse/mapzf/mapzf?city=nj'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestXfMap, self).setUp()

    def test_03_xf_map_hotim_热门咨询(self):
        """
        V6.24.V: 热门咨询模块，点击提问
        """
        ele = self.find_element('view[class="scrollitem"]')

        question = ele.attribute('data-question')
        ele.tap()

        self.delay(4)
        self.verifyPageName('/im/pages/chating/chating')
        imquestion = self.find_elements('view[class="record-chatting-item self"]')[-1].inner_wxml
        self.verifyContainsStr(question[0], imquestion)
        self.get_screenshot()

    def change(self):
        """
        点击“地铁找房”
        """
        self.find_element('view[class="metro_name_dt"]').tap()

    def test_05_xf_metro_change_切换地铁找房(self):
        """
        V6.24.X: 点击“地铁找房”
        """
        self.change()

        self.get_screenshot()

    def test_06_xf_metro_hotim_热门咨询(self):
        """
        V6.24.X: 进入地铁页面，点击问题咨询
        """
        self.change()
        self.delay(2)

        ele = self.find_element('view[class="scrollitem"]')

        question = ele.attribute('data-question')
        ele.tap()

        self.delay(4)
        self.verifyPageName('/im/pages/chating/chating')
        imquestion = self.find_elements('view[class="record-chatting-item self"]')[-1].inner_wxml
        self.verifyContainsStr(question[0], imquestion)
        self.get_screenshot()

    def test_07_xf_metro_sx_地铁筛选(self):
        """
        V6.24.X: 进入地铁页面，选择线路和站点，筛选
        """
        self.change()
        self.delay(2)

        self.find_element('view[class="screenTop_list"]').tap()
        self.delay(1)
        self.find_element('view[class="tfLine1 p10"]', inner_text='迈皋桥站').tap()

        self.find_element('view[class="screenBtn_confirm"]').tap()

        self.get_screenshot()

    def test_09_xf_metro_clear_清空筛选项(self):
        """
        V6.24.X: 进入地铁页面，选择“1号线”筛选，点击“清空”
        """
        self.change()
        self.delay(2)

        self.find_element('view[class="screenTop_list"]').tap()
        self.delay(1)
        self.find_element('view[class="tfLine1 p10"]', inner_text='迈皋桥站').tap()

        self.find_element('view[class="screenBtn_confirm"]').tap()

        self.delay(2)
        self.set_clear('view[class="screenTop_list screenTop_list_act"]')

        self.get_screenshot()

    def test_08_xf_map_clear_清空筛选项(self):
        """
        V6.24.X: 进入地图页面，选择“价格”筛选，点击“清空”
        """
        self.set_filter(kwargs={'price': '30000-35000元/㎡'})
        self.delay(2)
        self.set_clear('view[class="screenTop_list screenTop_list_act"]')

        self.get_screenshot()

    def test_04_xf_map_filter_change_设筛选来回切换(self):
        """
        V6.24.X: 筛选项来回切换
        """
        kw = {'price': '30000-35000元/㎡'}
        self.set_filter(kw)

        self.change()
        self.verifyPageName('/page/newhouse/metrozf/metrozf')

        self.change()
        self.verifyPageName('/page/newhouse/mapzf/mapzf')

        self.get_screenshot()

    def set_clear(self, sx):
        """
        地图页面，点击“sx”，点击清空
        sx: 点击的筛选项元素
        """
        self.find_element(sx).tap()
        self.find_element('view[class="screenBtn_clear"]').tap()

    def set_filter(self, kwargs):
        """
        设置筛选条件
        """
        # 价格
        if 'price' in kwargs.keys() and kwargs['price'] != '':
            self.find_element('view[class="screenTop_list"][data-type="price"]').tap()
            self.find_element('view[class="screenCon_list_price"]', inner_text=kwargs['price']).tap()
            self.find_element('view[class="screenBtn_confirm"]').tap()

        # 户型
        if 'roomtag' in kwargs.keys() and kwargs['roomtag'] != '':
            self.find_element('view[class="screenTop_list"][data-type="roomtag"]').tap()
            self.find_element('view[class="screenCon_list"]', inner_text=kwargs['roomtag']).tap()
            self.find_element('view[class="screenBtn_confirm"]').tap()

        # 装修
        if 'decoratetag' in kwargs.keys() and kwargs['decoratetag'] != '':
            self.find_element('view[class="screenTop_list"][data-type="decoratetag"]').tap()
            self.find_element('view[class="screenCon_list"]', inner_text=kwargs['decoratetag']).tap()
            self.find_element('view[class="screenBtn_confirm"]').tap()

        # 面积
        if 'mjtag' in kwargs.keys() and kwargs['mjtag'] != '':
            self.find_element('view[class="screenTop_list"][data-type="mjtag"]').tap()
            self.find_element('view[class="screenCon_list"]', inner_text=kwargs['mjtag']).tap()
            self.find_element('view[class="screenBtn_confirm"]').tap()

        # 更多
        if ('recommendTag' in kwargs.keys() and kwargs['recommendTag'] != '') \
                or ('channel' in kwargs.keys() and kwargs['channel'] != '') \
                or ('kptag' in kwargs.keys() and kwargs['kptag'] != ''):
            self.find_element('view[class="screenTop_list"][data-type="more"]').tap()
            if kwargs['recommendTag'] != '':
                self.find_element('view[class="screenCon_list"]', inner_text=kwargs['recommendTag']).tap()
            if kwargs['channel'] != '':
                self.find_element('view[class="screenCon_list"]', inner_text=kwargs['channel']).tap()
            if kwargs['kptag'] != '':
                self.find_element('view[class="screenCon_list"]', inner_text=kwargs['kptag']).tap()
            self.find_element('view[class="screenBtn_confirm"]').tap()

    @file_data('./test_xf_map_sx.yml')
    def test_02_xf_map_sx_地图筛选(self, **kwargs):
        """
        V6.24.X: 更新，地图找房页面，通过筛选项筛选地图数据
        """
        self.set_filter(kwargs)

        self.delay(3)
        self.get_screenshot()

    @file_data('./test_xf_map_search.yml')
    def test_01_xf_map_search_地图搜索(self, lpname="万科雨悦光年"):
        """
        地图找房页面，通过关键词搜索
        """
        self.find_element('image[class="map_search_btn"]').tap()
        self.delay(3)
        self.verifyPageName('/page/search/index')
        # 到搜索页面
        self.find_element('input[class="searchTR-input"]').input(lpname+'\n')
        self.delay(1)

        self.find_element(f'view[data-lpname="{lpname}"]').tap()
        self.delay(2)
        # 展示搜索结果
        if self.page.element_is_exists('cover-view[class="item-content"]'):
            self.find_element('cover-view[class="item-content"]').click()

            self.verifyPageName('/page/newhouse/detail')

        self.get_screenshot()