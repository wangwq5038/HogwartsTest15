from frame.frame_demo.base_page import BasePage
from frame.frame_demo.main import Main


class App(BasePage):

    def goto_main(self):
        return Main()
