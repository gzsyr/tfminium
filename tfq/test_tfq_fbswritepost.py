# add by zzh
from test.test_mine import TestMine


class TestFbsWritePost(TestMine):
    """
    房博士身份发帖
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestFbsWritePost, cls).setUpClass()
        cls().change_fbs()
        print("TestFbsWritePost setupclass")

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/writePost/writePost?city=qz"
        self.switch = False
        super(TestFbsWritePost, self).setUp()
        print("TestFbsWritePost setup")

    def test_fbs_input_title(self, text="测试帖子标题"):
        """
        房博士身份，发帖页面，输入标题
        """
        e1 = self.page.get_element('textarea[class="tip"]')
        e1.input(text)
        return self

    def test_fbs_input_content(self, text="输入内容"):
        """
        房博士身份，发帖页面，输入内容
        """
        e1 = self.page.get_element('textarea[class="tip_tiezi"]')
        e1.input(text)
        return self

    def test_fbs_chooseimage(self):
        """
        房博士身份，发帖页面，点击上传图片按钮
        """
        e1 = self.page.get_element('view[class="upload-btn"]')
        # e1.tap()

    def test_fbs_click_bk(self):
        """
        房博士身份，发帖页面，点击关联板块，弹出弹窗
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]')
        e1.tap()

    def test_fbs_choose_bk(self):
        """
        房博士身份，发帖页面，关联板块，选择板块
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]')
        e1.tap()
        self.delay(3)
        e2 = self.page.get_element('view[class="quick-add quick-addto3 quick-color3"]')
        e2.tap()
        self.delay(1)
        e3 = self.page.get_element('view[class="close_box"]')
        e3.tap()
        return self

    def test_fbs_click_lp(self):
        """
        房博士身份，发帖页面，点击关联楼盘，弹出关联楼盘弹窗
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()

    def test_fbs_search_lp(self):
        """
        房博士身份，发帖页面，关联楼盘，新房tab，输入内容搜索
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input("山海国际")
        self.delay(1)
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()

    def test_fbs_choose_lp(self, text="山海国际"):
        """
        房博士身份，发帖页面，关联楼盘，选择楼盘,点击添加楼盘
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input(text)
        self.delay(2)
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        self.delay(3)
        e4 = self.page.get_element('view[class="quick-add quick-addto2 quick-color2"][data-index="1"]', inner_text="添加")
        e4.tap()
        self.delay(2)
        e5 = self.page.get_element('view[class="close_box"]')
        e5.tap()
        return self

    def test_fbs_change_esftab(self):
        """
        房博士身份，发帖页面，关联楼盘，楼盘切换至二手房
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        self.delay(3)
        e2 = self.page.get_element('view[class="house_opt"]', inner_text="二手房")
        e2.tap()

    def test_fbs_change_xftab(self):
        """
        房博士身份，发帖页面，关联楼盘，楼盘切换至新房tab
       """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('view[class="house_opt activeHouse"]', inner_text="新房")
        e2.tap()

    def test_fbs_click_qz(self):
        """
        房博士身份，发帖页面，点击同步到圈子
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()

    def test_fbs_input_quanzi(self, text="圈子"):
        """
        房博士身份，发帖页面，点击同步到圈子，输入圈子，搜索
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input(text)
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()

    def test_fbs_add_quanzi(self, text="圈子"):
        """
        房博士身份，发帖页面，点击同步到圈子，输入圈子，搜索,添加圈子
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input(text)
        self.delay(1)
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        self.delay(3)
        e4 = self.page.get_element('view[class="quick-add quick-addto1 quick-color1"][data-index="1"]', inner_text="添加")
        e4.tap()

    def test_fbs_close_quanzi(self):
        """
        房博士身份，发帖页面，点击同步到圈子,删除已选择的圈子
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('image[class="delete_icon"]')
        e2.tap()

    def test_fbs_choose_quanzi(self, text="圈子"):
        """
        房博士身份，发帖页面，点击同步到圈子，输入圈子，搜索,添加圈子,点击右上角“确定”按钮
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input(text)
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        self.delay(3)
        e4 = self.page.get_element('view[class="quick-add quick-addto1 quick-color1"][data-index="1"]', inner_text="添加")
        e4.tap()
        self.delay(1)
        e5 = self.page.get_element('view[class="close_box"]')
        e5.tap()
        self.delay(1)
        return self

    def test_fbs_quanzi_search(self):
        """
        房博士身份，发帖页面，点击同步到圈子,“搜索”按钮

        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        self.delay(1)
        self.page.get_element('view[class="quick_unm_choose flex tfAlignC tfFlexC"]')

    def test_fbs_save_draft(self):
        """
        房博士身份，发帖页面，点击“保存草稿”按钮
        """
        e1 = self.page.get_element('image[class="save_draft"]')
        e1.tap()

    def test_fbs_submit(self):
        """
        房博士身份，发帖页面,点击提交按钮
        """
        self.page.get_element('button[class="submit-btn"]').tap()
        return self

    def test_fbs_write_post(self):
        """
        房博士身份，发帖页面，输入标题，内容，选择关联板块，关联楼盘，同步到圈子，点击“发布”按钮
        """
        self.test_fbs_input_title().delay(1).test_fbs_input_content().test_fbs_choose_bk().\
            test_fbs_choose_lp().test_fbs_choose_quanzi().test_fbs_submit()
        # self.page.get_element('textarea[class="tip"]').input("测试帖子标题")
        # delay(1)
        # self.page.get_element('textarea[class="tip_tiezi"]').input("输入帖子内容")
        # delay(1)
        # e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]')
        # e1.tap()
        # delay(3)
        # e2 = self.page.get_element('view[class="quick-add quick-addto3 quick-color3"]')
        # e2.tap()
        # delay(1)
        # e3 = self.page.get_element('view[class="close_box"]')
        # e3.tap()
        # delay(1)
        # e4 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        # e4.tap()
        # delay(1)
        # e5 = self.page.get_element('input[class="searchTR-input"]')
        # e5.input("山海国际")
        # delay(2)
        # e6 = self.page.get_element('view[class="search_txt"]')
        # e6.tap()
        # delay(3)
        # e7 = self.page.get_element('view[class="quick-add quick-addto2 quick-color2"][data-index="1"]', inner_text="添加")
        # e7.tap()
        # delay(1)
        # e8 = self.page.get_element('view[class="close_box"]')
        # e8.tap()
        # delay(1)
        # e9 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        # e9.tap()
        # delay(1)
        # e10 = self.page.get_element('input[class="searchTR-input"]')
        # e10.input("圈子")
        # delay(1)
        # e11 = self.page.get_element('view[class="search_txt"]')
        # e11.tap()
        # delay(3)
        # e12 = self.page.get_element('view[class="quick-add quick-addto1 quick-color1"][data-index="1"]', inner_text="添加")
        # e12.tap()
        # delay(1)
        # self.page.get_element('view[class="close_box"]').tap()
        # delay(1)
        # self.page.get_element('button[class="submit-btn"]').tap()
        # delay(1)

