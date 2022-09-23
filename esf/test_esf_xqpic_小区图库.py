from minium import ddt_class, ddt_case
from base.test_base import TestBase
@ddt_class()
class Testesfxqpic(TestBase):
    """
    小区详情页-点击相册-进入图片页面
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/pages/detail/detailImage/detailImage?blockId=3982"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testesfxqpic, self).setUp()
        print("Testesfxqpic setup")

    def test_click_pic_点击图片进入大图(self):
        """
        点击图片进入大图
        :return:
        """
        picview = self.page.element_is_exists('//scroll-view')
        if picview == True:
            pic = self.page.get_elements('//scroll-view/view/view[2]/view')
            pic[1].tap()
            self.get_screenshot()
        else:
            print('没有图库')