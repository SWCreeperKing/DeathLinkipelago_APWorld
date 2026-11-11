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
		"101": Region("101", world.player, world.multiworld),
		"102": Region("102", world.player, world.multiworld),
		"102 Yard": Region("102 Yard", world.player, world.multiworld),
		"103": Region("103", world.player, world.multiworld),
		"104": Region("104", world.player, world.multiworld),
		"104 Backyard": Region("104 Backyard", world.player, world.multiworld),
		"104 Frontyard": Region("104 Frontyard", world.player, world.multiworld),
		"105": Region("105", world.player, world.multiworld),
		"105 Backyard": Region("105 Backyard", world.player, world.multiworld),
		"106": Region("106", world.player, world.multiworld),
		"106 Backyard": Region("106 Backyard", world.player, world.multiworld),
		"106 Sideroom": Region("106 Sideroom", world.player, world.multiworld),
		"107": Region("107", world.player, world.multiworld),
		"107 Yard": Region("107 Yard", world.player, world.multiworld),
		"108": Region("108", world.player, world.multiworld),
		"108 Backyard": Region("108 Backyard", world.player, world.multiworld),
		"108 Upstairs Living Room": Region("108 Upstairs Living Room", world.player, world.multiworld),
		"109": Region("109", world.player, world.multiworld),
		"110": Region("110", world.player, world.multiworld),
		"111": Region("111", world.player, world.multiworld),
		"112": Region("112", world.player, world.multiworld),
		"112 Backyard": Region("112 Backyard", world.player, world.multiworld),
		"113": Region("113", world.player, world.multiworld),
		"113 Backyard": Region("113 Backyard", world.player, world.multiworld),
		"113 Bedroom": Region("113 Bedroom", world.player, world.multiworld),
		"Greenview St": Region("Greenview St", world.player, world.multiworld)
	}
	
	connect_region("Greenview St", "101", region_map, None, lambda state: has_mini_electric_lock_pick(state, player, options) and has_lockpick(state, player, options), False)
	connect_region("102 Yard", "102", region_map, None, lambda state: has_glass_knife(state, player, options), False)
	connect_region("Greenview St", "102", region_map, None, lambda state: has_front_door_key_102(state, player, options), False)
	connect_region("Greenview St", "102 Yard", region_map, None, lambda state: has_diy_simple_lockpick(state, player, options) or has_climbing_gloves(state, player, options), False)
	connect_region("Greenview St", "103", region_map, None, lambda state: (has_hacking_pda(state, player, options) and has_diy_simple_lockpick(state, player, options)) or (has_glass_knife(state, player, options) and has_diy_simple_lockpick(state, player, options)), False)
	connect_region("104 Backyard", "104", region_map, None, lambda state: has_glass_knife(state, player, options), False)
	connect_region("Greenview St", "104", region_map, None, lambda state: has_mini_electric_lock_pick(state, player, options), False)
	connect_region("104 Frontyard", "104", region_map, None, lambda state: has_lockpick(state, player, options), False)
	connect_region("Greenview St", "104 Backyard", region_map, None, lambda state: has_lockpick(state, player, options), False)
	connect_region("Greenview St", "104 Frontyard", region_map, None, lambda state: has_climbing_gloves(state, player, options), False)
	connect_region("104", "104 Frontyard", region_map, None, lambda state: has_lockpick(state, player, options), False)
	connect_region("Greenview St", "105", region_map, None, lambda state: (has_lockpick(state, player, options) and has_diy_simple_lockpick(state, player, options)) or (has_diy_simple_lockpick(state, player, options) and has_climbing_gloves(state, player, options)), False)
	connect_region("105 Backyard", "105", region_map, None, lambda state: has_glass_knife(state, player, options), False)
	connect_region("Greenview St", "105 Backyard", region_map, None, lambda state: has_lockpick(state, player, options), False)
	connect_region("106 Sideroom", "106", region_map, None, lambda state: has_lockpick(state, player, options), False)
	connect_region("Greenview St", "106", region_map, None, lambda state: has_lockpick(state, player, options), False)
	connect_region("Greenview St", "106 Backyard", region_map, None, lambda state: has_lockpick(state, player, options), False)
	connect_region("106 Backyard", "106 Sideroom", region_map, None, lambda state: True, False)
	connect_region("107 Yard", "107", region_map, None, lambda state: has_glass_knife(state, player, options) or has_lockpick(state, player, options) or has_mini_electric_lock_pick(state, player, options), False)
	connect_region("Greenview St", "107 Yard", region_map, None, lambda state: has_diy_simple_lockpick(state, player, options) or has_climbing_gloves(state, player, options), False)
	connect_region("108 Backyard", "108", region_map, None, lambda state: has_glass_knife(state, player, options), False)
	connect_region("Greenview St", "108", region_map, None, lambda state: has_mini_electric_lock_pick(state, player, options) or has_climbing_gloves(state, player, options) or has_glass_knife(state, player, options), False)
	connect_region("Greenview St", "108 Backyard", region_map, None, lambda state: has_lockpick(state, player, options) or has_crowbar(state, player, options), False)
	connect_region("108", "108 Upstairs Living Room", region_map, None, lambda state: has_mini_electric_lock_pick(state, player, options), False)
	connect_region("Greenview St", "109", region_map, None, lambda state: has_crowbar(state, player, options) or has_diy_simple_lockpick(state, player, options) or (has_diy_simple_lockpick(state, player, options) and has_glass_knife(state, player, options)), False)
	connect_region("Greenview St", "110", region_map, None, lambda state: True, False)
	connect_region("Greenview St", "111", region_map, None, lambda state: has_diy_simple_lockpick(state, player, options), False)
	connect_region("112 Backyard", "112", region_map, None, lambda state: has_diy_simple_lockpick(state, player, options) or has_glass_knife(state, player, options), False)
	connect_region("Greenview St", "112", region_map, None, lambda state: has_lockpick(state, player, options), False)
	connect_region("Greenview St", "112 Backyard", region_map, None, lambda state: has_diy_simple_lockpick(state, player, options) or has_climbing_gloves(state, player, options), False)
	connect_region("Greenview St", "113", region_map, None, lambda state: has_mini_electric_lock_pick(state, player, options) or has_glass_knife(state, player, options) or has_front_door_key_113(state, player, options), False)
	connect_region("Greenview St", "113 Backyard", region_map, None, lambda state: has_diy_simple_lockpick(state, player, options) or has_climbing_gloves(state, player, options), False)
	connect_region("113", "113 Bedroom", region_map, None, lambda state: has_lockpick(state, player, options), False)
	connect_region("113 Backyard", "113 Bedroom", region_map, None, lambda state: True, False)
	connect_region("Menu", "Greenview St", region_map, None, lambda state: True, False)
	for location in locs:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False, True)
	make_event_location(world, "Event: [Crowbar]", "Crowbar", "Crowbar", None, "Greenview St", region_map, rule_map, False)
	make_event_location(world, "Event: [Flashlight]", "Flashlight", "Flashlight", None, "Greenview St", region_map, rule_map, False)
	make_event_location(world, "Event: [House 102: Front Door Key to 102]", "House 102: Front Door Key to 102", "Front door key 102", None, "102", region_map, rule_map, False)
	make_event_location(world, "Event: [House 113 Bedroom: Front Door Key 113]", "House 113 Bedroom: Front Door Key 113", "Front door key 113", None, "113 Bedroom", region_map, rule_map, False)
	
	
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