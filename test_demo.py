import os
from time import sleep

from selenium import webdriver


def test_browser():
    # 使用os模块的getenv方法来获取声明环境变量browser
    browser = os.getenv("browser").lower()
    # 判断browser的值
    if browser == "headless":
        driver = webdriver.PhantomJS()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.get("https://home.testing-studio.com/")
    sleep(3)
