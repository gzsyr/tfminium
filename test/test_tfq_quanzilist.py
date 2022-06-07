import minium
from test.common import delay

class TestQuanZi(minium.MiniTest):
    """
    圈子广场
    """

    def setUp(self) -> None:
        self.app.navigate_to("/page/taofangquan/huati/huatiSquare?city=qz")
        delay(2)
        self.app.get_current_page()
        print("test  setup!!!!!!!!!!!!!")

    def test_click_quanzi(self):
        """
        点击圈子，进入圈子详情页
        :return:
        """
        e = self.page.get_element('view[class="flex tfAlignC hotSearch"]')
        e.tap()
        delay(2)

    def test_click_btn1(self):
        """
        点击圈子列表的”关注“按钮
        :return:
        """
        e = self.page.get_element('view[class="btn"]', inner_text="关注")
        e.tap()
        delay(2)

    def test_click_btn2(self):
        """
        点击圈子列表的”已关注“按钮
        :return:
        """
        e = self.page.get_element('view[class="btn"]', inner_text="已关注")
        e.tap()
        delay(2)