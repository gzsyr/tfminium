# add by zzh
import threading

from base.test_base import TestBase


class TestTfqShouYe(TestBase):

    """
    淘房圈首页
    """

    def setUp(self) -> None:
        self.page_name = "/page/find/find?city=qz"
        self.switch = True
        self.classname = self.__class__.__name__
        super(TestTfqShouYe, self).setUp()
        print("TestTfqShouYe  Setup")

    def test_goto_huati_list(self):
        """
        跳转至话题
        """
        self.page.get_element('view[class="tfq--hot-huati-more"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiList')
        self.get_screenshot()

    def test_click_mustread(self):
        """
        淘房圈首页点击必读
        """
        self.page.get_element('image[class="tfq--mustread"]').tap()

        self.verifyPageName('/page/index/webview')
        self.get_screenshot()

    def test_click_search(self):
        """
        淘房圈首页，点击搜索框
        """
        self.page.get_element('view[class="tfq--search-input"]').tap()

        self.verifyPageName('/page/taofangquan/search/search')
        self.get_screenshot()

    # @unittest.skip("v6.13.x删除此功能")
    # def test_z_click_share_top(self):
    #     """
    #     淘房圈首页，点击顶部分享按钮
    #     :return:
    #     """
    #     e = self.page.get_element("view[class='tfq--sharetxt']")
    #     e.tap()

    def test_click_banner(self):
        """
        淘房圈首页，如果有点击顶部第一张banner
        """
        b_l = self.page.element_is_exists('image[class="tfq--banner-img tfq--index_banner"]')
        if b_l == True:
            self.page.get_element('image[class="tfq--banner-img tfq--index_banner"]').tap()
        else:
            print("没有配置banner")

        self.get_screenshot()

    def test_click_topic1(self):
        """
        淘房圈首页，点击圈子模块第一个圈子
        """
        self.page.get_element('view[class="tfq--topicItem"][data-index="0"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_topic2(self):
        """
        淘房圈首页，点击圈子模块第二个圈子
        """
        e = self.page.get_element('view[class="tfq--topicItem"][data-index="1"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_topic3(self):
        """
        淘房圈首页，点击圈子模块第三个圈子
        """
        e = self.page.get_element('view[class="tfq--topicItem"][data-index="2"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_topic4(self):
        """
        淘房圈首页，点击圈子模块第四个圈子
        """
        e = self.page.get_element('view[class="tfq--topicItem"][data-index="3"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_qzSquare(self):
        """
        淘房圈首页，点击圈子模块圈子广场
        """
        self.page.get_element('image[class="tfq--topicImg"]'
                                  '[src="https://tfxcx.house365.com/static/2021tfq/square.png"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiSquare')
        self.get_screenshot()

    def test_click_active(self):
        """
        淘房圈首页，点击活动
        """
        b_l = self.page.element_is_exists('image[class="tfq--activity_qd]')
        if b_l == True:
            self.page.get_element('image[class="tfq--activity_qd]').tap()
            self.verifyPageName('/page/activity/luckydraw/luckydraw')
        else:
            print("没有配置活动")

        self.get_screenshot()


    def test_click_newpost_more(self):
        """
        淘房圈首页，点击最新热帖更多
        """
        self.page.get_element('view[class="tfq--toutiao_more"]').tap()

        self.verifyPageName('/page/taofangquan/tieziList/tieziList')
        self.get_screenshot()

    def test_click_newpost(self):
        """
        淘房圈首页，点击最新热帖第一条
        """
        self.page.get_element('view[class="tfq--toutiao-swiper-cont"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()


    def test_click_hotQuanzi_more(self):
        """
        淘房圈首页，热门圈子，点击“更多圈子”
        """
        self.page.get_element('navigator[class="tfq--more"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiSquare')
        self.get_screenshot()

    def test_click_hotQuanZi1(self):
        """
        淘房圈首页，热门圈子，点击第一个圈子
        """
        self.page.get_element('navigator[data-index="0"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_hotQuanZi2(self):
        """
        淘房圈首页，热门圈子，点击第二个圈子
        """
        self.page.get_element('navigator[data-index="1"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_hotQuanZi3(self):
        """
        淘房圈首页，热门圈子，点击第三个圈子
        """
        self.page.get_element('navigator[data-index="2"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_hotQuanZi4(self):
        """
        淘房圈首页，热门圈子，点击第四个圈子
        """
        self.page.get_element('navigator[data-index="3"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_post_content(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击正文内容
        """
        self.page.get_element('view[class="tfq--post_cont"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_post_quanzi(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击帖子圈子
        """
        self.page.get_element('view[class="tfq--posttag tfq--flex tfq--tfAlignC"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_z_click_post_share(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击分享按钮
        """
        self.page.get_element('button[class="tfq--shareDetail"]').tap()
        self.delay(1)
        self.verifyByScreenshot('tfq/sharemodal.png')

    def test_click_post_reply(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击回复的按钮
        """
        self.page.get_element('view[class="tfq--replyBtn"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_post_laud(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击点赞的按钮
        :return:
        """
        # 监听回调, 阻塞当前主线程
        called = threading.Semaphore(0)
        callback_args = None

        def callback(args):
            nonlocal callback_args
            called.release()
            callback_args = args

        self.app.hook_wx_method("showToast", callback=callback)
        self.page.get_element('view[class="tfq--laud-btn"]').tap()
        is_called = called.acquire(timeout=5)
        self.app.release_hook_wx_method("showToast")

        self.verifyStr(True, is_called, "toast called ")
        self.get_screenshot()

    # @unittest.skip("v6.13.x删除此功能")
    # def test_click_addgroup(self):
    #     """
    #     淘房圈首页 ，点击右下角“加群”按钮
    #     :return:
    #     """
    #     e = self.page.get_element('image[class="addgroup--addgroupimg"]')
    #     e.tap()


    def test_click_postbtn(self):
        """
        淘房圈首页 ，点击右下角“发帖”按钮
        :return:
        """
        self.page.get_element('image[class="tfq--postBtn_img"]').tap()

        self.verifyPageName('/page/taofangquan/writePost/writePost')
        self.get_screenshot()

    def tearDown(self) -> None:
        self.app.go_home()
        super(TestTfqShouYe, self).tearDown()

    # @unittest.skip("v6.13.x删除此功能")
    # def test_z_click_share_icon(self):
    #     """
    #     淘房圈首页 ，点击右下角“分享”按钮
    #     :return:
    #     """
    #     e = self.page.get_element('button[class="tfq--newHouseRfixed-share"]')
    #     e.tap()
    #
