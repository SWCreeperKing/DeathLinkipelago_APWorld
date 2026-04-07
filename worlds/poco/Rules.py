import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player, options):
	return {
		"Pickup Magenta Blossom": lambda state: has(state, player, options, "Potato Battery") and has(state, player, options, "Worm Castings"),
		"Pickup Fish": lambda state: has(state, player, options, "Maggot"),
		"Pickup Old Key": lambda state: has(state, player, options, "Feather"),
		"Craft Cyan Pigment": lambda state: has(state, player, options, "Cyan Berries"),
		"Craft Yellow Pigment": lambda state: has(state, player, options, "Yellow Moss"),
		"Craft Magenta Pigment": lambda state: has(state, player, options, "Magenta Blossom"),
		"Craft Red Paint": lambda state: has(state, player, options, "Snail Slime") and has(state, player, options, "Yellow Pigment") and has(state, player, options, "Magenta Pigment") and has(state, player, options, "Cyan Pigment"),
		"Craft Blue Paint": lambda state: has(state, player, options, "Snail Slime") and has(state, player, options, "Yellow Pigment") and has(state, player, options, "Magenta Pigment") and has(state, player, options, "Cyan Pigment"),
		"Craft Green Paint": lambda state: has(state, player, options, "Snail Slime") and has(state, player, options, "Yellow Pigment") and has(state, player, options, "Magenta Pigment") and has(state, player, options, "Cyan Pigment"),
		"Milk Beetle": lambda state: has(state, player, options, "Bucket"),
		"Craft Cooked Fish Dinner": lambda state: has(state, player, options, "Coal") and has(state, player, options, "Match") and has(state, player, options, "Frying Pan") and has(state, player, options, "Fish") and has(state, player, options, "Carrot") and has(state, player, options, "Beetle Milk"),
		"Pickup Cymbal Button": lambda state: done_quest(state, player, options, "Weevilton"),
		"Complete Nari's Quest": lambda state: has(state, player, options, "Magenta Blossom"),
		"Complete Ojet's Quest": lambda state: has(state, player, options, "Red Paint") and has(state, player, options, "Blue Paint") and has(state, player, options, "Green Paint"),
		"Complete Gultch's Quest": lambda state: has(state, player, options, "Cooked Fish Dinner"),
		"Complete Jaz's Quest": lambda state: has(state, player, options, "Pacifier") and has(state, player, options, "Bug Steak") and has(state, player, options, "Dog Treat") and done_quest(state, player, options, "Cerberus"),
		"Complete Dungsworth's Quest": lambda state: has(state, player, options, "Cymbal Button"),
		"Complete Weevilton's Quest": lambda state: has(state, player, options, "Fancy Button") and has(state, player, options, "Cute Button") and has(state, player, options, "Basic Button"),
		"Complete Cerberus's Quest": lambda state: has(state, player, options, "Pacifier") and has(state, player, options, "Bug Steak") and has(state, player, options, "Dog Treat") and done_quest(state, player, options, "Dungsworth") and done_quest(state, player, options, "Weevilton") and done_quest(state, player, options, "Scuttlesby"),
	}

def get_yaml_option(state, player, options, option) -> bool:
	return options.get_options_map(option).value

def has_amount(state, player, options, item, amount) -> bool:
	return state.has(item, player, amount)

def has(state, player, options, item) -> bool:
	return has_amount(state, player, options, item, 1)

def has_any(state, player, options, items) -> bool:
	return any(has(state, player, options, item) for item in items)

def has_all(state, player, options, items) -> bool:
	return all(has(state, player, options, item) for item in items)

def done_quest(state, player, options, quest) -> bool:
	return has(state, player, options, f"{quest}'s Quest Completion")