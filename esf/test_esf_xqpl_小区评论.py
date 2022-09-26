from ddt import file_data, ddt
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt
class Testesfxqpl(TestBase):
    """
    小区评论
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/pages/comment/publish/publish?blockId=3982&blockName=水佑岗小区&districtName=鼓楼区&streetName=水佐岗"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfxqpl, self).setUp()
        print("Testesfxqpl setup")

    @file_data('./test_func_pinglun.yml')
    def test_comment_sub_发表评论(self, **kwargs):
        """
        发表评论
        :return:
        """
        #评论内容
        self.page.get_element('textarea[class="commentInput"]').input(kwargs['comment'])

        #您的身份
        your_self = self.page.get_element(f'view[data-id="{kwargs["dateid"]}"]', inner_text=kwargs['yourself'])
        your_self.tap()
        self.delay(1)
        star0 = self.page.get_element(f'view[class="star"][data-index="0"][data-starindex="{kwargs["zhpj"]}"]')
        star0.tap()
        self.delay(1)
        star1 = self.page.get_element(f'view[class="star"][data-index="1"][data-starindex="{kwargs["jy"]}"]')
        star1.tap()
        self.delay(1)
        star2 = self.page.get_element(f'view[class="star"][data-index="2"][data-starindex="{kwargs["pt"]}"]')
        star2.tap()
        self.delay(1)
        star3 = self.page.get_element(f'view[class="star"][data-index="3"][data-starindex="{kwargs["jyy"]}"]')
        star3.tap()
        self.delay(1)
        star4 = self.page.get_element(f'view[class="star"][data-index="4"][data-starindex="{kwargs["pz"]}"]')
        star4.tap()
        self.delay(1)
        star5 = self.page.get_element(f'view[class="star"][data-index="5"][data-starindex="{kwargs["wy"]}"]')
        star5.tap()
        self.get_screenshot()

        sub = self.page.get_element('view[class="center submit"]')
        sub.tap()
        self.get_screenshot()

    def test_click_guifan_评论规范(self):
        """
        点击评论规范
        :return:
        """
        e = self.page.get_element('text', inner_text="评论规范")
        e.tap()
        self.delay(1)
        self.get_screenshot()



