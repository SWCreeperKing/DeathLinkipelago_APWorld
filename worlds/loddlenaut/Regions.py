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
		"Upgrades": Region("Upgrades", world.player, world.multiworld),
		"GUPPI Ravine": Region("GUPPI Ravine", world.player, world.multiworld),
		"GUPPI Campus": Region("GUPPI Campus", world.player, world.multiworld),
		"North of GUPPI Campus": Region("North of GUPPI Campus", world.player, world.multiworld),
		"Home Cave": Region("Home Cave", world.player, world.multiworld),
		"North West of Home Cave": Region("North West of Home Cave", world.player, world.multiworld),
		"North GUPPI Ravine": Region("North GUPPI Ravine", world.player, world.multiworld),
		"Ripple Reef": Region("Ripple Reef", world.player, world.multiworld),
		"North of Home Cave": Region("North of Home Cave", world.player, world.multiworld),
		"Tangle Bay": Region("Tangle Bay", world.player, world.multiworld),
		"West of Flotsam Flats": Region("West of Flotsam Flats", world.player, world.multiworld),
		"West of Home Cave": Region("West of Home Cave", world.player, world.multiworld),
		"South of Home Cave": Region("South of Home Cave", world.player, world.multiworld),
		"Flotsam Flats": Region("Flotsam Flats", world.player, world.multiworld),
		"North of Flotsam Flats": Region("North of Flotsam Flats", world.player, world.multiworld),
		"Grimy Gulf": Region("Grimy Gulf", world.player, world.multiworld),
		"West of Grimy Gulf": Region("West of Grimy Gulf", world.player, world.multiworld),
		"Goddle Grotto Entrance": Region("Goddle Grotto Entrance", world.player, world.multiworld),
		"Goddle Grotto": Region("Goddle Grotto", world.player, world.multiworld)
	}
	
	if options.cooksanity:
		region_map["Cooking"] = Region("Cooking", world.player, world.multiworld)
	if options.evolutionsanity:
		region_map["Evolutions"] = Region("Evolutions", world.player, world.multiworld)
	connect_region("Home Cave", "North West of Home Cave", region_map, None, None, False)
	connect_region("North West of Home Cave", "Home Cave", region_map, None, None, False)
	connect_region("Home Cave", "North of Home Cave", region_map, None, None, False)
	connect_region("North of Home Cave", "Home Cave", region_map, None, None, False)
	connect_region("Home Cave", "Ripple Reef", region_map, None, None, False)
	connect_region("Ripple Reef", "Home Cave", region_map, None, None, False)
	connect_region("Home Cave", "South of Home Cave", region_map, None, None, False)
	connect_region("South of Home Cave", "Home Cave", region_map, None, None, False)
	connect_region("Home Cave", "West of Home Cave", region_map, None, None, False)
	connect_region("West of Home Cave", "Home Cave", region_map, None, None, False)
	connect_region("Tangle Bay", "North West of Home Cave", region_map, None, None, False)
	connect_region("North West of Home Cave", "Tangle Bay", region_map, None, lambda state: has(state, player, options, "Tangle Bay"), False)
	connect_region("Tangle Bay", "West of Home Cave", region_map, None, None, False)
	connect_region("West of Home Cave", "Tangle Bay", region_map, None, lambda state: has(state, player, options, "Tangle Bay"), False)
	connect_region("Tangle Bay", "West of Flotsam Flats", region_map, None, lambda state: has(state, player, options, "West of Flotsam Flats"), False)
	connect_region("West of Flotsam Flats", "Tangle Bay", region_map, None, lambda state: has(state, player, options, "Tangle Bay"), False)
	connect_region("North West of Home Cave", "West of Home Cave", region_map, None, None, False)
	connect_region("West of Home Cave", "North West of Home Cave", region_map, None, None, False)
	connect_region("North West of Home Cave", "North of Home Cave", region_map, None, None, False)
	connect_region("North of Home Cave", "North West of Home Cave", region_map, None, None, False)
	connect_region("West of Home Cave", "South of Home Cave", region_map, None, None, False)
	connect_region("South of Home Cave", "West of Home Cave", region_map, None, None, False)
	connect_region("West of Home Cave", "West of Flotsam Flats", region_map, None, lambda state: has(state, player, options, "West of Flotsam Flats"), False)
	connect_region("West of Flotsam Flats", "West of Home Cave", region_map, None, None, False)
	connect_region("South of Home Cave", "West of Flotsam Flats", region_map, None, lambda state: has(state, player, options, "West of Flotsam Flats"), False)
	connect_region("West of Flotsam Flats", "South of Home Cave", region_map, None, None, False)
	connect_region("West of Flotsam Flats", "Flotsam Flats", region_map, None, lambda state: has(state, player, options, "Flotsam Flats"), False)
	connect_region("Flotsam Flats", "West of Flotsam Flats", region_map, None, lambda state: has(state, player, options, "West of Flotsam Flats"), False)
	connect_region("South of Home Cave", "Flotsam Flats", region_map, None, lambda state: has(state, player, options, "Flotsam Flats"), False)
	connect_region("Flotsam Flats", "South of Home Cave", region_map, None, None, False)
	connect_region("South of Home Cave", "North of Flotsam Flats", region_map, None, lambda state: has(state, player, options, "North of Flotsam Flats"), False)
	connect_region("North of Flotsam Flats", "South of Home Cave", region_map, None, None, False)
	connect_region("Flotsam Flats", "North of Flotsam Flats", region_map, None, lambda state: has(state, player, options, "North of Flotsam Flats"), False)
	connect_region("North of Flotsam Flats", "Flotsam Flats", region_map, None, lambda state: has(state, player, options, "Flotsam Flats"), False)
	connect_region("Flotsam Flats", "West of Grimy Gulf", region_map, None, lambda state: has(state, player, options, "West of Grimy Gulf"), False)
	connect_region("West of Grimy Gulf", "Flotsam Flats", region_map, None, lambda state: has(state, player, options, "Flotsam Flats"), False)
	connect_region("West of Grimy Gulf", "North of Flotsam Flats", region_map, None, lambda state: has(state, player, options, "North of Flotsam Flats"), False)
	connect_region("North of Flotsam Flats", "West of Grimy Gulf", region_map, None, lambda state: has(state, player, options, "West of Grimy Gulf"), False)
	connect_region("West of Grimy Gulf", "GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Ravine"), False)
	connect_region("GUPPI Ravine", "West of Grimy Gulf", region_map, None, lambda state: has(state, player, options, "West of Grimy Gulf"), False)
	connect_region("West of Grimy Gulf", "Grimy Gulf", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "Grimy Gulf"), False)
	connect_region("Grimy Gulf", "West of Grimy Gulf", region_map, None, lambda state: has(state, player, options, "West of Grimy Gulf"), False)
	connect_region("Grimy Gulf", "GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Ravine"), False)
	connect_region("GUPPI Ravine", "Grimy Gulf", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "Grimy Gulf"), False)
	connect_region("Grimy Gulf", "Goddle Grotto Entrance", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "Goddle Grotto Entrance"), False)
	connect_region("Goddle Grotto Entrance", "Grimy Gulf", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "Grimy Gulf"), False)
	connect_region("Goddle Grotto Entrance", "Goddle Grotto", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "Goddle Grotto") and has(state, player, options, "GUPPI Ravine"), False)
	connect_region("Goddle Grotto", "Goddle Grotto Entrance", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "Goddle Grotto Entrance"), False)
	connect_region("GUPPI Ravine", "North of Flotsam Flats", region_map, None, lambda state: has(state, player, options, "North of Flotsam Flats"), False)
	connect_region("North of Flotsam Flats", "GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Ravine"), False)
	connect_region("GUPPI Ravine", "Ripple Reef", region_map, None, None, False)
	connect_region("Ripple Reef", "GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Ravine"), False)
	connect_region("GUPPI Ravine", "North GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "North GUPPI Ravine"), False)
	connect_region("North GUPPI Ravine", "GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Ravine"), False)
	connect_region("GUPPI Ravine", "GUPPI Campus", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Campus"), False)
	connect_region("GUPPI Campus", "GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Ravine"), False)
	connect_region("North of Home Cave", "Ripple Reef", region_map, None, None, False)
	connect_region("Ripple Reef", "North of Home Cave", region_map, None, None, False)
	connect_region("North of Home Cave", "North GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "North GUPPI Ravine"), False)
	connect_region("North GUPPI Ravine", "North of Home Cave", region_map, None, None, False)
	connect_region("North GUPPI Ravine", "GUPPI Campus", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Campus"), False)
	connect_region("GUPPI Campus", "North GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "North GUPPI Ravine"), False)
	connect_region("North GUPPI Ravine", "North of GUPPI Campus", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "North of GUPPI Campus"), False)
	connect_region("North of GUPPI Campus", "North GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "North GUPPI Ravine"), False)
	connect_region("Ripple Reef", "North of Flotsam Flats", region_map, None, lambda state: has(state, player, options, "North of Flotsam Flats"), False)
	connect_region("North of Flotsam Flats", "Ripple Reef", region_map, None, None, False)
	connect_region("Ripple Reef", "South of Home Cave", region_map, None, None, False)
	connect_region("South of Home Cave", "Ripple Reef", region_map, None, None, False)
	connect_region("GUPPI Campus", "North of GUPPI Campus", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "North of GUPPI Campus"), False)
	connect_region("North of GUPPI Campus", "GUPPI Campus", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Campus"), False)
	connect_region("North of GUPPI Campus", "Goddle Grotto Entrance", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "Goddle Grotto Entrance"), False)
	connect_region("Goddle Grotto Entrance", "North of GUPPI Campus", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "North of GUPPI Campus"), False)
	connect_region("GUPPI Campus", "Goddle Grotto Entrance", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "Goddle Grotto Entrance"), False)
	connect_region("Goddle Grotto Entrance", "GUPPI Campus", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Campus"), False)
	connect_region("GUPPI Ravine", "Goddle Grotto Entrance", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "Goddle Grotto Entrance"), False)
	connect_region("Goddle Grotto Entrance", "GUPPI Ravine", region_map, None, lambda state: has_depth(state, player, options) and has(state, player, options, "GUPPI Ravine"), False)
	connect_region("Menu", "Upgrades", region_map, None, None, False)
	connect_region("Menu", "Evolutions", region_map, None, lambda state: has_any(state, player, options, ["GUPPI Campus", "Ripple Reef", "Tangle Bay", "Flotsam Flats", "Grimy Gulf", "Goddle Grotto"]), False)
	connect_region("Menu", "Cooking", region_map, None, lambda state: has(state, player, options, "Cooking Module"), False)
	connect_region("Menu", "Home Cave", region_map, None, None, False)
	for location in clean_biomes:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False)
	for location in find_biomes:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False)
	for location in upgrades:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False)
	for location in badges:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False)
	for location in recipes:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False)
	for location in evolutions:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False)
	make_event_location(world, "Clean the GUPPI Campus", "Clean GUPPI Campus 100%", "Biomes Cleaned", None, "GUPPI Campus", region_map, rule_map, False)
	make_event_location(world, "Clean the Ripple Reef", "Clean Ripple Reef 100%", "Biomes Cleaned", None, "Ripple Reef", region_map, rule_map, False)
	make_event_location(world, "Clean the Tangle Bay", "Clean Tangle Bay 100%", "Biomes Cleaned", None, "Tangle Bay", region_map, rule_map, False)
	make_event_location(world, "Clean the Flotsam Flats", "Clean Flotsam Flats 100%", "Biomes Cleaned", None, "Flotsam Flats", region_map, rule_map, False)
	make_event_location(world, "Clean the Grimy Gulf", "Clean Grimy Gulf 100%", "Biomes Cleaned", None, "Grimy Gulf", region_map, rule_map, False)
	make_event_location(world, "Clean the Goddle Grotto", "Clean Goddle Grotto 100%", "Biomes Cleaned", None, "Goddle Grotto", region_map, rule_map, False)
	
	make_event_location(world, "Event Pick: Tubey Melon (GUPPI Ravine)", "", "Tubey Melon", None, "GUPPI Ravine", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Pearl Berries (GUPPI Ravine)", "", "Pearl Berries", None, "GUPPI Ravine", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (GUPPI Campus)", "", "Tubey Melon", None, "GUPPI Campus", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Pearl Berries (GUPPI Campus)", "", "Pearl Berries", None, "GUPPI Campus", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (North of GUPPI Campus)", "", "Tubey Melon", None, "North of GUPPI Campus", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (Home Cave)", "", "Tubey Melon", None, "Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Coral Pear (Home Cave)", "", "Coral Pear", None, "Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Passion Fig (Home Cave)", "", "Passion Fig", None, "Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (North West of Home Cave)", "", "Tubey Melon", None, "North West of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Star Kelp (North West of Home Cave)", "", "Star Kelp", None, "North West of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Pearl Berries (North GUPPI Ravine)", "", "Pearl Berries", None, "North GUPPI Ravine", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (Ripple Reef)", "", "Tubey Melon", None, "Ripple Reef", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Coral Pear (Ripple Reef)", "", "Coral Pear", None, "Ripple Reef", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (North of Home Cave)", "", "Tubey Melon", None, "North of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Coral Pear (North of Home Cave)", "", "Coral Pear", None, "North of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Star Kelp (North of Home Cave)", "", "Star Kelp", None, "North of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Rainbow Star Kelp (North of Home Cave)", "", "Rainbow Star Kelp", None, "North of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Pearl Berries (North of Home Cave)", "", "Pearl Berries", None, "North of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (Tangle Bay)", "", "Tubey Melon", None, "Tangle Bay", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Star Kelp (Tangle Bay)", "", "Star Kelp", None, "Tangle Bay", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Rainbow Star Kelp (Tangle Bay)", "", "Rainbow Star Kelp", None, "Tangle Bay", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Kelp Heart (Tangle Bay)", "", "Kelp Heart", None, "Tangle Bay", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (West of Flotsam Flats)", "", "Tubey Melon", None, "West of Flotsam Flats", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Star Kelp (West of Flotsam Flats)", "", "Star Kelp", None, "West of Flotsam Flats", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Passion Fig (West of Flotsam Flats)", "", "Passion Fig", None, "West of Flotsam Flats", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (West of Home Cave)", "", "Tubey Melon", None, "West of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Star Kelp (West of Home Cave)", "", "Star Kelp", None, "West of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Rainbow Star Kelp (West of Home Cave)", "", "Rainbow Star Kelp", None, "West of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (South of Home Cave)", "", "Tubey Melon", None, "South of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Coral Pear (South of Home Cave)", "", "Coral Pear", None, "South of Home Cave", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (Flotsam Flats)", "", "Tubey Melon", None, "Flotsam Flats", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Lotus Kiwi (Flotsam Flats)", "", "Lotus Kiwi", None, "Flotsam Flats", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Lily Banana (Flotsam Flats)", "", "Lily Banana", None, "Flotsam Flats", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (North of Flotsam Flats)", "", "Tubey Melon", None, "North of Flotsam Flats", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Coral Pear (North of Flotsam Flats)", "", "Coral Pear", None, "North of Flotsam Flats", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Passion Fig (North of Flotsam Flats)", "", "Passion Fig", None, "North of Flotsam Flats", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (Grimy Gulf)", "", "Tubey Melon", None, "Grimy Gulf", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Coral Pear (Grimy Gulf)", "", "Coral Pear", None, "Grimy Gulf", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Passion Fig (Grimy Gulf)", "", "Passion Fig", None, "Grimy Gulf", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Star Kelp (Grimy Gulf)", "", "Star Kelp", None, "Grimy Gulf", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Rainbow Star Kelp (Grimy Gulf)", "", "Rainbow Star Kelp", None, "Grimy Gulf", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Kelp Heart (Grimy Gulf)", "", "Kelp Heart", None, "Grimy Gulf", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Lily Banana (Grimy Gulf)", "", "Lily Banana", None, "Grimy Gulf", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (West of Grimy Gulf)", "", "Tubey Melon", None, "West of Grimy Gulf", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Lily Banana (West of Grimy Gulf)", "", "Lily Banana", None, "West of Grimy Gulf", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (Goddle Grotto Entrance)", "", "Tubey Melon", None, "Goddle Grotto Entrance", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Kelp Heart (Goddle Grotto Entrance)", "", "Kelp Heart", None, "Goddle Grotto Entrance", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Lily Banana (Goddle Grotto Entrance)", "", "Lily Banana", None, "Goddle Grotto Entrance", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Coral Pear (Goddle Grotto Entrance)", "", "Coral Pear", None, "Goddle Grotto Entrance", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Tubey Melon (Goddle Grotto)", "", "Tubey Melon", None, "Goddle Grotto", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Pearl Berries (Goddle Grotto)", "", "Pearl Berries", None, "Goddle Grotto", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Crystal Crisp (Goddle Grotto)", "", "Crystal Crisp", None, "Goddle Grotto", region_map, rule_map, False)
	make_event_location(world, "Event Pick: Star Kelp (Goddle Grotto)", "", "Star Kelp", None, "Goddle Grotto", region_map, rule_map, False)
	
	for location in recipes:
		if location[1] in region_map:
			make_event_location(world, f"Event: {location[0]}", location[0], location[0].replace('Cook: ', ''), None, location[1], region_map, rule_map, False)
	
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
	if loc is not None: world.location_count += 1
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