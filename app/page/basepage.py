"""
base_page.py 基类模块： 主要用于初始化driver，定义find， 常用的基本方法
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.INFO(by)
        logging.INFO(locator)
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.INFO('click')
        self.find(by, locator).click()

    def find_by_scroll(self, text):
        logging.INFO(text)
        logging.INFO('find_by_scroll')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def get_toast_text(self):
        logging.INFO('get_toast_text')

        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.INFO(result)
        return result
