from brancher.constants import WOOD_EMOJI
from brancher.species import Species
from brancher.node import RootNode
import datetime, time
import pickle


class Tree:
    def __init__(self, name: str, species: Species):
        self.name = name
        self.species = species
        self.creation_time = int(time.time())
        self.stage = "seed"
        self.root_node = RootNode(species=self.species)
        self.age_secs = 0
        self.last_live_time = int(self.creation_time)

    def save(self):
        self.age_secs += int(time.time() - self.last_live_time)
        self.last_live_time = int(time.time())
        with open(f".tree_{self.name}.pkl", "wb") as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def tick(self):
        self.age_secs += int(time.time() - self.last_live_time)
        self.last_live_time = int(time.time())

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
