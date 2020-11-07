from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.delete_member_page import DeleteMemberPage


class EditMemberPage(BasePage):

    def click_edit_member(self):
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return DeleteMemberPage(self.driver)
