# add by zsy
from base.test_base import TestBase


class TestTfqFbsPage(TestBase):
    """
    房博士主页
    """
    def setUp(self) -> None:
        self.page_name = f'/page/taofangquan/personalDetails/fbs/fbs?city=qz&uid={self.fbs_uid}&role_uid={self.fbs_roleid}'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqFbsPage, self).setUp()
        print("TestFbsPage setup")

    def test_14_z_click_call_拨打电话(self):
        """
        房博士主页，点击下方“拨打电话”
        """
        self.find_element('view[class="link-button call"]').tap()
        self.delay(1)
        self.verifyByScreenshot('xf/call.png')

    def test_05_click_shidikanpan_实地看盘(self):
        """
        房博士主页，点击“实地看盘“
        """
        self.find_element('view[data-eventid="2951"]').tap()

        self.get_screenshot()

    def test_02_click_huxingjiexi_户型解析(self):
        """
        房博士主页，点击“户型解析”
        """
        self.find_element('view[data-eventid="2952"]').tap()

        self.get_screenshot()

    def test_03_click_jiaotongpeitao_交通配套(self):
        """
        房博士主页，点击“交通配套”
        """
        self.find_element('view[data-eventid="2953"]').tap()

        self.get_screenshot()

    def test_04_click_loupanpinglun_楼盘评论(self):
        """
        房博士主页，点击“楼盘评论”
        """
        self.find_element('view[data-eventid="2954"]').tap()

        self.get_screenshot()

    def click_huati(self):
        """
        房博士主页，点击“话题“
        """
        self.find_element('view[data-eventid="2955"]').tap()
        return self

    def test_01_click_huati_话题(self):
        """
        房博士主页，点击“话题“
        """
        self.click_huati()

        self.get_screenshot()

    def test_07_goto_loupanpinglun_楼盘评论详情(self):
        """
        房博士主页，点击楼盘评论，进入楼盘评论详情页
        """
        self.find_element('view[class="post_cont"]').tap()

        self.verifyPageName('/page/taofangquan/commentDetail/commentDetail')
        self.get_screenshot()

    def test_11_loupanpinglun_dianzan_楼盘评论点赞(self):
        """
        房博士主页，点击楼盘评论的“点赞”icon
        """
        tap = 'self.page.get_element(\'view[class="laud-btn"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞Ok')
        self.get_screenshot()

    def test_13_loupanpinglun_reply_楼盘评论回复(self):
        """
        房博士主页，点击楼盘评论的“回复”icon
        """
        self.find_element('view[class="replyBtn"]').tap()

        self.verifyPageName('/page/taofangquan/commentDetail/commentDetail')
        self.get_screenshot()

    def test_12_loupanpinglun_quanzi_楼盘评论圈子(self):
        """
        房博士主页，点击楼盘评论的圈子，进入圈子页面
        """
        self.find_element('view[class="posttag flex tfAlignC"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_08_huati_dianzan_话题点赞(self):
        """
        房博士主页，点击话题tab下第一条的“点赞”icon
        """
        self.click_huati().delay(1)
        tap = 'self.page.get_element(\'view[class="laud-btn"][data-index="0"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞Ok')
        self.get_screenshot()

    def test_10_huati_reply_话题回复(self):
        """
        房博士主页，点击话题tab下的第一条的“回复”icon
        """
        self.click_huati().delay(2)
        self.find_element('view[class="replyBtn"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_06_goto_huatidetail_话题详情(self):
        """
        房博士主页，点击话题tab下的第一条，进入详情页
        """
        # self.test_click_huati().delay(2).page.get_element('view[class="postitem"][data-postsid="13684"]').tap()
        self.click_huati().delay(1)
        self.find_element('view[class="postitem"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_09_huati_quanzi_话题圈子(self):
        """
        房博士主页，点击话题tab下的第一条带圈子的内容，进入对应圈子详情
        """
        self.click_huati().delay(1).find_element('view[class="posttag flex tfAlignC"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

