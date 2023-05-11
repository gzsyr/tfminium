from ddt import file_data, ddt
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt
class TestEsfMypublishtype(TestBase):
    """
    我的发布
    """
    def setUp(self) -> None:
        self.page_name = '/esf/village/myPublish/publishType/publishType?city=nj'
        self.classname = self.__class__.__name__
        self.switch = False
        super(TestEsfMypublishtype, self).setUp()

    @ddt_case(
        1, 2, 3, 4
    )
    def test_01_click_type_点击类别4个(self, value):
        """
        我的发布，切换tab
        """
        obj = self.page.get_element(f'view[class="center column type"][data-type = "{value}"]')
        obj.tap()
        self.delay(3)
        self.get_screenshot()

    def test_02_cilic_type_发布说明(self):
        """
        点击发布说明
        :return:
        """
        self.page.get_element('view[class="center explain"]').tap()
        self.delay(3)
        self.get_screenshot()

