# 通讯录界面
from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.member_invite_menu_page import MemberInviteMenuPage
from app.page.personal_information_page import PersionalInformationPage


class AddressListPage(BasePage):
    # 通讯录界面
    # def __init__(self, driver):
    #     self.driver = driver

    def click_addmember(self):
        # 滚动查找添加成员
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()\
        #                          .scrollable(true).instance(0))\
        #                          .scrollIntoView(new UiSelector()\
        #                          .text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)

    def click_contact(self, contactname):
        # 点击联系人
        self.find_by_scroll(contactname).click()
        return PersionalInformationPage(self.driver)

    def click_search(self, contactname):
        # 点击搜索按钮
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hxw']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(contactname)
