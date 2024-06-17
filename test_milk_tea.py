import pytest
from milk_tea import Milk_tea
from topping import Topping


@pytest.fixture
def milk_tea_test():
    return Milk_tea('Classic Milk Tea', 'Large', 'Regular Ice', 'Less Sugar', 'Black Tea', 'Thai',
                    [Topping('Pearls', 0.4), Topping('Pudding', 0.5)])


class Test_MilkTea:
    # Test case for calculating the price of Milk Tea
    def test_calculate_price(self, milk_tea_test):
        milk_tea = milk_tea_test
        assert milk_tea.calculate_price() == pytest.approx(5.95, rel=1e-2)

    # Test case for string representation of Milk Tea
    def test_str(self, milk_tea_test):
        milk_tea = milk_tea_test
        assert str(milk_tea) == "MilkTea, Flavour: Thai"
