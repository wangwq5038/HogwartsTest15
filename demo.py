# import os
# from time import sleep
#
# from selenium import webdriver
#
#
# def test_browser():
#     # 使用os模块的getenv方法来获取声明环境变量browser
#     browser = os.getenv("browser").lower()
#     # 判断browser的值
#     if browser == "headless":
#         driver = webdriver.PhantomJS()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         driver = webdriver.Chrome()
#     driver.get("https://home.testing-studio.com/")
#     sleep(3)



import chevron

# print(chevron.render('Hello, {{mustache}}!', {'mustache': 'world'}))
# args = {
#   'template': 'Hello, {{ mustache }}!',
#
#   'data': {
#     'mustache': 'World'
#   }
# }
#
# print(chevron.render(**args))
# import chevron
#
# args = {
#     'template': 'Hello, {{> thing }}!',
#
#     'partials_dict': {
#         'thing': 'World'
#     }
# }
#
# print(chevron.render(**args))


# def get_account(num):
#     accounts = []
#     for index in range(1, num+1):
#         accounts.append(
#             {"username": "user%s" % index, "password": str(index) * 6},
#         )
#
#     print(accounts)
#
# if __name__ == '__main__':
#     get_account(10)

#
# import keyword
#
# print(keyword.kwlist)

# import sys; x = 'runoob';
# print(sys.stdout.write(x + '\n'))

# x = "a"
# y = "b"
# # 换行输出
# print(x)
# print(y)
#
# print('----------------------')
# # 不换行输出
# print(x, end=" ")
# print(y, end=" ")
# print()



# import sys
# print('================Python import mode==========================')
# print ('命令行参数为:')
# for i in sys.path:
#     print (i)
# # print ('\n python 路径为',sys.path)

# a, b, c = 1, 2, "runoob"
# print(a)
# print(b)
# print(c)

# def reverseWords(input):
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ")
#     print(inputWords)
#     # 翻转字符串
#     # 假设列表 list = [1,2,3,4],
#     # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
#     # inputWords[-1::-1] 有三个参数
#     # 第一个参数 -1 表示最后一个元素
#     # 第二个参数为空，表示移动到列表末尾
#     # 第三个参数为步长，-1 表示逆向
#     inputWords = inputWords[-1::-1]
#     print(inputWords)
#
#     # 重新组合字符串
#     output = ' '.join(inputWords)
#     print(output)
#
#     return output
#
#
# if __name__ == "__main__":
#     input = 'I like runoob'
#     rw = reverseWords(input)
#     print(rw)

# print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
# print({x: x ** 2 for x in (2, 4, 6)})

# def a():
#     '''这是文档字符串'''
#     pass
# print(a.__doc__)

# !/usr/bin/python3

# a = 10
# b = 20
#
# # if (a and b):
# #     print("1 - 变量 a 和 b 都为 true")
# # else:
# #     print("1 - 变量 a 和 b 有一个不为 true")
# print((a and b))
# print((a or b))
# print(not (a and b))
# print(a is b)
# print((a is not b))

# var2 = 1
# if var2:
#     print ("2 - if 表达式条件为 true")
#     print (var2)
# print ("Good bye!")

# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
#
# ### 退出提示
# input("点击 enter 键退出")

# n = 100
#
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
#
# print("1 到 %d 之和为: %d" % (n, sum))

# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
#
# print("Good bye!")


# flag = 1
#
# while (flag): print('欢迎访问菜鸟教程!')
#
# print("Good bye!")

# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")

# import sys  # 引入 sys 模块
#
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# it = iter(list)  # 创建迭代器对象
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)

# 可写函数说明
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
#
#
# # 调用printme函数
# # printme(str="菜鸟教程")
# print("菜鸟教程")

# 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
#
# # 调用printinfo 函数
# # printinfo(10)
# printinfo(70, 60, 50)
#
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list.index(5))
# print(list.count(5))
# list.reverse()
# print(list)
import os, sys
# f = open("C:\\Users\\wangwq\\tmp\\foo.txt", "r+")
# num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# str = f.read(30)
# str = f.readlines()
# print(str)
# for line in f:
#     print(line, end='')
# print(num)
# ret = os.access("C:\\Users\\wangwq\\tmp\\foo.txt", os.F_OK)
# # print ("F_OK - 返回值 %s"% ret)
# # print ("F_OK - 返回值{}".format(ret))
# print (f"F_OK - 返回值{ret}")




# f.close()



# while True:
#     try:
#         x = int(input("请输入一个数字: "))
#         break
#     except ValueError:
#         print("您输入的不是数字，请再次尝试输入！")

# def this_fails():
#     x = 1 / 0
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('My exception occurred, value:', e.value)

class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')

#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
# super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法
# # super(Child, c)

# from datetime import date
# now = date.today()
# print(now)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#
#     print(average([20, 30, 70]))
#     40.0
#     """
#     return sum([20, 30, 70]) / len([20, 30, 70])
#
# import doctest
# doctest.testmod()   # 自动验证嵌入测试

# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

# # 用户输入数字
# num1 = input('输入第一个数字：')
# num2 = input('输入第二个数字：')
#
# # 求和
# sum = float(num1) + float(num2)
#
# # 显示计算结果
# print(f'数字 {num1} 和 {num2} 相加结果为： {sum}')
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j}x{i}={i*j}\t', end='')
#     print()

# # 引入日历模块
# import calendar
#
# # 输入指定年月
# yy = int(input("输入年份: "))
# mm = int(input("输入月份: "))
#
# # 显示日历
# print(calendar.month(yy, mm))

def recur_fibo(n):
    """递归函数
    输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


# # 获取用户输入
# nterms = int(input("您要输出几项? "))
#
# # 检查输入的数字是否正确
# if nterms <= 0:
#     print("输入正数")
# else:
#     print("斐波那契数列:")
#     for i in range(nterms):
#         print(recur_fibo(i))

