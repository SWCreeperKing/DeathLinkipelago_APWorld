import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player, options):
	return {
		"Cutout Forest Coin #10": lambda state: has_dash(state, player, options),
		"Cutout Forest Coin #11": lambda state: has_dash(state, player, options),
		"Cutout Forest Coin #12": lambda state: has_dash(state, player, options),
		"Cutout Forest Coin #13": lambda state: has_dash(state, player, options),
		"Origami Tree CD #1": lambda state: has_bounce_pads(state, player, options),
		"Bunny Circuit CD #1": lambda state: has_bounce_pads(state, player, options),
		"Cardbun Viewing Area Coin #1": lambda state: has_bounce_pads(state, player, options),
		"Cardbun Viewing Area Coin #2": lambda state: has_bounce_pads(state, player, options),
		"Cardbun Viewing Area CD #1": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #4": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #5": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #6": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #7": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #8": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #9": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #10": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay CD #1": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay CD #2": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay CD #3": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #19": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #20": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #21": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay CD #5": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #25": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #26": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #27": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #28": lambda state: has_bounce_pads(state, player, options),
		"Paper Bay Coin #29": lambda state: has_bounce_pads(state, player, options),
		"Skin from Ara #1": lambda state: has_unlock(state, player, options, "Ribbon Village") and has_coin_count(state, player, options, 50),
		"Skin from Ara #2": lambda state: has_unlock(state, player, options, "Ribbon Village") and has_coin_count(state, player, options, 150),
		"Conbunn Suit": lambda state: has_unlock(state, player, options, "Cardbun Festival"),
		"Space Suit": lambda state: has_unlock(state, player, options, "Cardboard Station (Sticker Park)"),
		"Skin from Fuya": lambda state: has_unlock(state, player, options, "Connie's Garden (Cutout Forest)"),
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

def has_unlock(state, player, options, transition) -> bool:
	return has(state, player, options, f"Transition Unlock: {transition}")

def has_dash(state, player, options) -> bool:
	return has(state, player, options, 'Dash')

def has_bounce_pads(state, player, options) -> bool:
	return has(state, player, options, 'Bounce Pads')

def has_coin_count(state, player, options, amt) -> bool:
	return has_amount(state, player, options, 'Real Coin', amt)