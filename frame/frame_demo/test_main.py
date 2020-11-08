from frame.frame_demo.main import Main


class Test_main:

    def test_main(self):
        result = Main().goto_search().click_x().search()
        assert result
