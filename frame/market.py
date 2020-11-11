from selenium.webdriver.common.by import By

from frame.Search import Search
from frame.base_page import BasePage


class Market(BasePage):

    def goto_search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.parse_yaml("./market.yaml", "goto_search")
        return Search(self.driver)
