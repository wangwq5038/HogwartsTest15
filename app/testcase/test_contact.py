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
        name = "aaaa010"
        gender = "男"
        phonenum = "13512340020"
        result = self.main.goto_address() \
            .click_addmember() \
            .add_member_menual() \
            .add_contact(name, gender, phonenum).get_toast()
        assert '添加成功' == result
