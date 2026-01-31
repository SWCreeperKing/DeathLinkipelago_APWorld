import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/Werepelago/blob/master/Werepelago/Archipelago/ApShenanigans.cs]

def get_rule_map(player):
	return {
		"Kyle's Life Savings": lambda state: has_level(state, player, "Monday") and has_level(state, player, "Tuesday") and has_level(state, player, "Thursday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Rebellion's Megaphone": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"E.O.T.M Scrapbook": lambda state: has_level(state, player, "Tuesday") and has_level(state, player, "Thursday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"The CEO's Suit": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Deluxe Toilet Paper Roll": lambda state: has_level(state, player, "Tuesday") and has_level(state, player, "Thursday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Mr. Shoop's Head": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Gold Wolf Plushie": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Wooden Stake and Garlic": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Thursday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Peanut Butter Cookie": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Lethal Pepper Spray": lambda state: has_level(state, player, "Sunday"),
		"Kill Charlie": lambda state: has_level(state, player, "Tuesday") and has_level(state, player, "Thursday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Ena": lambda state: has_level(state, player, "Tuesday"),
		"Kill Jonathan": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Thursday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Erin": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday"),
		"Kill Harrison": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Emma": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Mason": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Thursday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Phoebe": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Thursday") and has_level(state, player, "Sunday"),
		"Kill Chloe": lambda state: has_level(state, player, "Wednesday") and has_level(state, player, "Saturday"),
		"Kill Abby": lambda state: has_level(state, player, "Thursday"),
		"Kill William": lambda state: has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Isabel": lambda state: has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Shruti": lambda state: has_level(state, player, "Thursday") and has_level(state, player, "Saturday"),
		"Kill Glenn": lambda state: has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday"),
		"Kill Cerulean": lambda state: has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday"),
		"Kill Noah": lambda state: has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Angie": lambda state: has_level(state, player, "Thursday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Seung": lambda state: has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Levi": lambda state: has_level(state, player, "Thursday") and has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Samuel": lambda state: has_level(state, player, "Thursday") and has_level(state, player, "Saturday"),
		"Kill Amy": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday"),
		"Kill Janina": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill David": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Beowulf": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill John": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Sunday"),
		"Kill Youngeun": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday"),
		"Kill Karina": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday"),
		"Kill Cameron": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Taro": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Nevaeh": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Rod": lambda state: has_level(state, player, "Friday") and has_level(state, player, "Saturday") and has_level(state, player, "Sunday"),
		"Kill Austin": lambda state: has_level(state, player, "Friday"),
		"Kill Sierra": lambda state: has_level(state, player, "Saturday"),
		"Kill Nicole": lambda state: has_level(state, player, "Saturday"),
		"Kill Eggsy": lambda state: has_level(state, player, "Saturday"),
		"Survive Monday Night": lambda state: has_level(state, player, "Monday") and has_washer(state, player),
		"Survive Tuesday Night": lambda state: has_level(state, player, "Tuesday") and has_washer(state, player),
		"Survive Wednesday Night": lambda state: has_level(state, player, "Wednesday") and has_washer(state, player) and has_vacuum(state, player),
		"Survive Thursday Night": lambda state: has_level(state, player, "Thursday") and has_washer(state, player) and has_vacuum(state, player),
		"Survive Friday Night": lambda state: has_level(state, player, "Friday") and has_washer(state, player) and has_vacuum(state, player) and has_knapper(state, player),
		"Survive Saturday Night": lambda state: has_level(state, player, "Saturday") and has_washer(state, player) and has_vacuum(state, player) and has_knapper(state, player),
		"Survive Sunday Night": lambda state: has_level(state, player, "Sunday") and has_washer(state, player) and has_vacuum(state, player),
	}

def has_level(state, player, level) -> bool:
	return state.has(f"Unlock {level} Night", player, 1)

def has_washer(state, player) -> bool:
	return state.has("Washer", player, 1)

def has_vacuum(state, player) -> bool:
	return state.has("Vacuum", player, 1)

def has_knapper(state, player) -> bool:
	return state.has("Knapper", player, 1)