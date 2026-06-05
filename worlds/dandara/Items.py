from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

progression_items = {
	"FearKey": 1,
	"FreeNara": 1,
	"TimeFlag": 1,
	"Boss StoryEvent Key 1": 1,
	"Boss StoryEvent Key 2": 1,
	"Stone of Creation": 1,
	"Rock of Remembrance": 1,
	"Stone of Intention": 1,
	"Pearl of Dreams": 1,
	"Shell Mirror": 1,
	"Heart of the Great Salt": 17,
	"Scarf of Freedom": 1,
	"Essence of Salt": 9,
	"Infusion of Salt": 9,
	"Essence of Salt Enhancer": 6,
	"Infusion of Salt Enhancer": 6,
	"Jonny B. Missiles": 1,
	"Anxiety Shock": 1,
	"Memories Shaft": 1,
	"Logic Blast": 1,
	"Skin Knitter": 1,
	"Displaced Presence": 1,
	"Paint Platform": 1,
	"Music Platform": 1,
	"DLC StoryEvent 1": 1,
	"DLC StoryEvent 2": 1,
	"DLC StoryEvent 3": 1,
	"DLC StoryEvent 4": 1,
	"DLC StoryEvent 5": 1,
	"DLC StoryEvent 6": 1,
	"DLC StoryEvent 7": 1,
	"Wall Break": 1,
	"Essence Enhancer Permit": 1,
	"Infusion Enhancer Permit": 1,
	"Freedom Enhancer Permit": 1,
	"Heart Enhancer Permit": 1
}

useful_items = {
	"Map": 1,
	"Bracers of the Patient": 1,
	"Arrow of Freedom": 1,
	"Salt's Awareness": 1
}

filler_items = {
	"Pleas of the Salt Fear": 24,
	"Pleas of the Salt": 44
}

item_table = {
	**{item: ItemClassification.progression for item in progression_items},
	**{item: ItemClassification.useful for item in useful_items},
	**{item: ItemClassification.filler for item in filler_items},
	"Salt": ItemClassification.filler
}

raw_items = [item for item, classification in item_table.items()]

def gen_create_items(world):
	pool = world.multiworld.itempool
	options = world.options
	for item, amt in progression_items.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(item))
	for item, amt in useful_items.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(item))
	for item, amt in filler_items.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(item))
	for _ in range(world.location_count):
		pool.append(world.create_item("Salt"))