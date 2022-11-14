from ddt import ddt, file_data
from base.test_base import TestBase

from rent.rent_content import ZufangContent
import pyautogui
import pyperclip
@ddt
class Testrentshangpu(ZufangContent):
    """
    商铺发布
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/publish/index/index?publishType=rent&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentshangpu, self).setUp()
        print("Testrentshangpu setup")

    @file_data('./test_rent_shangpu.yml')
    def test_publish_商铺_发布商铺(self, **kwargs):
        """
        发布商铺
        :param kwargs:
        :return:
        """
        self.page.get_element(f'view[class="between houseType"][data-type="{kwargs["datatype"]}"]').tap()
        self.delay(3)
        # 重置
        self.set_result()
        # 输入内容
        self.rent_content(kwargs)
        self.delay(3)
        self.get_screenshot()
        self.delay(3)

    def rent_content(self, kwargs):
        """
        填写商铺发布内容
        :return:
        """
        # 上传图片
        self.set_img()
        # 小区名称
        self.set_xqmc(kwargs['xqmc'])
        # 商铺性质
        self.set_spxz(kwargs['spxz'])
        # 商铺类型
        self.set_splx(kwargs['splx'])
        # 楼层
        self.set_louceng(kwargs['louceng'])
        # 楼栋号
        self.set_loudonghao(kwargs['loudong'])
        # 单元号
        self.set_danyuan(kwargs['danyuan'])
        # 室号
        self.set_shihao(kwargs['shi'])
        # 面积
        self.set_area(kwargs['area'])
        # 租金
        self.set_price(kwargs['price'])
        # 转让费
        self.set_zhuanrangfei(kwargs['zhuanrangfei'])
        # 物业费
        self.set_wuyefei(kwargs['wuyefei'])
        # 装修
        self.set_zhuangxiu(kwargs['zhuangxiu'])
        # 临街
        self.set_linjie(kwargs['linjie'])
        # self.get_screenshot()
        self.delay(3)
        # 下一步
        self.set_xiayibu()
        # 房源标题
        self.set_title(kwargs['title'])
        # 房屋配置
        self.set_spfwpz()
        # 房源描述
        self.set_desc(kwargs['fyms'])
        # 联系人
        self.set_name(kwargs['name'])
        # 房屋权属信息-去认证
        self.set_renzheng(kwargs['zjlx'], kwargs['zjhm'], kwargs['qqh'], kwargs['cqrxm'], kwargs['cqrsfzh'])
        self.get_screenshot()
        self.delay(3)
        # 发布
        self.set_fabu()
        self.get_screenshot()
        self.delay(3)