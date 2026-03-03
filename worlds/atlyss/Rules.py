import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player):
	return {
	}

def can_grind(state, player, level, area_data) -> bool:
	if level > 26: return can_grind(state, player, 26, area_data)
	if level <= 1: return True
	
	for area in area_data:
	    if not has_area(state, player, area[0]): continue
	    if area[1] <= level <= area[2]: return can_grind(state, player, area[1] - 1, area_data)
	    
	return False

def has_area(state, player, area) -> bool:
	return state.has(area, player, 1)

def has_quest(state, player, quest) -> bool:
	return state.has(f"Complete: {quest}", player, 1)

def can_grind_level(state, player, level) -> bool:
	return can_grind(state, player, level, location_grind_data)

def can_grind_fish(state, player, level) -> bool:
	return can_grind(state, player, level, fishing_grind_data)

def can_grind_mine(state, player, level) -> bool:
	return can_grind(state, player, level, mining_grind_data)