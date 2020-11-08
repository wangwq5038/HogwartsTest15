from selenium.webdriver.common.by import By

from frame.frame_demo.base_page import BasePage
from frame.frame_demo.click_x import Click_x


class Main(BasePage):

    def goto_search(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        return Click_x()
