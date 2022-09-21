from minium import ddt_class, ddt_case
import pyautogui
from base.test_base import TestBase
@ddt_class()
class Testesfjgzs(TestBase):
    """
    价格走势
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/pages/priceTrend/priceTrend?blockId=8819&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfjgzs, self).setUp()
        print("Testesfjgzs setup")

    def test_click_title_点击小区名(self):
        """
        点击小区名
        :return:
        """
        e = self.page.get_element('view[class="flex align_center villageName"]')
        e.tap()
        self.get_screenshot()

    def test_click_collect_关注和取消关注(self):
        """
        点击关注，取消关注
        :return: 
        """
        collect = self.page.element_is_exists('view[class="center collect"]')
        if collect == True:
            self.page.get_element('view[class="center collect"]').tap()
            self.delay(2)

            collected = self.page.element_is_exists('view[class="center collected"]')
            if collected == True:
                self.page.get_element('view[class="center collected"]').tap()
                self.delay(2)
                self.get_screenshot()
            else:
                self.page.get_element('view[class="center collect"]').tap()
                self.delay(2)
                self.get_screenshot()
        else:
            self.page.get_element('view[class="center collected"]').tap()

    def test_click_date_点击日期tab(self):
        """
        点击近6月、近1年、近2年，tab切换
        :return:
        """
        june_pitchon = self.page.element_is_exists('view[class="center pr timeSlot active"][data-type="1"]')
        if june_pitchon == True:
            self.page.get_element('view[class="center pr timeSlot"][data-type="2"]').tap()
            self.delay(2)
            self.get_screenshot()
            self.page.get_element('view[class="center pr timeSlot"][data-type="3"]').tap()
            self.delay(2)
            self.get_screenshot()
            self.page.get_element('view[class="center pr timeSlot"][data-type="1"]').tap()
            self.delay(2)
            self.get_screenshot()
        else:
            print(0)

    def test_click_sellhouse_在售房源进入详情(self):
        """
        在售房源-进入房源详情页
        :return:
        """
        self.page.scroll_to(350, 500)
        self.delay(1)
        elm_items = self.page.get_elements('view[class="item"]')
        elm_first_item = elm_items[0]
        elms = elm_first_item.get_element('sell_item').get_elements('view')
        elms[0].tap()
        self.delay(3)
        self.get_screenshot()

    def test_click_allhouse_查看全部房源(self):
        """
        点击查看全部房源按钮
        :return:
        """
        self.page.scroll_to(1150, 500)
        self.delay(1)
        e = self.page.get_element('view[class="center more"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

    def test_click_mfpg_点击卖房评估(self):
        """
        点击卖房评估
        :return:
        """
        self.page.scroll_to(1550, 500)
        self.elay(1)
        e = self.page.get_element('view[class="center evaluate"]')
        e.tap()
        self.elay(3)
        self.get_screenshot()

    def test_click_bnzf_点击帮你找房(self):
        """
        点击帮你找房
        :return:
        """
        self.page.scroll_to(1550, 500)
        self.delay(1)
        e = self.page.get_element('view[class="center help"]')
        e.tap()
        self.delay(3)
        self.get_screenshot()

