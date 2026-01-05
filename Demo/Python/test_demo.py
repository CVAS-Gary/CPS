import pytest
from demo import deduplicate_and_sort


def test_basic():
    assert deduplicate_and_sort([3, 1, 2, 2]) == [1, 2, 3]


def test_empty():
    assert deduplicate_and_sort([]) == []


def test_non_int_raises():
    with pytest.raises(ValueError):
        deduplicate_and_sort([1, "a", 2])

def test_all_duplicates():
    assert deduplicate_and_sort([2, 2, 2]) == [2]

def test_none_in_list():
    with pytest.raises(ValueError):
        deduplicate_and_sort([None, 1])
