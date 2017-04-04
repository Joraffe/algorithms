import pytest
from array_algorithms import binary_search


@pytest.fixture
def new_arr():
  return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def test_binary_search(new_arr):
  assert binary_search(new_arr, 3) == 2
  assert binary_search(new_arr, 5) == 4
  assert binary_search(new_arr, 11) == 10
