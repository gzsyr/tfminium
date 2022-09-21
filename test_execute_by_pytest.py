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


def del_file(path_data):
    """
    删除screenshot  或者   minitest生成的outputs（删除名为全数字的文件夹）
    如：del_screenshot_png(WORKSPACE_DIR + '\\screenshot')
    path_data: 要删除的路径
    """
    for i in os.listdir(path_data):
        file_data = path_data + '\\' + i
        if os.path.isfile(file_data):
            os.remove(file_data)
        else:
            if i.isdigit():
                shutil.rmtree(file_data)
            else:
                del_file(file_data)


def change_report_name(report_path):
    """
    修改allure报告的名称，待补充
    """
    file = report_path + '\\widgets\\summary.json'


if __name__ == '__main__':

    date = time.strftime('%Y-%m-%d')
    dir_name = sys.argv[1] if len(sys.argv) > 1 else date   # 命令行输入有参数，使用该参数，如待测版本，默认当前日期
    allure_result_path = WORKSPACE_DIR + "\\allureResult\\result-"+dir_name   # allure 结果路径
    pytest.main(["-v",
                 "-s",
                 # "-rs",
                 # "--show-capture=all",
                 "--html=pytestReport.html",  # html的报告
                 "--co",  # 仅收集用例
                 "--alluredir", allure_result_path,   # 使用allure报告
                 "./city/test_index_allcity_城市.py::TestAllcity::test_select_qz_选择泉州",   # 先切换到泉州站测新房相关
                 "./zixun",
                 "./tfq",
                 "./xf",
                 "./mine",
                 "./city/test_index_allcity_城市.py::TestAllcity::test_select_nj_选择南京",   # 后切换到南京站测二手房相关
                 "./esf",
                 "./rent",
                 "--reruns", '3',
                 "--reruns-delay", '2'
                 ])

    a_report_path = WORKSPACE_DIR + '\\allureReport\\report-'+dir_name  # allure 报告路径

    command_allure_generate = f"allure generate --clean {allure_result_path} -o {a_report_path}"
    os.system(command_allure_generate)  # 生成测试报告
    #
    # command_allure_open = f'allure open {a_report_path}'
    # os.system(command_allure_open)  # 打开测试报告