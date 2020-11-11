import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from frame.hand_black import handle_black
from frame.singleton import singleton


# @singleton
class BasePage:
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        """
        初始化应用
        """
        if driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            # noReset 保留缓存， 比如登录状态
            caps["noReset"] = "True"
            self.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        """
        查找元素
        :param by:
        :param locator:
        :return:
        """
        try:
            if locator is None:
                result = self.driver.find_element(*by)
            else:
                result = self.driver.find_element(by, locator)
            self.error_num = 0
            return result
        except Exception as e:
            if self.error_num > self.max_num:
                raise e
            self.error_num += 1
            for black_ele in self._black_list:
                ele = self.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    return self.find(by, locator)
            raise e

    def parse_yaml(self, path, func_name):
        with open(path, encoding='utf-8') as f:
            data = yaml.load(f)
        self.parse(data[func_name])

    def parse(self, steps):
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            elif 'send' == step['action']:
                self.find(step['by'], step['locator']).send_keys("content")
