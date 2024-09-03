# -*- coding: utf-8 -*- 
# @Time : 2022/5/31 10:02 
# @Author : zcm 
# @File : test_news_detail_video_视频资讯.py
# @desc:
import time

from base.test_base import TestBase


class TestNewsdetailVideo(TestBase):
    """
    资讯详情页视频稿件+楼盘名片稿件
    """

    def setUp(self) -> None:
        self.page_name = "/page/news/detail?id=029783878&city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewsdetailVideo, self).setUp()

    def test_01_click_video_播放(self):
        """
        资讯详情页视频稿件，点击视频播放
        """
        self.find_element('video#myVideo').play()

        self.get_screenshot()

    def test_02_click_firstloupan_楼盘名片(self):
        """
        资讯详情页视频稿件，点击楼盘名片组件
        """
        self.page.scroll_to(1500, 500)
        self.page.get_element('image.lpList-img').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_03_click_kfbm_看房报名(self):
        """
        资讯详情页视频稿件，点击楼盘名片的看房报名
        """
        self.page.scroll_to(1000, 500)
        self.page.get_element('button[data-type="kf"]').tap()
        self.delay(7)
        self.verifyByScreenshot('zixun/bmcg.png')

    def test_04_click_dy_楼盘名片订阅(self):
        """
        资讯详情页视频稿件，点击楼盘名片的订阅
        """
        self.page.scroll_to(1000, 500)
        self.page.get_element('button[class="lpList-btn"][data-type="dy"]').tap()
        self.delay(7)
        self.verifyByScreenshot('zixun/365app.png')

    def test_05_click_yh_楼盘名片优惠(self):
        """
        资讯详情页视频稿件，点击楼盘名片的优惠
        """
        self.page.scroll_to(1000, 500)
        self.page.get_element('button[data-type="yh"]').tap()
        self.delay(7)
        self.verifyByScreenshot('zixun/bmcg.png')

    def test_12_click_tel_楼盘名片电话(self):
        """
        资讯详情页视频稿件，点击楼盘名片的拨打电话
        """
        self.page.scroll_to(1000, 500)
        self.page.get_element('button[class="lpList-btn lpList-btn-tel"]').tap()
        self.delay(1)
        self.verifyByScreenshot('xf/call.png')

    def test_07_click_firsttjlp_推荐楼盘(self):
        """
        资讯详情页视频稿件，点击第一个推荐楼盘
        """
        self.page.scroll_to(2000, 300)
        self.find_element('//view[@class="tjlplist-rl"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_13_click_firsttjlp_tel_推荐楼盘电话(self):
        """
        资讯详情页视频稿件，点击第一个推荐楼盘的电话
        """
        self.page.scroll_to(2000, 300)
        self.find_element('//button[@class="tjlplist-tel"]').tap()

        # self.verifyByScreenshot('xf/call.png')

    def test_08_click_backindex_回到首页(self):
        """
        资讯详情页视频稿件，点击首页
        """
        self.page.get_element('//view[@class="newHouseRfixed-index xfxq_index"]').tap()

        self.verifyPageName('/page/index/index')
        self.get_screenshot()

    def test_15_click_share_分享(self):
        """
        资讯详情页视频稿件，点击分享
        """
        self.find_element('//button[@class="newHouseRfixed-share xfxq_fx"]').tap()

        self.get_screenshot()

    def test_09_click_writecomment_直接评论(self):
        """
        资讯详情页视频稿件，点击写评论，直接通过trigger发布
        """
        self.find_element('button.fixBL-l').tap()
        tm = time.strftime('%Y-%m-%d %H:%M:%S')
        tap = 'self.page.get_element(\'input.fixBIntB-input\').trigger("confirm", {"value": "'+tm+'"})'
        self.verifyStr(True, self.getShowToast(tap), '发布评论ok')

    def test_10_click_comments_全部评论页面评论(self):
        """
        资讯详情页视频稿件，进入全部评论页面，点击评论输入框，直接通过trigger发布,并点赞
        """
        # 进入全部评论页面
        self.page.get_element('view.fixBL-r').tap()
        self.delay(4)
        # 点击评论框
        self.page.get_element('button.fixBL-l').tap()
        # self.input_value_by_mk('zixun/ip.png')
        # 写评论
        tm = time.strftime('%Y-%m-%d %H:%M:%S')
        tap = 'self.page.get_element(\'input.fixBIntB-input\').trigger("confirm", {"value": "' + tm + '"})'
        self.verifyStr(True, self.getShowToast(tap), '评论成功')
        self.delay(1)

        # 点赞页面第一条评论
        tap = 'self.page.get_element(\'button.pllist-zan\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞成功')

        self.get_screenshot()

    def test_11_click_dianzan_直接点赞(self):
        """
        资讯详情页视频稿件，点击点赞图标
        """
        self.delay(2)
        tap = 'self.find_element(\'button[data-type="pl_zan"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞成功')

    def test_14_click_wyzx_咨询(self):
        """
        资讯详情页视频稿件，点击我要咨询
        """
        self.find_element('button[class="fixBR-btn zx"]').tap()
        self.verifyByScreenshot('xf/call.png')

    def test_00_click_firstyd_推荐阅读(self):
        """
        资讯详情页视频稿件，点击推荐阅读
        """
        try:
            self.page.get_element('view[class="tjydlist-li tfFlex tfFlexSb tfAlingnC"]').tap()
        except:
            print('此条资讯无推荐阅读')

        self.get_screenshot()

