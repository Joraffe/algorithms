import pytest
from tree_algorithms import Tree


@pytest.fixture
def new_tree():
  root = Tree(1)
  b2 = root.add_child(2)
  b3 = root.add_child(3)
  l4 = b2.add_child(4)
  l5 = b2.add_child(5)
  l6 = b3.add_child(6)
  l7 = b3.add_child(7)
  return root


def test_breadth_first_search(new_tree):
  assert new_tree.breadth_first_search(2).value == 2
  assert len(new_tree.breadth_first_search(2).children) == 2
  assert new_tree.breadth_first_search(3).value == 3
  assert len(new_tree.breadth_first_search(3).children) == 2
  assert new_tree.breadth_first_search(7).value == 7
  assert len(new_tree.breadth_first_search(7).children) == 0


def test_depth_first_search(new_tree):
  assert new_tree.depth_first_search(2).value == 2
  assert len(new_tree.depth_first_search(2).children) == 2

  assert new_tree.depth_first_search(3).value == 3
  assert len(new_tree.depth_first_search(3).children) == 2

  assert new_tree.depth_first_search(7).value == 7
  assert len(new_tree.depth_first_search(7).children) == 0
