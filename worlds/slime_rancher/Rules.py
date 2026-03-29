import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player, options):
	return {
		"Treasure Pod - Hidden Cave near Ranch Entry": lambda state: has_cracker(state, player, options, 3),
		"Treasure Pod - Dry Reef Entrance": lambda state: has_cracker(state, player, options, 1),
		"Treasure Pod - Dry Reef Arch Island": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Next to Slime Gate Ring Isle": lambda state: has_cracker(state, player, options, 1),
		"Treasure Pod - Under Overgrowth Exit": lambda state: has_cracker(state, player, options, 2),
		"Treasure Pod - Cliff Near Tabby Slimes": lambda state: has_cracker(state, player, options, 1),
		"Treasure Pod - Tabby Gordo": lambda state: has_cracker(state, player, options, 1),
		"Treasure Pod - Phosphor Gordo": lambda state: has_cracker(state, player, options, 1),
		"Slime Sea - The Mustache Shrine": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 3),
		"Treasure Pod - The Grotto": lambda state: has_cracker(state, player, options, 2),
		"Treasure Pod - Slime Sea Cosmetic (Angelic)": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Bridge Behind Indigo Quarry": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Alcove Behind Indigo Quarry": lambda state: has_cracker(state, player, options, 1) and has_jetpack(state, player, options),
		"Hobson's Note - Cliff Across Indigo Quarry": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Middle of Nowhere": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options) and has_energy(state, player, options, 3),
		"Treasure Pod - Dry Reef Ledge": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Wooden Staircase Escape": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Hobson's Note - Moss Blanket Ledge": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Entrance Cliff": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Mushroom Tree Ledge": lambda state: has_cracker(state, player, options, 1) and has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Flower Bed": lambda state: has_cracker(state, player, options, 1),
		"Map Fragment - Moss Blanket": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Back Island": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2),
		"Hobson's Note - Moss Blanket Mushroom Island": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Underwater Pond": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Cosmetic (Cheshire)": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Wooden Ramps": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Quarry Cave Stalagmite near Rock Gordo": lambda state: has_cracker(state, player, options, 3),
		"Treasure Pod - Moss Blanket Ledge Near Flower Area": lambda state: has_cracker(state, player, options, 1) and has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Flower Area": lambda state: has_cracker(state, player, options, 1),
		"Treasure Pod - Quarry Cave Grass near Rock Gordo": lambda state: has_cracker(state, player, options, 1),
		"Hobson's Note - Mushroom Feral Slime Area": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Quarry Entryway": lambda state: has_cracker(state, player, options, 1),
		"Treasure Pod - Quarry Entryway Ledge": lambda state: has_cracker(state, player, options, 3),
		"Treasure Pod - The Lab": lambda state: has_cracker(state, player, options, 1),
		"Treasure Pod - Mushroom Feral Slime Big Tree": lambda state: has_cracker(state, player, options, 1) and has_jetpack(state, player, options),
		"Treasure Pod - Quarry 3rd Area Coral Columns": lambda state: has_cracker(state, player, options, 1),
		"Treasure Pod - Crystal Slime Cave Pillar": lambda state: has_cracker(state, player, options, 2),
		"Treasure Pod - Island Near Hunter Gordo": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2),
		"Treasure Pod - Underwater After Log Tunnel": lambda state: has_cracker(state, player, options, 2),
		"Treasure Pod - Through Crystal Slime Cave": lambda state: has_cracker(state, player, options, 3),
		"Treasure Pod - In the Quarry Pond": lambda state: has_cracker(state, player, options, 2),
		"Treasure Pod - Moss Blanket Alcove Cliff": lambda state: has_cracker(state, player, options, 1) and has_jetpack(state, player, options),
		"Treasure Pod - Alcove Above Moss Teleporter": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Near Island Teleport Gordo": lambda state: has_cracker(state, player, options, 1) and has_jetpack(state, player, options),
		"Treasure Pod - In Quarry Wooden Structure": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Northernmost Cliff of Indigo Quarry Mainland": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Rad Gordo Cave": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Cliff Past Rad Gordo": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Near Quarry Exit Teleporter": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Hobson's Note - Ash Isle": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Ash Isle Fireflower Patch": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Ash Isle Ledge": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Ruins Door Puzzle": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Under Log Tunnel": lambda state: has_cracker(state, player, options, 3),
		"Treasure Pod - Ring Island Flower Patch Cliff": lambda state: has_cracker(state, player, options, 1) and has_jetpack(state, player, options),
		"Treasure Pod - Ring Island Brick Wall Ledge": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Ring Island Cosmetic (Gilded)": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Ring Island Hidden Cave": lambda state: has_cracker(state, player, options, 3),
		"Hobson's Note - Ring Island": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Dry Reef Cosmetic (Tiger)": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Moss Blanket Under Big Tree": lambda state: has_cracker(state, player, options, 3),
		"Treasure Pod - Moss Blanket Mushroom Island": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Ancient Top Floor Alcove": lambda state: has_cracker(state, player, options, 3),
		"Treasure Pod - Ancient Bottom Floor Cave": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Ancient Flower Bed": lambda state: has_cracker(state, player, options, 1) and has_jetpack(state, player, options),
		"Treasure Pod - Ancient Hidden Dungeon": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2),
		"Treasure Pod - Ancient Bottom Floor Under Tree": lambda state: has_cracker(state, player, options, 1),
		"Treasure Pod - Ancient Ruins Behind Wall": lambda state: has_cracker(state, player, options, 2),
		"Treasure Pod - Ancient Ruins In A High Place": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2),
		"Hobson's Note - Ancient Ruins Back Half Oasis": lambda state: has_jetpack(state, player, options),
		"Hobson's Note - End of Ancient Ruins": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - End of Ancient Ruins Bridge Alcove": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - End of Ancient Ruins Complimentary Pod": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - End of Ancient Ruins Cosmetic (Monochrome)": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Ancient Ruins '???'": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Boom Gordo": lambda state: has_cracker(state, player, options, 2),
		"Treasure Pod - On Top of Ancient Ruins": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2),
		"Ancient Ruins - At the End of a Broken Pillar Path": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Ancient Ruins - Hidden Room Behind a Leaf Drape": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Outside The Desert Teleporter Room": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Inside The Desert Teleporter Room": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Hobson's Note - Entrance to Glass Desert": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert On a Rock": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Hobson's Note - Glass Desert Rock Slime Fountain": lambda state: has_jetpack(state, player, options),
		"Map Fragment - Glass Desert": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Desert Fountain Hiding Place": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - On Top of Glass Desert Entrance": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Above Tangle Gordo": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Cliff Above Secret Style": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Cosmetic (Nebula)": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Leftside Ruins Secret Style": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Leftside Ruins": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Leftside Isle": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Edge of Glass Desert Cliff": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2),
		"Treasure Pod - Glass Desert Cliff Above Tangle Gordo": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Under Glass Desert Western Ruins": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Crevasse Pod": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2),
		"Treasure Pod - Glass Desert Cliff Ruins": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2),
		"Treasure Pod - Glass Desert Northern Ruins": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Hobson's Note - Glass Desert Northern Courtyard": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Western Ruins": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options),
		"Treasure Pod - Firey Glass Cliff": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Western": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Western Secret Style": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Northern": lambda state: has_jetpack(state, player, options),
		"Treasure Pod - Glass Desert Northern Cliff": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options) and has_energy(state, player, options, 2),
		"Treasure Pod - Glass Desert Northern Steeple": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2),
		"Hobson's Note - Glass Desert Northern Ruins": lambda state: has_jetpack(state, player, options),
		"Hobson's Note - Glass Desert Slime Statue": lambda state: has_jetpack(state, player, options),
		"Hobson's Note - Doors Like These": lambda state: has_jetpack(state, player, options),
		"Glass Desert - Hover from One Tower to Another": lambda state: has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 1),
		"Glass Desert - Hidden High Above the Ancient Fountain": lambda state: has_cracker(state, player, options, 2) and has_jetpack(state, player, options) and has_energy(state, player, options, 1),
		"Ash Isle - Blooming From Fire Flowers": lambda state: has_jetpack(state, player, options),
		"Buy Personal Upgrade (Heart Module lv.2)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Heart Module lv.3)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Heart Module lv.4)": lambda state: can_access_7zee(state, player, options),
		"Buy Personal Upgrade (Tank Booster lv.2)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Tank Booster lv.3)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Tank Booster lv.4)": lambda state: can_access_7zee(state, player, options),
		"Buy Personal Upgrade (Dash Boots lv.2)": lambda state: can_access_7zee(state, player, options),
		"Buy Personal Upgrade (Power Core lv.2)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Power Core lv.3)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Treasure Cracker lv.1)": lambda state: can_access_lab(state, player, options),
		"Buy Personal Upgrade (Treasure Cracker lv.2)": lambda state: can_access_lab(state, player, options),
		"Buy Personal Upgrade (Treasure Cracker lv.3)": lambda state: can_access_lab(state, player, options),
		"Buy Personal Upgrade (Air Drive)": lambda state: can_access_dry_reef(state, player, options),
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
	return any(has(state, player, options, item) for item in items)

def has_cracker(state, player, options, level) -> bool:
	return has_amount(state, player, options, 'Progressive Treasure Cracker', level)

def has_energy(state, player, options, amount) -> bool:
	return has_amount(state, player, options, 'Progressive Max Energy', amount)

def has_jetpack(state, player, options) -> bool:
	return has(state, player, options, 'Progressive Jetpack')

def has_region(state, player, options, region) -> bool:
	return has(state, player, options, f"Region Unlock: {region}")

def can_access_dry_reef(state, player, options) -> bool:
	return has_region(state, player, options, 'Dry Reef')

def can_access_to_ruins_from_trans(state, player, options) -> bool:
	return has_region(state, player, options, 'Indigo Quarry') and has_region(state, player, options, 'Moss Blanket') and has_region(state, player, options, 'Ancient Ruins')

def can_access_7zee(state, player, options) -> bool:
	return can_access_dry_reef(state, player, options) and can_access_to_ruins_from_trans(state, player, options)

def can_access_lab(state, player, options) -> bool:
	return can_access_dry_reef(state, player, options) and has_region(state, player, options, 'Indigo Quarry') and has_region(state, player, options, 'The Lab')