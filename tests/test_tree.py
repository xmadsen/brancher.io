# -*- coding: utf-8 -*-
import pytest

from brancher.tree import Tree
from brancher.constants import TREE_SPECIES


@pytest.fixture
def test_tree():
    return Tree(name="Testric Logston", species=TREE_SPECIES["Loblolly Pine"])


def test_can_create_tree(test_tree):
    assert isinstance(test_tree, Tree)


# def
# @pytest.fixture
# def draw():


# def test_setup_fails(something, other):
#     pass


# def test_call_fails(something):
#     assert 0


# def test_fail2():
#     assert 0
