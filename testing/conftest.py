import pytest


@pytest.fixture(scope='module')
def open_start():
    print("开始计算")
    yield
    print("计算结束")


"""
作业3【选做】：【参考了网上的答案】
~~~
https://blog.csdn.net/waitan2018/article/details/104320927
~~~

1、注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
2、env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据
"""


def pytest_addoption(parser):
    parser.addoption("--env", action="store",
                     default='test',
                     choices=['test', 'dev', 'st'],
                     help="将自定义命令行参数 'env' 添加到pytest配置中")


"""
从配置对象获取 env 的值
"""


@pytest.fixture(scope="session")
def env(pytestconfig):
    return pytestconfig.getoption('env')


"""
任何fixture或者测试用例都可以调用env来获得设备信息
"""
