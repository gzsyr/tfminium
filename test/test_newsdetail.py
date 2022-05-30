# -*- coding: utf-8 -*- 
# @Time : 2022/5/30 10:44 
# @Author : zcm 
# @File : test_newsdetail.py 
# @desc:

import minium
from test.common import delay

class TestNewsDetail(minium.MiniTest):
    """
    资讯详情页
    """

    def setUp(self) -> None:
        self.app.navigate_to("/page/news/detail?id=029970948&city=qz")
        delay(3)
        self.app.get_current_page()
        print("setUp!!!!")
        delay(2)

    def test_click_firsttjlp(self):
        """
        点击第一个推荐楼盘
        :return:
        """
        e = self.page.get_element('//view[@class="tjlplist-rl"]')
        c = e.attribute('class')
        print('class:', c)
        e.tap()
        delay(2)

    def test_click_backindex(self):
        """
        点击首页
        :return:
        """
        e = self.page.get_element('//view[@class="newHouseRfixed-index xfxq_index"]')
        c = e.attribute('class')
        print('class:', c)
        e.tap()
        delay(2)

    def test_click_zshare(self):
        """
        点击分享
        :return:
        """
        e = self.page.get_element('//button[@class="newHouseRfixed-share xfxq_fx"]')
        c = e.attribute('class')
        print('class:', c)
        e.tap()
        delay(2)

    def test_click_ztel(self):
        """
        点击拨打电话图标
        :return:
        """
        e = self.page.get_element('//button[@class="tjlplist-tel"]')
        c = e.attribute('class')
        print('class:', c)
        e.tap()
        delay(2)

    def test_click_writecomment(self):
        """
        点击写评论，直接通过trigger发布
        :return:
        """
        e = self.page.get_element('button.fixBL-l')
        c = e.attribute('class')
        print('class:', c)
        e.tap()
        delay(2)
        e2 = self.page.get_element('input.fixBIntB-input')
        print(e2.attribute('class'))
        delay(2)
        e2.trigger("confirm", {"value": "测试"})
        delay(2)
        # e3 = self.page.get_element('button.fixBIntB-send')
        # print(e3.attribute('class'))
        # e3.tap()
        # delay(2)

    def test_click_comments(self):
        """
        点击评论图标
        :return:
        """
        e = self.page.get_element('view.fixBL-r')
        c = e.attribute('class')
        print('class:', c)
        e.tap()
        delay(2)

    def test_click_wyzx(self):
        """
        点击我要咨询
        :return:
        """
        e = self.page.get_element('button[class="fixBR-btn zx"]')
        c = e.attribute('class')
        print('class:', c)
        e.tap()
        delay(2)
