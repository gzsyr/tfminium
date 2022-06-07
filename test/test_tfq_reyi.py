# add by zzh  淘房圈正在热议页面
import minium
from test.common import delay

class TestReYi(minium.MiniTest):
    """
    淘房圈正在热议页面
    """

    def setUp(self) -> None:
        self.app.navigate_to("/page/taofangquan/tieziList/tieziList?city=qz")
        delay(3)
        self.app.get_current_page()
        print("test  setup!!!!!!!!!!!!!")

    def tearDown(self) -> None:
        delay(2)

    def test_click_title(self):
        """
        正在热议页面，点击帖子标题
        """
        self.page.get_element('view[class="hotCont list-desc"]').tap()

    def test_click_postbt(self):
        """
        正在热议页面，点击底部发帖入口
        """
        self.page.get_element('view[class="write_Post tfFlex tfAlignC tfFlexC"]').tap()
