from brancher.constants import UNITS_IN_SECONDS, YEAR_IN_SECONDS
import random


class Node:
    def __init__(self, species, parent):
        self.species = species
        self.parent = parent


class RootNode(Node):
    def __init__(self, species):
        super().__init__(species, parent=None)
        self.trunk = TrunkNode(species=self.species, parent=self, length=0)

    def __str__(self):
        return " ▁▂▁ "


class TrunkNode(Node):
    def __init__(self, species, parent, length=0):
        super().__init__(species, parent)
        self.length = length
        self.children = []
        self.growth_rate = (
            (
                species.growth_rate_range[0]
                + (species.growth_rate_range[1] - species.growth_rate_range[0])
                * random.random()
            )
            / 12
            / YEAR_IN_SECONDS
        )

    def grow(self, time: int, unit: str):
        assert unit in UNITS_IN_SECONDS

        duration = float(time * UNITS_IN_SECONDS[unit])
        self.length += self.growth_rate * duration
