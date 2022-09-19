# add by zzh
import time

from base.test_base import TestBase


class TestTfqSearch(TestBase):
    """
    淘房圈搜索页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/search/search?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqSearch, self).setUp()
        print("TestTfqSearch  Setup")

    def test_input_clear_and_search_result_select(self):
        """
        淘房圈搜索页面，输入内容“测试”，搜索，点击搜索框内的清除按钮，再次搜索当天日期，选择第一条结果，进详情页
        """
        self.page.get_element('input[class="searchTR-input"]').input("测试")
        self.delay(1)
        self.page.get_element('view[class="search_txt"]').tap()
        self.delay(1)
        self.page.get_element('view[class="cancle"]')

        self.page.get_element('input[class="searchTR-input"]').input(time.strftime('%Y-%m-%d'))
        self.delay(1)
        self.page.get_element('view[class="search_txt"]').tap()
        self.delay(1)
        if not self.page.element_is_exists('view[class="notresult"]', max_timeout=3):
            self.page.get_element('view[class="post_Title list-desc"]').tap()

            self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_keywords_to_delete(self):
        """
        淘房圈搜索页面，点击搜索历史删除按钮
        """
        b_l = self.page.element_is_exists('view[class="searchBT-r"]')
        if b_l == True:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            e = self.page.get_element('view[class="searchBT-r"]')
            e.tap()
            self.app.restore_wx_method("showModal")
            self.delay(2)
            self.capture("提示")
            self.native.handle_modal("取消", "提示")
        else:
            print("没有搜索历史")

        self.get_screenshot()

    def test_keywords_search(self):
        """
        淘房圈搜索页面,有搜索历史，点击搜索历史搜索，选择结果的第一条，进详情页
        """
        b_l = self.page.element_is_exists('view[class="searchBT-r"]')
        if b_l == True:
            self.page.get_element('text[class="item"]').tap()

            self.delay(1)
            self.page.get_element('view[class="post_Title list-desc"]').tap()

            self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        else:
            print("没有搜索历史")

        self.get_screenshot()

    def test_click_title(self):
        """
        淘房圈搜索页面，点击热帖墙标题
        """
        self.page.get_element('view[class="hotCont list-desc"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_more(self):
        """
        淘房圈搜索页面，点击更多热帖
        """
        self.page.get_element('view[class="morewall"]').tap()

        self.verifyPageName('/page/taofangquan/tieziList/tieziList')
        self.get_screenshot()

