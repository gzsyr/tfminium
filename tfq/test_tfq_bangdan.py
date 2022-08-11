from test.test_base import TestBase


class TestBangDan(TestBase):
    """
    榜单页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/bangdan/main?main_id=1&city=qz"
        self.switch = False
        super(TestBangDan, self).setUp()
        print("TestBangDan setup")

    def test_click_tiezi(self):
        """
        淘房圈-榜单页面，点击帖子
        """
        self.page.get_element('view[class="post_title tfLine1"]').tap()

    def test_click_post(self):
        """
        淘房圈-榜单页面，点击”发帖“
        """
        self.page.get_element('image[class="postBtn_img"]').tap()

    def test_click_more(self):
        """
        淘房圈-榜单页面，点击”推荐榜单“
        """
        self.page.get_element('view[class="more_txt"]').tap()

    def test_click_share(self):
        """
        淘房圈-榜单页面，点击”分享“
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()


    def test_click_share_hb(self):
        """
        淘房圈-榜单页面，点击”分享“，生成海报
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(2)
        self.page.get_element('button[class="share-btn pyq"]').tap()

    def test_z_click_share_hy(self):
        """
        淘房圈-榜单页面，点击”分享“，分享好友
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(2)
        self.page.get_element('button[class="share-btn hy"]').tap()


