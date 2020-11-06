"""
编辑联系人页面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# from app.page.member_invite_menu_page import MemberInviteMenuPage
from app.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_contact(self, name, gender, phonenum):

        # 设置用户名 性别 手机号
        self.driver.find_element(MobileBy.XPATH, \
                                 "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, \
                                 "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        if gender == '男':
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//android.widget.EditText').send_keys(
            phonenum)
        # 点击【保存】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        from app.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
