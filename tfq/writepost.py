# add by zsy

from base.test_mine import TestMine


class WritePost(TestMine):
    """
    发帖页面的相关按钮
    """
    # 以下是发帖页面元素
    def goto_post_detail(self):
        """
        发帖完成后，发布成功页面，点击“查看发布详情”
        """
        e = self.find_element('navigator', inner_text='查看发布详情 >')
        print(e.outer_wxml)
        e.tap()

    def wp_submit(self):
        """
        发帖页面，点击发布按钮
        """
        self.find_element('button[class="submit-btn"]').tap()
        self.delay(2)

    def wp_input_title(self, value='测试帖子标题'):
        """
        发帖页面，输入标题
        """
        self.find_element('textarea[class="tip"]').input(value)
        self.delay(1)
        return self

    def wp_input_content(self, cont='输入帖子内容'):
        """
        发帖页面，输入内容
        """
        self.find_element('textarea[class="tip_tiezi"]').input(cont)
        self.delay(1)
        return self

    def wp_chooseimage(self):
        """
        发帖页面，点击上传图片按钮
        """
        self.find_element('view[class="upload-btn"]')

    def wp_choose_bk(self):
        """
        发帖页面，关联板块，选择板块
        """
        self.find_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]').tap()
        self.delay(2)
        self.find_element('view[data-index="0"]', inner_text='添加').tap()
        self.delay(1)
        self.find_element('view[class="close_box"]').tap()
        self.delay(1)

        return self

    def wp_choose_lp(self, lpname='山海国际'):
        """
        发帖页面，关联楼盘，选择楼盘,点击添加楼盘
        """
        self.find_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]').tap()
        self.delay(1)
        self.find_element('input[class="searchTR-input"]').input(lpname)
        self.delay(1)
        self.find_element('view[class="search_txt"]').tap()
        self.delay(3)
        self.find_element('view[class="quick-add quick-addto2 quick-color2"][data-index="0"]', inner_text="添加").tap()
        self.delay(1)
        self.find_element('view[class="close_box"]').tap()
        self.delay(1)

        return self

    def wp_change_esftab(self):
        """
        发帖页面，关联楼盘，楼盘切换至二手房
        """
        e1 = self.find_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        self.delay(2)
        e2 = self.find_element('view[data-type="secondHouse"]', inner_text="二手房")
        e2.tap()
        self.delay(1)

    def wp_change_xftab(self):
        """
        发帖页面，关联楼盘，楼盘切换至新房tab
        """
        e1 = self.find_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        self.delay(1)
        e2 = self.find_element('view[data-type="newHouse"]', inner_text="新房")
        e2.tap()

    def wp_choose_quanzi(self, quanzi='圈子'):
        """
        发帖页面，点击同步到圈子，输入圈子，搜索,添加圈子,点击右上角“确定”按钮
        """
        self.find_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]').tap()
        self.delay(1)
        self.find_element('input[class="searchTR-input"]').input(quanzi)
        self.find_element('view[class="search_txt"]').tap()
        self.delay(1)
        if not self.page.element_is_exists('view[class="quick-add quick-notadd quick-color1"]', inner_text='已添加'):
            self.find_element('view[class="quick-add quick-addto1 quick-color1"][data-index="0"]', inner_text="添加").tap()
        self.delay(1)
        self.find_element('view[class="close_box"]').tap()
        self.delay(1)

        return self


    def wp_quanzi_show_my_fav(self):
        """
        置业顾问身份，发帖页面，点击同步到圈子，展示“我关注的”内容列表
        """
        self.find_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]').tap()
        self.set_pick_filter('picker', 1)
        self.delay(1)
        return self

    def wp_save_draft(self):
        """
        发帖页面，点击“保存草稿”按钮
        """
        self.find_element('image[class="save_draft"]').tap()
        return self

    # 以下是运营身份独有的
    def yy_choose_h5(self):
        """
        发帖页面，运营身份，链接选择h5
        """
        self.find_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
        self.delay(1)
        self.find_element('radio[value="0"]').tap()
        self.delay(1)
        self.find_element('input[class="affiliateLink_input"]', inner_text="最多15个字").input("输入链接标题")
        self.delay(1)
        self.find_element('input[class="affiliateLink_input"]', inner_text="输入链接").input("https://m.house365.com")
        self.delay(1)
        self.find_element('view[class="upload-btn"]')
        self.delay(1)

    def yy_choose_nbxcx(self):
        """
        运营身份，发帖页面，链接选择内部小程序
        """
        self.find_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
        self.delay(1)
        self.find_element('radio[value="1"]').tap()
        self.delay(1)

    def yy_choose_wbxcx(self):
        """
        运营身份，发帖页面，链接选择外部小程序,输入内容，选择“确定”
        """
        self.find_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
        self.delay(1)
        self.find_element('radio[value="2"]').tap()
        self.delay(1)
        self.find_element('input[class="affiliateLink_input"]', inner_text="最多15个字").input("输入链接标题")
        self.delay(1)
        self.find_element('input[class="affiliateLink_input"]', inner_text="输入appId").input("wx437db912a2e4078e")
        self.delay(1)
        self.find_element('input[class="affiliateLink_input"]', inner_text="输入链接").input("/pages/index/index")
        self.delay(1)
        self.find_element('button[class="linkBtn"]').tap()
        self.delay(1)

    def yy_click_reset(self):
        """
        运营身份，发帖页面，链接选择h5，点击“重置”
        """
        self.find_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
        self.delay(1)
        self.find_element('radio[value="0"]').tap()
        self.delay(1)
        self.find_element('input[class="affiliateLink_input"]', inner_text="最多15个字").input("输入链接标题")
        self.delay(1)
        self.find_element('button[class="linkBtn_plain"]')
        self.delay(1)

    def yy_choose_vest(self, name=''):
        """
        运营身份，发帖页面，点击关联用户入口，进入选择马甲页面，输入“马甲”，搜索，选择第一个结果
        """
        if name == '':
            print('不关联马甲发帖')
        else:
            self.find_element('view[class="associated_users_name tfLine1"]').tap()
            self.delay(1)
            self.find_element('input[placeholder="请输入搜索昵称"]').input(name)
            self.delay(1)
            self.find_element('view[class="search-btn"]').tap()
            self.delay(1)
            self.find_element('view[class="item tfLine1"][data-index="0"]').tap()
            self.delay(1)

        return self

    def yy_write_vote(self, title='投票标题', ipt=None, ismultiple=False):
        """
        运营身份，发帖页面,填写投票，支持多选
        title: 投票标题
        ipt: 选项值，最大3个
        ismultiple: 是否多选
        """
        if ipt is None:
            ipt = ['选项一', '选项二', '选项三', '选项4', '选项5', '选项6', '选项7', '选项8', '选项9', '选项10'
                   , '选项11', '选项12', '选项13']

        b_l = self.page.element_is_exists('view[class="vote-button look"]')
        if b_l == True:
            self.find_element('view[class="vote-button look"]').tap()
            self.delay(2)
            self.find_element('button[class="submit"]').tap()
            self.delay(1)
        else:
            self.find_element('view[class="vote-button create"]', inner_text='投票').tap()
            self.delay(1)
            self.find_element('input[class="vote-title"]').input(title)
            self.delay(1)

            for i in range(0, min(len(ipt), 12)):
                if i > 1:
                    self.find_element('view[class="add"]').tap()
                    self.delay(1)
                self.find_element(f'input[data-index="{i}"]').input(ipt[i])
                self.delay(1)

            if ismultiple:
                self.find_element('switch[name="multiple"]').tap()
                self.delay(1)
            self.find_element('button[class="submit"]').tap()
            self.delay(1)

        return self

    def write_pk(self, left_title='观点一标题', left_cont='观点一描述', right_title='观点二标题', right_cont='观点二描述'):
        """
        V6.26.X: 1004926  PK页面
        输入PK内容
        """

        # 是否是“查看PK”按钮
        b_l = self.page.element_is_exists('view[class="vote-button look"]')
        if b_l == True:
            self.find_element('view[class="vote-button look"]').tap()
            self.delay(2)
            self.find_element('button[class="submit"]').tap()
            self.delay(1)
        else:
            self.find_element('view[class="vote-button create"]', inner_text='PK').tap()
            self.delay(1)

            # 输入观点一
            self.find_element('input[type="text"][data-index="0"]').input(left_title)
            self.delay(1)
            self.find_element('textarea[data-index="0"]').input(left_cont)
            self.delay(1)
            # 输入观点二
            self.find_element('input[type="text"][data-index="1"]').input(right_title)
            self.delay(1)
            self.find_element('textarea[data-index="1"]').input(right_cont)
            self.delay(1)

            self.find_element('button[class="submit"]').tap()
            self.delay(1)

        return self