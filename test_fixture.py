import pytest


@pytest.fixture(scope="module")
def login():
    print("这是登录方法")
    return ("Tom", "123")


@pytest.fixture()
def operate():
    print("登录后的操作")


def test_case1(login, operate):
    print(login)
    print("test_case1, 需要登录")


def test_case2():
    print("test_case2, 不需要登录")


def test_case3(login):
    print(login)
    print("test_case3, 需要登录")
