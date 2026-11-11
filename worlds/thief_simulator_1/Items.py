import math
from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

unlocks = []

items = [
	"DIY Simple Lockpick",
	"Lockpick",
	"Climbing Gloves",
	"Mini electric lock pick",
	"Jewelry tools",
	"Safecracking tools",
	"Glass knife",
	"Hacking tools",
	"Car lock pick gun",
	"Hacking PDA",
	"Car key signal cloner",
	"Round lockpick",
	"Hacking laptop",
	"Hacking laptop Pro",
	"Bolt Cutters",
	"Van"
]

item_table = {
	**{item: ItemClassification.progression for item in unlocks},
	**{item: ItemClassification.progression for item in items},
	"$15": ItemClassification.filler,
	"Diamond": ItemClassification.progression
}

raw_items = [item for item, classification in item_table.items()]

def gen_create_items(world):
	pool = world.multiworld.itempool
	options = world.options
	for item in unlocks:
		world.location_count -= 1
		pool.append(world.create_item(item))
	for item in items:
		world.location_count -= 1
		pool.append(world.create_item(item))
	for _ in range(50):
		world.location_count -= 1
		pool.append(world.create_item("Diamond"))
	for _ in range(world.location_count):
		pool.append(world.create_item("$15"))