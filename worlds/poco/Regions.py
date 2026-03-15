from BaseClasses import Location, Region, Item, ItemClassification, LocationProgressType
from .Locations import *
from .Rules import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

priority_map = []

def gen_create_regions(world):
	player = world.player
	options = world.options
	rule_map = get_rule_map(world.player)
	
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
	
	region_map["Menu"].connect(region_map["Gripp's Hoard"], rule = lambda state: True)
	region_map["Gripp's Hoard"].connect(region_map["Junk Rivers"], rule = lambda state: has_item(state, player, "Axe"))
	region_map["Junk Rivers"].connect(region_map["Launch Pad"], rule = lambda state: True)
	region_map["Launch Pad"].connect(region_map["Tunnels"], rule = lambda state: True)
	region_map["Launch Pad"].connect(region_map["Garden"], rule = lambda state: has_item(state, player, "Coin"))
	region_map["Launch Pad"].connect(region_map["Lake Path"], rule = lambda state: True)
	region_map["Lake Path"].connect(region_map["Water Gate"], rule = lambda state: has_item(state, player, "Valve Handle"))
	region_map["Water Gate"].connect(region_map["Garden"], rule = lambda state: True)
	region_map["Launch Pad"].connect(region_map["Mountain"], rule = lambda state: has_item(state, player, "Potato Battery"))
	region_map["Lake Path"].connect(region_map["Fisherman's Island"], rule = lambda state: has_item(state, player, "Spoon"))
	region_map["Gripp's Hoard"].connect(region_map["Backrooms #1"], rule = lambda state: has_item(state, player, "Old Key"))
	region_map["Backrooms #1"].connect(region_map["Backrooms #2"], rule = lambda state: has_item(state, player, "Bone Key"))
	region_map["Backrooms #2"].connect(region_map["Backrooms #3"], rule = lambda state: has_item(state, player, "Golden Key"))
	region_map["Garden"].connect(region_map["Garden Cave"], rule = lambda state: has_item(state, player, "Machete"))
	region_map["Mountain"].connect(region_map["Mountain Top"], rule = lambda state: has_item(state, player, "Rope"))
	region_map["Tunnels"].connect(region_map["Tunnels Cave"], rule = lambda state: done_quest(state, player, "Cerberus"))
	for location in locations:
		make_location(world, location[0], region_map[location[1]], rule_map)
	make_event_location(world, "Complete Nari's Quest", "Complete Nari's Quest", "Nari's Quest Completion", None, region_map["Garden"], rule_map)
	make_event_location(world, "Complete Ojet's Quest", "Complete Ojet's Quest", "Ojet's Quest Completion", None, region_map["Water Gate"], rule_map)
	make_event_location(world, "Complete Gultch's Quest", "Complete Gultch's Quest", "Gultch's Quest Completion", None, region_map["Mountain"], rule_map)
	make_event_location(world, "Complete Jaz's Quest", "Complete Jaz's Quest", "Jaz's Quest Completion", None, region_map["Lake Path"], rule_map)
	make_event_location(world, "Complete Dungsworth's Quest", "Complete Dungsworth's Quest", "Dungsworth's Quest Completion", None, region_map["Lake Path"], rule_map)
	make_event_location(world, "Complete Weevilton's Quest", "Complete Weevilton's Quest", "Weevilton's Quest Completion", None, region_map["Mountain Top"], rule_map)
	make_event_location(world, "Complete Scuttlesby's Quest", "Complete Scuttlesby's Quest", "Scuttlesby's Quest Completion", None, region_map["Backrooms #3"], rule_map)
	make_event_location(world, "Complete Cerberus's Quest", "Complete Cerberus's Quest", "Cerberus's Quest Completion", None, region_map["Tunnels"], rule_map)
	
	for region in region_map.values():
		world.multiworld.regions.append(region)

def make_location(world, location_name, region, rule_map):
	world.location_count += 1
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
	
	return location