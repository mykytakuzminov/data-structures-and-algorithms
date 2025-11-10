import pytest
from algorithms.recursion.recursion import sum, max, reverse


# ====== Tests: sum ======
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4], 10),
    ([1.5, 2.5, 3.0], 7.0),
    ([47], 47),
    ([], 0),
])
def test_sum_basic(input_list, expected):
    """Test sum with normal cases, single element, and empty list."""
    assert sum(input_list) == expected


def test_sum_type_error():
    """Check that sum raises TypeError for non-numeric elements."""
    with pytest.raises(TypeError):
        sum([1, "2", 3])


# ====== Tests: max ======
@pytest.mark.parametrize("input_list, expected", [
    ([-2, 4, 9, 7, 3], 9),
    ([3.5, 2.5, 6.0], 6.0),
    ([47], 47),
])
def test_max(input_list, expected):
    """Test max with normal cases and single element."""
    assert max(input_list) == expected


def test_max_value_error():
    """Check that max raises ValueError for an empty list."""
    with pytest.raises(ValueError):
        max([])


def test_max_element_type_error():
    """Check that max raises TypeError for non-numeric elements."""
    with pytest.raises(TypeError):
        max([1, "2", 3])


# ====== Tests: reverse  ======
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4], [4, 3, 2, 1]),
    (['a', 'b', 'c'], ['c', 'b', 'a']),
    ([47], [47]),
    ([], []),
])
def test_reverse_array(input_list, expected):
    """Test reverse with normal cases, single element, and empty list."""
    assert reverse(input_list) == expected
