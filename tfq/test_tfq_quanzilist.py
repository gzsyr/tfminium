from test.test_base import TestBase


class TestQuanZi(TestBase):
    """
    圈子广场
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/huati/huatiSquare?city=qz"
        self.switch = False
        super(TestQuanZi, self).setUp()
        print("TestQuanZi  Setup")

    def test_click_quanzi(self):
        """
        点击圈子，进入圈子详情页
        :return:
        """
        e = self.page.get_element('view[class="hotSearch"]')
        e.tap()

    def test_click_btn1(self):
        """
        点击圈子列表的”关注“按钮
        :return:
        """
        ret = self.page.element_is_exists('view[class="btn"]', inner_text="关注")
        if ret == True:
            self.page.get_element('view[class="btn"]', inner_text="关注").tap()
        else:
            print("第一条圈子已关注，此用例直接pass")

    def test_click_btn2(self):
        """
        点击圈子列表的”已关注“按钮
        :return:
        """
        e = self.page.get_element('view[class="btn"]', inner_text="已关注")
        e.tap()

