from brancher.constants import WOOD_EMOJI
from brancher.species import Species
from brancher.node import RootNode
import datetime, time
import pickle


class Tree:
    def __init__(self, name: str, species: Species):
        self.name = name
        self.species = species
        self.creation_time = time.time()
        self.stage = "seed"
        self.root_node = RootNode()
        self.age_secs = 0

    def age(self) -> int:
        """Return age of tree in seconds."""
        return int(time.time() - self.age_secs)

    def save(self):
        self.age_secs = self.age()
        with open(f".tree_{self.name}.pkl", "wb") as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def tick(self):
        self.age_secs = self.age()

    @classmethod
    def load(self, pickled_tree_path):
        with open(pickled_tree_path, "rb") as f:
            return pickle.load(f)

    def __str__(self):
        return str(self.root_node)

    def __eq__(self, other):
        if isinstance(other, Tree):
            return (
                self.name == other.name
                and self.species == other.species
                and self.creation_time == other.creation_time
                and self.age_secs == other.age_secs
            )
        return False


# class Branch:
