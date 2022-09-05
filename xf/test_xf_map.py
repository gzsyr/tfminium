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

    @file_data('./test_xf_map_sx.yml')
    def test_xf_map_sx(self, **kwargs):
        """
        地图找房页面，通过筛选项筛选地图数据(先清空筛选项)
        """
        self.page.get_element('cover-image[class="map_filter_btn"]').click()

        # self.page.get_element('cover-image[class="cancel"]').click()

        if kwargs['price'] != '':
            self.page.get_element('cover-view[data-type="price"]', inner_text=kwargs['price']).click()
        if kwargs['roomtag'] != '':
            self.page.get_element('cover-view[data-type="roomtag"]', inner_text=kwargs['roomtag']).click()
        if kwargs['recommendTag'] != '':
            self.page.get_element('cover-view[data-type="recommendTag"]', inner_text=kwargs['recommendTag']).click()
        if kwargs['channel'] != '':
            self.page.get_element('cover-view[data-type="channel"]', inner_text=kwargs['channel']).click()
        if kwargs['mjtag'] != '':
            self.page.get_element('cover-view[data-type="mjtag"]', inner_text=kwargs['mjtag']).click()
        if kwargs['kptag'] != '':
            self.page.get_element('cover-view[data-type="kptag"]', inner_text=kwargs['kptag']).click()
        if kwargs['decoratetag'] != '':
            self.page.get_element('cover-view[data-type="decoratetag"]', inner_text=kwargs['decoratetag']).click()

        self.page.get_element('cover-view[class="confirm"]').click()

        self.get_screenshot()

    @file_data('./test_xf_map_search.yml')
    def test_xf_map_search(self, lpname="万科雨悦光年"):
        """
        地图找房页面，通过关键词搜索
        """
        self.page.get_element('cover-image[class="map_search_btn"]').click()

        self.verifyPageName('/page/search/index')
        # 到搜索页面
        self.page.get_element('input[class="searchTR-input"]').input(lpname+'\n')
        self.delay(1)

        self.page.get_element(f'view[data-lpname="{lpname}"]').tap()
        self.delay(2)
        # 展示搜索结果
        if self.page.element_is_exists('cover-view[class="item-content"]'):
            self.page.get_element('cover-view[class="item-content"]').click()

            self.verifyPageName('/page/newhouse/detail')

        self.get_screenshot()