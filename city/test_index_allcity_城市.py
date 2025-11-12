# add by zsy
import pytest

from base.test_base import TestBase


class TestAllcity(TestBase):
    def setUp(self) -> None:
        self.page_name = "/page/index/city"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestAllcity, self).setUp()
        print("TestAllcity setup atest")

    @pytest.mark.qz
    def test_select_qz_选择泉州(self):
        """
        选择站点：泉州
        :return:
        """
        while self.get_newcity() != '泉州':
            print('当前城市不是泉州，需要切换')
            self.page.get_element('text[class="hot-city"]', inner_text="泉州").tap()
            self.delay(1)
        self.app.go_home()
        self.get_screenshot()

    @pytest.mark.im_consult
    def test_select_nj_选择南京(self):
        """
        选择站点：南京
        :return:
        """
        while self.get_newcity() != '南京':
            print('当前城市不是南京，需要切换')
            self.page.get_element('text[class="hot-city"]', inner_text="南京").tap()
            self.delay(1)
        self.app.go_home()
        self.get_screenshot()

