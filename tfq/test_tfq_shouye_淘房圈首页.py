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

    def test_22_goto_huati_list_话题列表(self):
        """
        跳转至话题
        """
        self.page.get_element('view[class="tfq--hot-huati-more"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiList')
        self.get_screenshot()

    def test_08_click_mustread_必读(self):
        """
        淘房圈首页点击必读
        """
        self.page.get_element('image[class="tfq--mustread"]').tap()

        self.verifyPageName('/page/index/webview')
        self.get_screenshot()

    def test_17_click_search_搜索(self):
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

    def test_02_click_banner_联板广告(self):
        """
        淘房圈首页，如果有点击顶部第一张banner
        """
        b_l = self.page.element_is_exists('image[class="tfq--banner-img tfq--index_banner"]')
        if b_l == True:
            self.page.get_element('image[class="tfq--banner-img tfq--index_banner"]').tap()
        else:
            print("没有配置banner")

        self.get_screenshot()

    def test_18_click_topic1_圈子模块一(self):
        """
        淘房圈首页，点击圈子模块第一个圈子
        """
        self.page.get_element('view[class="tfq--topicItem"][data-index="0"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_19_click_topic2_圈子模块二(self):
        """
        淘房圈首页，点击圈子模块第二个圈子
        """
        e = self.page.get_element('view[class="tfq--topicItem"][data-index="1"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_20_click_topic3_圈子模块三(self):
        """
        淘房圈首页，点击圈子模块第三个圈子
        """
        e = self.page.get_element('view[class="tfq--topicItem"][data-index="2"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_21_click_topic4_圈子模块四(self):
        """
        淘房圈首页，点击圈子模块第四个圈子
        """
        e = self.page.get_element('view[class="tfq--topicItem"][data-index="3"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def delete_test_16_click_qzSquare_圈子广场(self):
        """
        V6.44.x: delete
        淘房圈首页，点击圈子模块圈子广场
        """
        self.page.get_element('image[class="tfq--topicImg"]'
                                  '[src="https://tfxcx.house365.com/static/2021tfq/square.png"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiSquare')
        self.get_screenshot()

    def test_01_click_active_活动(self):
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


    def test_10_click_newpost_more_最新热帖更多(self):
        """
        淘房圈首页，点击最新热帖更多
        """
        self.find_element('view[class="tfq--toutiao_more"]').tap()

        self.verifyPageName('/page/taofangquan/tieziList/tieziList')
        self.get_screenshot()

    def test_09_click_newpost_最新热帖(self):
        """
        淘房圈首页，点击最新热帖第一条
        """
        self.find_element('swiper-item[data-index="0"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()


    def test_07_click_hotQuanzi_more_更多圈子(self):
        """
        淘房圈首页，热门圈子，点击“更多圈子”
        """
        self.page.get_element('view[class="tfq--more"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiSquare')
        self.get_screenshot()

    def test_03_click_hotQuanZi1_热门圈子一(self):
        """
        淘房圈首页，热门圈子，点击第一个圈子
        """
        self.page.get_element('navigator[data-index="0"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_04_click_hotQuanZi2_热门圈子二(self):
        """
        淘房圈首页，热门圈子，点击第二个圈子
        """
        self.page.get_element('navigator[data-index="1"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_05_click_hotQuanZi3_热门圈子三(self):
        """
        淘房圈首页，热门圈子，点击第三个圈子
        """
        self.page.get_element('navigator[data-index="2"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_06_click_hotQuanZi4_热门圈子四(self):
        """
        淘房圈首页，热门圈子，点击第四个圈子
        """
        self.page.get_element('navigator[data-index="3"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_11_click_post_content_点击帖子正文(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击正文内容
        """
        self.page.get_element('view[class="tfq--post_cont"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_13_click_post_quanzi_点击圈子(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击帖子圈子
        """
        self.page.get_element('view[class="tfq--posttag tfq--flex tfq--tfAlignC"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_23_z_click_post_share_分享(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击分享按钮
        """
        self.page.get_element('button[class="tfq--shareDetail"]').tap()
        self.delay(1)
        self.verifyByScreenshot('tfq/sharemodal.png')

    def test_14_click_post_reply_帖子回复按钮(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击回复的按钮
        """
        self.page.get_element('view[class="tfq--replyBtn"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_12_click_post_laud_帖子点赞(self):
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


    def test_15_click_postbtn_发帖按钮(self):
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
