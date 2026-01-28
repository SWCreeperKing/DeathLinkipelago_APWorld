from BaseClasses import Item, ItemClassification
from typing import Dict, List
from .Connections import zones
from .Options import SlimeRancherOptions


class SlimeRancherItem(Item):
    game = "Slime Rancher"

region_unlocks = [f"Region Unlock: {zone}" for zone in zones]

non_progressive_useful_items = {
    "Air Burst": 1,
    "Liquid Slot": 1,
    "Golden Sure Shot": 1,
    "Drone": 4,
    "Advanced Drone": 4,
    "Market Link": 3
}

progressive_useful_item_count = {
    "Progressive Max Health": 4,
    "Progressive Max Ammo": 4,
    "Progressive Run Efficiency": 2,
    "Progressive Market Stonks": 5,  # increase final market value by 5% per
}

progressive_progression_item_count = {
    # "Key": 11,
    "Progressive Max Energy": 3,
    "Progressive Jetpack": 2,  # jetpack + efficiency
    "Progressive Treasure Cracker": 3,
}

filler_items = ["75x Newbucks", "81x Newbucks", "99x Newbucks", "100x Newbucks"]

item_table: Dict[str, ItemClassification] = {
    **{item: ItemClassification.progression for item in region_unlocks},
    **{item: ItemClassification.progression for item in progressive_progression_item_count},
    **{item: ItemClassification.useful for item in non_progressive_useful_items},
    **{item: ItemClassification.useful for item in progressive_useful_item_count},
    **{item: ItemClassification.filler for item in filler_items},
    "Trap Slime": ItemClassification.trap
}

raw_items: List[str] = [item for item, classification in item_table.items()]

def create_items(world):
    pool = world.multiworld.itempool
    options: SlimeRancherOptions = world.options

    for zone in region_unlocks:
        if "Reef" in zone and options.start_with_dry_reef: continue
        world.location_count -= 1
        pool.append(world.create_item(zone))

    for u_progressive, amt in non_progressive_useful_items.items():
        world.location_count -= amt
        for _ in range(amt):
            pool.append(world.create_item(u_progressive))

    for p_useful, amt in progressive_useful_item_count.items():
        world.location_count -= amt
        for _ in range(amt):
            pool.append(world.create_item(p_useful))

    for p_progression, amt in progressive_progression_item_count.items():
        world.location_count -= amt
        for _ in range(amt):
            pool.append(world.create_item(p_progression))

    for _ in range(int(world.location_count * (options.trap_percent / 100))):
        world.location_count -= 1
        pool.append(world.create_item("Trap Slime"))

    for _ in range(world.location_count):
        pool.append(world.create_item(world.random.choice(filler_items)))
