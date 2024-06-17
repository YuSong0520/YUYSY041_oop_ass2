import pytest
from fruit_tea import Fruit_tea
from topping import Topping


# Fixtures for creating instances of different types of teas with toppings
@pytest.fixture
def fruit_tea_test():
    return Fruit_tea('Large', True, False, [Topping('Popping Boba', 0.5), Topping('Jelly', 0.3)])


# Test classes for each type of tea, using pytest
class Test_FruitTea:
    # Test case for calculating the price of Fruit Tea
    def test_calculate_price(self, fruit_tea_test):
        fruit_tea = fruit_tea_test
        assert fruit_tea.calculate_price() == pytest.approx(4.34, rel=1e-2)

    # Test case for string representation of Fruit Tea
    def test_str(self, fruit_tea_test):
        fruit_tea = fruit_tea_test
        assert str(fruit_tea) == "Fruit_tea, Fruity: True, Milky: False"
