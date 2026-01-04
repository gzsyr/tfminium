import pytest


def pytest_addoption(parser):
    """添加一个自定义的命令行参数"""
    parser.addoption(
        "--modify-items",
        action="store_true",  # 这是一个布尔值的 flag
        default=False,
        help="是否执行 pytest_collection_modifyitems 中的自定义逻辑"
    )


def pytest_collection_modifyitems(config, items):
    """
        pytest用例收集的顺序：
        收集阶段：pytest 扫描所有指定的文件和目录，找出所有的测试用例，并将它们放入一个列表（items）中。
        修改阶段：执行 pytest_collection_modifyitems 钩子函数。你可以在这个阶段对 items 列表进行修改，比如去重、排序、添加或删除用例。
        筛选阶段：应用所有的筛选条件，比如 -m (标记)、-k (关键字) 等。pytest 会遍历经过修改后的 items 列表，只选出那些符合筛选条件的用例。
        执行阶段：执行最后筛选出来的用例。

        只有当 --modify-items 被指定时，才执行修改逻辑
    """
    # 从配置中获取命令行参数的值
    if config.getoption("--modify-items"):
        print("--- 开始执行自定义的用例修改逻辑 ---")

        seen_nodeids = set()  # 存储已出现的用例唯一标识
        unique_items = []  # 存储去重后的用例列表
        print(f'items:{len(items)}')
        for item in items:
            # 获取用例唯一标识：nodeid 是 pytest 内置的唯一ID，不会重复
            nodeid = item.nodeid
            if nodeid not in seen_nodeids:
                seen_nodeids.add(nodeid)
                unique_items.append(item)  # 未重复，加入列表
                # print(item.nodeid)
                # print(seen_nodeids)
                # print(unique_items)
            else:
                # 可选：打印去重日志，方便调试
                print(f"移除重复用例：{nodeid}")

        # 用去重后的列表替换原列表
        items[:] = unique_items

        print("--- 自定义逻辑执行完毕 ---")
    else:
        print("--- 未指定 --modify-items，跳过自定义用例修改逻辑 ---")


