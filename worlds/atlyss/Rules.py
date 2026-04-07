import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player, options):
	return {
		"A Warm Welcome": lambda state: can_grind_level(state, player, options, 1),
		"Communing Catacombs": lambda state: can_grind_level(state, player, options, 1) and has_quest(state, player, options, "A Warm Welcome"),
		"Diva Must Die": lambda state: can_grind_level(state, player, options, 4) and has_quest(state, player, options, "Communing Catacombs"),
		"The Keep Within": lambda state: can_grind_level(state, player, options, 8) and has_quest(state, player, options, "Diva Must Die"),
		"Tethering Grove": lambda state: can_grind_level(state, player, options, 15) and has_quest(state, player, options, "The Keep Within"),
		"The Glyphik Booklet": lambda state: can_grind_level(state, player, options, 24) and has_quest(state, player, options, "Finding Ammagon") and has_all_areas(state, player, options, ["Luvora Garden", "Tuul Enclave", "Cresent Grove lvl 2"]),
		"Cleaning Terrace": lambda state: can_grind_level(state, player, options, 5) and has_quest(state, player, options, "Diva Must Die"),
		"Ancient Beings": lambda state: can_grind_level(state, player, options, 8) and has_quest(state, player, options, "The Keep Within"),
		"Wicked Wizboars": lambda state: can_grind_level(state, player, options, 10) and has_any_area(state, player, options, ["Tuul Valley", "Cresent Keep"]),
		"Spiraling In The Grove": lambda state: can_grind_level(state, player, options, 15) and has_quest(state, player, options, "Tethering Grove"),
		"Hell In The Grove": lambda state: can_grind_level(state, player, options, 20) and has_quest(state, player, options, "Tethering Grove"),
		"Nulversa Magica": lambda state: can_grind_level(state, player, options, 20),
		"Finding Ammagon": lambda state: can_grind_level(state, player, options, 14),
		"The Colossus": lambda state: can_grind_level(state, player, options, 15) and has_quest(state, player, options, "The Keep Within"),
		"Night Spirits": lambda state: can_grind_level(state, player, options, 1) and has_any_area(state, player, options, ["Arcwood Pass", "Effold Terrace"]),
		"Ridding Slimes": lambda state: can_grind_level(state, player, options, 1),
		"Huntin' Hogs": lambda state: can_grind_level(state, player, options, 7) and has_any_area(state, player, options, ["Tuul Valley", "Cresent Keep"]),
		"Purging the Grove": lambda state: can_grind_level(state, player, options, 15) and has_quest(state, player, options, "The Colossus"),
		"Cleansing the Grove": lambda state: can_grind_level(state, player, options, 20) and has_quest(state, player, options, "The Colossus"),
		"Nulversa Viscera": lambda state: can_grind_level(state, player, options, 20),
		"Call of Fury": lambda state: can_grind_level(state, player, options, 4),
		"Mastery of Strength": lambda state: can_grind_level(state, player, options, 10),
		"Beckoning Foes": lambda state: can_grind_level(state, player, options, 12),
		"Ghostly Goods": lambda state: can_grind_level(state, player, options, 1) and has_quest(state, player, options, "A Warm Welcome") and has_any_area(state, player, options, ["Sanctum Catacombs lvl 1", "Sanctum Catacombs lvl 2", "Sanctum Catacombs lvl 3"]),
		"Makin' a Mekspear": lambda state: can_grind_level(state, player, options, 7) and has_area(state, player, options, 'Effold Terrace') and has_any_area(state, player, options, ["Tuul Valley", "Cresent Keep", "Effold Terrace"]),
		"Makin' a Wizwand": lambda state: can_grind_level(state, player, options, 10) and has_all_areas(state, player, options, ["Tuul Valley", "Cresent Road"]),
		"Makin' a Vile Blade": lambda state: can_grind_level(state, player, options, 10) and has_all_areas(state, player, options, ["Cresent Road", "Effold Terrace", "Sanctum Catacombs lvl 2"]),
		"Makin' a Golem Chestpiece": lambda state: can_grind_level(state, player, options, 12) and has_quest(state, player, options, "The Keep Within"),
		"Makin' a Ragespear": lambda state: can_grind_level(state, player, options, 15) and has_quest(state, player, options, "Makin' a Mekspear") and has_all_areas(state, player, options, ["Effold Terrace", "Sanctum Catacombs lvl 3", "Bularr Fortress"]),
		"Makin' a Monolith Chestpiece": lambda state: can_grind_level(state, player, options, 16) and has_quest(state, player, options, "Makin' a Golem Chestpiece"),
		"Makin' a Firebreath Blade": lambda state: can_grind_level(state, player, options, 20),
		"Makin' a Follycannon": lambda state: can_grind_level(state, player, options, 24),
		"Summore' Spectral Powder!": lambda state: can_grind_level(state, player, options, 1) and has_quest(state, player, options, "Ghostly Goods") and has_any_area(state, player, options, ["Sanctum Catacombs lvl 1", "Sanctum Catacombs lvl 2", "Sanctum Catacombs lvl 3"]),
		"Makin' More Mekspears": lambda state: can_grind_level(state, player, options, 7) and has_quest(state, player, options, "Makin' a Mekspear") and has_area(state, player, options, 'Effold Terrace') and has_any_area(state, player, options, ["Tuul Valley", "Cresent Keep", "Effold Terrace"]),
		"Makin' More Wizwands": lambda state: can_grind_level(state, player, options, 10) and has_quest(state, player, options, "Makin' a Wizwand") and has_all_areas(state, player, options, ["Tuul Valley", "Cresent Road"]),
		"Makin' More Vile Blades": lambda state: can_grind_level(state, player, options, 10) and has_quest(state, player, options, "Makin' a Vile Blade") and has_all_areas(state, player, options, ["Cresent Road", "Effold Terrace", "Sanctum Catacombs lvl 2"]),
		"Summore' Golem Chestpieces": lambda state: can_grind_level(state, player, options, 12) and has_quest(state, player, options, "Makin' a Golem Chestpiece"),
		"Makin' More Ragespears": lambda state: can_grind_level(state, player, options, 15) and has_quest(state, player, options, "Makin' a Ragespear") and has_all_areas(state, player, options, ["Effold Terrace", "Sanctum Catacombs lvl 3", "Bularr Fortress"]),
		"Summore' Monolith Chestpieces": lambda state: can_grind_level(state, player, options, 16) and has_quest(state, player, options, "Makin' a Monolith Chestpiece"),
		"Nulversa, Greenversa!": lambda state: can_grind_level(state, player, options, 20),
		"Summore' Firebreath Blades": lambda state: can_grind_level(state, player, options, 20) and has_quest(state, player, options, "Makin' a Firebreath Blade"),
		"Makin' More Follycannons": lambda state: can_grind_level(state, player, options, 24) and has_quest(state, player, options, "Makin' a Follycannon"),
		"Focusin' in": lambda state: can_grind_level(state, player, options, 4),
		"Mastery of Dexterity": lambda state: can_grind_level(state, player, options, 10),
		"Whatta' Rush!": lambda state: can_grind_level(state, player, options, 12),
		"The Voice of Zuulneruda": lambda state: can_grind_level(state, player, options, 6) and has_quest(state, player, options, "Killing Tomb"),
		"Killing Tomb": lambda state: can_grind_level(state, player, options, 1),
		"Purging the Undead": lambda state: can_grind_level(state, player, options, 6) and has_quest(state, player, options, "Killing Tomb"),
		"Rattlecage Rage": lambda state: can_grind_level(state, player, options, 6) and has_quest(state, player, options, "Killing Tomb"),
		"Consumed Madness": lambda state: can_grind_level(state, player, options, 12) and has_quest(state, player, options, "The Voice of Zuulneruda"),
		"Eradicating the Undead": lambda state: can_grind_level(state, player, options, 12) and has_quest(state, player, options, "The Voice of Zuulneruda"),
		"Reviling the Rageboars": lambda state: can_grind_level(state, player, options, 14),
		"Gatling Galius": lambda state: can_grind_level(state, player, options, 22),
		"Reviling more Rageboars": lambda state: can_grind_level(state, player, options, 14) and has_quest(state, player, options, "Reviling the Rageboars"),
		"Facing Foes": lambda state: can_grind_level(state, player, options, 18),
		"The Gall of Galius": lambda state: can_grind_level(state, player, options, 22) and has_quest(state, player, options, "Gatling Galius"),
		"Up and Over It": lambda state: can_grind_level(state, player, options, 15),
		"Dense Ingots": lambda state: can_grind_level(state, player, options, 1),
		"Amberite Ingots": lambda state: can_grind_level(state, player, options, 6) and has_quest(state, player, options, "Dense Ingots") and has_any_area(state, player, options, ["Cresent Keep", "Tuul Valley"]),
		"Sapphite Ingots": lambda state: can_grind_level(state, player, options, 8) and has_quest(state, player, options, "Amberite Ingots"),
		"Reach Level 2": lambda state: can_grind_level(state, player, options, 2),
		"Reach Level 4": lambda state: can_grind_level(state, player, options, 4),
		"Reach Level 6": lambda state: can_grind_level(state, player, options, 6),
		"Reach Level 8": lambda state: can_grind_level(state, player, options, 8),
		"Reach Level 10": lambda state: can_grind_level(state, player, options, 10),
		"Reach Level 12": lambda state: can_grind_level(state, player, options, 12),
		"Reach Level 14": lambda state: can_grind_level(state, player, options, 14),
		"Reach Level 16": lambda state: can_grind_level(state, player, options, 16),
		"Reach Level 18": lambda state: can_grind_level(state, player, options, 18),
		"Reach Level 20": lambda state: can_grind_level(state, player, options, 20),
		"Reach Level 22": lambda state: can_grind_level(state, player, options, 22),
		"Reach Level 24": lambda state: can_grind_level(state, player, options, 24),
		"Reach Level 26": lambda state: can_grind_level(state, player, options, 26),
		"Reach Level 28": lambda state: can_grind_level(state, player, options, 28),
		"Reach Level 30": lambda state: can_grind_level(state, player, options, 30),
		"Reach Level 32": lambda state: can_grind_level(state, player, options, 32),
		"Buy Item #1 from Sally's Nook": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #2 from Sally's Nook": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #3 from Sally's Nook": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #4 from Sally's Nook": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #5 from Sally's Nook": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #1 from Skrit's Sikrit Market": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #2 from Skrit's Sikrit Market": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #3 from Skrit's Sikrit Market": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #4 from Skrit's Sikrit Market": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #5 from Skrit's Sikrit Market": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #1 from Frankie's Goods": lambda state: has_area(state, player, options, "Arcwood Pass"),
		"Buy Item #2 from Frankie's Goods": lambda state: has_area(state, player, options, "Arcwood Pass"),
		"Buy Item #3 from Frankie's Goods": lambda state: has_area(state, player, options, "Arcwood Pass"),
		"Buy Item #4 from Frankie's Goods": lambda state: has_area(state, player, options, "Arcwood Pass"),
		"Buy Item #5 from Frankie's Goods": lambda state: has_area(state, player, options, "Arcwood Pass"),
		"Buy Item #1 from Craig's Bazzar": lambda state: has_area(state, player, options, "Wall of the Stars"),
		"Buy Item #2 from Craig's Bazzar": lambda state: has_area(state, player, options, "Wall of the Stars"),
		"Buy Item #3 from Craig's Bazzar": lambda state: has_area(state, player, options, "Wall of the Stars"),
		"Buy Item #4 from Craig's Bazzar": lambda state: has_area(state, player, options, "Wall of the Stars"),
		"Buy Item #5 from Craig's Bazzar": lambda state: has_area(state, player, options, "Wall of the Stars"),
		"Buy Item #1 from Dye Merchant": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #2 from Dye Merchant": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #3 from Dye Merchant": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #4 from Dye Merchant": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #5 from Dye Merchant": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #1 from Tesh's Wares": lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 2"),
		"Buy Item #2 from Tesh's Wares": lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 2"),
		"Buy Item #3 from Tesh's Wares": lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 2"),
		"Buy Item #4 from Tesh's Wares": lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 2"),
		"Buy Item #5 from Tesh's Wares": lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 2"),
		"Buy Item #1 from Nesh's Wares": lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 3"),
		"Buy Item #2 from Nesh's Wares": lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 3"),
		"Buy Item #3 from Nesh's Wares": lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 3"),
		"Buy Item #4 from Nesh's Wares": lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 3"),
		"Buy Item #5 from Nesh's Wares": lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 3"),
		"Buy Item #1 from Rikko's Treasures": lambda state: has_area(state, player, options, "Cresent Grove lvl 1"),
		"Buy Item #2 from Rikko's Treasures": lambda state: has_area(state, player, options, "Cresent Grove lvl 1"),
		"Buy Item #3 from Rikko's Treasures": lambda state: has_area(state, player, options, "Cresent Grove lvl 1"),
		"Buy Item #4 from Rikko's Treasures": lambda state: has_area(state, player, options, "Cresent Grove lvl 1"),
		"Buy Item #5 from Rikko's Treasures": lambda state: has_area(state, player, options, "Cresent Grove lvl 1"),
		"Buy Item #1 from Cotoo's Treasures": lambda state: has_area(state, player, options, "Cresent Grove lvl 2"),
		"Buy Item #2 from Cotoo's Treasures": lambda state: has_area(state, player, options, "Cresent Grove lvl 2"),
		"Buy Item #3 from Cotoo's Treasures": lambda state: has_area(state, player, options, "Cresent Grove lvl 2"),
		"Buy Item #4 from Cotoo's Treasures": lambda state: has_area(state, player, options, "Cresent Grove lvl 2"),
		"Buy Item #5 from Cotoo's Treasures": lambda state: has_area(state, player, options, "Cresent Grove lvl 2"),
		"Buy Item #1 from Ruka's Furnace": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #2 from Ruka's Furnace": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #3 from Ruka's Furnace": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #4 from Ruka's Furnace": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #5 from Ruka's Furnace": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #1 from Torta's Fishing Shack": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #2 from Torta's Fishing Shack": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #3 from Torta's Fishing Shack": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #4 from Torta's Fishing Shack": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #5 from Torta's Fishing Shack": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #1 from Mad Statue's Gift": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #2 from Mad Statue's Gift": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #3 from Mad Statue's Gift": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #4 from Mad Statue's Gift": lambda state: has_area(state, player, options, "Sanctum"),
		"Buy Item #5 from Mad Statue's Gift": lambda state: has_area(state, player, options, "Sanctum"),
		"Fishing Lv. 1": lambda state: can_grind_fish(state, player, options, 1),
		"Fishing Lv. 2": lambda state: can_grind_fish(state, player, options, 2),
		"Fishing Lv. 3": lambda state: can_grind_fish(state, player, options, 3),
		"Fishing Lv. 4": lambda state: can_grind_fish(state, player, options, 4),
		"Fishing Lv. 5": lambda state: can_grind_fish(state, player, options, 5),
		"Fishing Lv. 6": lambda state: can_grind_fish(state, player, options, 6),
		"Fishing Lv. 7": lambda state: can_grind_fish(state, player, options, 7),
		"Fishing Lv. 8": lambda state: can_grind_fish(state, player, options, 8),
		"Fishing Lv. 9": lambda state: can_grind_fish(state, player, options, 9),
		"Fishing Lv. 10": lambda state: can_grind_fish(state, player, options, 10),
		"Mining Lv. 1": lambda state: can_grind_mine(state, player, options, 1),
		"Mining Lv. 2": lambda state: can_grind_mine(state, player, options, 2),
		"Mining Lv. 3": lambda state: can_grind_mine(state, player, options, 3),
		"Mining Lv. 4": lambda state: can_grind_mine(state, player, options, 4),
		"Mining Lv. 5": lambda state: can_grind_mine(state, player, options, 5),
		"Mining Lv. 6": lambda state: can_grind_mine(state, player, options, 6),
		"Mining Lv. 7": lambda state: can_grind_mine(state, player, options, 7),
		"Mining Lv. 8": lambda state: can_grind_mine(state, player, options, 8),
		"Mining Lv. 9": lambda state: can_grind_mine(state, player, options, 9),
		"Mining Lv. 10": lambda state: can_grind_mine(state, player, options, 10),
		"A New Journey": lambda state: can_grind_level(state, player, options, 0),
		"Clearing Catacombs (1-6)": lambda state: can_grind_level(state, player, options, 1) and has_area(state, player, options, "Sanctum Catacombs lvl 1"),
		"Clearing Catacombs (6-12)": lambda state: can_grind_level(state, player, options, 6) and has_area(state, player, options, "Sanctum Catacombs lvl 2"),
		"Becoming a Fighter": lambda state: can_grind_level(state, player, options, 10),
		"Becoming a Mystic": lambda state: can_grind_level(state, player, options, 10),
		"Becoming a Bandit": lambda state: can_grind_level(state, player, options, 10),
		"Clearing Catacombs (12-18)": lambda state: can_grind_level(state, player, options, 12) and has_area(state, player, options, "Sanctum Catacombs lvl 3"),
		"Clearing Grove (15-20)": lambda state: can_grind_level(state, player, options, 15) and has_area(state, player, options, "Cresent Grove lvl 1"),
		"Clearing Grove (20-25)": lambda state: can_grind_level(state, player, options, 20) and has_area(state, player, options, "Cresent Grove lvl 2"),
		"Judgement": lambda state: can_grind_level(state, player, options, 28) and has_amount(state, player, options, "Experience Bond", 1),
		"Corrupted Arcana": lambda state: can_grind_level(state, player, options, 28) and has_amount(state, player, options, "Experience Bond", 1),
		"Holier than Thou": lambda state: can_grind_level(state, player, options, 28) and has_amount(state, player, options, "Experience Bond", 1),
		"Altered Vision": lambda state: can_grind_level(state, player, options, 0) and has_amount(state, player, options, "Illusion Stone", 1),
		"Scaling the Tower": lambda state: can_grind_level(state, player, options, 0),
		"Scaling Stars": lambda state: can_grind_level(state, player, options, 15) and has_area(state, player, options, "Trial of the Stars"),
		"Rude!": lambda state: can_grind_level(state, player, options, 0),
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

def has_area(state, player, options, area) -> bool:
	if not state.multiworld.worlds[player].options.random_portals:
	  return state.has("Progressive Portal", player, portal_counts[area])
	if area.startswith("Sanctum Catacombs"):
	  area = "Catacombs"
	portal = f"{area} Portal"
	return state.has(portal, player, 1)

def has_any_area(state, player, options, areas) -> bool:
	return any(has_area(state, player, area) for area in areas)

def has_all_areas(state, player, options, areas) -> bool:
	return all(has_area(state, player, area) for area in areas)

def has_quest(state, player, options, quest) -> bool:
	return has(state, player, options, f"Complete: {quest}")

def can_grind(state, player, options, level, area_data) -> bool:
	if level > 30: return can_grind(state, player, 30, area_data)
	if level <= 1: return True
	
	for area in area_data:
	    if not has_area(state, player, options, area[0]): continue
	    if area[1] <= level <= area[2]: return can_grind(state, player, area[1] - 1, area_data)
	    
	return False

def can_grind_level(state, player, options, level) -> bool:
	return can_grind(state, player, options, level, location_grind_data)

def can_grind_fish(state, player, options, level) -> bool:
	return can_grind(state, player, options, level, fishing_grind_data)

def can_grind_mine(state, player, options, level) -> bool:
	return can_grind(state, player, options, level, mining_grind_data)

def can_beat_enemy(state, player, options, enemy_name) -> bool:
	return can_grind_level(state, player, options, enemy_data[enemy_name][0]) and has_any_area(state, player, options, enemy_data[enemy_name][1])