from minium import ddt_class, ddt_case
from base.common import delay
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
        super(Testesfjgzs, self).setUp()
        print("Testesfjgzs setup")

    def test_click_title(self):
        """
        点击小区名
        :return:
        """
        e = self.page.get_element('view[class="flex align_center villageName"]')
        e.tap()

    def test_click_collect(self):
        """
        点击关注，取消关注
        :return: 
        """
        collect = self.page.element_is_exists('view[class="center collect"]')
        if collect == True:
            self.page.get_element('view[class="center collect"]').tap()
            delay(2)

            collected = self.page.element_is_exists('view[class="center collected"]')
            if collected == True:
                self.page.get_element('view[class="center collected"]').tap()
            else:
                self.page.get_element('view[class="center collect"]').tap()
        else:
            self.page.get_element('view[class="center collected"]').tap()

    def test_click_date(self):
        """
        点击近6月、近1年、近2年，tab切换
        :return:
        """
        june_pitchon = self.page.element_is_exists('view[class="center pr timeSlot active"][data-type="1"]')
        if june_pitchon == True:
            self.page.get_element('view[class="center pr timeSlot"][data-type="2"]').tap()
            delay(2)
            self.page.get_element('view[class="center pr timeSlot"][data-type="3"]').tap()
            delay(2)
            self.page.get_element('view[class="center pr timeSlot"][data-type="1"]').tap()
        else:
            print(0)

    def test_click_sellhouse(self):
        """
        在售房源-进入房源详情页
        :return:
        """
        self.page.scroll_to(350, 500)
        delay(1)
        elm_items = self.page.get_elements('view[class="item"]')
        elm_first_item = elm_items[0]
        elms = elm_first_item.get_element('sell_item').get_elements('view')
        elms[0].tap()

    def test_click_allhouse(self):
        """
        点击查看全部房源按钮
        :return:
        """
        self.page.scroll_to(1150, 500)
        delay(1)
        e = self.page.get_element('view[class="center more"]')
        e.tap()

    def test_click_mfpg(self):
        """
        点击卖房评估
        :return:
        """
        self.page.scroll_to(1550, 500)
        delay(1)
        e = self.page.get_element('view[class="center evaluate"]')
        e.tap()

    def test_click_bnzf(self):
        """
        点击帮你找房
        :return:
        """
        self.page.scroll_to(1550, 500)
        delay(1)
        e = self.page.get_element('view[class="center help"]')
        e.tap()

