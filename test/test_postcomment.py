# add by zsy
from minium import ddt_class, ddt_case, ddt_data

from test.test_base import TestBase
from test.test_mine import TestMine


@ddt_class(testNameFormat="%(name)s")
class TestPostComment(TestMine):
    """
    所有身份 发布帖子评论、评论回复
    """
    def get_shenfen(self, value):
        if value == 1:
            self.change_C()
            text = "我是C端身份"
        elif value == 2:
            self.change_zygw()
            text = "我是置业顾问"
        elif value == 3:
            self.change_yy()
            text = "我是运营"
        else:
            self.change_fbs()
            text = "我是房博士"

        return text

    @ddt_case(
        ddt_data(1, name="C"),
        ddt_data(2, name="zygw"),
        ddt_data(3, name="yy"),
        ddt_data(4, name="fbs")
    )
    def test_postcomment(self, value):
        """
        不同身份，帖子详情页，点击底部发布评论弹窗，发布评论
        :param value:
        1：C端身份
        2：置业顾问
        3：运营
        4：房博士
        :return:
        """
        text = self.get_shenfen(value)

        self.delay(1)
        self.app.navigate_to("/page/taofangquan/tieziDetail/tieziDetail?city=qz&postsid=12746")
        self.delay(2)
        self.app.get_current_page()

        e1 = self.page.get_element('view[class="detail-fix-input"]')
        e1.tap()
        e2 = self.page.get_element('textarea[placeholder="说点什么吧"]')
        e2.input(text)
        e3 = self.page.get_element('button[class="send-btn"]')
        self.delay(1)
        e3.tap()

    @ddt_case(
        ddt_data(1, name="C"),
        ddt_data(2, name="zygw"),
        ddt_data(3, name="yy"),
        ddt_data(4, name="fbs")
    )
    def test_send_commentlist_reply(self, value):
        """
        不同身份，帖子详情页，点击第一个评论的“回复”按钮，发布评论回复
        :return:
        """
        text = self.get_shenfen(value)

        self.delay(1)
        self.app.navigate_to("/page/taofangquan/tieziDetail/tieziDetail?city=qz&postsid=12746")
        self.delay(2)
        self.app.get_current_page()

        self.page.get_element('view[class="commentList--reply-btn"]').tap()
        e2 = self.page.get_element('textarea[placeholder="说点什么吧"]')
        e2.input(text)
        e3 = self.page.get_element('button[class="send-btn"]')
        self.delay(1)
        e3.tap()