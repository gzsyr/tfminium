# add by yfl
import minium

from test.common import delay


class TestNewsHouseList(minium.MiniTest):
    """
    新房列表页面
    """

    def setUp(self) -> None:
        self.app.switch_tab('/page/newHouseList/newHouseList')
        # page = self.app.get_current_page()
        delay(2)
        try:
            cls = self.page.get_element('view[class="ads_mask-close"]')
            cls.tap()
            print("关闭弹窗广告")
        except minium.MiniElementNotFoundError:
            print("无弹窗广告")
        print("test  setup!!!!!!!!!!!!!")

    def test_click_search(self):
        """
        点击搜索框
        :return:
        """
        ele = self.page.get_element('view[class="search-input"]')
        ele.tap()
        print("search: ", ele)
        delay(2)

    # def test_search_result(self):
    #     """
    #     点击搜索框->搜索万科未来城
    #     :return:
    #     """
    #     ele = self.page.get_element('view[class="search-input"]')
    #     ele.tap()
    #     ele2 = self.page.get_element("input")
    #     ele2.tap()
    #     delay(2)
    #     self.native.input_text("万科未来城")
    #     delay(2)
    #     ele3 = self.page.get_element('view[class="searchBLi-l"]', text_contains='万科未来城')
    #     ele3.tap()
    #     print("search: ", ele)
    #     delay(2)

    def test_click_map(self):
        """
        点击地图
        :return:
        """
        ele = self.page.get_element('navigator[class="search-map"]')
        ele.tap()
        print("map: ", ele)
        delay(2)

    def test_click_ads(self):
        """
        点击广告
        :return:
        """
        ele = self.page.get_element('image[class="bannerTwo-img index_banner"]')
        ele.tap()
        print("ads: ", ele)
        delay(2)

    def test_click_yldc(self):
        """
        点击热门楼盘
        :return:
        """
        ele = self.page.get_element('view[class="newHouseIconEnterLi xflb_rmlp"]')
        ele.tap()
        print("rmlp: ", ele)
        delay(2)

    def test_click_bnzf(self):
        """
        点击帮你找房
        :return:
        """
        ele = self.page.get_element('view[class="newHouseIconEnterLi xflb_bnzf"]')
        ele.tap()
        print("bnzf: ", ele)
        delay(2)

    def test_click_vrkf(self):
        """
        点击VR看房
        :return:
        """
        ele = self.page.get_element('view[class="newHouseIconEnterLi xflb_vrkf"]')
        ele.tap()
        print("vrkf: ", ele)
        delay(2)

    def test_click_kft(self):
        """
        点击看房团
        :return:
        """
        ele = self.page.get_element('view[class="newHouseIconEnterLi xflb_kft"]')
        ele.tap()
        print("kft: ", ele)
        delay(2)

    def test_click_dgli1(self):
        """
        点击导购模块1
        :return:
        """
        ele = self.page.get_element('view[class="disflex tfAlignC newHouseDgLi xflb_dg1"]')
        ele.tap()
        print("dgLi1: ", ele)
        delay(2)

    def test_click_dgli2(self):
        """
        点击导购模块2
        :return:
        """
        ele = self.page.get_element('view[class="disflex tfAlignC newHouseDgLi xflb_dg2"]')
        ele.tap()
        print("dgLi2: ", ele)
        delay(2)

    def test_click_dgli3(self):
        """
        点击导购模块3
        :return:
        """
        ele = self.page.get_element('view[class="disflex tfAlignC newHouseDgLi xflb_dg3"]')
        ele.tap()
        print("dgLi3: ", ele)
        delay(2)

    def test_click_dgli4(self):
        """
        点击导购模块4
        :return:
        """
        ele = self.page.get_element('view[class="disflex tfAlignC newHouseDgLi xflb_dg4"]')
        ele.tap()
        print("dgLi4: ", ele)
        delay(2)

    def test_click_zx(self):
        """
        点击咨询
        :return:
        """
        ele = self.page.get_element('view[class="newHouseRfixed-wyzx xflb_fx"]')
        ele.tap()
        print("zx: ", ele)
        delay(2)

    def test_click_housedetail(self):
        """
        进入新房详情页
        :return:
        """
        ele = self.page.get_elements('view[class="tfFlex xflb_lp disflex-flexwrap-nowrap"]')
        ele[0].tap()
        print("goto_housedetail: ", ele)
        delay(4)

    def test_show_wz(self):
        """
        展开位置筛选
        :return:
        """
        ele = self.page.get_element("view", inner_text="位置")
        ele.tap()
        print("wz: ", ele)
        delay(2)

    def test_show_jg(self):
        """
        展开价格筛选
        :return:
        """
        ele = self.page.get_element("view", inner_text="价格")
        ele.tap()
        print("jg: ", ele)
        delay(2)

    def test_show_hx(self):
        """
        展开户型筛选
        :return:
        """
        ele = self.page.get_element("view", inner_text="户型")
        ele.tap()
        print("hx: ", ele)
        delay(2)

    def test_show_sx(self):
        """
        展开筛选
        :return:
        """
        ele = self.page.get_element("view", inner_text="筛选")
        ele.tap()
        print("sx: ", ele)
        delay(2)

    def test_show_px(self):
        """
        展开排序
        :return:
        """
        ele = self.page.get_element("view", inner_text="排序")
        ele.tap()
        print("px: ", ele)
        delay(2)

    def test_select_wz(self):
        """
        筛选鼓楼区
        :return:
        """
        ele = self.page.get_element("view", inner_text="位置")
        ele.tap()
        ele1 = self.page.get_element("view", inner_text="区域")
        ele1.tap()
        ele2 = self.page.get_element("view", inner_text="鼓楼区")
        ele2.tap()
        print("select_wz: ", ele2)
        delay(2)

    def test_select_jg(self):
        """
        筛选25000-3000元
        :return:
        """
        ele = self.page.get_element("view", inner_text="价格")
        ele.tap()
        ele1 = self.page.get_element("view", inner_text="25000-30000元/㎡")
        ele1.tap()
        print("select_wz: ", ele1)
        delay(2)

    def test_select_hx(self):
        """
        筛选二室
        :return:
        """
        ele = self.page.get_element("view", inner_text="户型")
        ele.tap()
        ele1 = self.page.get_element("view", inner_text="二室")
        ele1.tap()
        print("select_hx: ", ele1)
        delay(2)

    def test_select_sx(self):
        """
        筛选
        :return:
        """
        self.page.get_element("view", inner_text="筛选").tap()
        self.page.get_element("view", inner_text="品牌房企").tap()
        self.page.get_element("view", inner_text="住宅").tap()
        self.page.get_element("view", inner_text="80-100㎡").tap()
        self.page.get_element("view", inner_text="六月内开盘").tap()
        self.page.get_element("view", inner_text="精装修").tap()
        ele = self.page.get_element('view[class="newHouseMaskLi-sx-btn-confirm"]')
        ele.tap()
        print("select_sx: ", ele)
        delay(2)

    def test_select_px(self):
        """
        筛选排序
        :return:
        """
        ele = self.page.get_element("view", inner_text="排序")
        ele.tap()
        ele1 = self.page.get_element("view", inner_text="开盘时间由近到远")
        ele1.tap()
        print("select_px: ", ele1)
        delay(2)

    def test_z_click_fx(self):
        """
        点击分享
        :return:
        """
        ele = self.page.get_element('button[class="newHouseRfixed-share xfxq_fx"]')
        ele.tap()
        print("fx: ", ele)
        delay(2)
        # self.native.forward_miniprogram_inside("虚拟好友")
