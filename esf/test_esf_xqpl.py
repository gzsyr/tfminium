from ddt import file_data, ddt
from minium import ddt_class, ddt_case

from base.common import delay
from base.test_base import TestBase

@ddt
class Testesfxqpl(TestBase):
    """
    小区评论
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/pages/comment/publish/publish?blockId=8819&blockName=碧桂园凤凰城"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfxqpl, self).setUp()
        print("Testesfxqpl setup")

    @file_data('./test_func_pinglun.yml')
    def test_comment_sub(self, **kwargs):
        """
        发表评论
        :return:
        """
        #评论内容
        self.page.get_element('textarea[class="commentInput"]').input(kwargs['comment'])

        #您的身份
        your_self = self.page.get_element(f'view[data-id="{kwargs["dateid"]}"]', inner_text=kwargs['yourself'])
        your_self.tap()
        delay(1)
        star0 = self.page.get_element(f'view[class="star"][data-index="0"][data-starindex="{kwargs["zhpj"]}"]')
        star0.tap()
        delay(1)
        star1 = self.page.get_element(f'view[class="star"][data-index="1"][data-starindex="{kwargs["jy"]}"]')
        star1.tap()
        delay(1)
        star2 = self.page.get_element(f'view[class="star"][data-index="2"][data-starindex="{kwargs["pt"]}"]')
        star2.tap()
        delay(1)
        star3 = self.page.get_element(f'view[class="star"][data-index="3"][data-starindex="{kwargs["jyy"]}"]')
        star3.tap()
        delay(1)
        star4 = self.page.get_element(f'view[class="star"][data-index="4"][data-starindex="{kwargs["pz"]}"]')
        star4.tap()
        delay(1)
        star5 = self.page.get_element(f'view[class="star"][data-index="5"][data-starindex="{kwargs["wy"]}"]')
        star5.tap()
        self.get_screenshot()

        """
        yz = self.page.element_is_exists('view[class="center identity active"][data-id="1"]')
        if yz == True:
            self.page.get_element('view[class="center identity"][data-id="2"]').tap()
            delay(1)
            self.page.get_element('view[class="center identity"][data-id="3"]').tap()
            delay(1)
            self.page.get_element('view[class="center identity"][data-id="1"]').tap()
        else:
            self.page.get_element('view[class="center identity"][data-id="1"]').tap()

        zh = self.page.element_is_exists('view[class="center identity active"][data-id="2"]')
        if zh == True:
            self.page.get_element('view[class="center identity"][data-id="1"]').tap()
            delay(1)
            self.page.get_element('view[class="center identity"][data-id="3"]').tap()
            delay(1)
            self.page.get_element('view[class="center identity"][data-id="2"]').tap()
        else:
            self.page.get_element('view[class="center identity"][data-id="2"]').tap()

        sxxq = self.page.element_is_exists('view[class="center identity active"][data-id="3"]')
        if sxxq == True:
            self.page.get_element('view[class="center identity"][data-id="1"]').tap()
            delay(1)
            self.page.get_element('view[class="center identity"][data-id="2"]').tap()
            delay(1)
            self.page.get_element('view[class="center identity"][data-id="3"]').tap()
        else:
            self.page.get_element('view[class="center identity"][data-id="3"]').tap()

        #综合评价
        elms0 = self.page.get_elements('view[class="star"][data-index="0"]')
        if len(elms0) > 0:
            elms0[4].tap()
        else:
            print(0)
        delay(2)
        
        elms1 = self.page.get_elements('view[class="star"][data-index="1"]')
        if len(elms1) > 0:
            elms1[3].tap()
        else:
            print(1)
        delay(2)
        elms2 = self.page.get_elements('view[class="star"][data-index="2"]')
        if len(elms2) > 0:
            elms2[2].tap()
        else:
            print(2)
        delay(2)
        elms3 = self.page.get_elements('view[class="star"][data-index="3"]')
        if len(elms3) > 0:
            elms3[1].tap()
        else:
            print(3)
        delay(2)
        elms4 = self.page.get_elements('view[class="star"][data-index="4"]')
        if len(elms4) > 0:
            elms4[0].tap()
        else:
            print(0)
        delay(2)
        elms5 = self.page.get_elements('view[class="star"][data-index="5"]')
        if len(elms5) > 0:
            elms5[1].tap()
        else:
            print(5)
        delay(2)
        """
        sub = self.page.get_element('view[class="center submit"]')
        sub.tap()
        self.get_screenshot()

    def test_click_guifan(self):
        e = self.page.get_element('text', inner_text="评论规范")
        e.tap()
        self.get_screenshot()



