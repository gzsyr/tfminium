# add by zsy


# 帖子回复，评论回复，在test_tfq_postdetail.py中已经写了测试用例，此处不需要了
from minium import ddt_class, ddt_case, ddt_data

from base.test_mine import TestMine


@ddt_class(testNameFormat="%(name)s")
class TestPostComment(TestMine):
    """
    所有身份 发布帖子评论、评论回复
    """
    def setUp(self) -> None:
        """
        此处涉及切换身份，不继承TestMine的setup
        :return:
        """
        self.page_name = "/page/index/mine?city=qz"
        self.switch = True
        super(TestPostComment, self).setUp()
        print("TestPostComment  Setup")

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
    def postcomment(self, value):
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
        self.app.navigate_to(f"/page/taofangquan/tieziDetail/tieziDetail?city=qz&postsid={self.postid}")
        self.delay(2)
        self.app.get_current_page()

        e1 = self.page.get_element('view[class="detail-fix-input"]')
        e1.tap()
        e2 = self.page.get_element('textarea[placeholder="说点什么吧"]')
        e2.input(text)
        e3 = self.page.get_element('button[class="send-btn"]')
        self.delay(1)
        e3.tap()

    # 这个用例在最后发布的时候，点击的“发布”按钮，会引导到主评论，所以最后没有点击发布按钮
    @ddt_case(
        ddt_data(1, name="C"),
        ddt_data(2, name="zygw"),
        ddt_data(3, name="yy"),
        ddt_data(4, name="fbs")
    )
    def send_commentlist_reply(self, value):
        """
        不同身份，帖子详情页，点击第一个评论的“回复”按钮，发布评论回复
        :return:
        """
        text = self.get_shenfen(value)

        self.delay(1)
        self.app.navigate_to(f"/page/taofangquan/tieziDetail/tieziDetail?city=qz&postsid={self.postid}")
        self.delay(2)
        self.app.get_current_page()

        self.page.get_element('view[class="commentList--reply-btn"]').tap()
        e2 = self.page.get_element('textarea[name="quick_reply_content"]')
        e2.input(text)
        # e3 = self.page.get_element('button[class="send-btn"]')
        # e3[1].tap()

