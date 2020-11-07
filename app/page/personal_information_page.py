from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.editmember_page import EditMemberPage


class PersionalInformationPage(BasePage):

    # clickmenu1 = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hxm']")

    def click_menu(self):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hxm']").click()
        return EditMemberPage(self.driver)
