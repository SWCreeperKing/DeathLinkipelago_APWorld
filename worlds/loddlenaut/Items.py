from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

progression_items = {
	"Oxygen Upgrade": 3,
	"Boost Duration Module": 1,
	"Scanner Pointer Module": 1,
	"Puddle Scrubber": 1,
	"Blaster Module": 1,
	"Scrap Vac": 1,
	"Scanner Range Module": 1,
	"Laser Efficiency Module": 1,
	"Inventory Capacity Module": 1,
	"Microplastics Capacity Module": 1,
	"Depth Resistance Module": 1,
	"Scrubber Radius Module": 1,
	"Global Pollution Module": 1,
	"Cooking Module": 1
}

filler_items = {
	"Light Beacon": 15,
	"Water Purifier": 15,
	"Plant Pollinator": 15
}

useful_items = {
	"Recharge Ring": 10
}

region_unlocks = [
	"GUPPI Ravine",
	"GUPPI Campus",
	"North of GUPPI Campus",
	"North GUPPI Ravine",
	"Tangle Bay",
	"East of Flotsam Flats",
	"Flotsam Flats",
	"North of Flotsam Flats",
	"Grimy Gulf",
	"West of Grimy Gulf",
	"Goddle Grotto Entrance",
	"Goddle Grotto"
]

item_table = {
	**{item: ItemClassification.progression for item in progression_items},
	**{item: ItemClassification.filler for item in filler_items},
	**{item: ItemClassification.useful for item in useful_items},
	**{item: ItemClassification.progression for item in region_unlocks}
}

raw_items = [item for item, classification in item_table.items()]

def gen_create_items(world):
	pool = world.multiworld.itempool
	options = world.options
	for item in region_unlocks:
		world.location_count -= 1
		pool.append(world.create_item(item))
	for item, amt in progression_items.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(item))
	for item, amt in useful_items.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(item))
	for _ in range(world.location_count):
		pool.append(world.create_item(world.random.choice(list(filler_items.keys()))))