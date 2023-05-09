import time

from ddt import ddt, file_data

from base.test_base import TestBase


@ddt
class TestNewhouseDianping(TestBase):
    """
    楼盘点评页面
    """
    def setUp(self) -> None:
        self.page_name = '/page/taofangquan/lpdp/lpdp?pinyin=shanhaiguojixzl&city=qz'
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestNewhouseDianping, self).setUp()

    def test_click_IM_在线咨询(self):
        """
        V6.21.X: 1003947   楼盘点评页，点击咨询
        """
        self.page.get_element('view[class="consultEntrance--consultBtn"]').tap()

        self.delay(3)
        self.get_screenshot()

    def test_click_first_pinglun_点击评论(self):
        """
        楼盘点评页面，点击第一条点评
        """
        self.page.get_element('navigator[class="commentList--content-rich-text"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_click_lpquanzi_楼盘圈子(self):
        """
        楼盘点评页面，点击楼盘圈子，进入圈子详情页
        """
        self.page.get_element('view[class="qzwrap"]').tap()

        self.verifyPageName('/page/taofangquan/huati/huatiDetail')
        self.get_screenshot()

    def test_click_hot_post_热点聚集(self):
        """
        楼盘点评页面，点击综合评分下面的热点聚焦，进入帖子详情页
        """
        self.page.get_element('view[class="toutiao-swiper-item tfLine1"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    def test_submit_pinglun_存入草稿(self):
        """
        楼盘点评页面，点击评论入口，在评论页面，写入内容后，保存草稿
        """
        # 点击进入写点评页面
        self.page.get_element('view[class="detail-fix-input"]').tap()
        self.app.wait_for_page('/page/taofangquan/writePingjia/writePingjia')

        # 输入评论内容
        self.page.get_element('textarea[class="tip_pl"]').input('输入草稿内容' + time.strftime('%Y-%m-%d--%H:%M:%S'))
        # 点击 保存草稿
        self.page.get_element('image[class="save_draft"]').tap()

        self.get_screenshot()

    @file_data('./test_newhouse_dianping.yml')
    def test_submit_pinglun_发布评论(self, **kwargs):
        """
        楼盘点评页面，点击评论入口，在评论页面，发布评论
        """
        # 点击进入写点评页面
        self.page.get_element('view[class="detail-fix-input"]').tap()
        self.app.wait_for_page('/page/taofangquan/writePingjia/writePingjia')

        # 输入评论内容
        # 如果此处修改，需要同步修改 test_jjr_ctiezi_帖子相关.py
        self.page.get_element('textarea[class="tip_pl"]').input(kwargs['content'])

        # 如果存在“关联用户”先点击
        try:
            self.page.get_element('view[data-index="0"]', inner_text='关联用户').tap()
            if kwargs['mj']:
                # 运营账号，请选择马甲
                self.page.get_element('view[class="content"]', text_contains='请选择').tap()
                # 输入昵称搜索
                self.page.get_element('input[placeholder="请输入搜索昵称"]').input(kwargs['mj'])
                self.page.get_element('view[class="search-btn"]', inner_text='搜索').tap()
                self.delay(1)
                # 点击搜索结果列表第一个
                try:
                    self.page.get_element('view[class="item tfLine1"][data-index="0"]').tap()
                except:
                    self.page.get_element('view[class="close"]').tap()

        except:
            print('非运营账号，无关联用户')

        # 当前身份是房博士、置业顾问，点击评论类型即可
        try:
            self.page.get_element('view[class="item"]', inner_text=kwargs['type']).tap()

        except:
            print('非置业顾问/房博士账号')

        # 以下评价 亮星(C端+运营账号，可亮星）
        # 点亮综合评价
        # 如果此处修改，需要同步修改 test_jjr_ctiezi_帖子相关.py
        try:
            zhpj = kwargs['zhpj']
            self.page.get_element(f'view[data-type="multiple-score"][data-index="{zhpj}"]').tap()
            # 点亮价格
            jg = kwargs['jg']
            self.page.get_element(f'view[data-idx="0"][data-type="subitem-score"][data-index="{jg}"]').tap()
            # 点亮地段
            dd = kwargs['dd']
            self.page.get_element(f'view[data-idx="1"][data-type="subitem-score"][data-index="{dd}"]').tap()
            # 点亮交通
            jt = kwargs['jt']
            self.page.get_element(f'view[data-idx="2"][data-type="subitem-score"][data-index="{jt}"]').tap()
            # 点亮配套
            pt = kwargs['pt']
            self.page.get_element(f'view[data-idx="3"][data-type="subitem-score"][data-index="{pt}"]').tap()
            # 点亮环境
            hj = kwargs['hj']
            self.page.get_element(f'view[data-idx="4"][data-type="subitem-score"][data-index="{hj}"]').tap()
        except:
            print('无需点亮小星星')

        # 点击“提交”按钮
        tap = 'self.page.get_element(\'button[class="submit-btn"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '提交楼盘评论ok')
        self.get_screenshot()

    def test_click_first_dianzan_点赞评论(self):
        """
        楼盘点评页面，点击第一条评论的点赞按钮
        """
        tap = 'self.page.get_element(\'view[class="commentList--laud-btn"]\').tap()'
        self.verifyStr(True, self.getShowToast(tap), '点赞成功')
        self.get_screenshot()

    def test_click_first_reply_点击评论回复(self):
        """
        楼盘点评页面，点击第一条评论的回复按钮
        """
        self.page.get_element('view[class="commentList--tiezi-replay-btn"]').tap()

        self.verifyPageName('/page/taofangquan/tieziDetail/tieziDetail')
        self.get_screenshot()

    # V6.21.X: 已删除
    # def test_z_click_call_拨打电话(self):
    #     """
    #     楼盘点评页面，点击“致电淘房顾问”
    #     """
    #     self.page.wait_for('view[class="call"]')
    #     self.page.get_element('view[class="call"]').tap()
    #     self.delay(1)
    #     self.verifyByScreenshot('xf/call.png')

    def test_z_click_share_分享(self):
        """
        楼盘点评页面，点击“分享”
        """
        self.page.get_element('button[class="detail-fix-share"]').tap()

        self.get_screenshot()