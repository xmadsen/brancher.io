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

HOUR_IN_SECONDS = 60 * 60
DAY_IN_SECONDS = 24 * HOUR_IN_SECONDS
WEEK_IN_SECONDS = 7 * DAY_IN_SECONDS
MONTH_IN_SECONDS = 30 * WEEK_IN_SECONDS
YEAR_IN_SECONDS = 365 * DAY_IN_SECONDS