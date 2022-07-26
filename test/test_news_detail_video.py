# -*- coding: utf-8 -*- 
# @Time : 2022/5/31 10:02 
# @Author : zcm 
# @File : test_news_detail_video.py
# @desc:

from test.test_base import TestBase
from common import delay


class TestNewsdetailVideo(TestBase):
    """
    资讯详情页视频稿件+楼盘名片稿件
    """

    def setUp(self) -> None:
        self.page_name = "/page/news/detail?id=029783878&city=qz"
        self.switch = False
        super(TestNewsdetailVideo, self).setUp()
        delay(2)

    def test_01_click_video(self):
        """
        点击视频播放
        :return:
        """
        self.page.get_element('video#myVideo').play()

    def test_02_click_firstloupan(self):
        """
        点击楼盘名片组件
        :return:
        """
        page = self.app.get_current_page()
        page.scroll_to(1500, 500)
        self.page.get_element('image.lpList-img').tap()
        delay(2)

    def test_03_click_kfbm(self):
        """
        点击看房报名
        :return:
        """
        page = self.app.get_current_page()
        delay(2)
        page.scroll_to(1500, 500)
        self.page.get_element('button[data-type="kf"]').tap()
        # self.native.allow_authorize()

    def test_04_click_dy(self):
        """
        点击订阅
        :return:
        """
        page = self.app.get_current_page()
        delay(2)
        page.scroll_to(1500, 500)
        self.page.get_element('button[data-type="dy"]').tap()

    def test_05_click_yh(self):
        """
        点击优惠
        :return:
        """
        page = self.app.get_current_page()
        delay(2)
        page.scroll_to(1500, 500)
        self.page.get_element('button[data-type="yh"]').tap()

    def test_12_click_tel(self):
        """
        点击拨打电话
        :return:
        """
        page = self.app.get_current_page()
        delay(2)
        page.scroll_to(1500, 500)
        self.page.get_element('button[class="lpList-btn lpList-btn-tel"]').tap()

    def test_06_click_more(self):
        """
        点击更多
        :return:
        """
        page = self.app.get_current_page()
        delay(2)
        page.scroll_to(1500, 500)
        self.page.get_element('view[class="getMore"]').tap()

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

