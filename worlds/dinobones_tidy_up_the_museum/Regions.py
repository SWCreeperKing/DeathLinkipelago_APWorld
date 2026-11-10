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
		"Crate 1": Region("Crate 1", world.player, world.multiworld),
		"Crate 2": Region("Crate 2", world.player, world.multiworld),
		"Crate 3": Region("Crate 3", world.player, world.multiworld),
		"Crate 4": Region("Crate 4", world.player, world.multiworld),
		"Crate 5": Region("Crate 5", world.player, world.multiworld),
		"Crate 6": Region("Crate 6", world.player, world.multiworld),
		"Crate 7": Region("Crate 7", world.player, world.multiworld),
		"Crate 8": Region("Crate 8", world.player, world.multiworld),
		"Crate 9": Region("Crate 9", world.player, world.multiworld),
		"Crate 10": Region("Crate 10", world.player, world.multiworld),
		"Crate 11": Region("Crate 11", world.player, world.multiworld),
		"Crate 12": Region("Crate 12", world.player, world.multiworld),
		"Crate 13": Region("Crate 13", world.player, world.multiworld),
		"Crate 14": Region("Crate 14", world.player, world.multiworld),
		"Crate 15": Region("Crate 15", world.player, world.multiworld),
		"Crate 16": Region("Crate 16", world.player, world.multiworld),
		"Crate 17": Region("Crate 17", world.player, world.multiworld),
		"Crate 18": Region("Crate 18", world.player, world.multiworld),
		"Crate 19": Region("Crate 19", world.player, world.multiworld),
		"Crate 20": Region("Crate 20", world.player, world.multiworld),
		"Crate 21": Region("Crate 21", world.player, world.multiworld),
		"Crate 22": Region("Crate 22", world.player, world.multiworld),
		"Crate 23": Region("Crate 23", world.player, world.multiworld),
		"Crate 24": Region("Crate 24", world.player, world.multiworld),
		"Crate 25": Region("Crate 25", world.player, world.multiworld),
		"Crate 26": Region("Crate 26", world.player, world.multiworld),
		"Crate 27": Region("Crate 27", world.player, world.multiworld),
		"Crate 28": Region("Crate 28", world.player, world.multiworld)
	}
	
	connect_region("Menu", "Crate 1", region_map, None, lambda state: has_crate(state, player, options, 1), False)
	connect_region("Menu", "Crate 2", region_map, None, lambda state: has_crate(state, player, options, 2), False)
	connect_region("Menu", "Crate 3", region_map, None, lambda state: has_crate(state, player, options, 3), False)
	connect_region("Menu", "Crate 4", region_map, None, lambda state: has_crate(state, player, options, 4), False)
	connect_region("Menu", "Crate 5", region_map, None, lambda state: has_crate(state, player, options, 5), False)
	connect_region("Menu", "Crate 6", region_map, None, lambda state: has_crate(state, player, options, 6), False)
	connect_region("Menu", "Crate 7", region_map, None, lambda state: has_crate(state, player, options, 7), False)
	connect_region("Menu", "Crate 8", region_map, None, lambda state: has_crate(state, player, options, 8), False)
	connect_region("Menu", "Crate 9", region_map, None, lambda state: has_crate(state, player, options, 9), False)
	connect_region("Menu", "Crate 10", region_map, None, lambda state: has_crate(state, player, options, 10), False)
	connect_region("Menu", "Crate 11", region_map, None, lambda state: has_crate(state, player, options, 11), False)
	connect_region("Menu", "Crate 12", region_map, None, lambda state: has_crate(state, player, options, 12), False)
	connect_region("Menu", "Crate 13", region_map, None, lambda state: has_crate(state, player, options, 13), False)
	connect_region("Menu", "Crate 14", region_map, None, lambda state: has_crate(state, player, options, 14), False)
	connect_region("Menu", "Crate 15", region_map, None, lambda state: has_crate(state, player, options, 15), False)
	connect_region("Menu", "Crate 16", region_map, None, lambda state: has_crate(state, player, options, 16), False)
	connect_region("Menu", "Crate 17", region_map, None, lambda state: has_crate(state, player, options, 17), False)
	connect_region("Menu", "Crate 18", region_map, None, lambda state: has_crate(state, player, options, 18), False)
	connect_region("Menu", "Crate 19", region_map, None, lambda state: has_crate(state, player, options, 19), False)
	connect_region("Menu", "Crate 20", region_map, None, lambda state: has_crate(state, player, options, 20), False)
	connect_region("Menu", "Crate 21", region_map, None, lambda state: has_crate(state, player, options, 21), False)
	connect_region("Menu", "Crate 22", region_map, None, lambda state: has_crate(state, player, options, 22), False)
	connect_region("Menu", "Crate 23", region_map, None, lambda state: has_crate(state, player, options, 23), False)
	connect_region("Menu", "Crate 24", region_map, None, lambda state: has_crate(state, player, options, 24), False)
	connect_region("Menu", "Crate 25", region_map, None, lambda state: has_crate(state, player, options, 25), False)
	connect_region("Menu", "Crate 26", region_map, None, lambda state: has_crate(state, player, options, 26), False)
	connect_region("Menu", "Crate 27", region_map, None, lambda state: has_crate(state, player, options, 27), False)
	connect_region("Menu", "Crate 28", region_map, None, lambda state: has_crate(state, player, options, 28), False)
	for location in bones_pallet:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False, False)
	for location in bones_crate:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False, True)
	
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

def make_location(world, location_name, region_name, region_map, rule_map, is_location_crucial, is_location_local):
	loc = make_location_adv(world, location_name, location_name, world.location_name_to_id[location_name], region_name, region_map, rule_map, is_location_crucial)
	if loc is not None: 
	   world.location_count += 1
	   
	   if world.enable_local_fill and is_location_local:
	       world.local_fill_loc.append(loc)
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