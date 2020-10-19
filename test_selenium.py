import os
from time import sleep

import pytest
import selenium
from selenium import webdriver


# def setup(self):
#     self.driver = webdriver.Chrome()
#     self.driver.maximize_window()
#
#
# def teardown(self):
#     sleep(2)
#     self.driver.quit()

@pytest.fixture(scope="module")
def kj():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    sleep(2)
    driver.quit()


def test_selenium(self):
    self.driver.get("https://www.baidu.com/")
