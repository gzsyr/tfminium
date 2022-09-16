# pytest+allure
# 1、pip install pytest
# 2、pip install pytest-html
# 3、pip install allure-pytest
# 4、https://github.com/allure-framework/allure2/releases   下载allure设置环境变量path：D:\allure-2.19.0\bin

import os

import pytest

if __name__ == '__main__':
    pytest.main(["-v",
                 "-s",
                 # "-rs",
                 # "--show-capture=all",
                 "--html=pytestReport.html",  # html的报告
                 # "--co",  # 仅收集用例
                 "--alluredir", "./pytestResult-attach",   # 使用allure报告
                 # "./xf/test_newhouse_list.py::TestNewsHouseList::test_click_zx",   # 运行指定文件
                 "./zixun",
                 "./tfq",
                 "./xf",
                 "./mine",
                 "--reruns", '3',
                 "--reruns-delay", '2'
                 ])

    os.system(r"allure generate --clean ./pytestResult-attach -o ./pytestReport-attach")
    os.system(r"allure open ./pytestReport-attach")  # 打开测试报告