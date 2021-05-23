import pytest

from brancher.tree import Tree
from brancher.constants import TREE_SPECIES
from brancher.node import RootNode


@pytest.fixture
def test_tree():
    return Tree(name="Testric Logston", species=TREE_SPECIES["Loblolly Pine"])


def test_tree_starts_with_root_node(test_tree):
    assert isinstance(test_tree.root_node, RootNode)
