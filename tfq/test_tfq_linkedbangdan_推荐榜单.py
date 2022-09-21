from base.test_base import TestBase


class TestTfqLinkedBangdan(TestBase):
    """
    推荐榜单页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/bangdan/recommend?city=qz&main_id=1"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqLinkedBangdan, self).setUp()
        print("TestLinkedBangdan setup")

    def test_04_click_tab1_推荐第一个tab(self):
        """
        淘房圈-推荐榜单页面,点击第一个tab
        """
        self.page.get_elements('image[class="bd_icon"]')[0].tap()

        self.get_screenshot()

    def test_05_click_tab2_推荐第二个tab(self):
        """
        淘房圈-推荐榜单页面,点击第二个tab
        """
        self.page.get_elements('image[class="bd_icon"]')[1].tap()

        self.get_screenshot()

    def test_06_click_tiezi_点击帖子(self):
        """
        淘房圈-推荐榜单页面，点击帖子
        """
        self.page.get_element('view[class="post_title tfLine1"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_01_click_post_点击发帖(self):
        """
        淘房圈-推荐榜单页面，点击”发帖“
        """
        self.page.get_element('image[class="postBtn_img"]').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def test_02_click_share_分享(self):
        """
        淘房圈-推荐榜单页面，点击”分享“
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()

        self.get_screenshot()

    def test_03_click_share_hb_分享海报(self):
        """
        淘房圈-推荐榜单页面，点击”分享“，生成海报
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(2)
        self.page.get_element('button[class="share-btn pyq"]').tap()

        self.verifyStr(True,
                       self.page.element_is_exists('button[class="canvasToImage--saveToAlbumButton"]'),
                       '生成海报页 ok')
        self.get_screenshot()

    def test_07_z_click_share_hy_分享好友(self):
        """
        淘房圈-推荐榜单页面，点击”分享“，分享好友
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(2)
        self.page.get_element('button[class="share-btn hy"]').tap()

        self.get_screenshot()