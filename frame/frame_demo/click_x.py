from selenium.webdriver.common.by import By

from frame.frame_demo.base_page import BasePage
from frame.frame_demo.search import Search


class Click_x(BasePage):

    def click_x(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/rl_login_by_wx']//*[@text='微信登录']").click()
        return Search()
