# -*- coding: utf-8 -*- 
# @Time : 2022/5/30 9:58 
# @Author : zcm 
# @File : test_newslist.py 
# @desc:

import minium
from test.common import delay


class TestNewsList(minium.MiniTest):
    """
    资讯列表页
    """

    def setUp(self) -> None:
        self.app.navigate_to("/page/news/list?city=qz")
        delay(4)
        self.app.get_current_page()
        print("setUp!!!!")

    def test_click_firstnews(self):
        """
        点击第一条资讯
        :return:
        """
        e = self.page.get_element('//view[@class="list-box"]/navigator')
        c = e.attribute('class')
        print('class:', c)
        e.tap()
        delay(2)

    def test_click_loupandaogou(self):
        """
        点击楼盘导购，点击第一条资讯
        :return:
        """
        e = self.page.get_element('text', inner_text='楼盘导购')
        c = e.attribute('class')
        print('class:', c)
        e.tap()
        delay(2)
        e2 = self.page.get_element('//view[@class="list-box"]/navigator')
        c2 = e2.attribute('class')
        print('class:', c2)
        e2.tap()
        delay(2)
