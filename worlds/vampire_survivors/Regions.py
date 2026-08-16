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
		"Characters": Region("Characters", world.player, world.multiworld)
	}
	
	if options.enemysanity:
		region_map["Enemies"] = Region("Enemies", world.player, world.multiworld)
	if "Mad Forest" in world.final_included_stages_list:
		region_map["Mad Forest"] = Region("Mad Forest", world.player, world.multiworld)
	if "Eudaimonia M." in world.final_included_stages_list:
		region_map["Eudaimonia M."] = Region("Eudaimonia M.", world.player, world.multiworld)
	if "Inlaid Library" in world.final_included_stages_list:
		region_map["Inlaid Library"] = Region("Inlaid Library", world.player, world.multiworld)
	if "Dairy Plant" in world.final_included_stages_list:
		region_map["Dairy Plant"] = Region("Dairy Plant", world.player, world.multiworld)
	if "Gallo Tower" in world.final_included_stages_list:
		region_map["Gallo Tower"] = Region("Gallo Tower", world.player, world.multiworld)
	if "Cappella Magna" in world.final_included_stages_list:
		region_map["Cappella Magna"] = Region("Cappella Magna", world.player, world.multiworld)
	if "Il Molise" in world.final_included_stages_list:
		region_map["Il Molise"] = Region("Il Molise", world.player, world.multiworld)
	if "Moongolow" in world.final_included_stages_list:
		region_map["Moongolow"] = Region("Moongolow", world.player, world.multiworld)
	if "Green Acres" in world.final_included_stages_list:
		region_map["Green Acres"] = Region("Green Acres", world.player, world.multiworld)
	if "The Bone Zone" in world.final_included_stages_list:
		region_map["The Bone Zone"] = Region("The Bone Zone", world.player, world.multiworld)
	if "Boss Rash" in world.final_included_stages_list:
		region_map["Boss Rash"] = Region("Boss Rash", world.player, world.multiworld)
	if "Whiteout" in world.final_included_stages_list:
		region_map["Whiteout"] = Region("Whiteout", world.player, world.multiworld)
	if "The Coop" in world.final_included_stages_list:
		region_map["The Coop"] = Region("The Coop", world.player, world.multiworld)
	if "Space 54" in world.final_included_stages_list:
		region_map["Space 54"] = Region("Space 54", world.player, world.multiworld)
	if "Carlo Cart" in world.final_included_stages_list:
		region_map["Carlo Cart"] = Region("Carlo Cart", world.player, world.multiworld)
	if "Laborratory" in world.final_included_stages_list:
		region_map["Laborratory"] = Region("Laborratory", world.player, world.multiworld)
	if "Westwoods" in world.final_included_stages_list:
		region_map["Westwoods"] = Region("Westwoods", world.player, world.multiworld)
	if "Bat Country" in world.final_included_stages_list:
		region_map["Bat Country"] = Region("Bat Country", world.player, world.multiworld)
	if "Astral Stair" in world.final_included_stages_list:
		region_map["Astral Stair"] = Region("Astral Stair", world.player, world.multiworld)
	if "Mazerella" in world.final_included_stages_list:
		region_map["Mazerella"] = Region("Mazerella", world.player, world.multiworld)
	if "Tiny Bridge" in world.final_included_stages_list:
		region_map["Tiny Bridge"] = Region("Tiny Bridge", world.player, world.multiworld)
	if "Mt.Moonspell" in world.final_included_stages_list:
		region_map["Mt.Moonspell"] = Region("Mt.Moonspell", world.player, world.multiworld)
	if "Lake Foscari" in world.final_included_stages_list:
		region_map["Lake Foscari"] = Region("Lake Foscari", world.player, world.multiworld)
	if "Abyss Foscari" in world.final_included_stages_list:
		region_map["Abyss Foscari"] = Region("Abyss Foscari", world.player, world.multiworld)
	if "Ante Chamber" in world.final_included_stages_list:
		region_map["Ante Chamber"] = Region("Ante Chamber", world.player, world.multiworld)
	if "Room 1665" in world.final_included_stages_list:
		region_map["Room 1665"] = Region("Room 1665", world.player, world.multiworld)
	if "Neo Galuga" in world.final_included_stages_list:
		region_map["Neo Galuga"] = Region("Neo Galuga", world.player, world.multiworld)
	if "Hectic Highway" in world.final_included_stages_list:
		region_map["Hectic Highway"] = Region("Hectic Highway", world.player, world.multiworld)
	if "Ode to Castlevania" in world.final_included_stages_list:
		region_map["Ode to Castlevania"] = Region("Ode to Castlevania", world.player, world.multiworld)
	if "Polus Replica" in world.final_included_stages_list:
		region_map["Polus Replica"] = Region("Polus Replica", world.player, world.multiworld)
	if "Emerald Diorama" in world.final_included_stages_list:
		region_map["Emerald Diorama"] = Region("Emerald Diorama", world.player, world.multiworld)
	connect_region("Menu", "Characters", region_map, None, None, False)
	connect_region("Menu", "Enemies", region_map, None, None, False)
	stages = world.final_included_stages_list
	characters = world.final_included_characters_list
	chest_checks = options.chest_checks_per_stage
	for stage in stages:
		make_location(world, f"{stage} Beaten", stage, region_map, rule_map, False)
		make_event_location(world, f"Event: [{stage} Beaten]", f"{stage} Beaten", "Beat a Stage", None, stage, region_map, rule_map, False)
		if stage != EUDAI:
			for i in range(chest_checks):
				make_location(world, f"Open Chest #{i + 1} on {stage}", stage, region_map, rule_map, False)
		if stage == EUDAI and options.goal_requirement == 1:
			region_map["Menu"].connect(region_map[stage], rule = lambda state, stage_name=stage: has_stage(state, player, options, EUDAI) and has_amount(state, player, options, "Beat a Stage", world.ending_stage_count))
		else:
			region_map["Menu"].connect(region_map[stage], rule = lambda state, stage_name=stage: has_stage(state, player, options, f"{stage_name}"))
	for character in characters:
		make_location(world, f'Beat with {character}', 'Characters', region_map, rule_map, False)
	if options.enemysanity:
		for enemy, raw_find_locs in enemy_map.items():
			if enemy in enemy_arcana_map and not options.enemysanity_arcana_enemies:
				continue
			if enemy == 'Death' and ('Ode to Castlevania' not in stages or 'Richter Belmont' not in characters):
				continue
			if not any(loc in stages for loc in raw_find_locs):
				continue
			make_location(world, f"Kill {enemy}", 'Enemies', region_map, rule_map, False)
	
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