from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo.register_page import RegisterPage


class LoginPage:
    # 定义init方法获取到上个页面的driver对象
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        # 扫码登录
        pass

    # 进入到注册页面
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return RegisterPage(self.driver)
