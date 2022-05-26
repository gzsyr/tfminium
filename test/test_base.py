# add by zsy
import time

import minium


class TestBase(minium.MiniTest):
    """
    继承自minitest的testbase类，后面所有测试类均继承自该类
    """
    def delay(self, second):
        time.sleep(second)
        return self

    def tearDown(self) -> None:
        super().tearDown()
        self.delay(3)
        print("+++++++++tearDown+++++++++")