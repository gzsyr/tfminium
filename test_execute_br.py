# add by zsy
# 使用BeautifulReport出测试报告
# pip install BeautifulReport

import unittest
from BeautifulReport import BeautifulReport

from test.test_first import TestFirst
from test.test_kft import TestKFT


if __name__ == "__main__":
    # suite = unittest.TestSuite()  # 添加测试套件
    # loader = unittest.TestLoader()  # 定义loader加载器

    # suite.addTests(loader.loadTestsFromTestCase(TestFirst))
    # suite.addTests(loader.loadTestsFromTestCase(TestKFT))


    suite = unittest.defaultTestLoader.discover('./test/', pattern='test_tfq_*.py')

    br = BeautifulReport(suites=suite)
    br.report(description='淘房小程序淘房圈测试报告', filename='br_report_v613x.html')

    # 以下直接输出minitest的官方测试报告
    # 命令行运行：
    # minitest -s suite.json -c config.json -g

    # 查看测试报告
    # python -m http.server 12345 -d /path/to/dir/of/report
    # 浏览器输入地址
    # http://localhost:12345/
