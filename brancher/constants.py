from brancher.species import Species

HARDWOOD = "hardwood"
SOFTWOOD = "softwood"

WOOD_EMOJI = {HARDWOOD: "🌳", SOFTWOOD: "🌲"}

TREE_SPECIES = {
    "Loblolly Pine": Species(
        name="Loblolly Pine",
        wood_type=SOFTWOOD,
        first_seed_production=(12, 18),
        growth_rate_range=(2, 3),
        final_height_range=(60, 100),
        lifespan=100,
    ),
    "White Oak": Species(
        name="White Oak",
        wood_type=HARDWOOD,
        first_seed_production=(20, 50),
        growth_rate_range=(0.6, 1),
        final_height_range=(60, 100),
        lifespan=100,
    ),
}
