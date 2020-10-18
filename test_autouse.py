# coding=utf-8
import pytest


# 每条用例之前都先执行这个用例
# 自动执行fixture
@pytest.fixture(autouse="ture")
def myfixture():
    print("this is my fixture")


class TestAutouse:

    def test_one(self):
        print("执行test_one")
        assert 1 + 2 == 3

    def test_two(self):
        print("执行test_two")
        assert 1 == 1

    def test_three(self):
        print("执行test_three")
        assert 1 + 1 == 2
