from minium import ddt_class, ddt_case
from base.common import delay

from base.test_base import TestBase
@ddt_class()
class Testesfxqrp(TestBase):
    """
    小区热评
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/pages/comment/list/list"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfxqrp, self).setUp()
        print("Testesfxqrp setup")

    def test_click_search(self):
        """
        搜索
        :return:
        """
        e = self.page.get_element('view[class="flex align_center search"]')
        e.tap()
        self.verifyPageName('/esf/village/pages/comment/search/search', '搜索 ok')
        delay(3)

    def test_click_todo(self):
        """
        热评小区-点击去搜索
        :return:
        """
        e = self.page.get_element('view[class="center toDo"]')
        e.tap()
        self.get_screenshot()

    def test_click_hotcomment(self):
        """
        热评小区列表点击进详情
        :return:
        """
        hotlist = self.page.get_elements('view[class="between hotComment"]')
        hotlist[0].tap()
        self.get_screenshot()

    def test_click_commentim(self):
        """
        全部评论点击im
        :return:
        """
        elms_im = self.page.get_elements('view[class="msg"]')
        if len(elms_im) > 0:
            elms_im[0].tap()
            self.get_screenshot()
        else:
            print("没有评论")

    def test_click_commenttel(self):
        """
        全部评论点击im
        :return:
        """
        elms_tel = self.page.get_elements('view[class="tel"]')
        if len(elms_tel) > 0:
            elms_tel[0].tap()
            self.get_screenshot()
        else:
            print("没有评论")

    def test_click_commentlist(self):
        """
        点击全部评论列表
        :return:
        """
        elms_list = self.page.get_elements('view[class="commentItem"]')
        if len(elms_list) > 0:
            elms_list[0].tap()
            self.get_screenshot()
        else:
            print("没有评论")

    def test_goto_plimg(self):
        """
        点击评论图片
        :return:
        """
        plcom = self.page.element_is_exists('view[class="commentItem"]')
        if plcom == True:
            plimg = self.page.get_elements('//view[@class="commentItem"][1]//view[@class="flex pr commentImages"]/view')

            if len(plimg) > 0:
                plimg[0].tap()
                self.get_screenshot()
            else:
                print("没有评论图片")
        else:
            print("没有评论")

    def test_goto_pldz(self):
        """
        评论点赞
        :return:
        """
        self.page.scroll_to(300, 500)
        delay(1)
        pldz = self.page.element_is_exists('view[class="center"][data-index="0"][data-level="1"]')
        if pldz == True:
            dz = self.page.get_elements('view[class="center"][data-index="0"][data-level="1"]')
            dz[0].tap()
            self.get_screenshot()
        else:
            print("没有评论")

    def test_goto_qxdz(self):
        """
        取消点赞
        :return:
        """
        self.page.scroll_to(300, 500)
        delay(1)

        qxdz = self.page.element_is_exists('view[class="center like"][data-index="0"][data-level="1"]')
        if qxdz == True:
            qx = self.page.get_elements('view[class="center like"][data-index="0"][data-level="1"]')
            qx[0].tap()
            self.get_screenshot()
        else:
            print("没有点赞")

    def test_click_pllp(self):
        """
        全部评论点击楼盘链接
        :return:
        """
        self.page.scroll_to(300, 500)
        delay(1)
        pllp = self.page.get_elements('view[class="flex align_center villageName"]')
        if len(pllp) > 0:
            pllp[0].tap()
            self.get_screenshot()
        else:
            print("没有评论")

    def test_click_hover(self):
        """
        点击顶部
        :return:
        """
        self.page.scroll_to(500, 500)
        delay(1)
        e = self.page.get_element('//hoverbutton/view/view')
        e.tap()
        self.get_screenshot()
