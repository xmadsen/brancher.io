from brancher.constants import WOOD_EMOJI
from brancher.species import Species
import datetime, time


class Tree:
    def __init__(self, name: str, species: Species):
        self.name = name
        self.species = species
        self.creation_time = time.time()
        self.stage = "seed"

    def age(self) -> int:
        """Return age of tree in seconds."""
        return int(time.time() - self.creation_time)

    def __str__(self):
        blank_line = "│" + " " * 48 + "│"
        return "\n".join(blank_line for _ in range(20)) + "\n"


# class Branch:
