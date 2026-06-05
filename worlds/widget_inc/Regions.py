from BaseClasses import Location, Region, Item, ItemClassification, LocationProgressType
from .Locations import *
from .Rules import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

priority_map = []

def gen_create_regions(world):
	player = world.player
	options = world.options
	rule_map = get_rule_map(player, options)
	
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
	
	connect_region("Menu", "Tier 1", region_map, None, lambda state: has_tier(state, player, options, 1))
	connect_region("Tier 1", "Tier 2", region_map, None, lambda state: has_tier(state, player, options, 2))
	connect_region("Tier 2", "Tier 3", region_map, None, lambda state: has_tier(state, player, options, 3))
	connect_region("Tier 3", "Tier 4", region_map, None, lambda state: has_tier(state, player, options, 4))
	connect_region("Tier 4", "Tier 5", region_map, None, lambda state: has_tier(state, player, options, 5))
	connect_region("Tier 5", "Tier 6", region_map, None, lambda state: has_tier(state, player, options, 6))
	connect_region("Tier 6", "Tier 7", region_map, None, lambda state: has_tier(state, player, options, 7))
	connect_region("Tier 7", "Tier 8", region_map, None, lambda state: has_tier(state, player, options, 8))
	connect_region("Tier 8", "Tier 9", region_map, None, lambda state: has_tier(state, player, options, 9))
	connect_region("Tier 9", "Tier 10", region_map, None, lambda state: has_tier(state, player, options, 10))
	connect_region("Tier 10", "Tier 11", region_map, None, lambda state: has_tier(state, player, options, 11))
	connect_region("Tier 11", "Tier 12", region_map, None, lambda state: has_tier(state, player, options, 12))
	for location in tech_tree:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	
	for region in region_map.values():
		world.multiworld.regions.append(region)

def connect_region(from_region, to_region, region_map, name, rule):
	if from_region not in region_map: return
	if to_region not in region_map: return
	region_map[from_region].connect(region_map[to_region], name, rule = rule)

def make_location(world, location_name, region_name, region_map, rule_map):
	if region_name not in region_map: return None
	world.location_count += 1
	return make_location_adv(world, location_name, location_name, world.location_name_to_id[location_name], region_name, region_map, rule_map)

def make_event_location(world, location_name_a, location_name_b, item_name, id, region_name, region_map, rule_map):
	if region_name not in region_map: return None
	location = make_location_adv(world, location_name_a, location_name_b, id, region_name, region_map, rule_map)
	if location is None: return None
	return location.place_locked_item(Item(item_name, ItemClassification.progression, None, world.player))

def make_location_adv(world, location_name_a, location_name_b, id, region_name, region_map, rule_map):
	if region_name not in region_map: return None
	location = Location(world.player, location_name_a, id, region_map[region_name])
	region_map[region_name].locations.append(location)
	
	if location_name_b in rule_map:
	   location.access_rule = rule_map[location_name_b]
	
	if location_name_a in priority_map:
	   location.progress_type = priority_map[location_name_a]
	
	return location