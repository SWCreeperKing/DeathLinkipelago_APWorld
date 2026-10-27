import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player, options):
	return {
		"Cook: Coral Cannoli": lambda state: has(state, player, options, "Pearl Berries") and has(state, player, options, "Star Kelp") and has(state, player, options, "Coral Pear") and has(state, player, options, "Tubey Melon"),
		"Cook: Coral Nut Bread": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Tubey Melon") and has(state, player, options, "Lily Banana"),
		"Cook: Crispy Cookie": lambda state: has(state, player, options, "Crystal Crisp") and has(state, player, options, "Lily Banana") and has(state, player, options, "Star Kelp"),
		"Cook: Fishy Candy": lambda state: has(state, player, options, "Lily Banana") and has(state, player, options, "Coral Pear"),
		"Cook: Kelp Coffee Drop": lambda state: has(state, player, options, "Passion Fig") and has(state, player, options, "Kelp Heart") and has(state, player, options, "Star Kelp"),
		"Cook: Kelp Taco": lambda state: has(state, player, options, "Star Kelp") and has(state, player, options, "Kelp Heart") and has(state, player, options, "Coral Pear") and has(state, player, options, "Lily Banana"),
		"Cook: Kiwi Lime Pie": lambda state: has(state, player, options, "Lotus Kiwi") and has(state, player, options, "Pearl Berries"),
		"Cook: Rainbow Kelp Pie": lambda state: has(state, player, options, "Rainbow Star Kelp") and has(state, player, options, "Pearl Berries") and has(state, player, options, "Coral Nut Bread"),
		"Cook: Starfish Sandwich": lambda state: has(state, player, options, "Kelp Heart") and has(state, player, options, "Tubey Melon") and has(state, player, options, "Lotus Kiwi"),
		"Cook: Tropical Jelly": lambda state: has(state, player, options, "Tubey Melon") and has(state, player, options, "Lily Banana"),
		"Angler": lambda state: has(state, player, options, "Tubey Melon") and has(state, player, options, "Pearl Berries") and has(state, player, options, "Lily Banana") and has(state, player, options, "Star Kelp") and has(state, player, options, "Lotus Kiwi"),
		"Axo": lambda state: has(state, player, options, "Passion Fig") and has(state, player, options, "Coral Pear") and has(state, player, options, "Lotus Kiwi") and has(state, player, options, "Crystal Crisp") and has(state, player, options, "Crispy Cookie") and has(state, player, options, "Starfish Sandwich"),
		"Betta": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Kelp Heart") and has(state, player, options, "Passion Fig"),
		"Bunny": lambda state: has(state, player, options, "Lily Banana") and has(state, player, options, "Passion Fig"),
		"Butterfly": lambda state: has(state, player, options, "Lily Banana") and has(state, player, options, "Kelp Heart") and has(state, player, options, "Passion Fig") and has(state, player, options, "Kelp Coffee Drop"),
		"Manta": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Passion Fig") and has(state, player, options, "Starfish Sandwich"),
		"Octo": lambda state: has(state, player, options, "Lily Banana") and has(state, player, options, "Lotus Kiwi") and has(state, player, options, "Passion Fig") and has(state, player, options, "Pearl Berries") and has(state, player, options, "Coral Cannoli"),
		"Puffer": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Crystal Crisp") and has(state, player, options, "Lotus Kiwi") and has(state, player, options, "Tubey Melon") and has(state, player, options, "Star Kelp") and has(state, player, options, "Kiwi Lime Pie") and has(state, player, options, "Tropical Jelly"),
		"Siren": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Tubey Melon") and has(state, player, options, "Kelp Heart") and has(state, player, options, "Star Kelp") and has(state, player, options, "Rainbow Star Kelp") and has(state, player, options, "Kelp Taco") and has(state, player, options, "Tropical Jelly"),
		"Snake": lambda state: has(state, player, options, "Tubey Melon") and has(state, player, options, "Lily Banana"),
		"Wingfin": lambda state: has(state, player, options, "Lily Banana") and has(state, player, options, "Rainbow Star Kelp") and has(state, player, options, "Tubey Melon") and has(state, player, options, "Star Kelp") and has(state, player, options, "Kelp Heart"),
		"Whisker": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Tubey Melon") and has(state, player, options, "Star Kelp") and has(state, player, options, "Tropical Jelly"),
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

def has_depth(state, player, options) -> bool:
	return has(state, player, options, "Depth Resistance Module")