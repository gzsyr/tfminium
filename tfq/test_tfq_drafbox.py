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

    def test_click_draftitle(self):
        """
        草稿箱页面，点击帖子草稿标题
        """
        self.page.get_element('view[class="draft_tit"]').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def test_click_delete(self):
        """
        草稿箱页面，点击帖子草稿删除按钮，二次确定点击删除
        """
        b_l = self.page.element_is_exists('view[class="draft_delete"]')
        if b_l:
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            e = self.page.get_element('view[class="draft_delete"]')
            e.tap()
            self.app.restore_wx_method("showModal")
            self.delay(2)
            self.capture("删除")
            self.native.handle_modal("取消", "删除")
        else:
            print("没有帖子草稿")

        self.get_screenshot()

    def test_click_lptab(self):
        """
        草稿箱页面，切换至楼盘评论tab
        """
        self.page.get_element('view[class="draft_item"]', inner_text="楼盘评论").tap()

        self.get_screenshot()

    def test_click_lptitle(self):
        """
        草稿箱页面，切换至楼盘评论tab，点击楼盘评论标题
        """
        self.page.get_element('view[class="draft_item"]', inner_text="楼盘评论").tap()
        self.delay(3)

        exist = self.page.element_is_exists('view[class="tfLine1 mt10"]')
        if exist:
            self.page.get_element('view[class="tfLine1 mt10"]').tap()
        else:
            print("暂无楼盘评论，直接pass")

        self.get_screenshot()

    def test_click_lpdelete_confirm(self):
        """
        草稿箱页面，切换至楼盘评论tab，点击楼盘评论删除按钮，二次确认点击取消
        """
        self.page.get_element('view[class="draft_item"]', inner_text="楼盘评论").tap()
        self.delay(3)
        b_l = self.page.element_is_exists('view[class="draft_delete"]')
        if b_l:
            result = {"confirm": False}
            self.app.mock_wx_method("showModal", result=result)
            e = self.page.get_element('view[class="draft_delete"]')
            e.tap()
            self.app.restore_wx_method("showModal")
            self.delay(2)
            self.capture("删除")
            self.native.handle_modal("取消", "删除")
        else:
            print("没有楼盘评论草稿，直接pass")

        self.get_screenshot()
