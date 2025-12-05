from BaseClasses import Item, ItemClassification
from typing import Dict, List
from .Connections import zones


class SlimeRancherItem(Item):
	game = "Slime Rancher"

region_unlocks = [f"Region Unlock: {zone}" for zone in zones]

non_progressive_useful_items = [
	"Air Burst",
	"Liquid Slot",
	"Golden Sure Shot"
]

progressive_useful_item_count = {
	"Progressive Max Health": 4,
	"Progressive Max Ammo": 4,
	"Progressive Run Efficiency": 2,
}

progressive_progression_item_count = {
	# "Key": 11,
	"Progressive Max Energy": 3,
	"Progressive Jetpack": 2,  # jetpack + efficiency
	"Progressive Treasure Cracker": 3,
}

filler_items = ["Slime Plush", "25x Newbucks", "50x Newbucks", "75x Newbucks", "100x Newbucks"]

item_table: Dict[str, ItemClassification] = {
	**{item: ItemClassification.progression for item in region_unlocks},
	**{item: ItemClassification.progression for item in progressive_progression_item_count},
	**{item: ItemClassification.useful for item in non_progressive_useful_items},
	**{item: ItemClassification.useful for item in progressive_useful_item_count},
	**{item: ItemClassification.filler for item in filler_items},
}

raw_items: List[str] = [item for item, classification in item_table.items()]

def create_items(world):
	pool = world.multiworld.itempool
	options = world.options

	for zone in region_unlocks:
		if "Reef" in zone and options.start_with_dry_reef: continue
		world.location_count -= 1
		pool.append(world.create_item(zone))

	for u_progressive in non_progressive_useful_items:
		world.location_count -= 1
		pool.append(world.create_item(u_progressive))

	for p_useful, amt in progressive_useful_item_count.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(p_useful))

	for p_progression, amt in progressive_progression_item_count.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(p_progression))

	for _ in range(world.location_count):
		pool.append(world.create_item(world.random.choice(filler_items)))
