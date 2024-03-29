# -*- coding: utf-8 -*- 
# @Time : 2022/5/30 9:58 
# @Author : zcm 
# @File : test_news_list_资讯列表.py
# @desc:
from base.test_base import TestBase


class TestNewsList(TestBase):
    """
    资讯列表页
    """

    def setUp(self) -> None:
        self.page_name ="/page/news/list?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewsList, self).setUp()

    def test_click_firstnews_热门资讯(self):
        """
        资讯列表页，点击第一条资讯
        """
        self.find_element('view[class="txt tfline2"]').tap()

        self.verifyPageName('/page/news/detail')
        self.get_screenshot()

    def test_click_loupandaogou_楼盘导购资讯(self):
        """
        资讯列表页，点击楼盘导购，点击第一条资讯
        """
        self.find_element('view[class="flex-1"]', inner_text='楼盘导购').tap()
        self.delay(1)
        self.find_element('view[class="txt tfline2"]').tap()

        self.verifyPageName('/page/news/detail')
        self.get_screenshot()

    def test_click_adv_横幅广告(self):
        """
        资讯列表页，点击横幅广告
        """
        try:
            self.page.get_element('image[class="bannerTwo-img index_banner"]').tap()
        except:
            print('资讯列表页面无广告')

        self.get_screenshot()

