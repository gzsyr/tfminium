# -*-coding:utf-8-*-
import minium

from tfq.writepost import WritePost


class TestJJRTiezi(WritePost):
    """
    经纪人身份  帖子相关内容
    包括：发帖，评论，等最后删除帖子
    """
    @classmethod
    def setUpClass(cls) -> None:
        super(TestJJRTiezi, cls).setUpClass()
        cls().change_jjr()
        print("setupclass change_zygw")

    post_page = None

    def setUp(self) -> None:
        if self.post_page is None:
            self.page_name = '/page/taofangquan/writePost/writePost?city=nj'
            # self.page_name = f"/page/taofangquan/tieziDetail/tieziDetail?city=nj&postsid={self.jjr_postid}"
        else:
            self.page_name = self.post_page
        # self.page_name = f"/page/taofangquan/tieziDetail/tieziDetail?city=nj&postsid={self.jjr_postid}"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestJJRTiezi, self).setUp()

    def test_000_素材库生成帖子(self):
        """
        V6.38.x: 点击 素材库，带入素材库内容
        """
        self.click_sucaiku()

        try:
            self.select_sucaiku()
            self.verifyPageName('/page/taofangquan/writePost/writePost')
        except minium.MiniElementNotFoundError:
            print('没有内容库')

        self.get_screenshot()

    def test_000_素材库查看详情(self):
        """
        V6.38.X: 点击 素材库，选择”查看详情“进入素材内容，点击”一键生成“帖子
        """
        self.click_sucaiku()

        try:
            self.select_sucaiku()
            self.review_sucaiku()
            self.output_sucaiku()
            self.verifyPageName('/page/taofangquan/writePost/writePost')
        except:
            print('没有素材库')

        self.get_screenshot()

    def test_000_点击素材内容正文(self):
        """
        V6.38.X: 点击素材库页面的，素材正文
        """
        self.click_sucaiku()

        try:
            self.content_sucaiku()
            self.verifyPageName('/page/taofangquan/contentstore/storedetail')
        except:
            print('没有素材库')

        self.get_screenshot()

    def test_001_写帖子(self):
        """
        经纪人身份，发帖页面，输入标题，内容，选择关联板块，关联楼盘，同步到圈子，点击“发布”按钮
        """
        self.wp_input_title('一季度的江北核心区成交价是“涨”还是“降”？'). \
            wp_input_content('春节后的楼市回暖了，不少业主更有底气的调高了挂牌价'
                             '，成交量也上涨了……那么，到底量价齐升还是以交换量？'
                             '近期在摸底南京次新小区的房价，需要数据的可以关注～')

        self.wp_choose_quanzi('购房指南')
        self.wp_choose_quanzi('购房问答')
        self.get_screenshot('加入3个圈子')
        self.wp_close_quanzi()

        self.get_screenshot()
        TestJJRTiezi.post_page = f"/page/taofangquan/tieziDetail/tieziDetail?city=nj&postsid={self.jjr_postid}"

    def test_002_点击经纪人头像(self):
        """
        点击经纪人头像，跳转经纪人的房源店铺
        """
        self.find_element('image[class="avatar"]').tap()
        self.delay(2)

        self.get_screenshot()
        self.verifyPageName('/esf/sell/pages/broker/broker')

    def test_003_点击经纪人咨询(self):
        """
        点击经纪人咨询icon，进入im页面
        """
        self.find_element('view[class="connect fbs_contact_tap"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

    def test_004_点击经纪人店铺(self):
        """
        点击经纪人店铺，进入经纪人店铺
        """
        try:
            self.find_element('view[class="jjr_shop"]').tap()
            self.delay(2)

            self.get_screenshot()
            self.verifyPageName('/esf/sell/pages/broker/broker')

        except minium.MiniElementNotFoundError:
            print('该经纪人没有关联店铺')

    def test_005_点击经纪人房源(self):
        """
        点击经纪人发布的房源，进入房源详情页
        """
        try:
            self.find_element('view[class="sellItem--flex sellItem--sellItem"]').tap()

            self.delay(2)

            self.get_screenshot()
            self.verifyPageName('/esf/sell/pages/detail/detail')
        except minium.MiniElementNotFoundError:
            print('该经纪人无发布房源')

    def test_006_点击房源套数(self):
        """
        点击经纪人房源下方的套数，进入经纪人店铺
        """
        try:
            self.find_element('view[class="flex tfAlignC totalCount"]').tap()

            self.delay(2)

            self.get_screenshot()
            self.verifyPageName('/esf/sell/pages/broker/broker')
        except minium.MiniElementNotFoundError:
            print('该经纪人无发布房源')

    def test_007_点击底部经纪人咨询(self):
        """
        点击底部经纪人咨询，进入im
        """
        self.find_element('image[class="bottom-connect-avatar"]').tap()

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

    def test_008_点击推荐二手房(self):
        """
        点击推荐二手房，进入房源详情
        """
        self.page.scroll_to(2600, 200)
        self.delay(2)
        # 切换到二手房
        self.find_element('view[class="flex recommend_tab"]/view[data-index="2"]').tap()
        # self.find_element('view[class="tab"][data-index="2"]').tap()
        self.delay(1)
        # 点击小区
        self.find_element('view[class="villageItem--flex villageItem--village_item_wrapper"]').tap()
        self.delay(3)

        self.get_screenshot()
        self.verifyPageName('/esf/village/pages/detail/detail')

    def test_009_点击推荐二手房咨询(self):
        """
        点击推荐二手房咨询，进入IM
        """
        self.page.scroll_to(2600, 200)
        self.delay(2)
        # 切换到二手房
        # self.find_element('view[class="tab"][data-index="2"]').tap()
        self.find_element('view[class="flex recommend_tab"]/view[data-index="2"]').tap()
        self.delay(2)
        # 点击IM咨询
        self.find_element('view[class="villageItem--center villageItem--chat"]').tap()
        self.delay(3)

        self.get_screenshot()
        self.verifyPageName('/im/pages/chating/chating')

    def test_010_输入帖子评论内容(self):
        """
        回复帖子，评论不提交
        """
        self.find_element('view[class="post_cont"]').tap()
        self.find_element('textarea[name="quick_reply_content"][placeholder="说点什么吧"]'). \
            input('经纪人输入的内容')

        self.get_screenshot()

    def test_011_写楼盘评论(self):
        """
        写楼盘评论，不提交
        """
        page_name = '/page/taofangquan/writePingjia/writePingjia' \
                    '?city=nj&pinyin=huarunguojishequ&pid=0&h_name=华润国际社区'
        self.redirect_to_page(url='/page/taofangquan/writePingjia/writePingjia',
                              params={"city": "nj", "pinyin": "huarunguojishequ",
                                      "pid": "0", "h_name": "华润国际社区"}
                              )

        self.find_element('textarea[class="tip_pl"]').input('自动化测试忽略-这是经纪人的评价')
        self.find_element('view[data-type="multiple-score"][data-index="4"]').tap()

        self.get_screenshot()
