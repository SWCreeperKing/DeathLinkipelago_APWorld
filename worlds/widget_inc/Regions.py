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
	
	connect_region("Menu", "Tier 1", region_map, None, lambda state: has_tier(state, player, options, 1), False)
	connect_region("Tier 1", "Tier 2", region_map, None, lambda state: has_tier(state, player, options, 2), False)
	connect_region("Tier 2", "Tier 3", region_map, None, lambda state: has_tier(state, player, options, 3), False)
	connect_region("Tier 3", "Tier 4", region_map, None, lambda state: has_tier(state, player, options, 4), False)
	connect_region("Tier 4", "Tier 5", region_map, None, lambda state: has_tier(state, player, options, 5), False)
	connect_region("Tier 5", "Tier 6", region_map, None, lambda state: has_tier(state, player, options, 6), False)
	connect_region("Tier 6", "Tier 7", region_map, None, lambda state: has_tier(state, player, options, 7), False)
	connect_region("Tier 7", "Tier 8", region_map, None, lambda state: has_tier(state, player, options, 8), False)
	connect_region("Tier 8", "Tier 9", region_map, None, lambda state: has_tier(state, player, options, 9), False)
	connect_region("Tier 9", "Tier 10", region_map, None, lambda state: has_tier(state, player, options, 10), False)
	connect_region("Tier 10", "Tier 11", region_map, None, lambda state: has_tier(state, player, options, 11), False)
	connect_region("Tier 11", "Tier 12", region_map, None, lambda state: has_tier(state, player, options, 12), False)
	for location in tech_tree:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False)
	
	for region in region_map.values():
		world.multiworld.regions.append(region)

def connect_region(from_region, to_region, region_map, name, rule, is_connection_crucial):
	if from_region not in region_map:
	   if is_connection_crucial: throw_needed_region_error(from_region, f"connect_region, from: [{from_region}]")
	   return
	if to_region not in region_map:
	   if is_connection_crucial: throw_needed_region_error(to_region, f"connect_region, to: [{to_region}]")
	   return
	region_map[from_region].connect(region_map[to_region], name, rule = rule)

def make_location(world, location_name, region_name, region_map, rule_map, is_location_crucial):
	loc = make_location_adv(world, location_name, location_name, world.location_name_to_id[location_name], region_name, region_map, rule_map, is_location_crucial)
	if loc is not None: 
	   world.location_count += 1
	   
	   if world.enable_local_fill:
	       local_fill_loc.append(loc)
	return loc

def make_event_location(world, location_name_a, location_name_b, item_name, id, region_name, region_map, rule_map, is_location_crucial):
	location = make_location_adv(world, location_name_a, location_name_b, id, region_name, region_map, rule_map, is_location_crucial)
	if location is None: return None
	return location.place_locked_item(Item(item_name, ItemClassification.progression, None, world.player))

def make_location_adv(world, location_name_a, location_name_b, id, region_name, region_map, rule_map, is_location_crucial):
	if region_name not in region_map:
	   if is_location_crucial: throw_needed_region_error(region_name, f"make_location_adv, [{location_name_a}]")
	   return None
	
	location = Location(world.player, location_name_a, id, region_map[region_name])
	region_map[region_name].locations.append(location)
	
	if location_name_b in rule_map:
	   location.access_rule = rule_map[location_name_b]
	
	if location_name_a in priority_map:
	   location.progress_type = priority_map[location_name_a]
	
	return location

def throw_needed_region_error(region_name, sender):
	raise ValueError(f"For an unknown reason the region, [{region_name}] was not added as a region, it is required for [{sender}]")