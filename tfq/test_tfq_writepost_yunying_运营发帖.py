# add by zsy
import threading
import time

from ddt import ddt, file_data

from base.test_base import TestBase
from tfq.writepost import WritePost


@ddt
class TestTfqYyWritePost(WritePost):
    """
    运营身份发帖
    """

    # 变更setupclass、setup内容
    @classmethod
    def setUpClass(cls) -> None:
        super(TestTfqYyWritePost, cls).setUpClass()
        cls().change_yy()
        print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/page/taofangquan/writePost/writePost?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestTfqYyWritePost, self).setUp()
        print("TestYyWritePost setup")

    def test_yy_05_write_pk_发布PK(self, **kwargs):
        """
        V6.26.X: 1004926, 运营，带pk插件，成功发帖
        """
        kwargs['title'] = 'PK插件'
        kwargs['content'] = '这是运营发布的含有PK插件帖子'
        self.wp_input_title(time.strftime('%Y-%m-%d') + kwargs['title']).wp_input_content(kwargs['content'])

        # 输入PK
        self.write_pk()
        self.wp_submit()

        self.goto_post_detail()
        self.delay(3)
        TestBase.pkhuatiid = self.page.query['postsid']
        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()


    @file_data('./test_tfq_writepost_yunying_vote.yml')
    def test_yy_04_write_vote_post_发布投票(self, **kwargs):
        """
        运营，发帖页面，输入标题，内容，新增投票，点击“发布”按钮
        """
        self.wp_input_title(time.strftime('%Y-%m-%d')+kwargs['title']).wp_input_content(kwargs['content'])

        # 输入投票
        self.yy_write_vote(title=time.strftime('%Y-%m-%d')+kwargs['votetitle'],
                           ipt=kwargs['votelist'],
                           ismultiple=kwargs['ismultiple'])
        self.wp_submit()

        self.goto_post_detail()
        self.delay(3)
        TestBase.huatiid = self.page.query['postsid']
        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    @file_data('./test_tfq_writepost_yunying.yml')
    def test_yy_03_write_vest_post_发布帖子(self, **kwargs):
        """
        运营，选择马甲发帖，输入标题、内容，选择关联板块、关联楼盘、同步到圈子，点击“发布”按钮
        """
        self.wp_input_title(kwargs['title']+time.strftime('%Y-%m-%d')).\
            wp_input_content(kwargs['content']).\
            yy_choose_vest(kwargs['vestname']).\
            wp_choose_bk().\
            wp_choose_lp(kwargs['lpname']).\
            wp_choose_quanzi(kwargs['quanzi'])

        # eval('self.yy_choose_'+'h5'+'()')
        self.wp_submit()

        self.goto_post_detail()
        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_yy_01_quanzi_show_my_fav_我关注的(self):
        """
        运营身份，发帖页面，点击同步到圈子，展示“我关注的”内容列表
        """

        self.wp_quanzi_show_my_fav()

        self.verifyByScreenshot('tfq/test_yy_quanzi_show_my_fav.png')

    def test_yy_02_save_draft_保存草稿(self):
        """
        运营身份，发帖页面，点击“保存草稿”按钮
        """
        self.wp_input_title('运营' + time.strftime('%Y-%m-%d--%H:%M:%S'))

        # 监听回调, 阻塞当前主线程
        called = threading.Semaphore(0)
        callback_args = None

        def callback(args):
            nonlocal callback_args
            called.release()
            callback_args = args

        self.app.hook_wx_method("showToast", callback=callback)
        self.find_element('view[class="save_draft_icon"]').tap()
        is_called = called.acquire(timeout=5)
        self.app.release_hook_wx_method("showToast")

        self.verifyStr(True, is_called, "toast called ")
        self.get_screenshot()


    #
    # # 以下是发帖页面元素
    # def goto_post_detail(self):
    #     """
    #     运营身份发帖完成后，发布成功页面，点击“查看发布详情”
    #     """
    #     e = self.page.get_element('navigator', inner_text='查看发布详情 >')
    #     print(e.outer_wxml)
    #     e.tap()
    #
    # def yy_submit(self):
    #     """
    #     运营身份，发帖页面，点击发布按钮
    #     """
    #     self.page.get_element('button[class="submit-btn"]').tap()
    #     self.delay(2)
    #
    # def yy_input_title(self, value='测试帖子标题'):
    #     """
    #     运营身份，发帖页面，输入标题
    #     """
    #     self.page.get_element('textarea[class="tip"]').input(value)
    #     self.delay(1)
    #     return self
    #
    # def yy_input_content(self, cont='输入帖子内容'):
    #     """
    #     运营身份，发帖页面，输入内容
    #     """
    #     self.page.get_element('textarea[class="tip_tiezi"]').input(cont)
    #     self.delay(1)
    #     return self
    #
    # def yy_chooseimage(self):
    #     """
    #     运营身份，发帖页面，点击上传图片按钮
    #     """
    #     self.page.get_element('view[class="upload-btn"]')
    #
    # def yy_click_bk(self):
    #     """
    #     运营身份，发帖页面，点击关联板块，弹出弹窗
    #     """
    #     e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]')
    #     e1.tap()
    #     self.delay(2)
    #
    # def yy_choose_bk(self):
    #     """
    #     运营身份，发帖页面，关联板块，选择板块
    #     """
    #     self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="3"]').tap()
    #     self.delay(2)
    #     self.page.get_element('view[data-index="0"]', inner_text='添加').tap()
    #     self.delay(1)
    #     self.page.get_element('view[class="close_box"]').tap()
    #     self.delay(1)
    #
    #     return self
    #
    # def yy_choose_lp(self, lpname='山海国际'):
    #     """
    #     运营身份，发帖页面，关联楼盘，选择楼盘,点击添加楼盘
    #     """
    #     self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]').tap()
    #     self.delay(1)
    #     self.page.get_element('input[class="searchTR-input"]').input(lpname)
    #     self.delay(1)
    #     self.page.get_element('view[class="search_txt"]').tap()
    #     self.delay(3)
    #     self.page.get_element('view[class="quick-add quick-addto2 quick-color2"][data-index="0"]', inner_text="添加").tap()
    #     self.delay(1)
    #     self.page.get_element('view[class="close_box"]').tap()
    #     self.delay(1)
    #
    #     return self
    #
    # def yy_change_esftab(self):
    #     """
    #     运营身份，发帖页面，关联楼盘，楼盘切换至二手房
    #     """
    #     e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
    #     e1.tap()
    #     self.delay(2)
    #     e2 = self.page.get_element('view[data-type="secondHouse"]', inner_text="二手房")
    #     e2.tap()
    #     self.delay(1)
    #
    # def yy_change_xftab(self):
    #     """
    #     运营身份，发帖页面，关联楼盘，楼盘切换至新房tab
    #    """
    #     e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="2"]')
    #     e1.tap()
    #     self.delay(1)
    #     e2 = self.page.get_element('view[data-type="newHouse"]', inner_text="新房")
    #     e2.tap()
    #
    # def yy_choose_quanzi(self, quanzi='圈子'):
    #     """
    #     运营身份，发帖页面，点击同步到圈子，输入圈子，搜索,添加圈子,点击右上角“确定”按钮
    #     """
    #     self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="1"]').tap()
    #     self.delay(1)
    #     self.page.get_element('input[class="searchTR-input"]').input(quanzi)
    #     self.page.get_element('view[class="search_txt"]').tap()
    #     self.delay(1)
    #     self.page.get_element('view[class="quick-add quick-addto1 quick-color1"][data-index="0"]', inner_text="添加").tap()
    #     self.delay(1)
    #     self.page.get_element('view[class="close_box"]').tap()
    #     self.delay(1)
    #
    #     return self
    #
    # def yy_click_link(self):
    #     """
    #     运营身份，发帖页面，点击链接入口
    #     """
    #     e1 = self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]')
    #     e1.tap()
    #     self.delay(2)
    #
    # def yy_choose_h5(self):
    #     """
    #     运营身份，发帖页面，链接选择h5
    #     """
    #     self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
    #     self.delay(1)
    #     self.page.get_element('radio[value="0"]').tap()
    #     self.delay(1)
    #     self.page.get_element('input[class="affiliateLink_input"]', inner_text="最多15个字").input("输入链接标题")
    #     self.delay(1)
    #     self.page.get_element('input[class="affiliateLink_input"]', inner_text="输入链接").input("https://m.house365.com")
    #     self.delay(1)
    #     self.page.get_element('view[class="upload-btn"]')
    #     self.delay(1)
    #
    # def yy_choose_nbxcx(self):
    #     """
    #     运营身份，发帖页面，链接选择内部小程序
    #     """
    #     self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
    #     self.delay(1)
    #     self.page.get_element('radio[value="1"]').tap()
    #     self.delay(1)
    #
    # def yy_choose_wbxcx(self):
    #     """
    #     运营身份，发帖页面，链接选择外部小程序,输入内容，选择“确定”
    #     """
    #     self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
    #     self.delay(1)
    #     self.page.get_element('radio[value="2"]').tap()
    #     self.delay(1)
    #     self.page.get_element('input[class="affiliateLink_input"]', inner_text="最多15个字").input("输入链接标题")
    #     self.delay(1)
    #     self.page.get_element('input[class="affiliateLink_input"]', inner_text="输入appId").input("wx437db912a2e4078e")
    #     self.delay(1)
    #     self.page.get_element('input[class="affiliateLink_input"]', inner_text="输入链接").input("/pages/index/index")
    #     self.delay(1)
    #     self.page.get_element('button[class="linkBtn"]').tap()
    #     self.delay(1)
    #
    # def yy_click_reset(self):
    #     """
    #     运营身份，发帖页面，链接选择h5，点击“重置”
    #     """
    #     self.page.get_element('view[class="tfFlex tfAlignC tfFlexSb tz_associate"][data-type="4"]').tap()
    #     self.delay(1)
    #     self.page.get_element('radio[value="0"]').tap()
    #     self.delay(1)
    #     self.page.get_element('input[class="affiliateLink_input"]', inner_text="最多15个字").input("输入链接标题")
    #     self.delay(1)
    #     self.page.get_element('button[class="linkBtn_plain"]')
    #     self.delay(1)
    #
    # def yy_choose_vest(self, name='马甲'):
    #     """
    #     运营身份，发帖页面，点击关联用户入口，进入选择马甲页面，输入“马甲”，搜索，选择第一个结果
    #     """
    #     self.page.get_element('view[class="associated_users_name tfLine1"]').tap()
    #     self.delay(1)
    #     self.page.get_element('input[placeholder="请输入搜索昵称"]').input(name)
    #     self.delay(1)
    #     self.page.get_element('view[class="search-btn"]').tap()
    #     self.delay(1)
    #     self.page.get_element('view[class="item tfLine1"][data-index="0"]').tap()
    #     self.delay(1)
    #
    #     return self
    #
    # def yy_write_vote(self, title='投票标题', ipt=None, ismultiple=False):
    #     """
    #     运营身份，发帖页面,填写投票，支持多选
    #     title: 投票标题
    #     ipt: 选项值，最大3个
    #     ismultiple: 是否多选
    #     """
    #     if ipt is None:
    #         ipt = ['选项一', '选项二', '选项三', '选项4', '选项5', '选项6', '选项7', '选项8', '选项9', '选项10'
    #                , '选项11', '选项12', '选项13']
    #
    #     b_l = self.page.element_is_exists('navigator[class="vote-button look"]')
    #     if b_l == True:
    #         self.page.get_element('navigator[class="vote-button look"]').tap()
    #         self.delay(2)
    #         self.page.get_element('button[class="submit"]').tap()
    #         self.delay(1)
    #     else:
    #         self.page.get_element('navigator[class="vote-button create"]').tap()
    #         self.delay(1)
    #         self.page.get_element('input[class="vote-title"]').input(title)
    #         self.delay(1)
    #
    #         for i in range(0, min(len(ipt), 12)):
    #             if i > 1:
    #                 self.page.get_element('view[class="add"]').tap()
    #                 self.delay(1)
    #             self.page.get_element(f'input[data-index="{i}"]').input(ipt[i])
    #             self.delay(1)
    #
    #         if ismultiple:
    #             self.page.get_element('switch[name="multiple"]').tap()
    #             self.delay(1)
    #         self.page.get_element('button[class="submit"]').tap()
    #         self.delay(1)
    #
    #     return self