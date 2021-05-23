import pytest

from brancher.constants import TREE_SPECIES
from brancher.tree import Tree
from brancher.view import View


@pytest.fixture
def view():
    test_tree = Tree(name="Testric Logston", species=TREE_SPECIES["Loblolly Pine"])
    return View(test_tree)


def test_format_tree_in_box_renders_newborn_tree_correctly(view):
    assert view.format_tree_in_box() == (
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│                                                 │\n"
        "│______________________ ▁▂▁ ______________________│\n"
        "│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│"
    )
