from podemo.page.main_page import MainPage


class TestWx():

    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "aaaaaa10"
        accout = "aaaaaaaa10_hoawarts"
        phonenum = "13512355266"

        addmember = self.main.goto_addmember()
        addmember.add_member(username, accout, phonenum)
        assert username in addmember.add_member()
