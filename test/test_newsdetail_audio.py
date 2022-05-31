# -*- coding: utf-8 -*- 
# @Time : 2022/5/30 17:58 
# @Author : zcm 
# @File : test_newsdetail_audio.py 
# @desc:

import minium
from test.common import delay


class TestNewsDetailAudio(minium.MiniTest):
    """
    资讯详情页音频稿件
    """

    def setUp(self) -> None:
        self.app.navigate_to("/page/news/detail?id=029783880&city=qz")
        delay(3)
        self.app.get_current_page()
        print("setUp!!!!")

    def test_click_audio(self):
        """
        点击音频播放
        :return:
        """
        e = self.page.get_element('image.yinping_play')
        c = e.attribute('class')
        print('class:', c)
        e.tap()
        delay(2)
