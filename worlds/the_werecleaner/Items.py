from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/Werepelago/blob/master/Werepelago/Archipelago/ApShenanigans.cs]

item_table = {
	"Washer": ItemClassification.progression,
	"Vacuum": ItemClassification.progression,
	"Knapper": ItemClassification.progression,
	"Unlock Monday Night": ItemClassification.progression,
	"Unlock Tuesday Night": ItemClassification.progression,
	"Unlock Wednesday Night": ItemClassification.progression,
	"Unlock Thursday Night": ItemClassification.progression,
	"Unlock Friday Night": ItemClassification.progression,
	"Unlock Saturday Night": ItemClassification.progression,
	"Unlock Sunday Night": ItemClassification.progression,
	"Floor Penny": ItemClassification.filler
}

raw_items = [item for item, classification in item_table.items()]

def gen_create_items(world):
	pool = world.multiworld.itempool
	options = world.options
	for item, classification in item_table.items():
	    world.location_count -= 1
	    if item != "Unlock Monday Night":
	        pool.append(world.create_item(item))
	for _ in range(world.location_count):
		pool.append(world.create_item("Floor Penny"))