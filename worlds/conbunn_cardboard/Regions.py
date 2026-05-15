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
		"Cutout Forest": Region("Cutout Forest", world.player, world.multiworld),
		"Connie's Garden": Region("Connie's Garden", world.player, world.multiworld),
		"Ribbon Village": Region("Ribbon Village", world.player, world.multiworld),
		"Origami Tree": Region("Origami Tree", world.player, world.multiworld),
		"Paper Bay": Region("Paper Bay", world.player, world.multiworld),
		"Cardbun Viewing Area": Region("Cardbun Viewing Area", world.player, world.multiworld),
		"Ink Beach": Region("Ink Beach", world.player, world.multiworld),
		"Bunny Circuit": Region("Bunny Circuit", world.player, world.multiworld),
		"IBee's Honeycomb": Region("IBee's Honeycomb", world.player, world.multiworld),
		"Cardbun Museum": Region("Cardbun Museum", world.player, world.multiworld),
		"Paint Hills": Region("Paint Hills", world.player, world.multiworld),
		"Graffiti Panels": Region("Graffiti Panels", world.player, world.multiworld),
		"Mountain Confetti": Region("Mountain Confetti", world.player, world.multiworld),
		"Cotton Skies": Region("Cotton Skies", world.player, world.multiworld),
		"Clay Canyon": Region("Clay Canyon", world.player, world.multiworld),
		"Samual Golf": Region("Samual Golf", world.player, world.multiworld),
		"Sticker Park": Region("Sticker Park", world.player, world.multiworld),
		"Dragon Raceway": Region("Dragon Raceway", world.player, world.multiworld),
		"Cardboard Station": Region("Cardboard Station", world.player, world.multiworld),
		"Polystyrene Peak": Region("Polystyrene Peak", world.player, world.multiworld),
		"Glue Summit": Region("Glue Summit", world.player, world.multiworld),
		"Cardbun Festival": Region("Cardbun Festival", world.player, world.multiworld)
	}
	
	connect_region("Menu", "Cutout Forest", region_map, None, None)
	connect_region("Cutout Forest", "Connie's Garden (Cutout Forest)", region_map, None, lambda state: has_unlock(state, player, options, "Connie's Garden (Cutout Forest)"))
	connect_region("Cutout Forest", "Ribbon Village", region_map, None, lambda state: has_dash(state, player, options) and has_unlock(state, player, options, "Ribbon Village"))
	connect_region("Ribbon Village", "Origami Tree (Ribbon Village)", region_map, None, lambda state: has_unlock(state, player, options, "Origami Tree (Ribbon Village)"))
	connect_region("Ribbon Village", "Paper Bay", region_map, None, lambda state: has_unlock(state, player, options, "Paper Bay"))
	connect_region("Paper Bay", "Cardbun Viewing Area (Paper Bay)", region_map, None, lambda state: has_unlock(state, player, options, "Cardbun Viewing Area (Paper Bay)"))
	connect_region("Paper Bay", "Ink Beach (Paper Bay)", region_map, None, lambda state: has_bounce_pads(state, player, options) and has_unlock(state, player, options, "Ink Beach (Paper Bay)"))
	connect_region("Ribbon Village", "Bunny Circuit (Ribbon Village)", region_map, None, lambda state: has_unlock(state, player, options, "Bunny Circuit (Ribbon Village)"))
	connect_region("Ribbon Village", "IBee's Honeycomb (Ribbon Village)", region_map, None, lambda state: has_unlock(state, player, options, "IBee's Honeycomb (Ribbon Village)"))
	connect_region("Ribbon Village", "Cardbun Museum (Ribbon Village)", region_map, None, lambda state: has_unlock(state, player, options, "Cardbun Museum (Ribbon Village)"))
	connect_region("Ribbon Village", "Paint Hills", region_map, None, lambda state: has_bounce_pads(state, player, options))
	connect_region("Paint Hills", "Graffiti Panels (Paint Hills)", region_map, None, lambda state: has_unlock(state, player, options, "Graffiti Panels (Paint Hills)"))
	connect_region("Paint Hills", "Mountain Confetti", region_map, None, lambda state: has_bounce_pads(state, player, options))
	connect_region("Mountain Confetti", "Cotton Skies (Mountain Confetti)", region_map, None, lambda state: has_bounce_pads(state, player, options) and has_unlock(state, player, options, "Cotton Skies (Mountain Confetti)"))
	connect_region("Mountain Confetti", "Clay Canyon", region_map, None, lambda state: has_unlock(state, player, options, "Clay Canyon"))
	connect_region("Clay Canyon", "Samual Golf (Clay Canyon)", region_map, None, lambda state: has_unlock(state, player, options, "Samual Golf (Clay Canyon)"))
	connect_region("Clay Canyon", "Sticker Park", region_map, None, lambda state: has_unlock(state, player, options, "Sticker Park"))
	connect_region("Sticker Park", "Dragon Raceway (Sticker Park)", region_map, None, lambda state: has_bounce_pads(state, player, options) and has_unlock(state, player, options, "Dragon Raceway (Sticker Park)"))
	connect_region("Sticker Park", "Cardboard Station (Sticker Park)", region_map, None, lambda state: has_unlock(state, player, options, "Cardboard Station (Sticker Park)"))
	connect_region("Clay Canyon", "Polystyrene Peak", region_map, None, lambda state: has_unlock(state, player, options, "Polystyrene Peak"))
	connect_region("Polystyrene Peak", "Glue Summit (Polystyrene Peak)", region_map, None, lambda state: has_bounce_pads(state, player, options) and has_unlock(state, player, options, "Glue Summit (Polystyrene Peak)"))
	connect_region("Polystyrene Peak", "Cardbun Festival", region_map, None, lambda state: has_bounce_pads(state, player, options) and has_unlock(state, player, options, "Cardbun Festival"))
	connect_region("Ribbon Village", "Polystyrene Peak", region_map, None, lambda state: has_cable_car(state, player, options) and has_unlock(state, player, options, "Polystyrene Peak"))
	connect_region("Polystyrene Peak", "Ribbon Village", region_map, None, lambda state: has_cable_car(state, player, options) and has_unlock(state, player, options, "Ribbon Village"))
	connect_region("Polystyrene Peak", "Clay Canyon", region_map, None, None)
	connect_region("Clay Canyon", "Mountain Confetti", region_map, None, None)
	connect_region("Mountain Confetti", "Paint Hills", region_map, None, None)
	for location in coins:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in cds:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in skins:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map)
	for location in coins:
		if location[1] in region_map:
			make_event_location(world, f"Event: {location[0]}", location[0], "Real Coin", None, location[1], region_map, rule_map)
	
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