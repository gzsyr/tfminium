# add by zsy
from test.test_mine import TestMine


class TestZygwWritePost(TestMine):
    """
    置业顾问身份发帖
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestZygwWritePost, cls).setUpClass()
        cls().change_zygw()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/writePost/writePost?city=qz"
        self.switch = False
        super(TestZygwWritePost, self).setUp()
        print("TestZygwWritePost setup")

    def test_zygw_input_title(self, text="测试帖子标题"):
        """
        置业顾问身份，发帖页面，输入标题
        """
        e1 = self.page.get_element('textarea[class="tip"]')
        e1.input(text)
        return self

    def test_zygw_input_content(self, text="输入帖子内容"):
        """
        置业顾问身份，发帖页面，输入内容
        """
        e1 = self.page.get_element('textarea[class="tip_tiezi"]')
        e1.input(text)
        return self

    def test_zygw_chooseimage(self):
        """
        置业顾问身份，发帖页面，点击上传图片按钮
        """
        e1 = self.page.get_element('view[class="upload-btn"]')
        return self

    def test_zygw_click_bk(self):
        """
        置业顾问身份，发帖页面，点击关联板块，弹出弹窗
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]')
        e1.tap()
        return self

    def test_zygw_choose_bk(self):
        """
        置业顾问身份，发帖页面，关联板块，选择板块
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

    def test_zygw_click_lp(self):
        """
        置业顾问身份，发帖页面，点击关联楼盘，弹出关联楼盘弹窗
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        return self

    def test_zygw_search_lp(self, text="山海国际"):
        """
        置业顾问身份，发帖页面，关联楼盘，新房tab，输入内容搜索
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input(text)
        self.delay(1)
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        return self

    def test_zygw_choose_lp(self):
        """
        置业顾问身份，发帖页面，关联楼盘，选择楼盘,点击添加楼盘
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input("山海国际")
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

    def test_zygw_change_esftab(self):
        """
        置业顾问身份，发帖页面，关联楼盘，楼盘切换至二手房
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        self.delay(3)
        e2 = self.page.get_element('view[class="house_opt"]', inner_text="二手房")
        e2.tap()
        return self

    def test_zygw_change_xftab(self):
        """
        置业顾问身份，发帖页面，关联楼盘，楼盘切换至新房tab
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('view[class="house_opt activeHouse"]', inner_text="新房")
        e2.tap()
        return self

    def test_zygw_click_qz(self):
        """
        置业顾问身份，发帖页面，点击同步到圈子
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        return self

    def test_zygw_input_quanzi(self):
        """
        置业顾问身份，发帖页面，点击同步到圈子，输入圈子，搜索
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input("圈子")
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        return self

    def test_zygw_add_quanzi(self):
        """
        置业顾问身份，发帖页面，点击同步到圈子，输入圈子，搜索,添加圈子
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input("圈子")
        self.delay(1)
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        self.delay(3)
        e4 = self.page.get_element('view[class="quick-add quick-addto1 quick-color1"][data-index="1"]', inner_text="添加")
        e4.tap()
        return self

    def test_zygw_close_quanzi(self):
        """
        置业顾问身份，发帖页面，点击同步到圈子,删除已选择的圈子
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('image[class="delete_icon"]')
        e2.tap()
        return self

    def test_zygw_choose_quanzi(self):
        """
        置业顾问身份，发帖页面，点击同步到圈子，输入圈子，搜索,添加圈子,点击右上角“确定”按钮
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        self.delay(1)
        e2 = self.page.get_element('input[class="searchTR-input"]')
        e2.input("圈子")
        e3 = self.page.get_element('view[class="search_txt"]')
        e3.tap()
        self.delay(3)
        e4 = self.page.get_element('view[class="quick-add quick-addto1 quick-color1"][data-index="1"]', inner_text="添加")
        e4.tap()
        self.delay(1)
        e5 = self.page.get_element('view[class="close_box"]')
        e5.tap()
        return self

    def test_zygw_quanzi_search(self):
        """
        置业顾问身份，发帖页面，点击同步到圈子,“搜索”按钮
        """
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e1.tap()
        self.delay(1)
        self.page.get_element('view[class="quick_unm_choose flex tfAlignC tfFlexC"]')
        return self

    def test_zygw_save_draft(self):
        """
        置业顾问身份，发帖页面，点击“保存草稿”按钮
        """
        e1 = self.page.get_element('image[class="save_draft"]')
        e1.tap()
        return self

    def test_zygw_write_post(self):
        """
        置业顾问身份，发帖页面，输入标题，内容，选择关联板块，关联楼盘，同步到圈子，点击“发布”按钮
        """
        self.page.get_element('textarea[class="tip"]').input("测试帖子标题")
        self.delay(1)
        self.page.get_element('textarea[class="tip_tiezi"]').input("输入帖子内容")
        self.delay(1)
        e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]')
        e1.tap()
        self.delay(3)
        e2 = self.page.get_element('view[class="quick-add quick-addto3 quick-color3"]')
        e2.tap()
        self.delay(1)
        e3 = self.page.get_element('view[class="close_box"]')
        e3.tap()
        self.delay(1)
        e4 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
        e4.tap()
        self.delay(1)
        e5 = self.page.get_element('input[class="searchTR-input"]')
        e5.input("山海国际")
        self.delay(2)
        e6 = self.page.get_element('view[class="search_txt"]')
        e6.tap()
        self.delay(3)
        e7 = self.page.get_element('view[class="quick-add quick-addto2 quick-color2"][data-index="1"]', inner_text="添加")
        e7.tap()
        self.delay(1)
        e8 = self.page.get_element('view[class="close_box"]')
        e8.tap()
        self.delay(1)
        e9 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]')
        e9.tap()
        self.delay(1)
        e10 = self.page.get_element('input[class="searchTR-input"]')
        e10.input("圈子")
        self.delay(1)
        e11 = self.page.get_element('view[class="search_txt"]')
        e11.tap()
        self.delay(3)
        e12 = self.page.get_element('view[class="quick-add quick-addto1 quick-color1"][data-index="1"]', inner_text="添加")
        e12.tap()
        self.delay(1)
        self.page.get_element('view[class="close_box"]').tap()
        self.delay(1)
        e14 = self.page.get_element('button[class="submit-btn"]')
        e14.tap()