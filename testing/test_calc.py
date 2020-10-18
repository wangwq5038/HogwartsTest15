import pytest

from pythoncode.calaulator import Calaulator


class TestDemo:
    def setup_class(self):
        self.cala = Calaulator()
        print("test start")

    def teardowd_class(self):
        print("test end")

    def setup(self):
        print("计算开始")

    def teardown(self):
        print("计算结束")
    # @pytest.mark.login
    @pytest.mark.parametrize('a, b, expect', [[1, 1, 2], [10, 10, 20], [100, 100, 200]])
    def test_add(self, a, b, expect):

        result = self.cala.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [[10, 8, 2], [20, 10, 10], [100, 100, 0]])
    def test_sub(self, a, b, expect):
        result = self.cala.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [[10, 5, 50], [10, 10, 100], [100, 100, 10000]])
    def test_mul(self, a, b, expect):
        result = self.cala.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [[10, 5, 2], [20, 0, 2], [100, 100, 1]])
    def test_div(self, a, b, expect):
        if b != 0:
            result = self.cala.div(a, b)
            assert result == expect
        else:
            print("分母不能为零")

        # with pytest.raises(ZeroDivisionError):
        #     result = self.cala.div(a, b)
        #     assert result == expect
