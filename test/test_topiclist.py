import minium

from test.common import delay

class TestTopicList(minium.MiniTest):

    """
    话题列表页
    """

    def setUp(self) -> None:
        self.app.navigate_to("/page/taofangquan/huati/huatiList?city=qz")
        delay(3)
        self.app.get_current_page()
        print("setUp!!!!")

    def test_click_topictitle(self):
        """
        话题列表，点击话题标题
        :return:
        """
        e = self.page.get_element('view[class="title"]')
        e.tap()
        delay(2)

    def test_click_PK(self):
        """
        话题列表，点击pk话题pk按钮
        :return:
        """
        b_l = self.page.element_is_exists('view[class="Pk--button"]')
        if b_l == True:
            e = self.page.get_element('view[class="Pk--button"]')
            e.tap()
            delay(1)
        else:
            print("没有可点击的Pk按钮")

    def test_click_join(self):
        """
        话题列表，点击普通话题“查看详情”按钮
        :return:
        """
        e = self.page.get_element('view[class="join"]')
        e.tap()
        delay(2)

    def test_click_share(self):
        """
        话题列表，点击分享按钮
        :return:
        """
        e = self.page.get_element('button[class="newHouseRfixed-share"]')
        e.tap()
        delay(2)

