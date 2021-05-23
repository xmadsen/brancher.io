class Node:
    def __init__(self, parent):
        self.parent = parent


class RootNode(Node):
    def __init__(self):
        super().__init__(parent=None)
        self.trunk = TrunkNode(parent=self, length=0)

    def __str__(self):
        return " ▁▂▁ "


class TrunkNode(Node):
    def __init__(self, parent, length):
        super().__init__(parent)
        self.length = length
