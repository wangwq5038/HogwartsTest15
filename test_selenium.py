# from selenium.webdriver import ActionChains
# from selenium import webdriver
# driver = webdriver.Chrome()
# action = ActionChains(driver)
# action.send_keys()
#
# action.click(on_element=None)
# action.click_and_hold(on_element=None)
# action.context_click(on_element=None)
# action.double_click(on_element=None)
# action.drag_and_drop(source, target)
# action.drag_and_drop_by_offset(source, xoffset, yoffset)
#
#
# action.key_down(value, element=None)
# ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
#
# action.move_by_offset(xoffset, yoffset)
# action.move_to_element(to_element)
#
# action.move_to_element_with_offset(to_element, xoffset, yoffset)
#
#
#
# action.perform()
#
# action.release(on_element=None)
# action.send_keys(*keys_to_send)
# action.send_keys_to_element(element, *keys_to_send)
from time import sleep

from selenium import webdriver

# def test_handles():
#     driver = webdriver.Chrome()
#     handles = driver.window_handles
#     print(handles)
#     driver.switch_to.window(handles[-1])
# from selenium.webdriver.chrome.options import Options
#
#
# class TestHogwarts:
#     def setup_method(self, method):
#         options = Options()
#         options.debugger_address =
#         # self.driver = webdriver.Chrome()
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(5)
#     def teardown_method(self, method):
#         sleep(3)
#         self.driver.quit()
#
#
#     def test_hogwarts(self):
#         self.driver.get('https://www.baidu.com/')
#         self.driver.find_element_by_id('kw').send_keys('霍格沃兹测试学院')
#         self.driver.find_element_by_id('su').click()
#         self.driver.find_element_by_partial_link_text('测试开发工程师的黄埔军校').click()
#         handles = self.driver.window_handles
#         print(handles)
#         # self.driver.switch_to.window(handles[-1])
#         sleep(2)
#         self.driver.find_element_by_link_text('技术服务').click()




