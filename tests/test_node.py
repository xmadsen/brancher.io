import pytest

from brancher.tree import Tree
from brancher.constants import TREE_SPECIES
from brancher.node import RootNode, TrunkNode


@pytest.fixture
def root_node():
    return RootNode()


def test_root_node_inits_with_no_parent(root_node):
    assert root_node.parent is None


def test_root_node_inits_with_trunk_child(root_node):
    assert isinstance(root_node.trunk, TrunkNode)
