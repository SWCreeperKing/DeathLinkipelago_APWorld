import math
from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

crates = [
	"Crate 1",
	"Crate 2",
	"Crate 3",
	"Crate 4",
	"Crate 5",
	"Crate 6",
	"Crate 7",
	"Crate 8",
	"Crate 9",
	"Crate 10",
	"Crate 11",
	"Crate 12",
	"Crate 13",
	"Crate 14",
	"Crate 15",
	"Crate 16",
	"Crate 17",
	"Crate 18",
	"Crate 19",
	"Crate 20",
	"Crate 21",
	"Crate 22",
	"Crate 23",
	"Crate 24",
	"Crate 25",
	"Crate 26",
	"Crate 27",
	"Crate 28"
]

item_table = {
	**{item: ItemClassification.progression for item in crates},
	"Dust": ItemClassification.filler
}

raw_items = [item for item, classification in item_table.items()]

def gen_create_items(world):
	pool = world.multiworld.itempool
	options = world.options
	for item in crates:
		world.location_count -= 1
		pool.append(world.create_item(item))
	if world.enable_local_fill:
		fill = min(math.ceil(world.location_count * (options.local_fill.value/100)), len(world.local_fill_loc))
		world.location_count -= fill
		world.local_location_count += fill
	for _ in range(world.location_count):
		pool.append(world.create_item("Dust"))