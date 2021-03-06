from app.page.app import App


class TestContact:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        """
        添加联系人
        """
        name = "aaaa014"
        gender = "男"
        phonenum = "13512340024"
        result = self.main.goto_address() \
            .click_addmember() \
            .add_member_menual() \
            .add_contact(name, gender, phonenum).get_toast()
        assert '添加成功' == result

    def test_deletecontact(self):
        """
        删除联系人
        :return:
        """
        contactname = 'aaaa011'

        self.main.goto_address() \
            .click_contact(contactname). \
            click_menu(). \
            click_edit_member() \
            .delete_member(). \
            click_ok()
        assert contactname not in self.main.goto_address().driver.page_source

        # print(self.main.goto_address().driver.page_source)
