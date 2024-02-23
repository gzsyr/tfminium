# -*-coding:utf-8-*-
import minium

from tfq.writepost import WritePost


class TestTieziIM(WritePost):
    """
    C身份  帖子相关内容
    包括：发帖，评论，等最后删除帖子
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestTieziIM, cls).setUpClass()
        cls().change_C()
        print("setupclass TestTieziIM")

    post_page = None

    def setUp(self) -> None:
        if self.post_page is None:
            # self.page_name = '/page/taofangquan/writePost/writePost?city=nj'
            self.page_name = f"/page/taofangquan/tieziDetail/tieziDetail?city=nj&postsid={self.jjr_postid}"
        else:
            self.page_name = self.post_page
        # self.page_name = f"/page/taofangquan/tieziDetail/tieziDetail?city=nj&postsid={self.jjr_postid}"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTieziIM, self).setUp()

    def test_001_点击经纪人咨询(self):
        """
        点击经纪人咨询icon，进入im页面
        """
        self.find_element('view[class="connect fbs_contact_tap"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

    def test_002_点击底部经纪人咨询(self):
        """
        点击底部经纪人咨询，进入im
        """
        self.find_element('image[class="bottom-connect-avatar"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

    def test_003_点击推荐二手房咨询(self):
        """
        点击推荐二手房咨询，进入IM
        """
        self.page.scroll_to(2600, 200)
        self.delay(2)
        # 切换到二手房
        # self.find_element('view[class="tab"][data-index="2"]').tap()
        self.find_element('view[class="flex recommend_tab"]/view[data-index="2"]').tap()
        self.delay(2)
        # 点击IM咨询
        self.find_element('image[class="villageItem--chat"]').tap()
        self.delay(3)

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

