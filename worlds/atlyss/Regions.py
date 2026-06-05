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
		"Sanctum": Region("Sanctum", world.player, world.multiworld),
		"Outer Sanctum": Region("Outer Sanctum", world.player, world.multiworld),
		"Arcwood Pass": Region("Arcwood Pass", world.player, world.multiworld),
		"Effold Terrace": Region("Effold Terrace", world.player, world.multiworld),
		"Tuul Valley": Region("Tuul Valley", world.player, world.multiworld),
		"Sanctum Catacombs lvl 1": Region("Sanctum Catacombs lvl 1", world.player, world.multiworld),
		"Sanctum Catacombs lvl 2": Region("Sanctum Catacombs lvl 2", world.player, world.multiworld),
		"Sanctum Catacombs lvl 3": Region("Sanctum Catacombs lvl 3", world.player, world.multiworld),
		"Cresent Road": Region("Cresent Road", world.player, world.multiworld),
		"Tuul Enclave": Region("Tuul Enclave", world.player, world.multiworld),
		"Luvora Garden": Region("Luvora Garden", world.player, world.multiworld),
		"Cresent Keep": Region("Cresent Keep", world.player, world.multiworld),
		"Bularr Fortress": Region("Bularr Fortress", world.player, world.multiworld),
		"Cresent Grove lvl 1": Region("Cresent Grove lvl 1", world.player, world.multiworld),
		"Cresent Grove lvl 2": Region("Cresent Grove lvl 2", world.player, world.multiworld),
		"Gate of the Moon": Region("Gate of the Moon", world.player, world.multiworld),
		"Wall of the Stars": Region("Wall of the Stars", world.player, world.multiworld),
		"Redwoud": Region("Redwoud", world.player, world.multiworld),
		"Trial of the Stars": Region("Trial of the Stars", world.player, world.multiworld)
	}
	
	connect_region("Menu", "Sanctum", region_map, None, lambda state: True)
	connect_region("Sanctum", "Outer Sanctum", region_map, None, lambda state: has_area(state, player, options, "Outer Sanctum"))
	connect_region("Outer Sanctum", "Arcwood Pass", region_map, None, lambda state: has_area(state, player, options, "Arcwood Pass"))
	connect_region("Outer Sanctum", "Effold Terrace", region_map, None, lambda state: has_area(state, player, options, "Effold Terrace") and has_quest(state, player, options, "Diva Must Die"))
	connect_region("Outer Sanctum", "Tuul Valley", region_map, None, lambda state: has_area(state, player, options, "Tuul Valley"))
	connect_region("Arcwood Pass", "Sanctum Catacombs lvl 1", region_map, None, lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 1") and has_quest(state, player, options, "Communing Catacombs"))
	connect_region("Sanctum Catacombs lvl 1", "Sanctum Catacombs lvl 2", region_map, None, lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 2"))
	connect_region("Sanctum Catacombs lvl 2", "Sanctum Catacombs lvl 3", region_map, None, lambda state: has_area(state, player, options, "Sanctum Catacombs lvl 3"))
	connect_region("Arcwood Pass", "Cresent Road", region_map, None, lambda state: has_area(state, player, options, "Cresent Road") and has_quest(state, player, options, "The Keep Within"))
	connect_region("Tuul Valley", "Tuul Enclave", region_map, None, lambda state: has_area(state, player, options, "Tuul Enclave"))
	connect_region("Cresent Road", "Luvora Garden", region_map, None, lambda state: has_area(state, player, options, "Luvora Garden"))
	connect_region("Cresent Road", "Cresent Keep", region_map, None, lambda state: has_area(state, player, options, "Cresent Keep"))
	connect_region("Tuul Enclave", "Bularr Fortress", region_map, None, lambda state: has_area(state, player, options, "Bularr Fortress") and has_quest(state, player, options, "Finding Ammagon"))
	connect_region("Cresent Keep", "Cresent Grove lvl 1", region_map, None, lambda state: has_area(state, player, options, "Cresent Grove lvl 1") and has_quest(state, player, options, "The Keep Within"))
	connect_region("Cresent Grove lvl 1", "Cresent Grove lvl 2", region_map, None, lambda state: has_area(state, player, options, "Cresent Grove lvl 2"))
	connect_region("Cresent Keep", "Gate of the Moon", region_map, None, lambda state: has_area(state, player, options, "Gate of the Moon") and has_quest(state, player, options, "Tethering Grove"))
	connect_region("Gate of the Moon", "Wall of the Stars", region_map, None, lambda state: has_area(state, player, options, "Wall of the Stars"))
	connect_region("Gate of the Moon", "Redwoud", region_map, None, lambda state: has_area(state, player, options, "Redwoud"))
	connect_region("Wall of the Stars", "Trial of the Stars", region_map, None, lambda state: has_area(state, player, options, "Trial of the Stars") and has_quest(state, player, options, "Up and Over It"))
	if options.shop_sanity:
		for location in merchants:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map)
	
	for location in quests:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in levels:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in professions:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	make_location(world, "A New Journey", "Sanctum", region_map, rule_map)
	make_location(world, "Clearing Catacombs (1-6)", "Sanctum Catacombs lvl 1", region_map, rule_map)
	make_location(world, "Clearing Catacombs (6-12)", "Sanctum Catacombs lvl 2", region_map, rule_map)
	make_location(world, "Clearing Catacombs (12-18)", "Sanctum Catacombs lvl 3", region_map, rule_map)
	make_location(world, "Clearing Grove (15-20)", "Cresent Grove lvl 1", region_map, rule_map)
	make_location(world, "Clearing Grove (20-25)", "Cresent Grove lvl 2", region_map, rule_map)
	make_location(world, "Altered Vision", "Sanctum", region_map, rule_map)
	make_location(world, "Scaling the Tower", "Sanctum", region_map, rule_map)
	make_location(world, "Scaling Stars", "Trial of the Stars", region_map, rule_map)
	make_location(world, "Rude!", "Sanctum", region_map, rule_map)
	
	for location in quests:
		if location[1] in region_map:
			make_event_location(world, f"Quest Completion: {location[0]}", location[0], f"Complete: {location[0]}", None, location[1], region_map, rule_map)
	if options.is_class("fighter"):
		make_location(world, "Becoming a Fighter", "Sanctum", region_map, rule_map)
		make_location(world, "Judgement", "Sanctum", region_map, rule_map)
		
	
	if options.is_class("mystic"):
		make_location(world, "Becoming a Mystic", "Sanctum", region_map, rule_map)
		make_location(world, "Corrupted Arcana", "Sanctum", region_map, rule_map)
		make_location(world, "Holier than Thou", "Sanctum", region_map, rule_map)
		
	
	if options.is_class("bandit"):
		make_location(world, "Becoming a Bandit", "Sanctum", region_map, rule_map)
		
	
	
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