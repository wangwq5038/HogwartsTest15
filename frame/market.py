from selenium.webdriver.common.by import By

from frame.Search import Search
from frame.base_page import BasePage


class Market(BasePage):

    def goto_search(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self.driver)
