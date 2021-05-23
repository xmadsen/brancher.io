from brancher.tree import Tree
from brancher.constants import WOOD_EMOJI
from brancher.ui import UI_TEXT


class View:
    def __init__(self, tree: Tree):
        self.tree = tree
        self.update()

    def update(self):
        wood_detail = (
            self.tree.species.wood_type + " " + WOOD_EMOJI[self.tree.species.wood_type]
        ).center(15)
        species_detail = (
            self.tree.species.name + " - " + self.tree.stage.capitalize()
        ).center(31)
        self.ui_text = UI_TEXT.substitute(
            name=self.tree.name.ljust(8),
            age=str(self.tree.age()).rjust(8),
            wood_detail=wood_detail,
            species_detail=species_detail,
            tree=self.tree,
        )

    def draw(self):
        self.update()
        print(self.ui_text)
