from BaseClasses import Location, Region, Item, ItemClassification, LocationProgressType
from .Locations import *
from .Rules import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/Werepelago/blob/master/Werepelago/Archipelago/ApShenanigans.cs]

priority_map = []

def gen_create_regions(world):
	player = world.player
	rule_map = get_rule_map(world.player)
	
	region_map = {
		"Menu": Region("Menu", world.player, world.multiworld),
		"Levels": Region("Levels", world.player, world.multiworld),
		"Collectibles": Region("Collectibles", world.player, world.multiworld),
		"Killsanity": Region("Killsanity", world.player, world.multiworld)
	}
	
	region_map["Menu"].connect(region_map["Levels"])
	region_map["Menu"].connect(region_map["Collectibles"])
	region_map["Menu"].connect(region_map["Killsanity"])
	for location in starting_checks:
		make_location(world, location[0], region_map[location[1]], rule_map)
	for location in collectibles:
		make_location(world, location[0], region_map[location[1]], rule_map)
	for location in levels:
		make_location(world, location[0], region_map[location[1]], rule_map)
	for location in npcs:
		make_location(world, location[0], region_map[location[1]], rule_map)
	for location in levels:
		make_event_location(world, f"Beat: {location[0]}", location[0], "Nights Survived", None, region_map[location[1]], rule_map)
	
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