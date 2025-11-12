# add by zsy
import pytest

from base.test_base import TestBase
from base.test_mine import TestMine


class TestAlbum(TestMine):
    """
    搜索页面
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestAlbum, cls).setUpClass()
        cls().change_zygw()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/page/newhouse/xcny/xcnylist?pinyin=sjcs1&city=qz"
        # self.page_name = "/page/newhouse/xcny/xcnylist?pinyin=shanhaiguojixzl&city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestAlbum, self).setUp()

    def click_zbpt(self):
        """
        click周边配套大图
        """
        self.find_element('image[class="xcnyAllLi-img"][data-name="配套图"][data-index="1"]').tap()
        self.delay(4)

    def test_周边配套大图(self):
        """
        V6.50.x: 周边配套大图
        """
        self.click_zbpt()
        self.find_element('view[class="nav_zbpt"]', inner_text='查看周边配套 >').tap()

        self.get_screenshot()
        self.verifyPageName('/page/publicPages/map/map')

    @pytest.mark.im_consult
    def test_周边配套大图_咨询(self):
        """
        V6.50.X: 周边配套大图_咨询
        """
        self.click_zbpt()
        self.find_element('view[class="consultEntrance--consultBtn consultEntrance--consultBtn2"]').tap()
        self.delay(3)
        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_14508')

    def test_周边配套小图(self):
        """
        V6.50.x: 周边配套小图
        """
        self.find_element('view[class="firstImg_txt"]/text', inner_text='周边配套').tap()

        self.get_screenshot()
        self.verifyPageName('/page/publicPages/map/map')

    @pytest.mark.im_consult
    def test_click_picture_im(self):
        """
        V6.50.X: 点击大图 点击咨询
        """
        self.find_element('image[class="xcnyAllLi-img"]').tap()
        self.delay(6)
        self.find_element('view[class="consultEntrance--consultIcon"]').tap()
        self.delay(3)
        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')
        self.verifyPageParams('chatTo', 'slwkgj_14508')