# add by zsy
from ddt import ddt, file_data

from base.test_base import TestBase


@ddt
class TestFuncZhiBo(TestBase):
    """
    直播看房页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/chatroom/index?city=qz'
        self.switch = False
        super(TestFuncZhiBo, self).setUp()
        print('TestFuncZhiBo setup')

    @file_data('./test_func_zhibo.yml')
    def test_search(self, **kwargs):
        """
        直播看房页面，搜索 直播人的名字，并进入搜索结果第一条
        """
        self.goto_search(True, kwargs['anchor'])

        self.goto_zhibo()
        # 校验
        self.verifyContainsStr(kwargs['anchor'], self.page.get_element('view[class="zb-now-t flex flexSb"]').inner_text,
                               '点击搜索结果第一个，进入直播详情 ok')
        # self.verifyStr(True, self.page.element_is_exists('view[class="name"]', inner_text=kwargs['anchor']), '直播看房页面，搜索 主播 存在')

    @file_data('./test_func_zhibo.yml')
    def test_select_city(self, **kwargs):
        """
        直播看房页面，选择城市
        """
        self.goto_search(False, kwargs['city'])

        # 校验
        self.verifyStr(True, self.page.element_is_exists('view[class="mainContent"]'),
                       '城市列表页面数据 存在')

    def goto_zhibo(self):
        """
        点击列表页第一个直播，进入直播详情页
        """
        self.page.get_element('view[class="tt bold"]').click()
        self.delay(1)

    def goto_search(self, select=True, kw='六安楼市'):
        """
        进入直播搜索/城市选择页面
        select: True-进入搜索页
                False-进入城市列表页
        kw: 对应的选择词
        """
        if select:
            # 跳转到搜索页
            self.page.get_element('navigator[class="searchR"]').click()
            self.app.wait_for_page('/page/chatroom/search?city=qz')
            # 输入关键字搜索
            self.page.get_element('input[type="text"]').input(kw + "\n")
            self.delay(1)
        else:
            # 跳转到城市页
            self.page.get_element('navigator[class="searchL flex"]').click()
            self.app.wait_for_page('/page/chatroom/city?city=qz')
            # 输入关键字搜索
            self.delay(1)
            self.page.get_element(f'view[data-name="{kw}"]').click()

        return self