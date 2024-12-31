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
    allure_result_path = WORKSPACE_DIR + "\\allureResult\\result-"+dir_name   # allure 结果路径
    pytest.main(["-v",
                 "-s",
                 "--lf",
                 # "-rs",
                 # "--show-capture=all",
                 "--html=pytestReport.html",  # html的报告
                 # "--co",  # 仅收集用例
                 "--alluredir", allure_result_path,   # 使用allure报告
                 "./city/test_index_allcity_城市.py::TestAllcity::test_select_qz_选择泉州",   # 先切换到泉州站测新房相关
                 "./zixun",
                 "./tfq",
                 "./xf",
                 "./mine",
                 "./xiaoxi",
                 "./logout",
                 "./city/test_index_allcity_城市.py::TestAllcity::test_select_nj_选择南京",   # 后切换到南京站测二手房相关/
                 "./jjr",
                 "./esf",
                 "./rent",
                 "./mine_esf",
                 "--reruns", '3',
                 "--reruns-delay", '2'
                 ])

    a_report_path = WORKSPACE_DIR + '\\allureReport\\report-'+dir_name  # allure 报告路径

    command_allure_generate = f"allure generate --clean {allure_result_path} -o {a_report_path}"
    os.system(command_allure_generate)  # 生成测试报告
    #
    # 无需打开
    # command_allure_open = f'allure open {a_report_path}'
    # allure generate --clean ./allureResult/result-2023-08-03 -o ./allureReport/report-2023-08-03
    # os.system(command_allure_open)  # 打开测试报告