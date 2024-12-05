import pytest

from src.fair_sharer import fair_sharer

@pytest.mark.parametrize("values, num_iterations, expected_distribution",
                          [([0, 1000, 800, 0], 1, [100, 800, 900, 0]),
                           ([0, 1000, 800, 0], 2, [100, 890, 720, 90]),
                           ([1000, 0, 0, 0], 1, [800, 100, 0, 100]),
                           ([1000, 0, 0, 0], 2, [640, 180, 0, 180]),
                           ([1000, 0, 0, 0], 3, [512, 244, 0, 244]),
                           ([1000, 0, 0, 0], 4, [409.6, 295.2, 0, 295.2])])
def test_fair_sharer(values, num_iterations, expected_distribution):
    assert fair_sharer(values, num_iterations) == expected_distribution