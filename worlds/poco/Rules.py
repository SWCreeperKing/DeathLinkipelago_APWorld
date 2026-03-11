import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player):
	return {
		"Pickup Magenta Blossom": lambda state: has_item(state, player, "Potato Battery") and has_item(state, player, "Worm Castings"),
		"Pickup Fish": lambda state: has_item(state, player, "Maggot"),
		"Pickup Old Key": lambda state: has_item(state, player, "Feather"),
		"Craft Cyan Pigment": lambda state: has_item(state, player, "Cyan Berries"),
		"Craft Yellow Pigment": lambda state: has_item(state, player, "Yellow Moss"),
		"Craft Magenta Pigment": lambda state: has_item(state, player, "Magenta Blossom"),
		"Craft Red Paint": lambda state: has_item(state, player, "Snail Slime") and has_item(state, player, "Yellow Pigment") and has_item(state, player, "Magenta Pigment") and has_item(state, player, "Cyan Pigment"),
		"Craft Blue Paint": lambda state: has_item(state, player, "Snail Slime") and has_item(state, player, "Yellow Pigment") and has_item(state, player, "Magenta Pigment") and has_item(state, player, "Cyan Pigment"),
		"Craft Green Paint": lambda state: has_item(state, player, "Snail Slime") and has_item(state, player, "Yellow Pigment") and has_item(state, player, "Magenta Pigment") and has_item(state, player, "Cyan Pigment"),
		"Milk Beetle": lambda state: has_item(state, player, "Bucket"),
		"Craft Cooked Fish Dinner": lambda state: has_item(state, player, "Coal") and has_item(state, player, "Match") and has_item(state, player, "Frying Pan") and has_item(state, player, "Fish") and has_item(state, player, "Carrot") and has_item(state, player, "Beetle Milk"),
		"Complete Nari's Quest": lambda state: has_item(state, player, "Magenta Blossom"),
		"Complete Ojet's Quest": lambda state: has_item(state, player, "Red Paint") and has_item(state, player, "Blue Paint") and has_item(state, player, "Green Paint"),
		"Complete Gultch's Quest": lambda state: has_item(state, player, "Cooked Fish Dinner"),
		"Complete Jaz's Quest": lambda state: has_item(state, player, "Pacifier") and has_item(state, player, "Bug Steak") and has_item(state, player, "Dog Treat") and done_quest(state, player, "Cerberus"),
		"Complete Dungsworth's Quest": lambda state: has_item(state, player, "Cymbal Button"),
		"Complete Weevilton's Quest": lambda state: has_item(state, player, "Fancy Button") and has_item(state, player, "Cute Button") and has_item(state, player, "Basic Button"),
		"Complete Cerberus's Quest": lambda state: has_item(state, player, "Pacifier") and has_item(state, player, "Bug Steak") and has_item(state, player, "Dog Treat"),
	}

def has_item(state, player, item) -> bool:
	return state.has(item, player, 1)

def done_quest(state, player, quest) -> bool:
	return state.has(f"{quest}'s Quest Completion", player, 1)