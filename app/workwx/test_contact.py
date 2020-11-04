from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWx:

    def setup(self):
        # 定义了一个字典
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # noReset 保留缓存， 比如登录状态
        caps["noReset"] = "True"
        # 不停止应用，直接运行测试用例
        # caps["dontStopAppOnReset"] = "true"
        caps['skipDeviceInitialization'] = 'true'
        caps['skipServerInstallation'] = 'true'
        # caps["settings[waitForIdleTimeout]"] = 0
        # 关键  localhost:4723  本机ip:server端口
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        # 进入到通讯录界面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # 滚动查找添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        # 点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        """
        添加联系人
        """
        name = "aaaa004"
        gender = "男"
        phonenum = "13512340014"
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
        # sleep(2)
        # print(self.driver.page_source)
        # 验证 添加成功 toast
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == result
