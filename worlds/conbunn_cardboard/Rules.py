import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player):
	return {
		"Cutout Forest Coin #10": lambda state: has_dash(state, player),
		"Cutout Forest Coin #11": lambda state: has_dash(state, player),
		"Cutout Forest Coin #12": lambda state: has_dash(state, player),
		"Cutout Forest Coin #13": lambda state: has_dash(state, player),
		"Origami Tree CD #1": lambda state: has_bounce_pads(state, player),
		"Bunny Circuit CD #1": lambda state: has_bounce_pads(state, player),
		"Cardbun Viewing Area Coin #1": lambda state: has_bounce_pads(state, player),
		"Cardbun Viewing Area Coin #2": lambda state: has_bounce_pads(state, player),
		"Cardbun Viewing Area CD #1": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #4": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #5": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #6": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #7": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #8": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #9": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #10": lambda state: has_bounce_pads(state, player),
		"Paper Bay CD #1": lambda state: has_bounce_pads(state, player),
		"Paper Bay CD #2": lambda state: has_bounce_pads(state, player),
		"Paper Bay CD #3": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #19": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #20": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #21": lambda state: has_bounce_pads(state, player),
		"Paper Bay CD #5": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #25": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #26": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #27": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #28": lambda state: has_bounce_pads(state, player),
		"Paper Bay Coin #29": lambda state: has_bounce_pads(state, player),
		"Skin from Ara #1": lambda state: has_unlock(state, player, "Ribbon Village") and has_coin_count(state, player, 50),
		"Skin from Ara #2": lambda state: has_unlock(state, player, "Ribbon Village") and has_coin_count(state, player, 150),
		"Conbunn Suit": lambda state: has_unlock(state, player, "Cardbun Festival"),
		"Space Suit": lambda state: has_unlock(state, player, "Cardboard Station (Sticker Park)"),
		"Skin from Fuya": lambda state: has_unlock(state, player, "Connie's Garden (Cutout Forest)"),
	}

def has_unlock(state, player, transition) -> bool:
	return state.has(f"Transition Unlock: {transition}", player, 1)

def has_dash(state, player) -> bool:
	return state.has("Dash", player, 1)

def has_bounce_pads(state, player) -> bool:
	return state.has("Bounce Pads", player, 1)

def has_coin_count(state, player, amt) -> bool:
	return state.has("Real Coin", player, amt)