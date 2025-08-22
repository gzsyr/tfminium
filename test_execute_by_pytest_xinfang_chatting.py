# pytest+allure
# 1、pip install pytest
# 2、pip install pytest-html
# 3、pip install allure-pytest
# 4、https://github.com/allure-framework/allure2/releases   下载allure设置环境变量path：D:\allure-2.19.0\bin
# 失败重试
# pip install pytest-rerunfailures

import os
import shutil
import sys
import time

import pytest

WORKSPACE_DIR = os.path.abspath(os.getcwd())


if __name__ == '__main__':

    date = time.strftime('%Y-%m-%d')
    dir_name = sys.argv[1] if len(sys.argv) > 1 else date   # 命令行输入有参数，使用该参数，如待测版本，默认当前日期
    allure_result_path = WORKSPACE_DIR + "\\allureResult\\result-xf-"+dir_name   # allure 结果路径
    pytest.main(["-v",
                 "-s",
                 # "--lf",
                 # "-rs",
                 # "--show-capture=all",
                 "--html=pytestReport.html",  # html的报告
                 # "--co",  # 仅收集用例
                 "--alluredir", allure_result_path,   # 使用allure报告
                 "./city/test_index_allcity_城市.py::TestAllcity::test_select_qz_选择泉州",   # 先切换到泉州站测新房相关
                 # # # 泉州站用例
                 # "./xiaoxi",
                 # "xf/test_newhouse_detail_新房详情.py",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_cg_采光计算器咨询采光",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_cg_采光计算器咨询层高",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_goto_buttom_im_在线咨询",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_goto_wzzb_dt_地图页咨询",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_goto_wzzb_zbpt_周边配套咨询",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_goto_zlhx_IM_主力户型咨询",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_goto_xxxx_more_IM_详细信息咨询",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_PK_06_点击热门咨询",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_goto_photo_相册咨询",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_goto_hotim_点击热门咨询",
                 "xf/test_newhouse_detail_新房详情.py::TestNewhouseDetail::test_zbxx_周边学校_咨询",
                 "xf/test_newhouse_kpxx_历史开盘信息.py::TestNewhouseKpxx::test_01_点击咨询",
                 "xf/test_album_楼盘相册.py::TestAlbum::test_周边配套大图_咨询",
                 "xf/test_album_楼盘相册.py::TestAlbum::test_click_picture_im",
                 "xf/test_newhouse_dianping_楼盘点评.py::TestNewhouseDianping::test_click_IM_在线咨询",
                 "xf/test_newhouse_huxingdetail_户型详情.py::TestNewhouseHuxingDetail::test_005_hotim_热门咨询",
                 "xf/test_newhouse_huxingdetail_户型详情.py::TestNewhouseHuxingDetail::test_002_click_zygw_im_置业顾问咨询",
                 "xf/test_newhouse_lpxx_楼盘信息.py::TestNewhouseLpxx::test_002_click_zygw_im_置业顾问咨询",
                 "xf/test_newhouse_lpxx_楼盘信息.py::TestNewhouseLpxx::test_005_xxxx_咨询周边板块",
                 "xf/test_newhouse_lpxx_楼盘信息.py::TestNewhouseLpxx::test_007_gjdt_im_公交地铁咨询",
                 "xf/test_newhouse_yfyjdetail_房源详情.py::TestNewhouseYfyjDetail::test_001_hotim_热门咨询",
                 "xf/test_newhouse_yhcx_摇号查询.py::TestNewhouseYhcx::test_05_hotim_热门咨询",
                 "xf/test_newhouse_yhzs_摇号助手.py::TestNewHouseYhzs::test_click_IM_在线咨询",
                 "xf/test_newhouse_楼盘PK_测评.py::TestNewhousePKCP::test_PK_01_点击PK咨询底价",
                 "xf/test_newhouse_楼盘PK_测评.py::TestNewhousePKCP::test_PK_04_底部咨询底价",
                 "xf/test_newhouse_楼盘PK_测评.py::TestNewhousePKCP::test_PK_03_基本信息咨询底价",
                 "xf/test_newhouse_楼盘PK_测评.py::TestNewhousePKCP::test_CP_02_点击咨询和拨打电话",
                 "xf/test_rzfx_日照分析表格.py::TestRzfxBg::test_yfyj_咨询",
                 "xf/test_rzfx_日照分析表格.py::TestRzfxBg::test_z_在线咨询",
                 "xf/test_newhouse_list_新房列表.py::TestNewsHouseList::test_click_zygw_置业顾问咨询",
                 "xf/test_func_lpbd_楼盘榜单页.py::TestFuncLouPanBangdan::test_点击底部IM咨询",
                 "xf/test_func_lpbd_楼盘榜单页.py::TestFuncLouPanBangdan::test_点击底部IM咨询",
                 "xf/test_newhouse_huxingdetail_户型详情.py::TestNewhouseHuxingDetail::test_002_click_zygw_im_置业顾问咨询",
                 "xf/test_newhouse_huxingdetail_户型详情.py::TestNewhouseHuxingDetail::test_005_hotim_热门咨询",
                 "xf/test_newhouse_huxingdetail_户型详情.py::TestNewhouseHuxingDetail::test_007_底部咨询",
                 "xf/test_func_tjf_特价房.py::TestFuncTejiaFang::test_点击底部IM咨询",
                 "xf/test_func_tjf_特价房.py::TestFuncTejiaFang::test_点击列表IM咨询",
                 "xf/test_func_gfzl_购房资料.py::TestFuncGfzl::test_点击列表IM咨询",
                 "xf/test_func_gfzl_购房资料.py::TestFuncGfzl::test_点击底部IM咨询",
                 "xf/test_newhouse_huxinglist_户型列表.py::TestFuncHxList::test_点击底部IM咨询",
                 "xf/test_newhouse_huxinglist_户型列表.py::TestFuncHxList::test_点击列表IM咨询",


                 # 租房房源详情页
                 "rent/test_rent_detail_租房详情页.py::Testrentdetail::test_06_click_fyim_点击房源详情咨询",
                 "rent/test_rent_detail_租房详情页.py::Testrentdetail::test_22_click_zjim_点击租金详情咨询",
                 "rent/test_rent_detail_租房详情页.py::Testrentdetail::test_23_click_zbim_点击周边配套咨询",
                 "rent/test_rent_detail_租房详情页.py::Testrentdetail::test_24_click_hotim_点击热门咨询",
                 "rent/test_rent_detail_租房详情页.py::Testrentdetail::test_17_goto_zxmsg_点击在线咨询",

                 # 二手房源详情页
                 "esf/test_esf_detail_二手房详情.py::Testesfdetail::test_24_goto_zxmsg_点击在线咨询",
                 "esf/test_esf_detail_二手房详情.py::Testesfdetail::test_13_goto_cjmsg_咨询近期成交数据",
                 "esf/test_esf_detail_二手房详情.py::Testesfdetail::test_10_goto_rmim_点击热门咨询tab",
                 "esf/test_esf_detail_二手房详情.py::Testesfdetail::test_08_goto_xqzx_房源详情咨询",
                 "esf/test_esf_detail_二手房详情.py::Testesfdetail::test_06_goto_sfim_点击税费咨询",
                 "esf/test_esf_detail_二手房详情.py::Testesfdetail::test_05_goto_lcim_点击楼层咨询",
                 "esf/test_esf_detail_二手房详情.py::Testesfdetail::test_04_goto_ygim_首付和月供咨询",

                 "esf/test_esf_房源成交详情页.py",



                 # "./tfq",
                 # "./xf",
                 # "./mine",
                 # "./xiaoxi",
                 # "./logout",

                 # "./jjr",
                 # "./esf",
                 # "./rent",
                 # "./mine_esf",
                 "--reruns", '3',
                 "--reruns-delay", '2'
                 ])

    a_report_path = WORKSPACE_DIR + '\\allureReport\\report-xf-'+dir_name  # allure 报告路径

    command_allure_generate = f"allure generate --clean {allure_result_path} -o {a_report_path}"
    os.system(command_allure_generate)  # 生成测试报告
    #
    # 无需打开
    # command_allure_open = f'allure open {a_report_path}'
    # allure generate --clean ./allureResult/result-2024-10-21 -o ./allureReport/report-2024-10-21
    # os.system(command_allure_open)  # 打开测试报告