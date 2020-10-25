from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from podemo.page.add_member_page import AddMemberPage


class MainPage(object):
    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)

    def goto_addmember(self):
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]//span[@class="frame_nav_item_title"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH,
                                 '//*[@class="member_colRight_cnt_operation"]//a[@class="qui_btn ww_btn js_add_member"]').click()
        return AddMemberPage(self.driver)
