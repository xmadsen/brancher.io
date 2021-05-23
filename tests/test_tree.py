import pytest
import os

from brancher.tree import Tree
from brancher.constants import TREE_SPECIES
from brancher.node import RootNode


@pytest.fixture
def test_tree():
    return Tree(name="Testric Logston", species=TREE_SPECIES["Loblolly Pine"])


def test_tree_starts_with_root_node(test_tree):
    assert isinstance(test_tree.root_node, RootNode)


def test_tree_save_to_file(test_tree):
    test_tree.save()
    assert os.path.exists(".tree_Testric Logston.pkl")


def test_tree_loads_from_pickle(test_tree):
    before_tree = test_tree
    test_tree.save()
    after_tree = Tree.load(".tree_Testric Logston.pkl")

    assert before_tree == after_tree
