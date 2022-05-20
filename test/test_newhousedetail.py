import threading

import minium

from test.common import delay


class TestKFT(minium.MiniTest):
    """
    新房详情页页面
    """
    def setUp(self) -> None:
        self.app.navigate_to('/page/newhouse/detail?pinyin=shanhaiguojixzl&city=qz')
        page = self.app.get_current_page()
        print("test  setup!!!!!!!!!!!!!")
        delay(2)

    def test_goto_photo(self):
        """
        点击相册
        :return:
        """
        ele = self.page.get_element("image[class='newHouseBanner-img xfxq_xc']")
        ele.tap()
        delay(2)

    def test_goto_pk(self):
        """
        点击PK
        :return:
        """
        ele = self.page.get_element("navigator[class='pk-icon']")
        ele.tap()
        delay(2)

    def test_goto_dy(self):
        """
        点击订阅（爱心按钮）
        :return:
        """
        ele = self.page.get_element("view[class='dy-icon']")
        ele.tap()
        delay(2)

    def test_goto_fdjsq(self):
        """
        点击房贷计算器
        :return:
        """
        ele = self.page.get_element("view[class='newHouseInfor-price-r xfxq_jsq']")
        ele.tap()
        delay(2)

    def test_goto_addr(self):
        """
        点击地址右箭头
        :return:
        """
        ele = self.page.get_element("view[class='newHouseInfor-add-r']")
        ele.tap()
        delay(2)

    def test_goto_lpdp_gd(self):
        """
        点击楼盘点评滚动处
        :return:
        """
        ele = self.page.get_element("view[class='tfFlex tfFlexSb tfAlignC dpEntry']")
        ele.tap()
        delay(2)

    def test_goto_zxdt(self):
        """
        点击最新动态
        :return:
        """
        ele = self.page.get_element("view[class='newHouseIconInLi-b']", inner_text="最新动态")
        ele.tap()
        delay(2)

    def test_goto_hxjx(self):
        """
        点击户型解析
        :return:
        """
        ele = self.page.get_element("view[class='newHouseIconInLi-b']", inner_text="户型解析")
        ele.tap()
        delay(2)

    def test_goto_lpxq(self):
        """
        点击楼盘详情
        :return:
        """
        ele = self.page.get_element("view[class='newHouseIconInLi-b']", inner_text="楼盘详情")
        ele.tap()
        delay(2)

    def test_goto_yfyj(self):
        """
        点击一房一价
        :return:
        """
        ele = self.page.get_element("view[class='newHouseIconInLi-b']", inner_text="一房一价")
        ele.tap()
        delay(2)

    def test_goto_lpdp(self):
        """
        点击楼盘点评
        :return:
        """
        ele = self.page.get_element("view[class='newHouseIconInLi-b']", inner_text="楼盘点评")
        ele.tap()
        delay(2)

    def test_goto_msbm(self):
        """
        点击马上报名
        :return:
        """
        ele = self.page.get_element("view[class='ggweiR']", inner_text="马上报名")
        ele.tap()
        delay(2)

    def test_goto_bmqc(self):
        """
        点击报名清册
        :return:
        """
        ele = self.page.get_element("view[class='left-icon disflex tfAlignC tfFlexC']")
        ele.tap()
        delay(2)

    def test_goto_bmxh(self):
        """
        点击报名序号
        :return:
        """
        ele = self.page.get_element("view[class='disflex tfAlignC xf_xh_title']")
        ele.tap()
        delay(2)

    def test_goto_bmyfyj(self):
        """
        点击最新摇号下方的一房一价
        :return:
        """
        ele = self.page.get_element("view[class='yifangyijia']")
        ele.tap()
        delay(2)

    def test_goto_bmgfzl(self):
        """
        点击最新摇号下方的购房资料
        :return:
        """
        ele = self.page.get_element("view[class='goufangziliao']")
        ele.tap()
        delay(2)

    def test_goto_lpdt_more(self):
        """
        点击楼盘动态更多
        :return:
        """
        ele = self.page.get_element("view[class='tfFlex tfFlexSb newHouseTitle-line xfxq_lpdt disflex-alignitems-center']")
        ele.tap()
        delay(2)

    def test_goto_xxxx_more(self):
        """
        点击楼盘详细信息
        :return:
        """
        ele = self.page.get_element("view[class='tfFlex tfFlexSb newHouseTitle-line xfxq_lpdt']")
        ele.tap()
        delay(2)

    def test_goto_wzzb_dt(self):
        """
        点击位置周边下的地图
        :return:
        """
        # self.page.scroll_to(2200, 500)
        # delay(2)
        # ele = self.page.get_element("view[class='newHouseMap-map-icon xfxq_wzdt']")
        # ele.tap()
        # delay(4)
        # self.native.map_back_to_mp()
        # delay(2)

        called = threading.Semaphore(0)
        callback_args = None

        def callback(args):
            nonlocal callback_args
            called.release()
            callback_args = args
        self.app.hook_wx_method("openLocation", callback=callback)
        self.page.get_element("view[class='newHouseMap-map-icon xfxq_wzdt']").tap()
        delay(1)
        # self.native.allow_get_location(True)  # 授权获取位置
        self.native.map_back_to_mp()  # 确认选择位置
        is_called = called.acquire(timeout=10)
        self.app.release_hook_wx_method("openLocation")
        delay(10)
        # self.native.