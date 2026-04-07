import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player, options):
	return {
		"Kyle's Life Savings": lambda state: has_level(state, player, options, "Monday") or has_level(state, player, options, "Tuesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Rebellion's Megaphone": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"E.O.T.M Scrapbook": lambda state: has_level(state, player, options, "Tuesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"The CEO's Suit": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Deluxe Toilet Paper Roll": lambda state: has_level(state, player, options, "Tuesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Mr. Shoop's Head": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Gold Wolf Plushie": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Wooden Stake and Garlic": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Peanut Butter Cookie": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Lethal Pepper Spray": lambda state: has_level(state, player, options, "Sunday"),
		"Kill Charlie": lambda state: has_level(state, player, options, "Tuesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Ena": lambda state: has_level(state, player, options, "Tuesday"),
		"Kill Jonathan": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Erin": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday"),
		"Kill Harrison": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Emma": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Mason": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Phoebe": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Thursday") or has_level(state, player, options, "Sunday"),
		"Kill Chloe": lambda state: has_level(state, player, options, "Wednesday") or has_level(state, player, options, "Saturday"),
		"Kill Abby": lambda state: has_level(state, player, options, "Thursday"),
		"Kill William": lambda state: has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Isabel": lambda state: has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Shruti": lambda state: has_level(state, player, options, "Thursday") or has_level(state, player, options, "Saturday"),
		"Kill Glenn": lambda state: has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday"),
		"Kill Cerulean": lambda state: has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday"),
		"Kill Noah": lambda state: has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Angie": lambda state: has_level(state, player, options, "Thursday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Seung": lambda state: has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Levi": lambda state: has_level(state, player, options, "Thursday") or has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Samuel": lambda state: has_level(state, player, options, "Thursday") or has_level(state, player, options, "Saturday"),
		"Kill Amy": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday"),
		"Kill Janina": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill David": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Beowulf": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill John": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Sunday"),
		"Kill Youngeun": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday"),
		"Kill Karina": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday"),
		"Kill Cameron": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Taro": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Nevaeh": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Rod": lambda state: has_level(state, player, options, "Friday") or has_level(state, player, options, "Saturday") or has_level(state, player, options, "Sunday"),
		"Kill Austin": lambda state: has_level(state, player, options, "Friday"),
		"Kill Sierra": lambda state: has_level(state, player, options, "Saturday"),
		"Kill Nicole": lambda state: has_level(state, player, options, "Saturday"),
		"Kill Eggsy": lambda state: has_level(state, player, options, "Saturday"),
		"Survive Monday Night": lambda state: has_level(state, player, options, "Monday") and has_washer(state, player, options),
		"Survive Tuesday Night": lambda state: has_level(state, player, options, "Tuesday") and has_washer(state, player, options),
		"Survive Wednesday Night": lambda state: has_level(state, player, options, "Wednesday") and has_washer(state, player, options) and has_vacuum(state, player, options),
		"Survive Thursday Night": lambda state: has_level(state, player, options, "Thursday") and has_washer(state, player, options) and has_vacuum(state, player, options),
		"Survive Friday Night": lambda state: has_level(state, player, options, "Friday") and has_washer(state, player, options) and has_vacuum(state, player, options) and has_knapper(state, player, options),
		"Survive Saturday Night": lambda state: has_level(state, player, options, "Saturday") and has_washer(state, player, options) and has_vacuum(state, player, options) and has_knapper(state, player, options),
		"Survive Sunday Night": lambda state: has_level(state, player, options, "Sunday") and has_washer(state, player, options) and has_vacuum(state, player, options),
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

def has_level(state, player, options, level) -> bool:
	return has(state, player, options, f'Unlock {level} Night')

def has_washer(state, player, options) -> bool:
	return has(state, player, options, 'Washer')

def has_vacuum(state, player, options) -> bool:
	return has(state, player, options, 'Vacuum')

def has_knapper(state, player, options) -> bool:
	return has(state, player, options, 'Knapper')