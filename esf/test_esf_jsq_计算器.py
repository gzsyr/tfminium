from ddt import file_data
from minium import ddt_class, ddt_case
from base.test_base import TestBase

@ddt_class()
class Testesfjsq(TestBase):
    """
    房贷计算器
    """

    def setUp(self, true=None) -> None:
        self.page_name = "/page/tools/fdjsq/sd/index"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfjsq, self).setUp()
        print("Testesfjsq setup")

