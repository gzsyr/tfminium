import minium

from test.common import delay


class TestKFTRoute(minium.MiniTest):
    """
    看房团路线页面
    """
    def setUp(self) -> None:
        self.app.navigate_to('/page/houseteam/detail?id=8359&city=qz')
        page = self.app.get_current_page()
        print("test  setup!!!!!!!!!!!!!")


    def test_click_list(self):
        """
        点击第一个楼盘
        :return:
        """
        delay(2)
        ele = self.page.get_element('image[src="http://img11.house365.com/njnewhouse/2015/04/25/thumb/1429933967553b0f8fd1606.png"]')
        # ele = self.page.get_element('//navigator[@url="/page/newhouse/detail?pinyin=wandaokelagongguan&city=qz"]/view/view')
        ele.tap()
        print("click_list:", ele)
        # ele = self.page.get_elements('//view[@class="list__item line"]/navigator')
        # e = ele[0]
        # e.tap()
        # print("click_list:", e)
        delay(5)

    def test_click_first(self):
        """
        点击首页
        :return:
        """
        ele = self.page.get_element('to-home-btn[is="component/toHomeBtn"]').get_element('image[role="img"]')
        ele.tap()
        print("click_first:", ele)
        delay(2)

    def test_click_signup(self):
        """
        点击立即报名,点击我已阅读小√，输入手机号，点击获取验证码
        :return:
        """
        ele = self.page.get_element('view[class="f30 white t-c"]')
        ele.tap()
        delay(4)
        e2 = self.page.get_element('image.agree-icon').tap()
        e3 = self.page.get_element('input', inner_text='请填写11位手机号码').input('15105182846')
        e4 = self.page.get_element('button').tap()
        print("click_signup:", ele)
        delay(4)

    def test_click_activity(self):
        """
        点击活动流程
        :return:
        """
        ele = self.page.get_element('view[class="activity"]')
        ele.tap()
        print("click_activity:", ele)
        delay(2)

    def test_click_declare(self):
        """
        点击免责声明
        :return:
        """
        ele = self.page.get_element('view[class="declare"]')
        ele.tap()
        print("click_declare:", ele)
        delay(2)

    def test_click_zphone(self):
        """
        点击电话咨询图标
        :return:
        """
        ele = self.page.get_element('icon[class="icon-tel mt15"]')
        ele.tap()
        print("click_zphone:", ele)
        delay(2)
