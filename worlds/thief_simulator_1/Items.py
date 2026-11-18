import math
from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

unlocks = []

progressive_abilities = {
	"Progressive Appraisal": 4,
	"Progressive Backpack": 4,
	"Progressive Car theft": 3,
	"Progressive Lockpicking": 4,
	"Progressive Agility": 4,
	"Progressive Electronics": 3
}

item_table = {
	**{item: ItemClassification.progression for item in unlocks},
	**{item: ItemClassification.progression for item in progressive_abilities},
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
	for item, amt in progressive_abilities.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(item))
	for _ in range(50):
		world.location_count -= 1
		pool.append(world.create_item("Diamond"))
	for _ in range(world.location_count):
		pool.append(world.create_item("$15"))