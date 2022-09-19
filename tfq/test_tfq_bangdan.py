from base.test_base import TestBase


class TestTfqBangDan(TestBase):
    """
    榜单页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/bangdan/main?main_id=1&city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqBangDan, self).setUp()
        print("TestTfqBangDan setup")

    def test_click_tiezi(self):
        """
        淘房圈-榜单页面，点击帖子
        """
        self.page.get_element('view[class="post_title tfLine1"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_post(self):
        """
        淘房圈-榜单页面，点击”发帖“
        """
        self.page.get_element('image[class="postBtn_img"]').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def test_click_more(self):
        """
        淘房圈-榜单页面，点击”推荐榜单“
        """
        self.page.get_element('view[class="more_txt"]').tap()

        self.get_screenshot()

    def test_click_share(self):
        """
        淘房圈-榜单页面，点击”分享“
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()

        self.get_screenshot()

    def test_click_share_hb(self):
        """
        淘房圈-榜单页面，点击”分享“，生成海报
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
        淘房圈-榜单页面，点击”分享“，分享好友
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(2)
        self.page.get_element('button[class="share-btn hy"]').tap()
        self.delay(1)
        self.input_value_by_mk('tfq/share_send.png')

        self.get_screenshot()

