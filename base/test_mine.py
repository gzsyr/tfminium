#add by zzh
import minium

from base.test_base import TestBase


class TestMine(TestBase):
    """
    我的頁面
    """
    def change_roles(self, re_name=None, change_name=None, change_type=None):
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
            try:
                self.page.get_element('view[class="changeRole"]').tap()
            except minium.MiniElementNotFoundError:
                # 从置业顾问切换到其他角色 弹出切换的按钮
                self.page.get_element('image[class="changerole"]').tap()
            self.delay(1)

            # 勾选要切换的角色
            # self.page.get_element('view[class="name"]', inner_text=change_name).tap()
            self.find_element(f'radio[value="{change_type}"]').tap()

            self.delay(1)
            try:
                self.page.get_element('view[class="change-role-submit"]').tap()
            except minium.MiniElementNotFoundError:
                # 从置业顾问切换到其他角色“切换”按钮
                self.page.get_element('view[class="change-role-submit zygwchange-role-submit"]').tap()
            self.delay(1)
            print('需要切换身份')

        print("切换身份到：", change_name)
        return self

    def change_fbs(self):
        """
        测试切换身份,切换成房博士
        """
        if self.get_third_title() == '房博士':
            print('当前身份是房博士，无需切换')
        else:
        # try:
        #     self.page.get_element('view[class="disflex tfAlignC mxfbs-title"]', text_contains='明星房博士')
        # except:
            self.change_roles(re_name="fbs朱苏云", change_name="房博士-fbs朱苏云", change_type="1478")
            # self.change_roles(re_name="房博士zsy", change_name="房博士-房博士线上5160")
            print('切换到房博士身份')

    def change_zygw(self):
        """
        切换身份，切换成置业顾问
        :return:
        """
        if self.get_third_title() == '置业顾问':
            print('当前身份是置业顾问，无需切换')
        else:

        # try:
        #     self.page.get_element('view[class="disflex tfAlignC level"]', text_contains='置业顾问')
        # except minium.MiniElementNotFoundError:
            self.change_roles(re_name="线上", change_name="置业顾问-线上", change_type="1005")    # online
            # self.change_roles(re_name="测试机", change_name="置业顾问-线上zygw5160")
            print('切换到置业顾问身份')

    def change_yy(self):
        """
        切换身份，切换成运营角色
        :return:
        """
        if self.get_third_title() == '运营':
            print('当前身份是运营，无需切换')
        else:
            self.change_roles(re_name="yy朱苏云", change_name="运营-yy朱苏云", change_type="1481")
            # self.change_roles(re_name="zsyce", change_name="运营-yy5160")
        return self

    def change_C(self):
        """
        切换到C端身份
        :return:
        """
        if self.get_third_title() == 'C端用户':
            print('当前身份是C端用户，无需切换')
        else:
            self.change_roles(re_name="小露朱zsy", change_name="C端用户", change_type="0")

    def change_jjr(self):
        """
        切换到 经纪人 身份
        """
        if self.get_third_title() == '经纪人':
            print('当前身份是经纪人，无需切换')
        else:
            self.change_roles(re_name='颜测测试111', change_name="经纪人", change_type="50662")

