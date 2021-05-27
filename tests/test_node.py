import pytest

from brancher.tree import Tree
from brancher.constants import (
    UNITS_IN_SECONDS,
    TREE_SPECIES,
)
from brancher.node import RootNode, TrunkNode


@pytest.fixture
def root_node():
    return RootNode(species=TREE_SPECIES["Loblolly Pine"])


@pytest.fixture
def trunk_node(root_node):
    return TrunkNode(parent=root_node, species=root_node.species)


def test_root_node_inits_with_no_parent(root_node):
    assert root_node.parent is None


def test_root_node_inits_with_trunk_of_zero_length(root_node):
    assert isinstance(root_node.trunk, TrunkNode)
    assert root_node.trunk.length == 0


def test_trunk_nodes_init_with_no_children(trunk_node):
    assert len(trunk_node.children) == 0


@pytest.mark.parametrize(
    "time,unit",
    [
        (1, "s"),
        (2, "m"),
        (3, "h"),
        (4, "d"),
        (5, "w"),
        (6, "m"),
        (7, "y"),
    ],
)
def test_trunk_node_grows_at_rate(trunk_node, time, unit):
    initial_length = trunk_node.length
    trunk_node.grow(time, unit)
    grown_length = trunk_node.length
    assert (
        grown_length
        == initial_length + (time * UNITS_IN_SECONDS[unit]) * trunk_node.growth_rate
    )
