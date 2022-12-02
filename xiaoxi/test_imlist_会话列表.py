from ddt import ddt, file_data

from tfq.writepost import WritePost

@ddt
class TestXiaoxiImtest(WritePost):
    """
    IM会话列表
    """
    # @classmethod
    # def setUpClass(cls) -> None:
    #     super(TestXiaoxiImtest, cls).setUpClass()
    #     cls().change_zygw()
    #     print("setupclass")

    def setUp(self) -> None:
        self.page_name = "/im/pages/recentchat/recentchat?city=qz"
        self.switch = False
        self.classname = self.__class__.__name__
        super(TestXiaoxiImtest, self).setUp()
        print("TestZygwWritePost setup")

    def test_01_quguanzhu_去关注(self):
        # 点击去关注
        self.page.get_element('image[class="gzImg"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_02_jiaruheimingdan_黑名单(self):
        # 点击列表...加入黑名单
        try:
            self.page.get_element('view[class="recentchat-item-ico"]').get_element('image').tap()
            self.delay(3)
            result = {"confirm": True}
            self.app.mock_wx_method("showModal", result=result)
            self.page.get_element('view[class="swiperlahei-btn"]').tap()
            self.app.restore_wx_method("showModal")
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有会话列表')

    def test_03_heimingdan_黑名单(self):
        # 点击黑名单
        e = self.page.get_elements('view[class="t_tabitem flex tfAlignC"]')
        e[2].tap()
        self.delay(3)
        # 点击移除
        try:
            self.page.get_element('view[class="removeBlack"]').tap()
            self.delay(2)
            self.get_screenshot()
        except:
            print('没有黑名单列表')

    def test_04_weiduhuihua_只看未读会话(self):
        # 点击只看未读会话
        e = self.page.get_elements('view[class="t_tabitem flex tfAlignC"]')
        e[1].tap()
        self.delay(3)
        self.get_screenshot()

    def test_05_quanbuyidu_全部已读(self):
        # 点击全部已读
        e = self.page.get_elements('view[class="t_tabitem flex tfAlignC"]')
        e[0].tap()
        self.delay(3)
        # 点击只看未读会话
        e[1].tap()
        self.delay(3)
        self.get_screenshot()

    def test_06_xitongxiaoxi_系统消息(self):
        # 点击系统消息
        e = self.page.get_elements('view[class="tabBox"]')
        e[0].tap()
        self.delay(3)
        self.get_screenshot()

    def test_07_dianzan_点赞(self):
        # 点击点赞
        e = self.page.get_elements('view[class="tabBox"]')
        e[1].tap()
        self.delay(3)
        # 点击查看详情
        try:
            e1 = self.page.get_elements('view[class="go-detail"]')
            e1[0].tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有点赞列表')

    def test_08_pinglunhuifu_评论和回复(self):
        # 点击评论和回复
        e = self.page.get_elements('view[class="tabBox"]')
        e[2].tap()
        self.delay(3)
        # 点击查看详情
        try:
            e1 = self.page.get_elements('view[class="go-detail"]')
            e1[0].tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有评论和回复列表')

    def test_09_yaoqingpinglun_邀请评论(self):
        # 点击邀请评论
        e = self.page.get_elements('view[class="tabBox"]')
        e[3].tap()
        self.delay(3)
        # 点击查看详情
        try:
            e1 = self.page.get_elements('view[class="go-detail"]')
            e1[0].tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有邀请评论列表')

    def test_10_guanfangtongzhi_官方通知(self):
        # 点击官方通知
        try:
            e = self.page.get_element('view[class="recentchat-item isTop"]')
            e.tap()
            self.delay(3)
            # 点击查看详情
            e1 = self.page.get_elements('view[class="go-detail"]')
            e1[0].tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有官方通知')

    def test_11_taofangquan_淘房圈消息tab切换(self):
        # 点击点赞
        e = self.page.get_elements('view[class="tabBox"]')
        e[1].tap()
        self.delay(3)
        # 淘房圈消息页4个tab切换
        e1 = self.page.get_elements('view[class="tabItem"]')
        e1[0].tap()
        self.delay(3)
        e2 = self.page.get_elements('view[class="tabItem"]')
        e2[1].tap()
        self.delay(3)
        try:
            e3 = self.page.get_elements('view[class="tabItem"]')
            e3[2].tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有官方通知')
        e4 = self.page.get_elements('view[class="tabItem"]')
        e4[0].tap()
        self.delay(3)

    def test_12_zhiding_置顶(self):
        # 点击列表...置顶
        try:
            self.page.get_element('view[class="recentchat-item-ico"]').get_element('image').tap()
            self.delay(3)
            self.page.get_element('view[class="swipertop-btn"]').tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有会话列表')

    def test_13_quxiaozhiding_取消置顶(self):
        # 点击列表...取消置顶
        try:
            self.page.get_element('view[class="recentchat-item-ico"]').get_element('image').tap()
            self.delay(3)
            self.page.get_element('view[class="swipertop-btn"]').tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有会话列表')

    def test_14_cklishi_查看更多历史会话(self):
        # 点击查看更多历史会话消息
        self.page.scroll_to(950, 500)
        self.delay(1)
        self.page.get_element('view[class="historychat flex tfAlignC"]').tap()
        self.delay(3)
        self.get_screenshot()

    def test_15_dianjilishihuihua_点击历史会话(self):
        # 点击查看更多历史会话消息第一条
        self.page.scroll_to(950, 500)
        self.delay(1)
        self.page.get_element('view[class="historychat flex tfAlignC"]').tap()
        self.delay(3)
        try:
            e = self.page.get_elements('view[class="item flex tfAlignC"]')
            e[0].tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有历史会话消息')

    def test_16_clicklist_点击会话列表(self):
        # 点击会话列表进入详情页
        try:
            e = self.page.get_elements('view[class="recentchat-item-ico"]')
            e[0].tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('会话列表为空')

    def test_17_clickdele_点击删除(self):
        # 点击列表...加入删除
        try:
            self.page.get_element('view[class="recentchat-item-ico"]').get_element('image').tap()
            self.delay(3)
            self.page.get_element('view[class="swipedelete-btn"]').tap()
            self.delay(3)
            self.get_screenshot()
        except:
            print('没有会话列表')

