from ddt import ddt, file_data
from base.test_base import TestBase

@ddt
class Testpublishsucceed(TestBase):
    """
    发布成功
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/page/index/index"
        self.switch = True
        self.classname = self.__class__.__name__
        super(Testpublishsucceed, self).setUp()
        print("Testpublishsucceed setup")

    @file_data('./test_publish_succeed.yml')
    def test_publish_succeed_发布成功(self, **index):
        """
        发布出售
        :param kwargs:
        :return:
        """
        self.app.navigate_to('/esf/village/publish/success/success?type=%s&city=nj' % index['type'])
        self.delay(1)
        self.page.get_element('//view[@class="success"]/view[3]/text[2]').tap()
        self.get_screenshot()