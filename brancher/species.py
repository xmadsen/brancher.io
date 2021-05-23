from dataclasses import dataclass


@dataclass
class Species:
    name: str
    wood_type: str
    growth_rate_range: tuple  # feet per year
    first_seed_production: tuple  # years
    final_height_range: tuple  # feet
    lifespan: int  # years
