# 模块级，在模块始末调用
import pytest


def setup_module():
    print("\nsetup_module, 只执行一次，当有多个测试类时调用")


def teardown_module():
    print("\nteardown_module, 只执行一次，当有多个测试类时调用")


class TestPytest1(object):

    # 类级，在类始末调用（在类中）
    @classmethod
    def setup_class(cls):
        print("\nsetup_class1, 只执行一次")

    # 类级，在类始末调用（在类中）
    @classmethod
    def teardown_class(cls):
        print("\nteardown_class1, 只执行一次")

    # 方法级，在方法始末调用（在类中）
    def setup_method(self):
        print("\nsetup_method1, 每个测试方法都执行一次")

    # 方法级，在方法始末调用（在类中）
    def teardown_method(self):
        print("\nteardown_method1, 每个测试方法都执行一次")

    @pytest.mark.run(order=3)
    def test_three(self):
        print("test_three, 测试用例")

    @pytest.mark.run(order=-1)
    def test_four(self):
        print("test_four, 测试用例")


class TestPytest2(object):

    # 类级，在类始末调用（在类中）
    @classmethod
    def setup_class(cls):
        print("\nsetup_class2, 只执行一次")

    # 类级，在类始末调用（在类中）
    @classmethod
    def teardown_class(cls):
        print("\nteardown_class2, 只执行一次")

    # 方法级，在方法始末调用（在类中）
    def setup_method(self):
        print("\nsetup_method2, 每个测试方法都执行一次")

    # 方法级，在方法始末调用（在类中）
    def teardown_method(self):
        print("\nteardown_method2, 每个测试方法都执行一次")

    @pytest.mark.run(order=2)
    def test_two(self):
        print("test_two, 测试用例")

    @pytest.mark.run(order=1)
    def test_one(self):
        print("test_one, 测试用例")
