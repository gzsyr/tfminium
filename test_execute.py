import unittest



from zixun.test_news_list import TestNewsList

if __name__ == "__main__":
    suite = unittest.TestSuite()  # 添加测试套件
    loader = unittest.TestLoader()  # 定义loader加载器

    suite.addTests(loader.loadTestsFromTestCase(TestNewsList))
    result = unittest.TextTestRunner().run(suite)





    # 以下直接输出minitest的官方测试报告
    # 命令行运行：
    # minitest -s suite.json -c config.json -g

    # 查看测试报告
    # python -m http.server 12345 -d /path/to/dir/of/report
    # 浏览器输入地址
    # http://localhost:12345/

