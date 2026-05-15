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
		"Gripp's Hoard": Region("Gripp's Hoard", world.player, world.multiworld),
		"Junk Rivers": Region("Junk Rivers", world.player, world.multiworld),
		"Launch Pad": Region("Launch Pad", world.player, world.multiworld),
		"Tunnels": Region("Tunnels", world.player, world.multiworld),
		"Garden": Region("Garden", world.player, world.multiworld),
		"Lake Path": Region("Lake Path", world.player, world.multiworld),
		"Water Gate": Region("Water Gate", world.player, world.multiworld),
		"Mountain": Region("Mountain", world.player, world.multiworld),
		"Fisherman's Island": Region("Fisherman's Island", world.player, world.multiworld),
		"Backrooms #1": Region("Backrooms #1", world.player, world.multiworld),
		"Backrooms #2": Region("Backrooms #2", world.player, world.multiworld),
		"Backrooms #3": Region("Backrooms #3", world.player, world.multiworld),
		"Garden Cave": Region("Garden Cave", world.player, world.multiworld),
		"Mountain Top": Region("Mountain Top", world.player, world.multiworld),
		"Tunnels Cave": Region("Tunnels Cave", world.player, world.multiworld)
	}
	
	connect_region("Menu", "Gripp's Hoard", region_map, None, lambda state: True)
	connect_region("Gripp's Hoard", "Junk Rivers", region_map, None, lambda state: has(state, player, options, "Axe"))
	connect_region("Junk Rivers", "Launch Pad", region_map, None, lambda state: True)
	connect_region("Launch Pad", "Tunnels", region_map, None, lambda state: True)
	connect_region("Launch Pad", "Garden", region_map, None, lambda state: has(state, player, options, "Coin"))
	connect_region("Launch Pad", "Lake Path", region_map, None, lambda state: True)
	connect_region("Lake Path", "Water Gate", region_map, None, lambda state: has(state, player, options, "Valve Handle"))
	connect_region("Water Gate", "Garden", region_map, None, lambda state: True)
	connect_region("Launch Pad", "Mountain", region_map, None, lambda state: has(state, player, options, "Potato Battery"))
	connect_region("Lake Path", "Fisherman's Island", region_map, None, lambda state: has(state, player, options, "Spoon"))
	connect_region("Gripp's Hoard", "Backrooms #1", region_map, None, lambda state: has(state, player, options, "Old Key"))
	connect_region("Backrooms #1", "Backrooms #2", region_map, None, lambda state: has(state, player, options, "Bone Key"))
	connect_region("Backrooms #2", "Backrooms #3", region_map, None, lambda state: has(state, player, options, "Golden Key"))
	connect_region("Garden", "Garden Cave", region_map, None, lambda state: has(state, player, options, "Machete"))
	connect_region("Mountain", "Mountain Top", region_map, None, lambda state: has(state, player, options, "Rope"))
	connect_region("Tunnels", "Tunnels Cave", region_map, None, lambda state: done_quest(state, player, options, "Cerberus"))
	for location in locations:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in achievements:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in note:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	make_event_location(world, "Complete Nari's Quest", "Complete Nari's Quest", "Nari's Quest Completion", None, "Garden", region_map, rule_map)
	make_event_location(world, "Complete Ojet's Quest", "Complete Ojet's Quest", "Ojet's Quest Completion", None, "Water Gate", region_map, rule_map)
	make_event_location(world, "Complete Gultch's Quest", "Complete Gultch's Quest", "Gultch's Quest Completion", None, "Mountain", region_map, rule_map)
	make_event_location(world, "Complete Jaz's Quest", "Complete Jaz's Quest", "Jaz's Quest Completion", None, "Lake Path", region_map, rule_map)
	make_event_location(world, "Complete Dungsworth's Quest", "Complete Dungsworth's Quest", "Dungsworth's Quest Completion", None, "Lake Path", region_map, rule_map)
	make_event_location(world, "Complete Weevilton's Quest", "Complete Weevilton's Quest", "Weevilton's Quest Completion", None, "Mountain Top", region_map, rule_map)
	make_event_location(world, "Complete Scuttlesby's Quest", "Complete Scuttlesby's Quest", "Scuttlesby's Quest Completion", None, "Backrooms #3", region_map, rule_map)
	make_event_location(world, "Complete Cerberus's Quest", "Complete Cerberus's Quest", "Cerberus's Quest Completion", None, "Tunnels", region_map, rule_map)
	
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