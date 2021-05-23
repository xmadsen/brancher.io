from brancher.constants import WOOD_EMOJI
from brancher.species import Species
from brancher.node import RootNode
import datetime, time


class Tree:
    def __init__(self, name: str, species: Species):
        self.name = name
        self.species = species
        self.creation_time = time.time()
        self.stage = "seed"
        self.root_node = RootNode()

    def age(self) -> int:
        """Return age of tree in seconds."""
        return int(time.time() - self.creation_time)

    def __str__(self):
        return str(self.root_node)


# class Branch:
