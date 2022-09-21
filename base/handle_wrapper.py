# add by zsy
import minium


def handle_black(func):

    def wrapper(*args, **kwargs):
        error_times = 0
        total_times = 3

        print("开始解释器", error_times)

        instance = args[0]

        try:
            ele = func(*args, **kwargs)
            error_times = 0
            return ele
        except minium.MiniElementNotFoundError as e:
            print("没有找到元素")
            if error_times > total_times:
                raise e
            error_times += 1
            print("错误次数：", error_times)
            for i in range(total_times):
                print("i:", i)
                func(*args, **kwargs)
            print("for 循环over")
            raise e

    return wrapper