# add by zzh
from base.test_base import TestBase

class TestTfqLoupanDetail(TestBase):

    """
    投票楼盘详情页
    """
    def setUp(self) -> None:
        # self.huatiid = 20211
        self.page_name = f"/page/taofangquan/tieziDetail/tieziDetail?city=qz&postsid={self.lptoupiaoid}"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqLoupanDetail, self).setUp()
        print("TestTfqLoupanDetail setup")

    def test_01_投票楼盘单选(self):
        """
        V6.24.X: 进入帖子详情页，点击一个楼盘
        """
        TestBase.lptoupiaoid = 29486

        self.find_element('view[class="lpvote--vote-btn"]', inner_text='投票').tap()
        self.delay(1)

        self.verifyStr('已投', self.find_element('view[class="lpvote--vote-btn"]').inner_text)
        self.get_screenshot()

    def test_02_投票楼盘多选(self):
        """
        V6.24.X: 进入帖子详情页，点击多个楼盘
        """
        try:
            es = self.find_elements('view[class="lpvote--vote-btn"]', inner_text='投票')
            for e in es:
                e.tap()
        except:
            print('已投')

        self.delay(2)
        er = self.find_elements('view[class="lpvote--vote-btn"]')
        for e in er:
            self.verifyStr('已投', e.inner_text, 'yitou ok!')

        self.get_screenshot()

    def test_03_点击楼盘进详情(self):
        """
        V6.24.X: 进入帖子详情页，点击投票选项中的楼盘
        """
        self.find_element('image[class="lpvote--lpimg"]').tap()

        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()
