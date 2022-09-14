from ddt import file_data
from minium import ddt_class, ddt_case

from base.common import delay
from base.test_base import TestBase


@ddt_class()
class Testesfvr(TestBase):
    """
    vr详情页
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/sell/pages/readOnlyWeb/readOnlyWeb?url=https%3A%2F%2Fhouse.3dnest.cn%2Fmobile%2Findex.html%3Fcity%3Dnj%26house_id%3D336548747%26house_type%3Dsell%26m%3Ddbdd5208_3LzH_b6f9%26houseinfo%3Dhouse365"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfvr, self).setUp()
        print("Testesfvr setup")