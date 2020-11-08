from selenium.webdriver.common.by import By

from frame.frame_demo.base_page import BasePage


class Search(BasePage):

    def search(self):
        self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return True
