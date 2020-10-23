import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWork(object):

    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        handles = self.driver.window_handles
        print(handles)
        sleep(3)
        search = self.driver.find_element_by_id('su')
        # self.driver.refresh()
        print(search.get_attribute('value'))
        print(search.location)
        print(search.size)
        # print(self.driver.page_source)

    # def test_work(self):
    #     self.driver.find_element(By.ID, "menu_contacts").click()
    #     sleep(3)
    #
    # def test_cookie(self):
    #     # get_cookies() 可以获取当前页面的cookies
    #     # add_cookies() 可以把cookie添加到页面中去
    #     # cookies = self.driver.get_cookies()
    #     #cookies需要更新，有过期时间
    #     cookies = [
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
    #          'value': '1688850725669432'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
    #          'value': 'aXcZjoQTLxqg5PFZopFrtFxsmukxX0W01f5mDeKeOFslPkXNam6u7u-C9i3cQ9YsxksIckYb2ig9Ise4l7oR2jzKzJ8Lm7zbndzNWsfWmLUqGnnPCIUif-KPwS85BJt8Mq4IKJGrviWHf1ylJGiG6xOvD6GleVo4sHlTdII2l7Fc9zrdUy4ROykfNrmmIjZFNT998lahFzf5BNfTyw_iLsRKnry-1t7neggM9NLvBICLyUPgt7kbKkXgYpLlWdriT8oV85dS9E3chmjo7rEX-A'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
    #          'value': '1688850725669432'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
    #          'value': '1970325068168689'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
    #          'value': '6vssenVTlystJ8fb5uufJnzFhzZkzbrcqroKnjxJE94XOL-ACJiGnSOqp5Cm1RnT'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
    #          'value': 'a9342256'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
    #          'value': '3976622710929524'},
    #         {'domain': '.qq.com', 'expiry': 1666455710, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
    #          'value': 'GA1.2.1172056102.1603368053'},
    #         {'domain': '.qq.com', 'expiry': 1603470110, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
    #          'value': 'GA1.2.1392315918.1603368053'},
    #         {'domain': 'work.weixin.qq.com', 'expiry': 1603399588, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
    #          'secure': False, 'value': '4c1rb4f'},
    #         {'domain': '.work.weixin.qq.com', 'expiry': 1634904052, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
    #          'path': '/', 'secure': False, 'value': '0'},
    #         {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
    #          'secure': False, 'value': '1639913117'},
    #         {'domain': '.qq.com', 'expiry': 2147483650, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
    #          'value': '44b19f46f6c288caa6e7361bc7d94708754efe2ea6b137d1aac91eaa275ba1a2'},
    #         {'domain': '.qq.com', 'expiry': 1918312901, 'httpOnly': False, 'name': 'mobileUV', 'path': '/',
    #          'secure': False, 'value': '1_17537703209_cf311'},
    #         {'domain': '.qq.com', 'expiry': 1603972946, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
    #          'secure': False, 'value': '15193080151'},
    #         {'domain': '.qq.com', 'expiry': 1914147244, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
    #          'secure': False, 'value': '1_1639913117'},
    #         {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
    #          'secure': False, 'value': '6277662720'},
    #         {'domain': '.qq.com', 'expiry': 1908460753, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
    #          'secure': False, 'value': '6b5dfa01d2ed3659'},
    #         {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
    #          'value': 'H2K4eGOjTh'},
    #         {'domain': '.work.weixin.qq.com', 'expiry': 1605975727, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
    #          'path': '/', 'secure': False, 'value': 'zh'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
    #          'value': '1'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
    #          'value': 'direct'},
    #         {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
    #          'secure': False, 'value': '2887538432'}
    #     ]
    #     # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于一个小型的数据库
    #     # 可以通过key, value 把数据存储到shelve中
    #     # db = shelve.open("cookies")
    #     # db['cookie'] = cookies
    #     # db.close()
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     for cookie in cookies:
    #         self.driver.add_cookie(cookie)
    #     self.driver.refresh()
    #     # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    #     sleep(3)
    #
    # def test_shelve(self):
    #     # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于一个小型的数据库
    #     # 可以通过key, value 把数据存储到shelve中
    #     db = shelve.open("cookies")
    #     # db['cookie'] = cookies
    #     # db.close()
    #     cookies = db["cookie"]
    #     db.close()
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     for cookie in cookies:
    #         self.driver.add_cookie(cookie)
    #     self.driver.refresh()
    #     sleep(3)
    #     self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
    #     sleep(2)
    #     self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
    #         "D:\\HogwartsTest15\\testing\\worktest.xlsx")
    #     sleep(2)
    #     filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
    #     print(filename.get_attribute('value'))
    #     assert filename == "worktest.xlsx"
    #     sleep(3)
