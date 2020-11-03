
from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "aaaa21"
        account = "aaaaaa21_hogwarts"
        phonenum = "13412340021"

        addmember = self.main.goto_addmember()
        addmember.add_member(username, account, phonenum)
        assert username in addmember.get_member(username)
