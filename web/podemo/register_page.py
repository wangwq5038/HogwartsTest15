from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        # 注冊信息
        self.driver.find_element(By.ID, 'corp_name').send_keys("aaaaaa1")
        self.driver.find_element(By.ID, 'manager_name').send_keys("bbbbb1")
        self.driver.find_element(By.ID, 'register_tel').send_keys("13512354562")
        self.driver.find_element(By.ID, 'submit_btn').click()
        return True  # 为了在用例页面（test_xx.py）断言
