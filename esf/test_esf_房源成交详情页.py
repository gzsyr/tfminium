# -*-coding:utf-8-*-
import minium

from tfq.writepost import WritePost


class TestFangYuanChengjia(WritePost):
    """
    成交房源详情页
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestFangYuanChengjia, cls).setUpClass()
        cls().change_C()
        print("setupclass TestTieziIM")


    def setUp(self) -> None:
        self.page_name = "/page/publicPages/transactionDetail/transactionDetail?city=sz&id=1739b9688d4df7a170612e6521f35661baa017f9199225a3055845bce914c222"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestFangYuanChengjia, self).setUp()

    def test_001_点击底部IM咨询(self):
        """
        点击底部IM咨询，进入im页面
        """
        self.find_element('view[class="pr center chat"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

    def test_002_点击咨询同小区在售(self):
        """
        点击底部经纪人咨询，进入im
        """
        self.find_element('image[class="center sameBlockSell"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

    def test_003_点击咨询房源详细信息咨询(self):
        """
        点击咨询房源详细信息，进入IM
        """

        self.find_element('view[class="center chatBtn"]').tap()


        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

