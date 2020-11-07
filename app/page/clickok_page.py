from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage


class ClickOkPage(BasePage):

    def click_ok(self):
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        return True
