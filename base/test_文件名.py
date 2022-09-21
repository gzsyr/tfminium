# -*- coding: UTF-8 -*-
import unittest
import pytest


class 测试中文类名(unittest.TestCase):

    def test_001_中文(self):
        print("eeeee")

    def test_002(self):
        self.test_001_中文()


if __name__ == "__main__":
    pytest.main(["-v",
                 "-s",
                 "--co",
                 "test_文件名.py::测试中文类名"])