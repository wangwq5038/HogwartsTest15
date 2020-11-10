import allure


def handle_black(func):
    def wrapper(*args, **kwargs):
        from frame.base_page import BasePage
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            instance.error_num = 0
            return result
        except Exception as e:
            instance.driver.save_screenshot("tmp.png")
            with open("tmp.png", "rb") as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)

            if instance.error_num > instance.max_num:
                raise e
            instance.error_num += 1
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
