import pytest
from sparkling_tea import Sparkling_tea
from topping import Topping


@pytest.fixture
def sparkling_tea_test():
    return Sparkling_tea('Lychee Sparkling Tea', 'Large', 'Regular Ice', 'Regular Sugar', 'Green Tea',
                         [Topping('Lychee Jelly', 0.4)])


class Test_SparklingTea:
    # Test case for calculating the price of Sparkling Tea
    def test_calculate_price(self, sparkling_tea_test):
        sparkling_tea = sparkling_tea_test
        assert sparkling_tea.calculate_price() == pytest.approx(4.94, rel=1e-2)

    # Test case for string representation of Sparkling Tea
    def test_str(self, sparkling_tea_test):
        sparkling_tea = sparkling_tea_test
        assert str(sparkling_tea) == "SparklingTea"
