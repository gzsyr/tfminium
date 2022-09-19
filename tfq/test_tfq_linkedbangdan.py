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

    def test_click_tab1(self):
        """
        淘房圈-推荐榜单页面,点击第一个tab
        """
        self.page.get_elements('image[class="bd_icon"]')[0].tap()

        self.get_screenshot()

    def test_click_tab2(self):
        """
        淘房圈-推荐榜单页面,点击第二个tab
        """
        self.page.get_elements('image[class="bd_icon"]')[1].tap()

        self.get_screenshot()

    def test_click_tiezi(self):
        """
        淘房圈-推荐榜单页面，点击帖子
        """
        self.page.get_element('view[class="post_title tfLine1"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_post(self):
        """
        淘房圈-推荐榜单页面，点击”发帖“
        """
        self.page.get_element('image[class="postBtn_img"]').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def test_click_share(self):
        """
        淘房圈-推荐榜单页面，点击”分享“
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()

        self.get_screenshot()

    def test_click_share_hb(self):
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

    def test_z_click_share_hy(self):
        """
        淘房圈-推荐榜单页面，点击”分享“，分享好友
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(2)
        self.page.get_element('button[class="share-btn hy"]').tap()

        self.get_screenshot()