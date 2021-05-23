from brancher.game import Game
from brancher.tree import Tree
from brancher.view import View
from brancher.constants import TREE_SPECIES

if __name__ == "__main__":
    tree = Tree("Schultzy", TREE_SPECIES["Loblolly Pine"])
    view = View(tree)
    game = Game(view)
    game.run()
