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
        ).center(32)
        tree_in_box = self.format_tree_in_box()
        self.ui_text = UI_TEXT.substitute(
            name=self.tree.name.ljust(8),
            age=str(self.tree.age()).rjust(8),
            wood_detail=wood_detail,
            species_detail=species_detail,
            tree=tree_in_box,
        )

    def draw(self):
        self.update()
        print(self.ui_text)

    def format_tree_in_box(self):
        rows = []
        rows.append("│" + "░" * 49 + "│")
        rows.append("│" + str(self.tree).center(49, "_") + "│")
        for _ in range(14):
            rows.append("│                                                 │")

        tree_in_box = "\n".join(reversed(rows))

        return tree_in_box
