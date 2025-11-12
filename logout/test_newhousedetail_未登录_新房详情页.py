# -*-coding:utf-8-*-
from base.test_base import TestBase


class TestLogoutNewhouseDetail(TestBase):
    """
    未登录  新房详情页相关用例
    """

    def setUp(self) -> None:
        self.page_name = "/page/newhouse/detail?pinyin=shanhaiguojixzl&city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestLogoutNewhouseDetail, self).setUp()
        self.delay(2)


    def test_01_未登录_点击最新动态(self):
        """
        V6.19.x: 点击新房详情页的最新动态按钮
        """
        # self.find_elements("button[class='logincomponent--loginBtn']")[0].tap()
        self.find_element("view[class='newHouseIconInLi-b']", inner_text='最新动态').tap()

        self.get_screenshot()
        # self.input_value_by_mk('logout/phone_refuse.png')

    def test_02_未登录_点击户型解析(self):
        """
        V6.19.x: 点击新房详情页的户型解析按钮
        """
        # self.find_elements("button[class='logincomponent--loginBtn']")[1].tap()
        self.find_element("view[class='newHouseIconInLi-b']", inner_text='户型解析').tap()

        self.get_screenshot()
        # self.input_value_by_mk('logout/phone_refuse.png')

    def test_03_未登录_点击楼盘详情(self):
        """
        V6.19.x: 点击新房详情页的楼盘详情按钮
        """
        # self.find_elements("button[class='logincomponent--loginBtn']")[2].tap()
        self.find_element("view[class='newHouseIconInLi-b']", inner_text='楼盘详情').tap()

        self.get_screenshot()
        # self.input_value_by_mk('logout/phone_refuse.png')

    def test_04_未登录_点击一房一价(self):
        """
        V6.19.x: 点击新房详情页的一房一价按钮
        """
        # self.find_elements("button[class='logincomponent--loginBtn']")[3].tap()
        self.find_element("view[class='newHouseIconInLi-b']", inner_text='一房一价').tap()

        self.get_screenshot()
        # self.input_value_by_mk('logout/phone_refuse.png')

    def test_05_未登录_点击楼盘点评(self):
        """
        V6.19.x: 未登录，点击新房详情页的楼盘点评按钮
        """
        # self.find_elements("button[class='logincomponent--loginBtn']")[4].tap()
        self.find_element("view[class='newHouseIconInLi-b']", inner_text='楼盘点评').tap()

        self.get_screenshot()
        # self.input_value_by_mk('logout/phone_refuse.png')

    def test_06_未登录_点击主力户型(self):
        """
        V6.19.X: 未登录，点击新房详情页主力户型
        """
        self.page.scroll_to(2600, 500)
        # self.find_elements("button[class='logincomponent--loginBtn']")[5].tap()
        self.find_element("image[class='newHouseZlhxLiT-img']").tap()

        self.get_screenshot()
        # self.input_value_by_mk('logout/phone_refuse.png')

    def test_07_未登录_点击位置及周边查看更多(self):
        """
        V6.19.x: 未登录，点击新房详情页的位置及周边的查看更多
        """
        self.page.scroll_to(3000, 500)
        # self.find_elements("button[class='logincomponent--loginBtn']")[6].tap()
        self.find_element("view[class='infoTitle'][data-eventid='2648']").tap()

        self.get_screenshot()
        # self.input_value_by_mk('logout/phone_refuse.png')
        # self.delay(1)
        # self.input_value_by_mk('xf/mapreturn.png')  # del by V6.22.x

    def test_08_未登录_点击地图(self):
        """
        V6.19.x: 未登录，点击新房详情页的地图
        """
        self.page.scroll_to(3000, 500)
        # self.find_elements("button[class='logincomponent--loginBtn']")[7].tap()
        self.find_element("view[class='infoTitle'][data-eventid='2648']").tap()

        # self.get_screenshot()
        # self.input_value_by_mk('logout/phone_refuse.png')
        # self.delay(1)
        # self.input_value_by_mk('xf/mapreturn.png')  # del by V6.22.x

    def test_09_未登录_楼盘PK(self):
        """
        V6.40.X: 未登录，点击测试报告
        """
        url = '/page/newhouse/detail?pinyin=nananwanxingchengshiguangchang&city=qz'
        self.redirect_to_page(url=url)

        self.delay(10)
        self.find_element('view[class="infoWrap"][id="pk"]').tap()
        self.delay(10)
        self.get_screenshot()

    def test_10_未登录_查看测评报告(self):
        """
        V6.40.X: 未登录，点击测试报告
        """
        url = '/page/newhouse/detail?pinyin=nananwanxingchengshiguangchang&city=qz'
        self.redirect_to_page(url=url)

        self.page.scroll_to(2500, 200)
        self.delay(10)
        self.find_element('view[class="check-more"]').tap()
        self.delay(10)
        self.get_screenshot()

    def test_11_未登录_查看分析(self):
        """
        V6.41.X: 未登录，点击日照分析
        """
        url = '/page/newhouse/rizhaofenxi/rizhaofenxi?city=qz&pinyin=shanhaiguojixzl&tab=1'
        self.redirect_to_page(url=url)
        self.delay(12)
        # self.find_element('button[class="logincomponent--loginBtn"]').tap()
        self.find_element('view[class="icon tfFlex tfAlignC icon_1"]').tap()
        self.get_screenshot()
        # self.input_value_by_mk('logout/phone_refuse.png')
        self.delay(1)
