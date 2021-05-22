from brancher.constants import WOOD_EMOJI, SEED
import datetime, time


class Tree:
    def __init__(self, name: str, species: str, wood_type: str):
        self.name = name
        self.species = species

        assert wood_type in [
            "softwood",
            "hardwood",
        ], "Tree must be either a hardwood or softwood."
        self.wood_type = wood_type

        self.creation_time = time.time()
        self.stage = SEED

    def age(self) -> int:
        """Return age of tree in seconds."""
        return int(time.time() - self.creation_time)

    def __str__(self):
        blank_line = "│" + " " * 48 + "│"
        return "\n".join(blank_line for _ in range(20)) + "\n"
