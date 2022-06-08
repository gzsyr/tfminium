from test.test_base import TestBase


class TestLinkedBangdan(TestBase):
    """
    推荐榜单页面
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/bangdan/recommend?city=qz&main_id=1"
        self.switch = False
        super(TestLinkedBangdan, self).setUp()
        print("TestLinkedBangdan setup")

    def test_click_tab1(self):
        """
        淘房圈-推荐榜单页面,点击第一个tab
        """
        self.page.get_elements('image[class="bd_icon"]')[0].tap()


    def test_click_tab2(self):
        """
        淘房圈-推荐榜单页面,点击第二个tab
        """
        self.page.get_elements('image[class="bd_icon"]')[1].tap()

    def test_click_tiezi(self):
        """
        淘房圈-推荐榜单页面，点击帖子
        """
        self.page.get_element('view[class="post_title tfLine1"]').tap()

    def test_click_post(self):
        """
        淘房圈-推荐榜单页面，点击”发帖“
        """
        self.page.get_element('image[class="postBtn_img"]').tap()

    def test_click_moreBtn(self):
        """
        淘房圈-推荐榜单页面，点击”主榜单“
        """
        self.page.get_element('view[class="moreBtn"]').tap()

    def test_click_share(self):
        """
        淘房圈-推荐榜单页面，点击”分享“
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()

    def test_click_share_hb(self):
        """
        淘房圈-推荐榜单页面，点击”分享“，生成海报
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(2)
        self.page.get_element('button[class="share-btn pyq"]').tap()

    def test_click_share_hy(self):
        """
        淘房圈-推荐榜单页面，点击”分享“，分享好友
        """
        self.page.get_element('button[class="newHouseRfixed-share"]').tap()
        self.delay(2)
        self.page.get_element('button[class="share-btn hy"]').tap()