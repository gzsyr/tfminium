# add by zzh
import minium
from test.common import delay
from test.test_mine import TestMine


class TestYyWritePost(TestMine):
    """
    运营身份发帖
    """

    def setUp(self) -> None:
        self.change_yy()
        delay(1)
        self.app.navigate_to("/page/taofangquan/writePost/writePost?city=qz")
        delay(3)
        self.app.get_current_page()
        print("test  setup!!!!!!!!!!!!!")

    def test_input_title(self):
        """
        运营身份，发帖页面，输入标题
        """
        e1 = self.page.get_element('textarea[class="tip"]')
        e1.input("测试帖子标题")
        delay(1)

    def test_input_content(self):
        """
        运营身份，发帖页面，输入内容
        """
        e1 = self.page.get_element('textarea[class="tip_tiezi"]')
        e1.input("输入帖子内容")
        delay(1)

    def test_chooseimage(self):
        """
        运营身份，发帖页面，点击上传图片按钮
        """
        self.page.get_element('view[class="upload-btn"]')

    def test_click_bk(self):
        """
        运营身份，发帖页面，点击关联板块，弹出弹窗
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]')
        e1.tap()
        delay(2)

    def test_choose_bk(self):
        """
        运营身份，发帖页面，关联板块，选择板块
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]')
        e1.tap()
        delay(2)
        e2 = self.page.get_element('view[class="quick-add quick-addto3 quick-color3"]')
        e2.tap()
        delay(1)
        e3 = self.page.get_element('view[class="close_box"]')
        e3.tap()
        delay(1)

    def test_click_lp(self):
        """
        运营身份，发帖页面，点击关联楼盘，弹出关联楼盘弹窗
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        delay(1)

    def test_search_lp(self):
        """
        运营身份，发帖页面，关联楼盘，新房tab，输入内容搜索
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input("山海国际")
        delay(1)
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        delay(2)

    def test_choose_lp(self):
        """
        运营身份，发帖页面，关联楼盘，选择楼盘,点击添加楼盘
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input("山海国际")
        delay(1)
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        delay(3)
        e4 = self.page.get_element('view[class="quick-add quick-addto2 quick-color2"][data-index="1"]', inner_text="添加")
        e4.tap()
        delay(1)
        e5 = self.page.get_element('view[class="close_box"]')
        e5.tap()
        delay(1)

    def test_change_esftab(self):
        """
        运营身份，发帖页面，关联楼盘，楼盘切换至二手房
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        delay(2)
        e2 = self.page.get_element('view[class="house_opt"]', inner_text="二手房")
        e2.tap()
        delay(1)

    def test_change_xftab(self):
        """
        运营身份，发帖页面，关联楼盘，楼盘切换至新房tab
       """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        delay(1)
        e2 = self.page.get_element('view[class="house_opt activeHouse"]', inner_text="新房")
        e2.tap()

    def test_click_qz(self):
        """
        运营身份，发帖页面，点击同步到圈子
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        delay(1)

    def test_input_quanzi(self):
        """
        运营身份，发帖页面，点击同步到圈子，输入圈子，搜索
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input("圈子")
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        delay(1)

    def test_add_quanzi(self):
        """
        运营身份，发帖页面，点击同步到圈子，输入圈子，搜索,添加圈子
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input("圈子")
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        delay(1)
        e4 = self.page.get_element('view[class="quick-add quick-addto1 quick-color1"][data-index="1"]', inner_text="添加")
        e4.tap()
        delay(1)

    def test_close_quanzi(self):
        """
       运营身份，发帖页面，点击同步到圈子,删除已选择的圈子
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        delay(1)
        e2 = self.page.get_element('image[class="delete_icon"]')
        e2.tap()
        delay(1)

    def test_choose_quanzi(self):
        """
        运营身份，发帖页面，点击同步到圈子，输入圈子，搜索,添加圈子,点击右上角“确定”按钮
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input("圈子")
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        delay(1)
        e4 = self.page.get_element('view[class="quick-add quick-addto1 quick-color1"][data-index="1"]', inner_text="添加")
        e4.tap()
        delay(1)
        e5 = self.page.get_element('view[class="close_box"]')
        e5.tap()
        delay(1)

    def test_quanzi_search(self):
        """
        运营身份，发帖页面，点击同步到圈子,找到“搜索”按钮

        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        delay(1)
        self.page.get_element('view[class="quick_unm_choose flex tfAlignC tfFlexC"]')

    def test_save_draft(self):
        """
        运营身份，发帖页面，点击“保存草稿”按钮
        """
        e1 = self.page.get_element('image[class="save_draft"]')
        e1.tap()
        delay(1)

    def test_click_link(self):
        """
        运营身份，发帖页面，点击链接入口
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]')
        e1.tap()
        delay(2)

    def test_choose_h5(self):
        """
        运营身份，发帖页面，链接选择h5
        """
        self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
        delay(1)
        self.page.get_element('radio[value="0"]').tap()
        delay(1)
        self.page.get_element('input[class="affiliateLink_input"]', inner_text="最多15个字").input("输入链接标题")
        delay(1)
        self.page.get_element('input[class="affiliateLink_input"]', inner_text="输入链接").input("https://m.house365.com")
        delay(1)
        self.page.get_element('view[class="upload-btn"]')
        delay(1)

    def test_choose_nbxcx(self):
        """
        运营身份，发帖页面，链接选择内部小程序
        """
        self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
        delay(1)
        self.page.get_element('radio[value="1"]').tap()
        delay(1)

    def test_choose_wbxcx(self):
        """
        运营身份，发帖页面，链接选择外部小程序,输入内容，选择“确定”
        """
        self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
        delay(1)
        self.page.get_element('radio[value="2"]').tap()
        delay(1)
        self.page.get_element('input[class="affiliateLink_input"]', inner_text="最多15个字").input("输入链接标题")
        delay(1)
        self.page.get_element('input[class="affiliateLink_input"]', inner_text="输入appId").input("wx437db912a2e4078e")
        delay(1)
        self.page.get_element('input[class="affiliateLink_input"]', inner_text="输入链接").input("/pages/index/index")
        delay(1)
        self.page.get_element('button[class="linkBtn"]').tap()
        delay(1)

    def test_click_reset(self):
        """
        运营身份，发帖页面，链接选择h5，点击“重置”
        """
        self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
        delay(1)
        self.page.get_element('radio[value="0"]').tap()
        delay(1)
        self.page.get_element('input[class="affiliateLink_input"]', inner_text="最多15个字").input("输入链接标题")
        delay(1)
        self.page.get_element('button[class="linkBtn_plain"]')
        delay(1)

    def test_click_vest(self):
        """
        运营身份，发帖页面，点击关联用户入口，进入选择马甲页面
        """
        e1 = self.page.get_element('view[class="associated_users_name tfLine1"]')
        e1.tap()
        delay(2)

    def test_choose_vest(self):
        """
        运营身份，发帖页面，点击关联用户入口，进入选择马甲页面，输入“智慧”，搜索，选择第一个结果
        """
        e1 = self.page.get_element('view[class="associated_users_name tfLine1"]')
        e1.tap()
        delay(1)
        e2 = self.page.get_element('input[placeholder="请输入搜索昵称"]')
        e2.input("智慧")
        delay(1)
        self.page.get_element('view[class="search-btn"]').tap()
        delay(1)
        self.page.get_element('view[class="item tfLine1"][data-index="0"]').tap()
        delay(1)

    def test_click_vote(self):
        """
        运营身份，发帖页面,点击投票按钮
        """
        b_l = self.page.element_is_exists('navigator[class="vote-button look"]')
        if b_l == True:
            self.page.get_element('navigator[class="vote-button look"]').tap()
            delay(1)
            self.page.get_element('button[class="submit"]').tap()
            delay(1)
        else:
            self.page.get_element('navigator[class="vote-button create"]').tap()
            delay(1)

    def test_write_mvote(self):
        """
        运营身份，发帖页面,填写投票，支持多选
        """
        b_l = self.page.element_is_exists('navigator[class="vote-button look"]')
        if b_l == True:
            self.page.get_element('navigator[class="vote-button look"]').tap()
            delay(2)
            self.page.get_element('button[class="submit"]').tap()
            delay(1)
        else:
            e1 = self.page.get_element('navigator[class="vote-button create"]')
            e1.tap()
            delay(1)
            self.page.get_element('input[class="vote-title"]').input("投票标题")
            delay(1)
            self.page.get_element('input[data-index="0"]').input("选项一")
            delay(1)
            self.page.get_element('input[data-index="1"]').input("选项二")
            delay(1)
            self.page.get_element('view[class="add"]').tap()
            delay(2)
            self.page.get_element('input[data-index="2"]').input("选项三")
            delay(1)
            self.page.get_element('switch[name="multiple"]').tap()
            delay(1)
            # self.page.get_element('button[class="submit"]').tap()
            # delay(1)

    def test_write_dvote(self):
        """
        运营身份，发帖页面,填写投票，单选
        """
        b_l = self.page.element_is_exists('navigator[class="vote-button look"]')
        if b_l == True:
            self.page.get_element('navigator[class="vote-button look"]').tap()
            delay(1)
            self.page.get_element('button[class="submit"]').tap()
            delay(1)
        else:
            e1 = self.page.get_element('navigator[class="vote-button create"]')
            e1.tap()
            delay(1)
            self.page.get_element('input[class="vote-title"]').input("投票标题")
            delay(1)
            self.page.get_element('input[data-index="0"]').input("选项一")
            delay(1)
            self.page.get_element('input[data-index="1"]').input("选项二")
            delay(1)
            # self.page.get_element('button[class="submit"]').tap()
            # delay(1)

    def test_write_vote_post(self):
        """
        运营，发帖页面，未选择马甲，输入标题，内容，选择关联板块，关联楼盘，同步到圈子，含投票，点击“发布”按钮
        """
        self.page.get_element('textarea[class="tip"]').input("测试帖子标题含投票")
        delay(1)
        self.page.get_element('textarea[class="tip_tiezi"]').input("输入帖子内容")
        delay(1)
        # self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]').tap()
        # delay(1)
        # self.page.get_element('view[class="quick-add quick-addto3 quick-color3"]').tap()
        # delay(1)
        # self.page.get_element('view[class="close_box"]').tap()
        # delay(1)
        # self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]').tap()
        # delay(1)
        # self.page.get_element('input[class="searchTR-input"]').input("山海国际")
        # delay(1)
        # self.page.get_element('view[class="search_txt"]').tap()
        # delay(1)
        # self.page.get_element('view[class="quick-add quick-addto2 quick-color2"][data-index="1"]',
        #                       inner_text="添加").tap()
        # delay(1)
        # self.page.get_element('view[class="close_box"]').tap()
        # delay(1)
        # self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]').tap()
        # delay(1)
        # self.page.get_element('input[class="searchTR-input"]').input("圈子")
        # self.page.get_element('view[class="search_txt"]').tap()
        # delay(2)
        # self.page.get_element('view[class="quick-add quick-addto1 quick-color1"][data-index="1"]',
        #                       inner_text="添加").tap()
        # delay(1)
        # self.page.get_element('view[class="close_box"]').tap()
        # delay(1)
        b_l = self.page.element_is_exists('navigator[class="vote-button look"]')
        if b_l == True:
            self.page.get_element('navigator[class="vote-button look"]').tap()
            delay(1)
            self.page.get_element('button[class="submit"]').tap()
            delay(1)
        else:
            self.page.get_element('navigator[class="vote-button create"]').tap()
            delay(1)
            self.page.get_element('input[class="vote-title"]').input("投票标题")
            delay(1)
            self.page.get_element('input[data-index="0"]').input("选项一")
            delay(1)
            self.page.get_element('input[data-index="1"]').input("选项二")
            delay(1)
            self.page.get_element('view[class="add"]').tap()
            delay(1)
            self.page.get_element('input[data-index="2"]').input("选项三")
            delay(1)
            self.page.get_element('switch[name="multiple"]').tap()
            delay(1)
            self.page.get_element('button[class="submit"]').tap()
            delay(1)
        self.page.get_element('button[class="submit-btn"]').tap()
        delay(2)

    def test_write_vest_post(self):
        """
        运营，选择马甲发帖
        """
        self.page.get_element('textarea[class="tip"]').input("测试帖子标题，选择马甲发帖")
        delay(1)
        self.page.get_element('textarea[class="tip_tiezi"]').input("输入帖子内容")
        delay(1)
        e1 = self.page.get_element('view[class="associated_users_name tfLine1"]')
        e1.tap()
        delay(1)
        e2 = self.page.get_element('input[placeholder="请输入搜索昵称"]')
        e2.input("智慧")
        delay(1)
        self.page.get_element('view[class="search-btn"]').tap()
        delay(2)
        self.page.get_element('view[class="item tfLine1"][data-index="0"]').tap()
        delay(1)
        self.page.get_element('button[class="submit-btn"]').tap()
        delay(2)


















