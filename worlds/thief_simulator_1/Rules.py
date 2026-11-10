import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player, options):
	return {
		"House 101: Huway": lambda state: has_safecracking_tools(state, player, options) and has_hacking_tools(state, player, options),
		"House 101: Leovon 100 to clear": lambda state: has_safecracking_tools(state, player, options),
		"House 101: SomeSung": lambda state: has_safecracking_tools(state, player, options) and has_hacking_tools(state, player, options),
		"House 101: Bracelet": lambda state: has_jewelry_tools(state, player, options) and has_safecracking_tools(state, player, options),
		"House 101: Emerald Bracelet": lambda state: has_jewelry_tools(state, player, options) and has_safecracking_tools(state, player, options),
		"House 102: Vase": lambda state: has_safecracking_tools(state, player, options),
		"House 102: Huway": lambda state: has_hacking_tools(state, player, options),
		"House 102: SomeSung": lambda state: has_hacking_tools(state, player, options),
		"House 102: Emerald Bracelet": lambda state: has_jewelry_tools(state, player, options),
		"House 102: $50 Cash in Master Bedroom safe right side of Documents": lambda state: has_safecracking_tools(state, player, options),
		"House 102: $50 Cash in Master Bedroom safe left side of Documents": lambda state: has_safecracking_tools(state, player, options),
		"House 102: Documents": lambda state: has_safecracking_tools(state, player, options),
		"House 103: Huway": lambda state: has_hacking_tools(state, player, options),
		"House 103: Emerald Bracelet": lambda state: has_jewelry_tools(state, player, options) and has_safecracking_tools(state, player, options),
		"House 103: $50 Cash in Bedroom safe on top shelf left side": lambda state: has_safecracking_tools(state, player, options),
		"House 103: $50 Cash in Bedroom safe on top shelf right side": lambda state: has_safecracking_tools(state, player, options),
		"House 103: $50 Cash in Bedroom safe on bottom shelf": lambda state: has_safecracking_tools(state, player, options),
		"House 105: Huway": lambda state: has_hacking_tools(state, player, options),
		"House 105: Amethyst Bracelet": lambda state: has_jewelry_tools(state, player, options) and has_safecracking_tools(state, player, options),
		"House 106: Huway": lambda state: has_hacking_tools(state, player, options),
		"House 106: SomeSung": lambda state: has_hacking_tools(state, player, options),
		"House 107: Heirloom Bracelet": lambda state: has_jewelry_tools(state, player, options),
		"House 112: Bracelet": lambda state: has_jewelry_tools(state, player, options) and has_safecracking_tools(state, player, options),
		"House 112: $15 Cash in Master Bedroom inside safe bottom side": lambda state: has_safecracking_tools(state, player, options),
		"House 112: $15 Cash in Master Bedroom inside safe top side": lambda state: has_safecracking_tools(state, player, options),
		"House 106 Sideroom: $50 Cash inside Sideroom Safe bottom shelf left most side": lambda state: has_safecracking_tools(state, player, options),
		"House 106 Sideroom: $50 Cash inside Sideroom Safe bottom shelf middle left side": lambda state: has_safecracking_tools(state, player, options),
		"House 106 Sideroom: $50 Cash inside Sideroom Safe bottom shelf middle right side": lambda state: has_safecracking_tools(state, player, options),
		"House 106 Sideroom: $50 Cash inside Sideroom Safe bottom shelf right most side": lambda state: has_safecracking_tools(state, player, options),
		"House 106 Sideroom: $50 Cash inside Sideroom Safe top shelf right  most side": lambda state: has_safecracking_tools(state, player, options),
		"House 106 Sideroom: $50 Cash inside Sideroom Safe top shelf middle right side": lambda state: has_safecracking_tools(state, player, options),
		"House 106 Sideroom: $50 Cash inside Sideroom Safe top shelf middle left side": lambda state: has_safecracking_tools(state, player, options),
		"House 106 Sideroom: $50 Cash inside Sideroom Safe top shelf left most side": lambda state: has_safecracking_tools(state, player, options),
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

def has_crowbar(state, player, options) -> bool:
	return True

def has_diy_simple_lockpick(state, player, options) -> bool:
	return has(state, player, options, "DIY Simple Lockpick")

def has_lockpick(state, player, options) -> bool:
	return has(state, player, options, "Lockpick")

def has_climbing_gloves(state, player, options) -> bool:
	return has(state, player, options, "Climbing Gloves")

def has_mini_electric_lock_pick(state, player, options) -> bool:
	return has(state, player, options, "Mini electric lock pick")

def has_jewelry_tools(state, player, options) -> bool:
	return has(state, player, options, "Jewelry tools")

def has_safecracking_tools(state, player, options) -> bool:
	return has(state, player, options, "Safecracking tools")

def has_glass_knife(state, player, options) -> bool:
	return has(state, player, options, "Glass knife")

def has_hacking_tools(state, player, options) -> bool:
	return has(state, player, options, "Hacking tools")

def has_car_lock_pick_gun(state, player, options) -> bool:
	return has(state, player, options, "Car lock pick gun")

def has_hacking_pda(state, player, options) -> bool:
	return has(state, player, options, "Hacking PDA")

def has_car_key_signal_cloner(state, player, options) -> bool:
	return has(state, player, options, "Car key signal cloner")

def has_round_lockpick(state, player, options) -> bool:
	return has(state, player, options, "Round lockpick")

def has_hacking_laptop(state, player, options) -> bool:
	return has(state, player, options, "Hacking laptop")

def has_hacking_laptop_pro(state, player, options) -> bool:
	return has(state, player, options, "Hacking laptop Pro")

def has_bolt_cutters(state, player, options) -> bool:
	return has(state, player, options, "Bolt Cutters")

def has_van(state, player, options) -> bool:
	return has(state, player, options, "Van")

def has_front_door_key_102(state, player, options) -> bool:
	return has(state, player, options, "Front door key 102")

def has_front_door_key_113(state, player, options) -> bool:
	return has(state, player, options, "Front door key 113")