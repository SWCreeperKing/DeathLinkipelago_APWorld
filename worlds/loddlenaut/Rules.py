import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player, options):
	return {
		"Clean GUPPI Campus 25%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module") and has(state, player, options, "Scrap Vac") and has(state, player, options, "Depth Resistance Module"),
		"Clean GUPPI Campus 50%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module") and has(state, player, options, "Scrap Vac") and has(state, player, options, "Depth Resistance Module"),
		"Clean GUPPI Campus 75%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module") and has(state, player, options, "Scrap Vac") and has(state, player, options, "Depth Resistance Module"),
		"Clean GUPPI Campus 100%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module") and has(state, player, options, "Scrap Vac") and has(state, player, options, "Depth Resistance Module"),
		"Clean Tangle Bay 25%": lambda state: has(state, player, options, "Blaster Module") and has(state, player, options, "Scrap Vac"),
		"Clean Tangle Bay 50%": lambda state: has(state, player, options, "Blaster Module") and has(state, player, options, "Scrap Vac"),
		"Clean Tangle Bay 75%": lambda state: has(state, player, options, "Blaster Module") and has(state, player, options, "Scrap Vac"),
		"Clean Tangle Bay 100%": lambda state: has(state, player, options, "Blaster Module") and has(state, player, options, "Scrap Vac"),
		"Clean Flotsam Flats 25%": lambda state: has(state, player, options, "Blaster Module"),
		"Clean Flotsam Flats 50%": lambda state: has(state, player, options, "Blaster Module"),
		"Clean Flotsam Flats 75%": lambda state: has(state, player, options, "Blaster Module"),
		"Clean Flotsam Flats 100%": lambda state: has(state, player, options, "Blaster Module"),
		"Clean Grimy Gulf 25%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module"),
		"Clean Grimy Gulf 50%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module"),
		"Clean Grimy Gulf 75%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module"),
		"Clean Grimy Gulf 100%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module"),
		"Clean Goddle Grotto 25%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module"),
		"Clean Goddle Grotto 50%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module"),
		"Clean Goddle Grotto 75%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module"),
		"Clean Goddle Grotto 100%": lambda state: has(state, player, options, "Puddle Scrubber") and has(state, player, options, "Blaster Module"),
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
		"Evolve: Angler": lambda state: has(state, player, options, "Tubey Melon") and has(state, player, options, "Pearl Berries") and has(state, player, options, "Lily Banana") and has(state, player, options, "Star Kelp") and has(state, player, options, "Lotus Kiwi"),
		"Evolve: Axo": lambda state: has(state, player, options, "Passion Fig") and has(state, player, options, "Coral Pear") and has(state, player, options, "Lotus Kiwi") and has(state, player, options, "Crystal Crisp") and has(state, player, options, "Crispy Cookie") and has(state, player, options, "Starfish Sandwich"),
		"Evolve: Betta": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Kelp Heart") and has(state, player, options, "Passion Fig"),
		"Evolve: Bunny": lambda state: has(state, player, options, "Lily Banana") and has(state, player, options, "Passion Fig"),
		"Evolve: Butterfly": lambda state: has(state, player, options, "Lily Banana") and has(state, player, options, "Kelp Heart") and has(state, player, options, "Passion Fig") and has(state, player, options, "Kelp Coffee Drop"),
		"Evolve: Manta": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Passion Fig") and has(state, player, options, "Starfish Sandwich"),
		"Evolve: Octo": lambda state: has(state, player, options, "Lily Banana") and has(state, player, options, "Lotus Kiwi") and has(state, player, options, "Passion Fig") and has(state, player, options, "Pearl Berries") and has(state, player, options, "Coral Cannoli"),
		"Evolve: Puffer": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Crystal Crisp") and has(state, player, options, "Lotus Kiwi") and has(state, player, options, "Tubey Melon") and has(state, player, options, "Star Kelp") and has(state, player, options, "Kiwi Lime Pie") and has(state, player, options, "Tropical Jelly"),
		"Evolve: Siren": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Tubey Melon") and has(state, player, options, "Kelp Heart") and has(state, player, options, "Star Kelp") and has(state, player, options, "Rainbow Star Kelp") and has(state, player, options, "Kelp Taco") and has(state, player, options, "Tropical Jelly"),
		"Evolve: Snake": lambda state: has(state, player, options, "Tubey Melon") and has(state, player, options, "Lily Banana"),
		"Evolve: Wingfin": lambda state: has(state, player, options, "Lily Banana") and has(state, player, options, "Rainbow Star Kelp") and has(state, player, options, "Tubey Melon") and has(state, player, options, "Star Kelp") and has(state, player, options, "Kelp Heart"),
		"Evolve: Whisker": lambda state: has(state, player, options, "Coral Pear") and has(state, player, options, "Tubey Melon") and has(state, player, options, "Star Kelp") and has(state, player, options, "Tropical Jelly"),
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