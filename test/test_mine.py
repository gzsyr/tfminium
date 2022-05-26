#add by zzh
import minium
from test.common import delay
from test.test_base import TestBase


class TestMine(TestBase):
    """
    我的頁面
    """
    def change_roles(self, re_name=None, change_name=None):
        """
        re_name：我的页面上期望展示的身份昵称
        change_name：切换角色列表中的昵称
        当前身份昵称=re_name，不用切换角色
        当前身份昵称和re_name不一致，则切换成change_name,切换身份
        """
        self.app.switch_tab("/page/index/mine?city=qz")
        delay(2)
        self.app.get_current_page()
        b_l = self.page.element_is_exists('view[class="grzx_zcdl-1"]', inner_text=re_name)
        if b_l:
            print("不用切换角色")
        else:
            e1 = self.page.get_element('view[class="changeRole"]')
            e1.tap()
            delay(1)
            e2 = self.page.get_element('view[class="name"]', inner_text=change_name)
            e2.tap()
            delay(1)
            e3 = self.page.get_element('view[class="change-role-submit"]')
            e3.tap()
            delay(1)
        return self

    def change_fbs(self):
        """
        测试切换身份,切换成房博士
        """
        self.change_roles(re_name="fbs智慧", change_name="房博士-fbs智慧")

    def change_zygw(self):
        """
        切换身份，切换成置业顾问
        :return:
        """
        self.change_roles(re_name="线上", change_name="置业顾问-线上")

    def change_yy(self):
        """
        切换身份，切换成运营角色
        :return:
        """
        self.change_roles(re_name="fbs智慧", change_name="房博士-fbs智慧")
        return self

    def change_C(self):
        """
        切换到C端身份
        :return:
        """
        self.change_roles(re_name="fbs智慧", change_name="房博士-fbs智慧")



