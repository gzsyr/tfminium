# add by zsy
import minium

from test.common import delay


class TestKFT(minium.MiniTest):
    """
    看房团页面
    """
    def setUp(self) -> None:
        self.app.navigate_to('/page/houseteam/list')
        page = self.app.get_current_page()
        print("test  setup!!!!!!!!!!!!!")

    def test_goto_kfxq(self):
        """
        点击看房需求
        :return:
        """
        ele = self.page.get_element("view[class='kftfixed-r']")
        ele.tap()
        print("kft: ", ele)
        delay(2)

