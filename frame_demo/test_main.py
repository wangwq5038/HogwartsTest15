import pytest

from frame_demo.context import Context


class TestMain:
    context = Context()
    context.load("./tmp.yaml")

    @pytest.mark.parametrize("testcase", context.store.testcase.values(), ids=context.store.testcase.keys())
    def test_main(self, testcase):
        self.context.run_step_by_testcase(testcase)

    # def test_tmp():
    #     print("a")
