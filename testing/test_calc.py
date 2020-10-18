import pytest
import yaml

from pythoncode.calaulator import Calaulator


def get_data():
    with open("data.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    sub_datas = datas['sub']['datas']
    mul_datas = datas['mul']['datas']
    div_datas = datas['div']['datas']
    div_ids = datas['div']['ids']
    return [add_datas, add_ids, sub_datas, mul_datas, div_datas, div_ids]


class TestDemo:
    cala = Calaulator()

    # def setup_class(self):
    #     self.cala = Calaulator()
    #     print("test start")
    #
    # def teardowd_class(self):
    #     print("test end")
    #
    # def setup(self):
    #     print("计算开始")
    #
    # def teardown(self):
    #     print("计算结束")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a, b, expect', get_data()[0], ids=get_data()[1])
    def test_add(self, a, b, expect, open_start):

        result = self.cala.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, expect', get_data()[2])
    def test_sub(self, a, b, expect, open_start):
        result = self.cala.sub(a, b)
        assert result == expect

    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('a, b, expect', get_data()[3])
    def test_mul(self, a, b, expect, open_start):
        result = self.cala.mul(a, b)
        assert result == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expect', get_data()[4], ids=get_data()[5])
    def test_div(self, a, b, expect, open_start):
        if b != 0:
            result = self.cala.div(a, b)
            assert result == expect
        else:
            print("分母不能为零")

        # with pytest.raises(ZeroDivisionError):
        #     result = self.cala.div(a, b)
        #     assert result == expect
