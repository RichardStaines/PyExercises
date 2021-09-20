import factory_filter
import pytest


@pytest.mark.parametrize("data, expected_result",
                          [([5, 18, 4, 3, 2], 3),
                           ([5, 18, 5, 4, 3, 2], 4),
                           ([15, 2], 2),
                          ]
                         )
def test_factory_filter(data, expected_result):
    result = factory_filter.factory_filter(data)
    assert  result == expected_result
