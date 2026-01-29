from BaseClasses import Location, Region, Item, ItemClassification, LocationProgressType
from .Locations import *
from .Rules import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/Widgitpelago/blob/master/Widgitpelago/Archipelago/ApShenanigans.cs]

priority_map = []

def gen_create_regions(world):
	player = world.player
	rule_map = get_rule_map(world.player)
	
	region_map = {
		"Menu": Region("Menu", world.player, world.multiworld),
		"Tier 1": Region("Tier 1", world.player, world.multiworld),
		"Tier 2": Region("Tier 2", world.player, world.multiworld),
		"Tier 3": Region("Tier 3", world.player, world.multiworld),
		"Tier 4": Region("Tier 4", world.player, world.multiworld),
		"Tier 5": Region("Tier 5", world.player, world.multiworld),
		"Tier 6": Region("Tier 6", world.player, world.multiworld),
		"Tier 7": Region("Tier 7", world.player, world.multiworld),
		"Tier 8": Region("Tier 8", world.player, world.multiworld),
		"Tier 9": Region("Tier 9", world.player, world.multiworld),
		"Tier 10": Region("Tier 10", world.player, world.multiworld),
		"Tier 11": Region("Tier 11", world.player, world.multiworld),
		"Tier 12": Region("Tier 12", world.player, world.multiworld)
	}
	
	region_map["Menu"].connect(region_map["Tier 1"], rule = lambda state: has_tier(state, player, 1))
	region_map["Tier 1"].connect(region_map["Tier 2"], rule = lambda state: has_tier(state, player, 2))
	region_map["Tier 2"].connect(region_map["Tier 3"], rule = lambda state: has_tier(state, player, 3))
	region_map["Tier 3"].connect(region_map["Tier 4"], rule = lambda state: has_tier(state, player, 4))
	region_map["Tier 4"].connect(region_map["Tier 5"], rule = lambda state: has_tier(state, player, 5))
	region_map["Tier 5"].connect(region_map["Tier 6"], rule = lambda state: has_tier(state, player, 6))
	region_map["Tier 6"].connect(region_map["Tier 7"], rule = lambda state: has_tier(state, player, 7))
	region_map["Tier 7"].connect(region_map["Tier 8"], rule = lambda state: has_tier(state, player, 8))
	region_map["Tier 8"].connect(region_map["Tier 9"], rule = lambda state: has_tier(state, player, 9))
	region_map["Tier 9"].connect(region_map["Tier 10"], rule = lambda state: has_tier(state, player, 10))
	region_map["Tier 10"].connect(region_map["Tier 11"], rule = lambda state: has_tier(state, player, 11))
	region_map["Tier 11"].connect(region_map["Tier 12"], rule = lambda state: has_tier(state, player, 12))
	for location in tech_tree:
		make_location(world, location[0], region_map[location[1]], rule_map)
	
	for region in region_map.values():
		world.multiworld.regions.append(region)

def make_location(world, location_name, region, rule_map):
	return make_location_adv(world, location_name, location_name, world.location_name_to_id[location_name], region, rule_map)

def make_event_location(world, location_name_a, location_name_b, item_name, id, region, rule_map):
	location = make_location_adv(world, location_name_a, location_name_b, id, region, rule_map)
	location.place_locked_item(Item(item_name, ItemClassification.progression, None, world.player))

def make_location_adv(world, location_name_a, location_name_b, id, region, rule_map):
	location = Location(world.player, location_name_a, id, region)
	region.locations.append(location)
	
	if location_name_b in rule_map:
	   location.access_rule = rule_map[location_name_b]
	
	if location_name_a in priority_map:
	   location.progress_type = priority_map[location_name_a]
	
	world.location_count += 1
	return location