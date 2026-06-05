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
		"Levels": Region("Levels", world.player, world.multiworld),
		"Collectibles": Region("Collectibles", world.player, world.multiworld)
	}
	
	if options.kill_sanity:
		region_map["Killsanity"] = Region("Killsanity", world.player, world.multiworld)
	connect_region("Menu", "Levels", region_map, None, None)
	connect_region("Menu", "Collectibles", region_map, None, None)
	connect_region("Menu", "Killsanity", region_map, None, None)
	for location in starting_checks:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in collectibles:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in levels:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in npcs:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in levels:
		if location[1] in region_map:
			make_event_location(world, f"Beat: {location[0]}", location[0], "Nights Survived", None, location[1], region_map, rule_map)
	
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