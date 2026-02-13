from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

region_unlocks = [
	"Region Unlock: The Lab",
	"Region Unlock: The Overgrowth",
	"Region Unlock: The Grotto",
	"Region Unlock: Dry Reef",
	"Region Unlock: Indigo Quarry",
	"Region Unlock: Moss Blanket",
	"Region Unlock: Ancient Ruins Transition",
	"Region Unlock: Ancient Ruins",
	"Region Unlock: Glass Desert"
]

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
	"Progressive Market Stonks": 5
}

progressive_progression_item_count = {
	"Progressive Max Energy": 3,
	"Progressive Jetpack": 2,
	"Progressive Treasure Cracker": 3
}

filler_items = [
	"75x Newbucks",
	"81x Newbucks",
	"99x Newbucks",
	"100x Newbucks"
]

item_table = {
	**{item: ItemClassification.progression for item in region_unlocks},
	**{item: ItemClassification.useful for item in non_progressive_useful_items},
	**{item: ItemClassification.useful for item in progressive_useful_item_count},
	**{item: ItemClassification.progression for item in progressive_progression_item_count},
	**{item: ItemClassification.filler for item in filler_items},
	"Trap Slime": ItemClassification.trap
}

raw_items = [item for item, classification in item_table.items()]

def gen_create_items(world):
	pool = world.multiworld.itempool
	options = world.options
	for zone in region_unlocks:
	    if "Reef" in zone and options.start_with_dry_reef: continue
	    world.location_count -= 1
	    pool.append(world.create_item(zone))
	
	for item, amt in non_progressive_useful_items.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(item))
	
	for item, amt in progressive_useful_item_count.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(item))
	
	for item, amt in progressive_progression_item_count.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(item))
	
	for _ in range(int(world.location_count * (options.trap_percent / 100))):
		world.location_count -= 1
		pool.append(world.create_item("Trap Slime"))
	
	for _ in range(world.location_count):
		pool.append(world.create_item(world.random.choice(filler_items)))