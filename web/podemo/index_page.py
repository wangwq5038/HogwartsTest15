from selenium import webdriver
from selenium.webdriver.common.by import By

from web.podemo.login_page import LoginPage
from web.podemo.register_page import RegisterPage


class IndexPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        # 点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()

        # return LoginPage   通过return 完成页面跳转
        return LoginPage(self.driver)

    def goto_register(self):
        # 点击注册按钮
        self.driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self.driver)
