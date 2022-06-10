# add by zsy
# 使用BeautifulReport出测试报告
# pip install BeautifulReport

import unittest
from BeautifulReport import BeautifulReport

# from test.test_android import TestAndroid
from test.test_first import TestFirst
from test.test_kft import TestKFT
from test.test_newhousedetail import TestNewhouseDetail
from test.test_tfq_bangdan import TestBangDan
from test.test_tfq_commentdetail import TestCommentDetail
from test.test_tfq_drafbox import TestDrafBox
from test.test_tfq_fbspage import TestFbsPage
from test.test_tfq_fbswritepost import TestFbsWritePost
from test.test_tfq_huatidetail import TestHuaTiDetail
from test.test_tfq_linkedbangdan import TestLinkedBangdan
from test.test_tfq_mycomments import TestMyComments
from test.test_tfq_myhuati import TestMyHuaTi
from test.test_tfq_mypost import TestMyPost
from test.test_tfq_myquanzi import TestMyQuzi
from test.test_tfq_postcomment import TestPostComment
from test.test_tfq_postdetail import TestPostDetail
from test.test_tfq_quanzidetail import TestQuanZiDetail
from test.test_tfq_quanzilist import TestQuanZi
from test.test_tfq_reyi import TestReYi
from test.test_tfq_search import TestTfqSearch
from test.test_tfq_shouye import TestTfqShouYe
from test.test_tfq_topiclist import TestTopicList
from test.test_tfq_yunyingwritepost import TestYyWritePost
from test.test_tfq_zygwwirtepost import TestZygwWritePost

if __name__ == "__main__":
    suite = unittest.TestSuite()  # 添加测试套件
    loader = unittest.TestLoader()  # 定义loader加载器

    # suite.addTests(loader.loadTestsFromTestCase(TestFirst))
    # suite.addTests(loader.loadTestsFromTestCase(TestKFT))
    # suite.addTests(loader.loadTestsFromTestCase(TestAndroid))
    # suite.addTests(loader.loadTestsFromTestCase(TestNewhouseDetail))
    suite.addTests((loader.loadTestsFromTestCase(TestTfqShouYe)))
    suite.addTests((loader.loadTestsFromTestCase(TestBangDan)))
    suite.addTests((loader.loadTestsFromTestCase(TestCommentDetail)))
    suite.addTests((loader.loadTestsFromTestCase(TestDrafBox)))
    suite.addTests((loader.loadTestsFromTestCase(TestFbsPage)))
    suite.addTests((loader.loadTestsFromTestCase(TestFbsWritePost)))
    suite.addTests((loader.loadTestsFromTestCase(TestHuaTiDetail)))
    suite.addTests((loader.loadTestsFromTestCase(TestLinkedBangdan)))
    suite.addTests((loader.loadTestsFromTestCase(TestMyComments)))
    suite.addTests((loader.loadTestsFromTestCase(TestMyHuaTi)))
    suite.addTests((loader.loadTestsFromTestCase(TestMyPost)))
    suite.addTests((loader.loadTestsFromTestCase(TestMyQuzi)))
    suite.addTests((loader.loadTestsFromTestCase(TestPostComment)))
    suite.addTests((loader.loadTestsFromTestCase(TestPostDetail)))
    suite.addTests((loader.loadTestsFromTestCase(TestQuanZiDetail)))
    suite.addTests((loader.loadTestsFromTestCase(TestQuanZi)))
    suite.addTests((loader.loadTestsFromTestCase(TestReYi)))
    suite.addTests((loader.loadTestsFromTestCase(TestTfqSearch)))
    suite.addTests((loader.loadTestsFromTestCase(TestTopicList)))
    suite.addTests((loader.loadTestsFromTestCase(TestYyWritePost)))
    suite.addTests((loader.loadTestsFromTestCase(TestZygwWritePost)))

    br = BeautifulReport(suites=suite)
    br.report(description='淘房小程序淘房圈测试报告', filename='br_report.html')

    # 以下直接输出minitest的官方测试报告
    # 命令行运行：
    # minitest -s suite.json -c config.json -g

    # 查看测试报告
    # python -m http.server 12345 -d /path/to/dir/of/report
    # 浏览器输入地址
    # http://localhost:12345/
