# -*- coding: utf-8 -*- 
# @Time : 2022/5/31 15:03
# @Author : zcm
# @File : test_news_detail_audio.py
# @desc:

from test.test_base import TestBase
from common import delay


class TestNewsDetailAudio(TestBase):
    """
    资讯详情页音频稿件+精选栏目关注组件
    """

    def setUp(self) -> None:
        self.page_name = "/page/news/detail?id=029783880&city=qz"
        self.switch = False
        super(TestNewsDetailAudio, self).setUp()
        delay(2)

    def test_01_click_lanmu(self):
        """
        点击栏目关注组件订阅
        :return:
        """
        self.page.get_element('button.inforR').tap()
        delay(2)

    def test_02_click_audio(self):
        """
        点击音频组件播放
        :return:
        """
        self.page.get_element('image.yinping_play').tap()

    def test_03_click_morepl(self):
        """
        点击更多评论
        :return:
        """
        self.page.get_element('view', inner_text='更多评论').tap()

    def test_04_click_bnzf(self):
        """
        点击帮你找房
        :return:
        """
        e = self.page.get_element('button[class="fixBR-btn zf"]').tap()
        delay(3)

    def test_07_click_firsttjlp(self):
        """
        点击第一个推荐楼盘
        :return:
        """
        e = self.page.get_element('//view[@class="tjlplist-rl"]')
        delay(2)
        e.tap()
        delay(3)

    def test_13_click_tel(self):
        """
        点击拨打电话图标
        :return:
        """
        e = self.page.get_element('//button[@class="tjlplist-tel"]')
        delay(2)
        e.tap()

    def test_08_click_backindex(self):
        """
        点击首页
        :return:
        """
        e = self.page.get_element('//view[@class="newHouseRfixed-index xfxq_index"]')
        delay(2)
        e.tap()

    def test_15_click_share(self):
        """
        点击分享
        :return:
        """
        e = self.page.get_element('//button[@class="newHouseRfixed-share xfxq_fx"]')
        delay(2)
        e.tap()

    def test_09_click_writecomment(self):
        """
        点击写评论，直接通过trigger发布
        :return:
        """
        e = self.page.get_element('button.fixBL-l')
        delay(2)
        e.tap()
        e2 = self.page.get_element('input.fixBIntB-input')
        delay(2)
        e2.trigger("confirm", {"value": "测试"})

    def test_10_click_comments(self):
        """
        点击评论图标，点击评论输入框，直接通过trigger发布,并点赞
        :return:
        """
        e = self.page.get_element('view.fixBL-r')
        delay(2)
        e.tap()
        delay(2)
        e2 = self.page.get_element('button.fixBL-l')
        delay(2)
        e2.tap()
        delay(2)
        e3 = self.page.get_element('input.fixBIntB-input')
        delay(2)
        e3.trigger("confirm", {"value": "测试"})
        delay(2)
        self.page.get_element('button.pllist-zan').tap()

    def test_11_click_dianzan(self):
        """
        点击点赞图标
        :return:
        """
        e = self.page.get_element('button[class="pllist-zan"]')
        delay(2)
        e.tap()

    def test_14_click_wyzx(self):
        """
        点击我要咨询
        :return:
        """
        e = self.page.get_element('button[class="fixBR-btn zx"]')
        delay(2)
        e.tap()

    def test_00_click_firstyd(self):
        """
        点击推荐阅读
        :return:
        """
        try:
            e = self.page.get_elements('view[class="tjydlist-li tfFlex tfFlexSb tfAlingnC"]')
            e[0].tap()
            delay(2)
        except:
            return