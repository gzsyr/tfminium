import time

import minium

from test.common import delay


class TestKFT(minium.MiniTest):
    """
    看房团页面
    """
    def setUp(self) -> None:
        self.app.navigate_to('/page/houseteam/list?city=qz')
        page = self.app.get_current_page()
        print("test  setup!!!!!!!!!!!!!")
        delay(2)

    def test_click_kfxq(self):
        """
        手机号需要预先输入，
        看房团页面，点击看房需求,
        键入当日日期，
        点击楼盘输入框，进入新页面，
        点击输入框，输入‘苏宁’
        点击‘苏宁测试1’，返回，
        点击立即报名
        :return:
        """
        delay(2)
        ele = self.page.get_element("view[class='kftfixed-r']")
        ele.tap()
        delay(2)
        import datetime
        today = datetime.date.today()
        e3 = time.strftime(format(today))
        e2 = self.page.get_element('picker')
        e2.trigger("change", {"value": e3})
        delay(2)
        e4 = self.page.get_element('view.kfxqLi-l').tap()
        delay(2)
        e5 = self.page.get_element('input.searchTR-input').input('苏宁')
        delay(2)
        e6 = self.page.get_element('text.searchBLi-l').tap()
        delay(2)
        e7 = self.page.get_element('button.kfxqSub.kgt_tjxq').tap()
        print("click_kfxq: ", ele)
        delay(2)

    def test_click_route1(self):
        """
        点击第一条路线
        :return:
        """
        ele = self.page.get_element('view[class="kftliLi-l"]', inner_text="测试22")
        ele.tap()
        print("click_route1:", ele)
        delay(2)

    def test_click_zphone(self):
        """
        点击电话咨询
        :return:
        """
        ele = self.page.get_element('view[class="kftliBtn-style bg_448bc3 kgt_phone"]')
        ele.tap()
        print("click_zphone:", ele)
        delay(2)

    def test_click_signup(self):
        """
        点击我要报名,点击我已阅读小√，输入手机号，点击获取验证码
        :return:
        """
        ele = self.page.get_element('view[class="kftliBtn-style bg_ff5500"]')
        ele.tap()
        delay(4)
        e2 = self.page.get_element('image.agree-icon').tap()
        e3 = self.page.get_element('input', inner_text='请填写11位手机号码').input('15105182846')
        e4 = self.page.get_element('button').tap()
        print("click_signup:", ele)
        delay(2)

    def test_click_addgroup(self):
        """
        点击加群图标
        :return:
        """
        ele = self.page.get_element('add-group[is="component/addgroup"]').get_element('image[role="img"]')
        ele.tap()
        print("click_addgroup:", ele)
        delay(5)

    def test_click_zallroutes(self):
        """
        点击全部路线下拉箭头
        :return:
        """
        ele = self.page.get_element('view[class="headTR-select"]')
        delay(2)
        ele.tap()
        print("click_zallroutes:", ele)
        delay(2)