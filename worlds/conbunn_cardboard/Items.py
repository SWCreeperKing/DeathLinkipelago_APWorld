from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

unlocks = [
	"Transition Unlock: Connie's Garden (Cutout Forest)",
	"Transition Unlock: Ribbon Village",
	"Transition Unlock: Origami Tree (Ribbon Village)",
	"Transition Unlock: Paper Bay",
	"Transition Unlock: Cardbun Viewing Area (Paper Bay)",
	"Transition Unlock: Ink Beach (Paper Bay)",
	"Transition Unlock: Bunny Circuit (Ribbon Village)",
	"Transition Unlock: IBee's Honeycomb (Ribbon Village)",
	"Transition Unlock: Cardbun Museum (Ribbon Village)",
	"Transition Unlock: Graffiti Panels (Paint Hills)",
	"Transition Unlock: Cotton Skies (Mountain Confetti)",
	"Transition Unlock: Clay Canyon",
	"Transition Unlock: Samual Golf (Clay Canyon)",
	"Transition Unlock: Sticker Park",
	"Transition Unlock: Dragon Raceway (Sticker Park)",
	"Transition Unlock: Cardboard Station (Sticker Park)",
	"Transition Unlock: Polystyrene Peak",
	"Transition Unlock: Glue Summit (Polystyrene Peak)",
	"Transition Unlock: Cardbun Festival"
]

abilities = [
	"Bounce Pads",
	"Dash"
]

CDs = {
	"CD": 40
}

item_table = {
	**{item: ItemClassification.progression for item in unlocks},
	**{item: ItemClassification.progression for item in abilities},
	**{item: ItemClassification.progression for item in CDs},
	"Cardboard Coin": ItemClassification.filler
}

raw_items = [item for item, classification in item_table.items()]

def gen_create_items(world):
	pool = world.multiworld.itempool
	options = world.options
	for item in unlocks:
		world.location_count -= 1
		pool.append(world.create_item(item))
	for item in abilities:
		world.location_count -= 1
		pool.append(world.create_item(item))
	for item, amt in CDs.items():
		world.location_count -= amt
		for _ in range(amt):
			pool.append(world.create_item(item))
	for _ in range(world.location_count):
		pool.append(world.create_item("Cardboard Coin"))