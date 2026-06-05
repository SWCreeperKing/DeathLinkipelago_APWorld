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
		"Menu": Region("Menu", world.player, world.multiworld)
	}
	
	if options.bacteria:
		region_map["Bacteria"] = Region("Bacteria", world.player, world.multiworld)
	if options.virus:
		region_map["Virus"] = Region("Virus", world.player, world.multiworld)
	if options.fungus:
		region_map["Fungus"] = Region("Fungus", world.player, world.multiworld)
	if options.parasite:
		region_map["Parasite"] = Region("Parasite", world.player, world.multiworld)
	if options.prion:
		region_map["Prion"] = Region("Prion", world.player, world.multiworld)
	if options.nano_virus:
		region_map["Nano Virus"] = Region("Nano Virus", world.player, world.multiworld)
	if options.bio_weapon:
		region_map["Bio Weapon"] = Region("Bio Weapon", world.player, world.multiworld)
	if options.bacteria:
		connect_region("Menu", "Bacteria", region_map, None, lambda state: has(state, player, options, "Bacteria"))
	
	if options.bacteria:
		for location in bacteria_techs:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map)
	
	if options.bacteria:
		make_event_location(world, "Event: Beat Bacteria on Normal", "Beat Bacteria on Normal", "Victory", None, "Bacteria", region_map, rule_map)
		
	
	if options.virus:
		connect_region("Menu", "Virus", region_map, None, lambda state: has(state, player, options, "Virus"))
	
	if options.virus:
		for location in virus_techs:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map)
	
	if options.virus:
		make_event_location(world, "Event: Beat Virus on Normal", "Beat Virus on Normal", "Victory", None, "Virus", region_map, rule_map)
		
	
	if options.fungus:
		connect_region("Menu", "Fungus", region_map, None, lambda state: has(state, player, options, "Fungus"))
	
	if options.fungus:
		for location in fungus_techs:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map)
	
	if options.fungus:
		make_event_location(world, "Event: Beat Fungus on Normal", "Beat Fungus on Normal", "Victory", None, "Fungus", region_map, rule_map)
		
	
	if options.parasite:
		connect_region("Menu", "Parasite", region_map, None, lambda state: has(state, player, options, "Parasite"))
	
	if options.parasite:
		for location in parasite_techs:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map)
	
	if options.parasite:
		make_event_location(world, "Event: Beat Parasite on Normal", "Beat Parasite on Normal", "Victory", None, "Parasite", region_map, rule_map)
		
	
	if options.prion:
		connect_region("Menu", "Prion", region_map, None, lambda state: has(state, player, options, "Prion"))
	
	if options.prion:
		for location in prion_techs:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map)
	
	if options.prion:
		make_event_location(world, "Event: Beat Prion on Normal", "Beat Prion on Normal", "Victory", None, "Prion", region_map, rule_map)
		
	
	if options.nano_virus:
		connect_region("Menu", "Nano Virus", region_map, None, lambda state: has(state, player, options, "Nano Virus"))
	
	if options.nano_virus:
		for location in nano_virus_techs:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map)
	
	if options.nano_virus:
		make_event_location(world, "Event: Beat Nano Virus on Normal", "Beat Nano Virus on Normal", "Victory", None, "Nano Virus", region_map, rule_map)
		
	
	if options.bio_weapon:
		connect_region("Menu", "Bio Weapon", region_map, None, lambda state: has(state, player, options, "Bio Weapon"))
	
	if options.bio_weapon:
		for location in bio_weapon_techs:
			if location[1] in region_map:
				make_location(world, location[0], location[1], region_map, rule_map)
	
	if options.bio_weapon:
		make_event_location(world, "Event: Beat Bio Weapon on Normal", "Beat Bio Weapon on Normal", "Victory", None, "Bio Weapon", region_map, rule_map)
		
	
	
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