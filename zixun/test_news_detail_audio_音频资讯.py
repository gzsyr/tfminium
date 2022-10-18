# -*- coding: utf-8 -*- 
# @Time : 2022/5/31 15:03
# @Author : zcm
# @File : test_news_detail_audio_音频资讯.py
# @desc:
import time

from base.test_base import TestBase


class TestNewsDetailAudio(TestBase):
    """
    资讯详情页音频稿件+精选栏目关注组件
    """

    def setUp(self) -> None:
        self.page_name = "/page/news/detail?id=029783880&city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewsDetailAudio, self).setUp()

    def test_01_click_dingyue_订阅(self):
        """
        资讯音频详情页，点击栏目关注组件订阅
        """
        self.page.get_element('button.inforR').tap()
        self.delay(1)

        self.verifyByScreenshot('zixun/dy.png')

    def test_02_click_audio_播放(self):
        """
        资讯音频详情页，点击音频组件播放
        """
        self.page.get_element('image.yinping_play').tap()

        self.get_screenshot()

    def test_03_click_morepl_更多评论(self):
        """
        资讯音频详情页，点击更多评论
        """
        self.page.get_element('view', inner_text='更多评论').tap()

        self.verifyPageName('/page/news/pllist')
        self.get_screenshot()

    def test_04_click_bnzf_帮你找房(self):
        """
        资讯详情页，点击帮你找房
        """
        self.delay(1)
        self.page.get_element('button[class="fixBR-btn zf"]').tap()

        self.verifyPageName('/page/newhouse/bnzf/bnzf')
        self.get_screenshot()

    def test_07_click_firsttjlp_推荐楼盘(self):
        """
        资讯音频详情页，点击第一个推荐楼盘
        """
        self.delay(1)
        self.page.get_element('//view[@class="tjlplist-rl"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_13_click_firsttjlp_tel_楼盘电话(self):
        """
        资讯音频详情页，点击推荐楼盘第一个电话图标
        """
        self.page.get_element('//button[@class="tjlplist-tel"]').tap()
        self.delay(1)

        self.verifyByScreenshot('xf/call.png')

    def test_08_click_backindex_回到首页(self):
        """
        资讯音频详情页，点击首页
        """
        self.page.get_element('//view[@class="newHouseRfixed-index xfxq_index"]').tap()

        self.verifyPageName('/page/index/index')
        self.get_screenshot()

    def test_15_click_share_分享(self):
        """
        资讯音频详情页，点击分享
        """
        self.page.get_element('//button[@class="newHouseRfixed-share xfxq_fx"]').tap()

        self.get_screenshot()

    def test_09_click_writecomment_直接评论(self):
        """
        资讯音频详情页，点击写评论，直接通过trigger发布
        """
        self.page.get_element('button.fixBL-l').tap()
        tm = time.strftime('%Y-%m-%d %H:%M:%S')
        tap = 'self.page.get_element(\'input.fixBIntB-input\').trigger("confirm", {"value": "'+tm+'"})'
        self.verifyStr(True, self.getShowToast(tap), '评论成功')

        self.get_screenshot()

    def test_10_click_comments_全部评论页面评论(self):
        """
        资讯音频详情页，进入全部评论页面，点击评论输入框，直接通过trigger发布,并点赞
        """
        # 进入全部评论页面
        self.page.get_element('view.fixBL-r').tap()
        self.delay(4)
        # 点击评论框
        self.page.get_element('button.fixBL-l').tap()
        # self.input_value_by_mk('zixun/ip.png')
        # 写评论
        tm = time.strftime('%Y-%m-%d %H:%M:%S')
        tap = 'self.page.get_element(\'input.fixBIntB-input\').trigger("confirm", {"value": "'+tm+'"})'
        self.verifyStr(True, self.getShowToast(tap), '评论成功')
        self.delay(1)

        # 点赞页面第一条评论
        tap = 'self.page.get_element(\'button.pllist-zan\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞成功')

        self.get_screenshot()

    def test_11_click_dianzan_直接点赞(self):
        """
        资讯音频详情页，点击点赞图标
        """
        self.delay(2)
        tap = 'self.page.get_element(\'button[class="pllist-zan"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞成功')

        self.get_screenshot()

    def test_14_click_wyzx_我要咨询(self):
        """
        资讯音频详情页，点击我要咨询
        """
        self.page.get_element('button[class="fixBR-btn zx"]').tap()

        self.verifyByScreenshot('xf/call.png')

    def test_00_click_firstyd_推荐阅读(self):
        """
        资讯音频详情页，点击推荐阅读
        """
        try:
            self.page.get_element('view[class="tjydlist-li tfFlex tfFlexSb tfAlingnC"]').tap()
        except:
            print('此条资讯无推荐阅读')

        self.get_screenshot()

