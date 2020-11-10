from frame.main import Main


class TestMain:

    def test_main(self):
        main = Main().goto_market().goto_search()

# def enhance(func):
#     print('before')
#     func()
#     print('after')

# 装饰器使用
# def tmp(func):
#     def wrapper(*args, **kwargs):
#         print('before')
#         func(*args, **kwargs)
#         print('after')
#     return wrapper
#
# @tmp
# def a():
#     print('a')
#
#
#
#
#
#
# def test_a():
#     # enhance(a)
#     a()
