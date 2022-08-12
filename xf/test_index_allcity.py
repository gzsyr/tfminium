# add by zsy
from base.test_base import TestBase


class TestAllcity(TestBase):
    def setUp(self) -> None:
        self.page_name = "/page/index/city"
        self.switch = False
        super(TestAllcity, self).setUp()
        print("TestAllcity setup atest")

    def test_select_qz(self):
        """
        选择站点：泉州
        :return:
        """
        self.page.get_element('text[class="hot-city"]', inner_text="泉州").click()

    # def click_location(self):
    #     """
    #     点击重新定位按钮
    #     :return:
    #     """
    #     called = threading.Semaphore(0)
    #     callback_args = None
    #
    #     def callback(args):
    #         nonlocal callback_args
    #         called.release()
    #         callback_args = args
    #
    #     self.app.hook_wx_method("getLocation", callback=callback)
    #     self.page.get_element("text[class='hot-city']", inner_text="重新定位").tap()
    #     delay(1)
    #     self.native.allow_get_location(True)  # 授权获取位置
    #     self.native.map_back_to_mp()  # 确认选择位置
    #     is_called = called.acquire(timeout=10)
    #     self.app.release_hook_wx_method("getLocation")
    #     delay(10)