# add by zsy
# 使用BeautifulReport出测试报告
# pip install BeautifulReport
import sys
import time
import unittest

from BeautifulReport import BeautifulReport


if __name__ == "__main__":
    suite = unittest.TestSuite()  # 添加测试套件
    loader = unittest.TestLoader()  # 定义loader加载器


    # suite.addTests(loader.discover('./tfq/', pattern='test_*.py', top_level_dir='./'))
    suite.addTests(loader.discover('./xf/', pattern='test_*.py', top_level_dir='./'))
    # suite.addTests(loader.discover('./zixun/', pattern='test_*.py', top_level_dir='./'))
    # suite.addTests(loader.discover('./mine/', pattern='test_*.py', top_level_dir='./'))
    # print(suite.countTestCases())
    # suite = unittest.defaultTestLoader.discover('./tfq-V1/', pattern='test_tfq_*.py')
    #
    br = BeautifulReport(suites=suite)
    dt = time.strftime('%Y-%m-%d-%H-%M')
    fn = sys.argv[2]+'.html' if len(sys.argv)>2 else f'tfq_report_{dt}.html'
    br.report(description=sys.argv[1] if len(sys.argv)>1 else '淘房小程序-淘房圈-测试报告', filename=fn)

    # 以下直接输出minitest的官方测试报告
    # 命令行运行：
    # minitest -s suite.json -c config.json -g

    # 查看测试报告
    # python -m http.server 12345 -d /path/to/dir/of/report
    # 浏览器输入地址
    # http://localhost:12345/
