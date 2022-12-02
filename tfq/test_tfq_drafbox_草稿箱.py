from base.test_base import TestBase


class TestTfqDrafBox(TestBase):
    """
    草稿箱页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/mine/draftBox/draftBox?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqDrafBox, self).setUp()
        print("TestTfqDrafBox setup")

    def test_02_click_draftitle_点击帖子标题(self):
        """
        草稿箱页面，点击帖子草稿标题
        """
        self.find_element('view[class="draft_tit"]').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def test_01_click_delete_删除草稿(self):
        """
        草稿箱页面，点击帖子草稿删除按钮，二次确定点击删除
        """
        b_l = self.page.element_is_exists('view[class="draft_delete"]')
        if b_l:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.find_element('view[class="draft_delete"]').tap()
            self.app.restore_wx_method("showModal")
            self.delay(2)
        else:
            print("没有帖子草稿")

        self.get_screenshot()

    def test_04_click_lptab_楼盘评论(self):
        """
        草稿箱页面，切换至楼盘评论tab
        """
        self.find_element('view[class="draft_item"]', inner_text="楼盘评论").tap()

        self.get_screenshot()

    def test_05_click_lptitle_楼盘评论标题(self):
        """
        草稿箱页面，切换至楼盘评论tab，点击楼盘评论标题
        """
        self.find_element('view[class="draft_item"]', inner_text="楼盘评论").tap()
        self.delay(3)

        exist = self.page.element_is_exists('view[class="tfLine1 mt10"]')
        if exist:
            self.find_element('view[class="tfLine1 mt10"]').tap()
        else:
            print("暂无楼盘评论，直接pass")

        self.get_screenshot()

    def test_03_click_lpdelete_confirm_删除楼盘评论(self):
        """
        草稿箱页面，切换至楼盘评论tab，点击楼盘评论删除按钮，二次确认点击取消
        """
        self.find_element('view[class="draft_item"]', inner_text="楼盘评论").tap()
        self.delay(3)
        b_l = self.page.element_is_exists('view[class="draft_delete"]')
        if b_l:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.find_element('view[class="draft_delete"]').tap()
            self.app.restore_wx_method("showModal")
            self.delay(2)
        else:
            print("没有楼盘评论草稿，直接pass")

        self.get_screenshot()
