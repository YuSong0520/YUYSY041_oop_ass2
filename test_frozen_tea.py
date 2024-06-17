from frozen_tea import Frozen_tea
from topping import Topping
import pytest


@pytest.fixture
def frozen_tea_test():
    return Frozen_tea('Strawberry Frozen Tea', 'Large', 'Regular Ice', 'Less Sugar', 'Green Tea', True, False,
                      [Topping('Strawberry Popping Boba', 0.5)])


# Test classes for each type of tea, using pytest

class Test_FrozenTea:
    # Test case for calculating the price of Frozen Tea
    def test_calculate_price(self, frozen_tea_test):
        frozen_tea = frozen_tea_test
        assert frozen_tea.calculate_price() == pytest.approx(5.74, rel=1e-2)

    # Test case for string representation of Frozen Tea
    def test_str(self, frozen_tea_test):
        frozen_tea = frozen_tea_test
        assert str(frozen_tea) == "FrozenTea, Fruity: False, Milky: True"
