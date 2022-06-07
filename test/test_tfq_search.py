# add by zzh
import minium
from test.common import delay

class TestTfqSearch(minium.MiniTest):
    """
    淘房圈搜索页面
    """

    def setUp(self) -> None:
        self.app.navigate_to("/page/taofangquan/search/search?city=qz")
        delay(3)
        self.app.get_current_page()
        print("test  setup!!!!!!!!!!!!!")

    def tearDown(self) -> None:
        delay(2)

    def test_input_search(self):
        """
        淘房圈搜索页面，输入内容“测试”，搜索
        """
        self.page.get_element('input[class="searchTR-input"]').input("测试")
        delay(1)
        self.page.get_element('view[class="search_txt"]').tap()
        delay(1)

    def test_input_clear(self):
        """
        淘房圈搜索页面，输入内容“测试”，搜索，点击搜索框内的清除按钮
        """
        self.page.get_element('input[class="searchTR-input"]').input("测试")
        delay(1)
        self.page.get_element('view[class="search_txt"]').tap()
        delay(1)
        self.page.get_element('view[class="cancle"]')

    def test_click_search_result(self):
        """
        淘房圈搜索页面，输入内容“测试”，搜索，点击搜索结果
        """
        self.page.get_element('input[class="searchTR-input"]').input("测试")
        delay(1)
        self.page.get_element('view[class="search_txt"]').tap()
        delay(3)
        self.page.get_element('view[class="post_Title list-desc"]').tap()

    def test_click_delete(self):
        """
        淘房圈搜索页面，点击搜索历史删除按钮
        """
        b_l = self.page.element_is_exists('view[class="searchBT-r"]')
        if b_l == True:
            result = {"confirm": False}
            self.app.mock_wx_method("showModal", result=result)
            e = self.page.get_element('view[class="searchBT-r"]')
            e.tap()
            self.app.restore_wx_method("showModal")
            delay(2)
            self.capture("提示")
            self.native.handle_modal("取消", "提示")
        else:
            print("没有搜索历史")

    def test_click_history_search(self):
        """
        淘房圈搜索页面,有搜索历史，点击搜索历史搜索
        """
        b_l = self.page.element_is_exists('view[class="searchBT-r"]')
        if b_l == True:
            self.page.get_element('text[class="item"]').tap()
        else:
            print("没有搜索历史")

    def test_click_title(self):
        """
        淘房圈搜索页面，点击热帖墙标题
        """
        self.page.get_element('view[class="hotCont list-desc"]').tap()

    def test_click_more(self):
        """
        淘房圈搜索页面，点击更多热帖
        """
        self.page.get_element('view[class="morewall"]').tap()




