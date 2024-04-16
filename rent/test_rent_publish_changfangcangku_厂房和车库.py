from ddt import ddt, file_data
from base.test_base import TestBase

from rent.rent_content import ZufangContent
import pyautogui
import pyperclip
@ddt
class Testrentchangfangcangku(ZufangContent):
    """
    厂房仓库发布
    """
    def setUp(self, true=None) -> None:
        self.page_name = "/esf/village/publish/index/index?publishType=rent&city=nj"
        self.switch = true
        self.classname = self.__class__.__name__
        super(Testrentchangfangcangku, self).setUp()
        print("Testrentchangfangcangku setup")

    @file_data('./test_rent_changfangcangku.yml')
    def test_publish_厂房仓库_发布厂房仓库和车库车位(self, **kwargs):
        """
        发布厂房仓库和车库车位
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

    def rent_content(self, kwargs):
        """
        填写厂房仓库和车库车位发布内容
        :return:
        """
        # 小区名称
        self.set_xqmc(kwargs['xqmc'])
        # 朝向
        self.set_chaoxiang(kwargs['chaoxiang'])
        # 楼层
        self.set_louceng(kwargs['louceng'])
        # 楼栋号
        self.set_loudonghao(kwargs['loudong'], ckcwloudong=kwargs['ckcwloudong'])
        # 单元号
        self.set_danyuan(kwargs['danyuan'], ckcwdanyuan=kwargs['ckcwdanyuan'])
        # 室号
        self.set_shihao(kwargs['shi'], ckcwshi=kwargs['ckcwshi'])
        # 面积
        self.set_area(kwargs['area'])
        # 租金
        self.set_price(kwargs['price'])
        # self.get_screenshot()
        self.delay(3)
        # 下一步
        self.set_xiayibu()
        # 房源标题
        self.set_title(kwargs['title'])
        # 房源描述
        self.set_desc(kwargs['fyms'])
        # 联系人
        self.set_cfckname(kwargs['name'])
        # 房屋权属信息-去认证
        self.set_renzheng(kwargs['zjlx'], kwargs['zjhm'], kwargs['qqh'], kwargs['cqrxm'], kwargs['cqrsfzh'])

        # 上传图片
        self.set_img()

        self.get_screenshot()
        self.delay(3)
        # 发布
        self.set_fabu()
        self.get_screenshot()