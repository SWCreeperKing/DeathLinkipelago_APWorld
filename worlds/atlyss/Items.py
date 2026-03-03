from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

any_progressives = {
	"Progressive Any Weapon": 5,
	"Progressive Any Helmet": 6,
	"Progressive Any Cape": 5,
	"Progressive Any Chest Piece": 5,
	"Progressive Any Leggings": 5,
	"Progressive Any Trinket": 6
}

fighter_progressives = {
	"Progressive Fighter Weapon": 6,
	"Progressive Fighter Chest Piece": 3,
	"Progressive Fighter Leggings": 3
}

mystic_progressives = {
	"Progressive Mystic Weapon": 5,
	"Progressive Mystic Helmet": 1,
	"Progressive Mystic Chest Piece": 3,
	"Progressive Mystic Leggings": 2
}

bandit_progressives = {
	"Progressive Bandit Weapon": 6,
	"Progressive Bandit Chest Piece": 3,
	"Progressive Bandit Leggings": 3
}

item_counts_useful = {
	"Tome of Naivety": 2,
	"Tome of Unlearning": 2,
	"Agility Stone": 1,
	"Angela's Tear": 1,
	"Flux Stone": 1,
	"Might Stone": 1,
	"Soul Pearl": 1
}

item_counts_filler = {
	"Black Dye": 1,
	"Blue Dye": 1,
	"Brown Dye": 1,
	"Cyan Dye": 1,
	"Green Dye": 1,
	"Grey Dye": 1,
	"Lime Dye": 1,
	"Orange Dye": 1,
	"Pink Dye": 1,
	"Purple Dye": 1,
	"Red Dye": 1,
	"White Dye": 1,
	"Yellow Dye": 1
}

item_counts_progression = {
	"Epic Carrot": 1,
	"Experience Bond": 1,
	"Illusion Stone": 1
}

item_table = {
	**{item: ItemClassification.progression_skip_balancing for item in any_progressives},
	**{item: ItemClassification.progression_skip_balancing for item in fighter_progressives},
	**{item: ItemClassification.progression_skip_balancing for item in mystic_progressives},
	**{item: ItemClassification.progression_skip_balancing for item in bandit_progressives},
	**{item: ItemClassification.useful for item in item_counts_useful},
	**{item: ItemClassification.filler for item in item_counts_filler},
	**{item: ItemClassification.progression for item in item_counts_progression}
}

raw_items = [item for item, classification in item_table.items()]

def gen_create_items(world):
	pool = world.multiworld.itempool
	options = world.options