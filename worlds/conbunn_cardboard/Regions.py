from BaseClasses import Location, Region, Item, ItemClassification, LocationProgressType
from .Locations import *
from .Rules import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

priority_map = []

def gen_create_regions(world):
	player = world.player
	rule_map = get_rule_map(world.player)
	
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
		"Cotten Skies": Region("Cotten Skies", world.player, world.multiworld),
		"Clay Canyon": Region("Clay Canyon", world.player, world.multiworld),
		"Samual Golf": Region("Samual Golf", world.player, world.multiworld),
		"Sticker Park": Region("Sticker Park", world.player, world.multiworld),
		"Dragon Raceway": Region("Dragon Raceway", world.player, world.multiworld),
		"Cardboard Station": Region("Cardboard Station", world.player, world.multiworld),
		"Polystyrene Peak": Region("Polystyrene Peak", world.player, world.multiworld),
		"Glue Summit": Region("Glue Summit", world.player, world.multiworld),
		"Cardbun Festival": Region("Cardbun Festival", world.player, world.multiworld)
	}
	
	region_map["Menu"].connect(region_map["Cutout Forest"])
	region_map["Cutout Forest"].connect(region_map["Connie's Garden"], rule = lambda state: has_unlock(state, player, "Connie's Garden"))
	region_map["Cutout Forest"].connect(region_map["Ribbon Village"], rule = lambda state: has_dash(state, player) and has_unlock(state, player, "Ribbon Village"))
	region_map["Ribbon Village"].connect(region_map["Origami Tree"], rule = lambda state: has_unlock(state, player, "Origami Tree"))
	region_map["Ribbon Village"].connect(region_map["Paper Bay"], rule = lambda state: has_unlock(state, player, "Paper Bay"))
	region_map["Paper Bay"].connect(region_map["Cardbun Viewing Area"], rule = lambda state: has_unlock(state, player, "Cardbun Viewing Area"))
	region_map["Paper Bay"].connect(region_map["Ink Beach"], rule = lambda state: has_bounce_pads(state, player) and has_unlock(state, player, "Ink Beach"))
	region_map["Ribbon Village"].connect(region_map["Bunny Circuit"], rule = lambda state: has_unlock(state, player, "Bunny Circuit"))
	region_map["Ribbon Village"].connect(region_map["IBee's Honeycomb"], rule = lambda state: has_unlock(state, player, "IBee's Honeycomb"))
	region_map["Ribbon Village"].connect(region_map["Cardbun Museum"], rule = lambda state: has_unlock(state, player, "Cardbun Museum"))
	region_map["Ribbon Village"].connect(region_map["Paint Hills"], rule = lambda state: has_bounce_pads(state, player))
	region_map["Paint Hills"].connect(region_map["Graffiti Panels"], rule = lambda state: has_unlock(state, player, "Graffiti Panels"))
	region_map["Paint Hills"].connect(region_map["Mountain Confetti"])
	region_map["Paint Hills"].connect(region_map["Cotten Skies"], rule = lambda state: has_unlock(state, player, "Cotten Skies"))
	region_map["Mountain Confetti"].connect(region_map["Clay Canyon"], rule = lambda state: has_unlock(state, player, "Clay Canyon"))
	region_map["Clay Canyon"].connect(region_map["Samual Golf"], rule = lambda state: has_unlock(state, player, "Samual Golf"))
	region_map["Clay Canyon"].connect(region_map["Sticker Park"], rule = lambda state: has_unlock(state, player, "Sticker Park"))
	region_map["Sticker Park"].connect(region_map["Dragon Raceway"], rule = lambda state: has_unlock(state, player, "Dragon Raceway"))
	region_map["Sticker Park"].connect(region_map["Cardboard Station"], rule = lambda state: has_unlock(state, player, "Cardboard Station"))
	region_map["Clay Canyon"].connect(region_map["Polystyrene Peak"], rule = lambda state: has_unlock(state, player, "Polystyrene Peak"))
	region_map["Polystyrene Peak"].connect(region_map["Glue Summit"], rule = lambda state: has_unlock(state, player, "Glue Summit"))
	region_map["Polystyrene Peak"].connect(region_map["Cardbun Festival"], rule = lambda state: has_unlock(state, player, "Cardbun Festival"))
	for location in coins:
		make_location(world, location[0], region_map[location[1]], rule_map)
	for location in cds:
		make_location(world, location[0], region_map[location[1]], rule_map)
	for location in skins:
		make_location(world, location[0], region_map[location[1]], rule_map)
	for location in coins:
		make_event_location(world, f"Event: {location[0]}", location[0], "Real Coin", None, region_map[location[1]], rule_map)
	
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