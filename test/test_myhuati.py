import minium
from test.common import delay

class TestMyHuaTi(minium.MiniTest):
    """
    我的话题页面
    """

    def setUp(self) -> None:
        self.app.navigate_to("/page/mine/myHuati/myHuati?city=qz")
        delay(2)
        self.app.get_current_page()
        print("test  setup!!!!!!!!!!!!!")

    def tearDown(self) -> None:
        delay(2)

    def test_click(self):
        """
        我的话题页面，点击话题
        """
        self.page.get_element('view[class="title"]').tap()