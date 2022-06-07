# add by zzh
import minium
from test.common import delay
from test.test_base import TestBase


class TestTfq(TestBase):

    """
    淘房圈首页
    """

    def setUp(self) -> None:
        self.page_name = "/page/find/find?city=qz"
        self.switch = True
        super(TestTfq, self).setUp()
        print("TestTfq  Setup")

    def test_swich_ht(self):
        """
        跳转至话题
        :return:
        """
        self.app.navigate_to("/page/taofangquan/huati/huatiList?city=qz")

    def test_click_mustread(self):
        """
        淘房圈首页点击必读
        :return:
        """
        e = self.page.get_element('image[class="tfq--mustread"]')
        e.tap()
        print("元素：", e)
        delay(2)

    def test_click_search(self):
        """
        淘房圈首页，点击搜索框
        :return:
        """
        e = self.page.get_element('view[class="tfq--search-input"]')
        e.tap()
        delay(2)

    def test_click_share1(self):
        """
        淘房圈首页，点击顶部分享按钮
        :return:
        """
        e = self.page.get_element("view[class='tfq--sharetxt']")
        e.tap()
        delay(2)

    def test_click_banner(self):
        """
        淘房圈首页，点击顶部banner
        :return:
        """
        b_l = self.page.element_is_exists('image[class="tfq--banner-img tfq--index_banner"]')
        if b_l == True:
            e = self.page.get_element('image[class="tfq--banner-img tfq--index_banner"]')
            e.tap()
            delay(2)
        else:
            print("没有配置banner")

    def test_click_topic1(self):
        """
        淘房圈首页，点击圈子模块第一个圈子
        :return:
        """
        e = self.page.get_element('view[class="tfq--topicItem"][data-index="0"]')
        e.tap()
        delay(2)

    def test_click_topic2(self):
        """
        淘房圈首页，点击圈子模块第二个圈子
        :return:
        """
        e = self.page.get_element('view[class="tfq--topicItem"][data-index="1"]')
        e.tap()
        delay(2)

    def test_click_topic3(self):
        """
        淘房圈首页，点击圈子模块第三个圈子
        :return:
        """
        e = self.page.get_element('view[class="tfq--topicItem"][data-index="2"]')
        e.tap()
        delay(2)

    def test_click_topic4(self):
        """
        淘房圈首页，点击圈子模块第四个圈子
        :return:
        """
        e = self.page.get_element('view[class="tfq--topicItem"][data-index="3"]')
        e.tap()
        delay(2)

    def test_click_qzSquare(self):
        """
        淘房圈首页，点击圈子模块圈子广场
        :return:
        """
        e = self.page.get_element('image[class="tfq--topicImg"]'
                                  '[src="https://tfxcx.house365.com/static/2021tfq/square.png"]')
        e.tap()
        delay(2)

    def test_click_active(self):
        """
        淘房圈首页，点击活动
        :return:
        """
        b_l = self.page.element_is_exists('image[class="tfq--activity_qd]')
        if b_l == True:
            e = self.page.get_element('image[class="tfq--activity_qd]')
            e.tap()
            delay(2)
        else:
            print("没有配置活动")


    def test_click_hottopic(self):
        """
        淘房圈首页，点击热门话题中的第一个
        :return:
        """
        e = self.page.get_element('view[class="tfq--title tfq--tfline2"]')
        e.tap()
        delay(2)

    def test_click_newpost(self):
        """
        淘房圈首页，点击最新热帖
        :return:
        """
        e = self.page.get_element('view[class="tfq--toutiao-swiper-item tfq--tfLine1"]')
        e.tap()
        delay(2)

    def test_click_more(self):
        """
        淘房圈首页，热门圈子，点击“更多圈子”
        :return:
        """
        e = self.page.get_element('navigator[class="tfq--more"]')
        e.tap()
        delay(2)

    def test_click_hotQuanZi1(self):
        """
        淘房圈首页，热门圈子，点击第一个圈子
        :return:
        """
        e = self.page.get_elements('image[class="tfq--ico"]')[0]
        e.tap()
        delay(2)

    def test_click_hotQuanZi2(self):
        """
        淘房圈首页，热门圈子，点击第二个圈子
        :return:
        """
        e = self.page.get_elements('image[class="tfq--ico"]')[1]
        e.tap()
        delay(2)

    def test_click_hotQuanZi3(self):
        """
        淘房圈首页，热门圈子，点击第三个圈子
        :return:
        """
        e = self.page.get_elements('image[class="tfq--ico"]')[2]
        e.tap()
        delay(2)

    def test_click_hotQuanZi4(self):
        """
        淘房圈首页，热门圈子，点击第四个圈子
        :return:
        """
        e = self.page.get_elements('image[class="tfq--ico"]')[3]
        e.tap()
        delay(2)

    def test_click_post_content(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击正文内容
        :return:
        """
        e = self.page.get_element('view[class="tfq--post_cont"]')
        e.tap()
        delay(2)

    def test_click_post_quanzi(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击帖子圈子
        :return:
        """
        e = self.page.get_element('view[class="tfq--posttag tfq--flex tfq--tfAlignC"]')
        e.tap()
        delay(2)

    def test_click_post_share(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击分享按钮
        :return:
        """
        e = self.page.get_element('button[class="tfq--shareDetail"]')
        e.tap()
        delay(2)

    def test_click_post_reply(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击回复的按钮
        :return:
        """
        e = self.page.get_element('view[class="tfq--replyBtn"]')
        e.tap()
        delay(2)

    def test_click_post_laud(self):
        """
        淘房圈首页-好帖推荐，第一个帖子，点击点赞的按钮
        :return:
        """
        e = self.page.get_element('view[class="tfq--laud-btn"]')
        e.tap()
        delay(2)

    def test_click_addgroup(self):
        """
        淘房圈首页 ，点击右下角“加群”按钮
        :return:
        """
        e = self.page.get_element('image[class="addgroup--addgroupimg"]')
        e.tap()
        delay(2)


    def test_click_postbtn(self):
        """
        淘房圈首页 ，点击右下角“发帖”按钮
        :return:
        """
        e = self.page.get_element('image[class="tfq--postBtn_img"]')
        e.tap()
        delay(2)

    def test_click_share2(self):
        """
        淘房圈首页 ，点击右下角“分享”按钮
        :return:
        """
        e = self.page.get_element('button[class="tfq--newHouseRfixed-share"]')
        e.tap()
        delay(2)




