from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

items = [
	"Axe",
	"Cog",
	"Coal",
	"Carrot",
	"Worm Castings",
	"Fancy Button",
	"Coin",
	"Cute Button",
	"Feather",
	"Snail Slime",
	"Valve Handle",
	"Potato Battery",
	"Yellow Moss",
	"Spoon",
	"Basic Button",
	"Match",
	"Maggot",
	"Bone Key",
	"Magenta Blossom",
	"Yellow Pigment",
	"Magenta Pigment",
	"Fish",
	"Old Key",
	"Frying Pan",
	"Machete",
	"Cyan Berries",
	"Cyan Pigment",
	"Red Paint",
	"Blue Paint",
	"Green Paint",
	"Bucket",
	"Beetle Milk",
	"Cooked Fish Dinner",
	"Rope",
	"Golden Key",
	"Cymbal Button",
	"Dog Treat",
	"Bug Steak",
	"Pacifier"
]

item_table = {
	**{item: ItemClassification.progression for item in items},
	"Clown Nose": ItemClassification.filler
}

raw_items = [item for item, classification in item_table.items()]

def gen_create_items(world):
	pool = world.multiworld.itempool
	options = world.options
	for item in items:
		world.location_count -= 1
		pool.append(world.create_item(item))
	for _ in range(world.location_count):
		pool.append(world.create_item("Clown Nose"))