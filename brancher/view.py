from brancher.tree import Tree
from brancher.constants import WOOD_EMOJI


class View:
    def __init__(self, tree: Tree):
        self.tree = tree

    def draw(self):
        header = (
            f"\n    ┌─────────────────────────────┐\n"
            f"    │   {self.tree.name.ljust(8)} {str(self.tree.age()).rjust(8)} seconds │\n"
            f"┏━━━┷━━━━━━━━━━━━┱────────────────┴──────────────┐\n"
            f"┃{(self.tree.wood_type + ' ' + WOOD_EMOJI[self.tree.wood_type]).center(15)}┃{(self.tree.species + ' - ' + self.tree.stage.capitalize()).center(31)}│\n"
            f"┡━━━━━━━━━━━━━━━━┹───────────────────────────────┤\n"
        )
        footer = "└────────────────────────────────────────────────┘"

        output = header + str(self.tree) + footer
        print(output)
