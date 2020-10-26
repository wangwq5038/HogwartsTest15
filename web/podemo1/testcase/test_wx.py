from web.podemo1.page.main_page import MainPage


class TestWx:

    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "aaaaa5"
        account = "bbbbb5_hogwarts"
        phonenum = "13212340005"

        addmember = self.main.goto_addmember()
        addmember.add_member(username, account, phonenum)
        assert username in addmember.get_member()
