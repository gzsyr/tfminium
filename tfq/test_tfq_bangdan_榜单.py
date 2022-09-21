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

    def test_05_click_tiezi_点击帖子(self):
        """
        淘房圈-榜单页面，点击帖子
        """
        self.page.get_element('view[class="post_title tfLine1"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_02_click_post_发帖按钮(self):
        """
        淘房圈-榜单页面，点击”发帖“
        """
        self.page.get_element('image[class="postBtn_img"]').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def test_01_click_more_推荐榜单(self):
        """
        淘房圈-榜单页面，点击”推荐榜单“
        """
        self.page.get_element('view[class="more_txt"]').tap()

        self.get_screenshot()

    def test_03_click_share_分享(self):
        """
        淘房圈-榜单页面，点击”分享“
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()

        self.get_screenshot()

    def test_04_click_share_hb_分享海报(self):
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

    def test_06_z_click_share_hy_分享好友(self):
        """
        淘房圈-榜单页面，点击”分享“，分享好友
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(2)
        self.page.get_element('button[class="share-btn hy"]').tap()
        self.delay(1)
        self.input_value_by_mk('tfq/share_send.png')

        self.get_screenshot()

