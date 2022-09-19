# add by zsy
# 使用BeautifulReport出测试报告
# pip install BeautifulReport
import os
import shutil
import sys
import time
import unittest

from BeautifulReport import BeautifulReport

WORKSPACE_DIR = os.path.abspath(os.getcwd())


def del_screenshot_png(path_data):
    for i in os.listdir(path_data):
        file_data = path_data + '\\' + i
        if os.path.isfile(file_data):
            os.remove(file_data)
        else:
            if i.isdigit():
                shutil.rmtree(file_data)
            else:
                del_screenshot_png(file_data)


if __name__ == "__main__":
    suite = unittest.TestSuite()  # 添加测试套件
    loader = unittest.TestLoader()  # 定义loader加载器

    # del_screenshot_png(WORKSPACE_DIR + '\\outputs')
    # del_screenshot_png(WORKSPACE_DIR + '\\screenshot')

    # suite.addTests(loader.discover('./tfq-V1/', pattern='test_*.py', top_level_dir='./'))
    suite.addTests(loader.discover('./tfq/', pattern='test_*.py', top_level_dir='./'))
    suite.addTests(loader.discover('./xf/', pattern='test_*.py', top_level_dir='./'))
    suite.addTests(loader.discover('./zixun/', pattern='test_*.py', top_level_dir='./'))
    suite.addTests(loader.discover('./mine/', pattern='test_*.py', top_level_dir='./'))
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
