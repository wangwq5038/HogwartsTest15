"""
base_page.py 基类模块： 主要用于初始化driver，定义find， 常用的基本方法
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
import logging  # 引入logging模块
import os.path
import time


class BasePage:
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    log_name = log_path + rq + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # 将日志输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)  # 输出到console的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # print(f"root_logger.handlers:{logging.getLogger().handlers}")
    # for h in logger.handlers[:]:
    #     logger.removeHandler(h)
    # logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        self.logger.info(by)
        self.logger.info(locator)
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.logger.info('click')
        self.find(by, locator).click()

    def find_by_scroll(self, text):
        self.logger.info(text)
        self.logger.info('find_by_scroll')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def get_toast_text(self):
        self.logger.info('get_toast_text')

        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        self.logger.info(result)
        return result
