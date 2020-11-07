from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.clickok_page import ClickOkPage


class DeleteMemberPage(BasePage):

    def delete_member(self):
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        return ClickOkPage(self.driver)
