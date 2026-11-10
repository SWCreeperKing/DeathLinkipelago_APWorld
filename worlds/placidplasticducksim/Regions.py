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
		"Column 1": Region("Column 1", world.player, world.multiworld),
		"Column 2": Region("Column 2", world.player, world.multiworld),
		"Column 3": Region("Column 3", world.player, world.multiworld),
		"Column 4": Region("Column 4", world.player, world.multiworld),
		"Column 5": Region("Column 5", world.player, world.multiworld),
		"Column 6": Region("Column 6", world.player, world.multiworld),
		"Column 7": Region("Column 7", world.player, world.multiworld),
		"Column 8": Region("Column 8", world.player, world.multiworld),
		"Column 9": Region("Column 9", world.player, world.multiworld),
		"Column 10": Region("Column 10", world.player, world.multiworld)
	}
	
	connect_region("Menu", "Column 1", region_map, None, lambda state: has_column(state, player, options, 1), False)
	connect_region("Column 1", "Column 2", region_map, None, lambda state: has_column(state, player, options, 2), False)
	connect_region("Column 2", "Column 3", region_map, None, lambda state: has_column(state, player, options, 3), False)
	connect_region("Column 3", "Column 4", region_map, None, lambda state: has_column(state, player, options, 4), False)
	connect_region("Column 4", "Column 5", region_map, None, lambda state: has_column(state, player, options, 5), False)
	connect_region("Column 5", "Column 6", region_map, None, lambda state: has_column(state, player, options, 6), False)
	connect_region("Column 6", "Column 7", region_map, None, lambda state: has_column(state, player, options, 7), False)
	connect_region("Column 7", "Column 8", region_map, None, lambda state: has_column(state, player, options, 8), False)
	connect_region("Column 8", "Column 9", region_map, None, lambda state: has_column(state, player, options, 9), False)
	connect_region("Column 9", "Column 10", region_map, None, lambda state: has_column(state, player, options, 10), False)
	for location in base_game:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False)
	if options.ducks_please:
		for location in ducks_please:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map, False)
	
	if options.duck_addiction:
		for location in duck_addiction:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map, False)
	
	if options.so_many_ducks:
		for location in so_many_ducks:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map, False)
	
	if options.ducks_galore:
		for location in ducks_galore:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map, False)
	
	if options.ducklings:
		for location in ducklings:
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