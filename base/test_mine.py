#add by zzh
import minium

from base.test_base import TestBase


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
        print("当前页面路径", self.page.path)
        if self.page.path != "/page/index/mine":
            self.app.switch_tab("/page/index/mine?city=qz")
            self.delay(3)

        # b_l = self.page.element_is_exists('view[class="grzx_zcdl-1"]', inner_text=re_name)
        # if b_l:
        #     print("不用切换角色")
        # else:
        #     e1 = self.page.get_element('view[class="changeRole"]')
        #     e1.tap()
        #     self.delay(1)
        #     e2 = self.page.get_element('view[class="name"]', inner_text=change_name)
        #     e2.tap()
        #     self.delay(1)
        #     e3 = self.page.get_element('view[class="change-role-submit"]')
        #     e3.tap()
        #     self.delay(1)
        try:
            # self.page.get_element('view[class="grzx_zcdl-1"]', inner_text=re_name)
            # self.page.get_element('view[class="disflex disflex-alignitems-flex-end"]')
            # page > view.tfFlex.j - center.head > view.headR.disflex > view.grzx_inf > view.disflex.disflex - alignitems - flex - end > view
            self.page.get_element('view.disflex.disflex-alignitems-flex-end > view', inner_text=re_name)
        except minium.MiniElementNotFoundError:
            self.page.get_element('view[class="changeRole"]').tap()
            self.delay(1)
            self.page.get_element('view[class="name"]', inner_text=change_name).tap()
            self.delay(1)
            self.page.get_element('view[class="change-role-submit"]').tap()
            self.delay(1)
            print('需要切换身份')

        print("切换身份到：", change_name)
        return self

    def change_fbs(self):
        """
        测试切换身份,切换成房博士
        """
        try:
            self.page.get_element('view[class="disflex tfAlignC mxfbs-title"]', text_contains='明星房博士')
        except:
            self.change_roles(re_name="fbs朱苏云", change_name="房博士-fbs朱苏云")
            print('切换到房博士身份')

    def change_zygw(self):
        """
        切换身份，切换成置业顾问
        :return:
        """
        try:
            self.page.get_element('view[class="disflex tfAlignC level"]', text_contains='置业顾问')
        except minium.MiniElementNotFoundError:
            self.change_roles(re_name="线上", change_name="置业顾问-线上")    # online
            # self.change_roles(re_name="线上", change_name="置业顾问-测试pre环境")    # dev
            print('切换到置业顾问身份')

    def change_yy(self):
        """
        切换身份，切换成运营角色
        :return:
        """
        self.change_roles(re_name="yy朱苏云", change_name="运营-yy朱苏云")
        return self

    def change_C(self):
        """
        切换到C端身份
        :return:
        """
        self.change_roles(re_name="小露朱zsy", change_name="C端用户")



