from ddt import file_data, ddt
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt
class Testesfjubao(TestBase):
    """
    举报页
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/report/report?sellId=331233705&real=1"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfjubao, self).setUp()
        print("Testesfjubao setup")

    @file_data('./test_func_jubao.yml')
    def test_sub_jb_填写举报信息(self, **kwargs):
        """
        填写举报信息
        :param kwargs:
        :return:
        """
        self.delay(3)
        self.set_pick_filter('picker[range-key="name"]', kwargs['title'])
        self.page.get_element('textarea[class="descInput"]').input(kwargs['desc'])
        sub = 'self.page.get_element(\'view[class="center submitBtn"]\').tap()'
        self.verifyStr(True, self.getShowToast(sub), '举报成功ok')
        self.get_screenshot()
        #self.get_capture()
        #self.verifyByScreenshot('esf/jubao.png')






