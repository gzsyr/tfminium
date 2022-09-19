# add by zzh
from base.test_base import TestBase


class TestTfqTopicList(TestBase):

    """
    话题列表页
    """

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/huati/huatiList?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqTopicList, self).setUp()
        print("TestTopicList  Setup")

    def test_click_topictitle(self):
        """
        话题列表，点击话题标题
        :return:
        """
        self.page.get_element('view[class="title"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_PK(self):
        """
        话题列表，点击pk话题pk按钮
        :return:
        """
        b_l = self.page.element_is_exists('view[class="Pk--button"]')
        if b_l == True:
            self.page.get_element('view[class="Pk--button"]').tap()
        else:
            print("没有可点击的Pk按钮")

        self.get_screenshot()

    def test_click_join(self):
        """
        话题列表，点击普通话题“查看详情”按钮
        :return:
        """
        self.page.get_element('view[class="join"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_share(self):
        """
        话题列表，点击分享按钮
        :return:
        """

        self.page.get_element('button[class="newHouseRfixed-share"]').tap()

        self.get_screenshot()

