# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestLogoutTfq(TestBase):
    """
    未登录  淘房圈相关用例
    """
    def setUp(self) -> None:
        self.classname = self.__class__.__name__
        count = 0
        while self.get_newcity() != '泉州' and count < 3:
            print('当前城市不是泉州，需要切换')
            self.app.navigate_to('/page/index/city')
            self.page.get_element('text[class="hot-city"]', inner_text="泉州").tap()
            count += 1
        super(TestLogoutTfq, self).setUp()

    def test_tfq_shouye_新人有奖(self):
        """
        V6.19.X: 首次进入淘房圈首页（泉州站后台开启新人有奖活动）
        """
        count = 0
        while self.page.path != "/page/find/find" and count < 3:
            self.app.switch_tab("/page/find/find?city=qz")
            self.delay(1)
            count += 1
            print('切换到淘房圈首页！', self.page.path, count)

        self.delay(1)
        ret = self.get_newcomergift()
        if ret == False:
            self.verifyStr(True, self.element_is_exist('view[class="newcomergift--alterWrap"]'), '有新人广告')
        self.get_screenshot()
        self.remove_newcomergift()

    def test_tfq_huati_新人有奖(self):
        """
        V6.19.X: 进入话题详情页（泉州站后台开启新人有奖活动）
        """
        self.app.relaunch(f"/page/taofangquan/tieziDetail/tieziDetail?city=qz&postsid={self.huatiid}")
        self.delay(1)
        ret = self.get_newcomergift()
        if ret == False:
            self.verifyStr(True, self.element_is_exist('view[class="newcomergift--alterWrap"]'), '有新人广告')
        self.get_screenshot()
        self.remove_newcomergift()

    def test_tfq_post_新人有奖(self):
        """
        V6.19.X: 进入帖子详情页（泉州站后台开启新人有奖活动）
        """
        self.app.relaunch(f"/page/taofangquan/tieziDetail/tieziDetail?city=qz&postsid={self.postid}")
        self.delay(1)
        ret = self.get_newcomergift()
        if ret == False:
            self.verifyStr(True, self.element_is_exist('view[class="newcomergift--alterWrap"]'), '有新人广告')
        self.get_screenshot()
        self.remove_newcomergift()

