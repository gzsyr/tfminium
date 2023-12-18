from ddt import ddt, file_data
from base.test_base import TestBase

@ddt
class Testrentzupublist(TestBase):
    """
    求租发布
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/publish/lookRoom/rent?city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentzupublist, self).setUp()
        print("Testrentzupublist setup")

    def test_publish_zurent_求租发布(self):
        self.delay(2)
        # 房屋类型
        self.page.get_element('view[class="center option optionChecked"][data-id="1"]').tap()
        self.delay(3)

        # 您的意向位置
        self.page.get_element('view[class="between location"]').tap()
        self.delay(3)
        self.page.get_element('//scroll-view[@class="level level_2"]/view[2]').tap()
        self.delay(3)
        self.page.get_element('//scroll-view[@class="flex_1 level"]/view[5]').tap()
        self.delay(3)
        self.page.get_element('view[class="center confirm"]', inner_text='确定').tap()

        # 意向租房类型
        self.page.get_element('view[class="center option"][data-id="1"][data-key="rent_type"]', inner_text='合租单间').tap()
        self.delay(3)

        # 您租房预算
        self.page.get_element('view[class="center option"][data-id="3"][data-key="rent_price"]',
                              inner_text='1500-2000元').tap()
        self.delay(3)

        # 入住时间
        self.page.scroll_to(800, 500)
        self.delay(1)
        self.page.get_element('view[class ="center option"][data-id="1"][data-key="rent_other"]',
                              inner_text='一周以内').tap()
        self.delay(3)

        self.get_screenshot()
        self.delay(5)

        # 立即找房
        self.page.get_element('view[class ="center submit"]', inner_text='立刻找房').tap()
        self.delay(3)

        self.get_screenshot()
        self.delay(3)

        # 点击个人中心
        self.page.get_element('text[class="color"]').tap()
        self.delay(1)


