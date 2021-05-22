from brancher.game import Game
from brancher.tree import Tree
from brancher.view import View

if __name__ == "__main__":
    tree = Tree("Schultzy", "Loblolly Pine", "softwood")
    view = View(tree)
    game = Game(view)
    game.run()
