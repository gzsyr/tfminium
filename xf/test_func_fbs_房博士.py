# add by zsy
import base64
import inspect
import time

from base.test_base import TestBase


class TestFuncFbs(TestBase):
    """
    房博士相关页面
    """
    def setUp(self) -> None:
        self.classname = self.__class__.__name__
        self.page_name = '/fbs/doctorList/doctorPage?id=313&city=qz'
        self.switch = False
        super(TestFuncFbs, self).setUp()
        print('TestFuncFbs setup test')

    def test_05_fbs_ask_and_submit_房博士页提问(self):
        """
        房博士页面，点击“向xxx提问”，提交问题“用例名称年-月-日”后，点击“提交”
        """
        self.click_ask().input_ask_content().ask_submit()

        # 校验
        self.verifyPageName('/fbs/detail/detail')
        self.get_screenshot()

    def test_07_fbs_to_shouye_房博士页回首页(self):
        """
        房博士页面，点击悬浮按钮“回到首页”
        """
        self.click_shouye()

        # 校验
        self.verifyPageName('/page/index/index')
        self.get_screenshot()

    def test_06_fbs_click_label_房博士页标签(self):
        """
        房博士页面，点击第一个问答的 标签
        """
        self.page.get_element('view[data-id="1"]').click()

        self.verifyPageName('/fbs/questionList/questionList')
        self.get_screenshot()

    def test_02_detail_click_label_问答详情标签(self):
        """
        房博士页面，点击第一个问答进入 问答详情，在问答详情页点击 标签
        """
        self.click_first_title()
        self.delay(1)
        self.detail_click_label()

        self.verifyPageName('/fbs/questionList/questionList')
        self.get_screenshot()

    def test_01_detail_ask_and_submit_提问(self):
        """
        房博士页面，点击热门问答列表第一个 进入问答详情，点击“向xx提问”并提交问题
        """
        self.click_first_title().detail_click_ask().input_ask_content()

        # self.upload_img()

        self.ask_submit()
        # 校验
        self.verifyPageName('/fbs/detail/detail')
        self.get_screenshot()

    def delete_04_detail_goto_shouye_问答详情回首页(self):
        """
        房博士页面，点击热门问答列表第一个 进入问答详情，点击“回首页”
        V6.32.X: 删除
        """
        self.click_first_title().click_shouye()

        # 校验
        self.verifyPageName('/page/index/index')
        self.get_screenshot()

    def test_03_detail_goto_newhouse_问答详情推荐楼盘(self):
        """
        房博士页面，点击热门问答列表第一个 进入问答详情，点击推荐楼盘列表第一个
        """
        self.click_first_title().detail_click_first_newhouse()

        # 校验
        self.verifyPageName('/page/newhouse/detail')
        self.get_screenshot()

    def test_08_z_detail_call_问答详情电话(self):
        """
        房博士页面，点击热门问答列表第一个 进入问答详情，推荐楼盘列表第一个，点击电话按钮
        """
        self.click_first_title().detail_click_call()

        self.verifyByScreenshot('xf/call.png')

    # 以下是房博士主页的元素点击
    def click_first_title(self):
        """
        房博士主页，点击，第一条问答，进入问答详情页
        """
        self.page.get_element('view[class="wdLi"]').click()
        return self

    def click_ask(self):
        """
        房博士主页，点击“向TA提问”
        """
        self.page.get_element('view[class="ljzx"]').click()
        return self

    # 以下是 我要提问页 的元素点击
    def input_ask_content(self):
        """
        我要提问页，输入提问内容 年-月-日
        """
        cont = time.strftime('%Y-%m-%d') + inspect.stack()[1].function
        self.page.wait_for('textarea[class="contentInput"]')
        self.page.get_element('textarea[class="contentInput"]').input(cont)
        return self

    def upload_img(self):
        """
        我要提问页，上传图片
        """
        self.page.get_element('view[class="btnUpload"]').click()
        image_name = "askfbs.png"
        with open(image_name, 'rb') as fd:
            c = fd.read()
            image_b64data = base64.b64encode(c).decode('utf-8')
        self.app.mock_choose_image(image_name, image_b64data)
        ret = self.app.call_wx_method('chooseImage', {})

    def ask_submit(self):
        """
        我要提问页，点击“提交”按钮
        """
        self.page.get_element('button[class="btnSubmit"]').click()
        return self

    # 以下是 问答详情页 的元素
    def detail_click_label(self):
        """
        问答详情页，点击 标签
        """
        self.page.wait_for('view[class="tagT"]')
        self.page.get_element('view[class="tagT"]').click()
        return self

    def detail_click_ask(self):
        """
        问答详情页，点击 向xxx提问
        """
        self.page.wait_for('button[class="askButton-twoBtn-two tfFlex tfFlexV tfFlexC w100100"]')
        self.page.get_element('button[class="askButton-twoBtn-two tfFlex tfFlexV tfFlexC w100100"]').click()
        return self

    def detail_click_first_newhouse(self):
        """
        问答详情页，点击 第一个楼盘
        """
        self.page.wait_for('view[class="tjlplist"]')
        self.page.get_element('image[class="tjlplist-img"]').click()

    def detail_click_call(self):
        """
        问答详情页，点击第一个 拨打电话
        """
        self.page.wait_for('view[class="tjlplist"]')
        self.page.get_element('button[class="tjlplist-tel"]').click()

    def click_shouye(self):
        """
        房博士主页/问答详情页，点击“回首页”按钮
        """
        # self.page.wait_for('image[class="img-style"]')
        # self.page.get_element('image[class="toHomeBtn--img-style"]').click()
        ele = self.page.get_element('to-home-btn').get_element('view').get_element('image')
        ele.tap()
        return self

