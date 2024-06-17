from hot_tea import Hot_tea
from topping import Topping
import pytest


@pytest.fixture
def hot_tea_test():
    return Hot_tea('Jasmine Green Tea', 'Medium', 'No Ice', 'Regular Sugar', 'Green Tea',
                   [Topping('Jasmine Flower', 0.3)])


class Test_HotTea:
    # Test case for calculating the price of Hot Tea
    def test_calculate_price(self, hot_tea_test):
        hot_tea = hot_tea_test
        assert hot_tea.calculate_price() == pytest.approx(4.04, rel=1e-2)

    # Test case for string representation of Hot Tea
    def test_str(self, hot_tea_test):
        hot_tea = hot_tea_test
        assert str(hot_tea) == "HotTea"
