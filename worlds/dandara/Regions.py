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
		"Crib of Creation": Region("Crib of Creation", world.player, world.multiworld),
		"Dream Lands": Region("Dream Lands", world.player, world.multiworld),
		"Ephemeral Station": Region("Ephemeral Station", world.player, world.multiworld),
		"Exile of Contemplations": Region("Exile of Contemplations", world.player, world.multiworld),
		"Golden Fortress": Region("Golden Fortress", world.player, world.multiworld),
		"Hidden Bridge": Region("Hidden Bridge", world.player, world.multiworld),
		"Hidden Realms": Region("Hidden Realms", world.player, world.multiworld),
		"Intention Capital": Region("Intention Capital", world.player, world.multiworld),
		"Masters' Auditorium": Region("Masters' Auditorium", world.player, world.multiworld),
		"Primal Woods": Region("Primal Woods", world.player, world.multiworld),
		"Remembrance Desert": Region("Remembrance Desert", world.player, world.multiworld),
		"StartArea": Region("StartArea", world.player, world.multiworld),
		"The Colossal Bridge": Region("The Colossal Bridge", world.player, world.multiworld),
		"The Enduring Fortress": Region("The Enduring Fortress", world.player, world.multiworld),
		"The Masquerade Ball": Region("The Masquerade Ball", world.player, world.multiworld),
		"The Pioneer Facility": Region("The Pioneer Facility", world.player, world.multiworld),
		"The Privileged Keep": Region("The Privileged Keep", world.player, world.multiworld),
		"The Salt Is Hesitant": Region("The Salt Is Hesitant", world.player, world.multiworld),
		"Village of Artists": Region("Village of Artists", world.player, world.multiworld),
		"UNKNOWN_AREANAME": Region("UNKNOWN_AREANAME", world.player, world.multiworld),
		"Heart Shop": Region("Heart Shop", world.player, world.multiworld),
		"Mana Shop": Region("Mana Shop", world.player, world.multiworld),
		"Health Flask Shop": Region("Health Flask Shop", world.player, world.multiworld),
		"Mana Flask Shop": Region("Mana Flask Shop", world.player, world.multiworld)
	}
	
	connect_region("Menu", "Crib of Creation", region_map, None, lambda state: True, False)
	connect_region("Crib of Creation", "Village of Artists", region_map, None, lambda state: True, False)
	connect_region("Crib of Creation", "Primal Woods", region_map, None, lambda state: has(state, player, options, "Stone of Creation") or has(state, player, options, "Displaced Presence"), False)
	connect_region("Village of Artists", "Crib of Creation", region_map, None, lambda state: True, False)
	connect_region("Village of Artists", "The Colossal Bridge", region_map, None, lambda state: has(state, player, options, "Stone of Creation") or has(state, player, options, "Displaced Presence"), False)
	connect_region("Village of Artists", "Hidden Realms", region_map, None, lambda state: (has_blast(state, player, options) and has(state, player, options, "FearKey") and has(state, player, options, "Paint Platform")) or (has_blast(state, player, options) and has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation")) or (has_blast(state, player, options) and has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence")), False)
	connect_region("Dream Lands", "The Colossal Bridge", region_map, None, lambda state: has(state, player, options, "Stone of Intention"), False)
	connect_region("Primal Woods", "Crib of Creation", region_map, None, lambda state: has(state, player, options, "Stone of Creation") or has(state, player, options, "Displaced Presence"), False)
	connect_region("Primal Woods", "The Colossal Bridge", region_map, None, lambda state: True, False)
	connect_region("Primal Woods", "Intention Capital", region_map, None, lambda state: (has(state, player, options, "Stone of Creation") and has(state, player, options, "Rock of Remembrance")) or (has(state, player, options, "Displaced Presence") and has(state, player, options, "Rock of Remembrance")), False)
	connect_region("Primal Woods", "Golden Fortress", region_map, None, lambda state: (has(state, player, options, "Stone of Creation") and has(state, player, options, "Rock of Remembrance") and has(state, player, options, "Pearl of Dreams")) or (has(state, player, options, "Displaced Presence") and has(state, player, options, "Rock of Remembrance") and has(state, player, options, "Pearl of Dreams")), False)
	connect_region("Primal Woods", "Hidden Realms", region_map, None, lambda state: (has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation") and has(state, player, options, "Rock of Remembrance")) or (has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence") and has(state, player, options, "Memories Shaft")), False)
	connect_region("The Colossal Bridge", "Village of Artists", region_map, None, lambda state: has(state, player, options, "Stone of Creation") or has(state, player, options, "Displaced Presence"), False)
	connect_region("The Colossal Bridge", "Dream Lands", region_map, None, lambda state: has(state, player, options, "Stone of Intention"), False)
	connect_region("The Colossal Bridge", "Remembrance Desert", region_map, None, lambda state: has(state, player, options, "Stone of Creation") or has(state, player, options, "Displaced Presence"), False)
	connect_region("The Colossal Bridge", "Primal Woods", region_map, None, lambda state: has(state, player, options, "Stone of Creation") or has(state, player, options, "Displaced Presence"), False)
	connect_region("The Colossal Bridge", "Intention Capital", region_map, None, lambda state: has(state, player, options, "Stone of Creation") or has(state, player, options, "Displaced Presence"), False)
	connect_region("Remembrance Desert", "The Colossal Bridge", region_map, None, lambda state: True, False)
	connect_region("Remembrance Desert", "Hidden Realms", region_map, None, lambda state: has(state, player, options, "FearKey"), False)
	connect_region("Intention Capital", "The Colossal Bridge", region_map, None, lambda state: True, False)
	connect_region("Intention Capital", "Primal Woods", region_map, None, lambda state: has(state, player, options, "Displaced Presence") or has(state, player, options, "Stone of Intention"), False)
	connect_region("Intention Capital", "Golden Fortress", region_map, None, lambda state: has(state, player, options, "Stone of Intention") and has(state, player, options, "Pearl of Dreams") and has(state, player, options, "Wall Break"), False)
	connect_region("Intention Capital", "Hidden Realms", region_map, None, lambda state: (has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation") and has(state, player, options, "Stone of Intention")) or (has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence") and has(state, player, options, "Stone of Intention")), False)
	connect_region("Intention Capital", "Ephemeral Station", region_map, None, lambda state: (has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation")) or (has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence")) or (has_blast(state, player, options) and has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation") and has(state, player, options, "Stone of Intention")) or (has_blast(state, player, options) and has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence") and has(state, player, options, "Stone of Intention")), False)
	connect_region("Golden Fortress", "Intention Capital", region_map, None, lambda state: has(state, player, options, "Wall Break"), False)
	connect_region("Golden Fortress", "Primal Woods", region_map, None, lambda state: has(state, player, options, "Pearl of Dreams") and has(state, player, options, "Stone of Intention"), False)
	connect_region("Hidden Realms", "Village of Artists", region_map, None, lambda state: (has_blast(state, player, options) and has(state, player, options, "FearKey") and has(state, player, options, "Paint Platform")) or (has_blast(state, player, options) and has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation")) or (has_blast(state, player, options) and has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence")), False)
	connect_region("Hidden Realms", "Remembrance Desert", region_map, None, lambda state: (has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation")) or (has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence")), False)
	connect_region("Hidden Realms", "Primal Woods", region_map, None, lambda state: (has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation") and has(state, player, options, "Rock of Remembrance")) or (has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence") and has(state, player, options, "Memories Shaft")), False)
	connect_region("Hidden Realms", "Intention Capital", region_map, None, lambda state: (has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation") and has(state, player, options, "Stone of Intention")) or (has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence") and has(state, player, options, "Stone of Intention")), False)
	connect_region("Hidden Realms", "Exile of Contemplations", region_map, None, lambda state: has(state, player, options, "Shell Mirror") or (has(state, player, options, "Shell Mirror") and has(state, player, options, "Displaced Presence")) or (has(state, player, options, "Shell Mirror") and has(state, player, options, "Displaced Presence") and has(state, player, options, "Skin Knitter")), False)
	connect_region("Hidden Realms", "Ephemeral Station", region_map, None, lambda state: has(state, player, options, "Displaced Presence") or (has(state, player, options, "Stone of Creation") and has(state, player, options, "Stone of Intention")) or (has(state, player, options, "Stone of Intention") and has(state, player, options, "Displaced Presence")) or (has_blast(state, player, options) and has(state, player, options, "Stone of Intention") and has(state, player, options, "Displaced Presence")) or (has_blast(state, player, options) and has(state, player, options, "Stone of Creation") and has(state, player, options, "Stone of Intention")), False)
	connect_region("Hidden Realms", "Masters' Auditorium", region_map, None, lambda state: has(state, player, options, "Stone of Creation") or has(state, player, options, "Displaced Presence"), False)
	connect_region("Hidden Realms", "Hidden Bridge", region_map, None, lambda state: has(state, player, options, "Skin Knitter") or (has(state, player, options, "Displaced Presence") and has(state, player, options, "Skin Knitter")) or (has_blast(state, player, options) and has(state, player, options, "Displaced Presence")) or (has_blast(state, player, options) and has(state, player, options, "Skin Knitter") and has(state, player, options, "Stone of Creation")) or (has_blast(state, player, options) and has(state, player, options, "Skin Knitter") and has(state, player, options, "Displaced Presence")), False)
	connect_region("Hidden Realms", "The Enduring Fortress", region_map, None, lambda state: (has_blast(state, player, options) and has(state, player, options, "Stone of Creation") and has(state, player, options, "DLC StoryEvent 1")) or (has_blast(state, player, options) and has(state, player, options, "DLC StoryEvent 1") and has(state, player, options, "Displaced Presence")) or (has(state, player, options, "DLC StoryEvent 1") and has(state, player, options, "Displaced Presence")) or (has(state, player, options, "DLC StoryEvent 1") and has(state, player, options, "Displaced Presence") and has(state, player, options, "Skin Knitter")), False)
	connect_region("Hidden Realms", "The Pioneer Facility", region_map, None, lambda state: (has_blast(state, player, options) and has(state, player, options, "Stone of Creation") and has(state, player, options, "DLC StoryEvent 1")) or (has_blast(state, player, options) and has(state, player, options, "DLC StoryEvent 1") and has(state, player, options, "Displaced Presence")) or (has(state, player, options, "DLC StoryEvent 1") and has(state, player, options, "Displaced Presence")) or (has(state, player, options, "DLC StoryEvent 1") and has(state, player, options, "Displaced Presence") and has(state, player, options, "Skin Knitter")), False)
	connect_region("Hidden Realms", "The Privileged Keep", region_map, None, lambda state: (has_blast(state, player, options) and has(state, player, options, "Stone of Creation") and has(state, player, options, "DLC StoryEvent 1")) or (has_blast(state, player, options) and has(state, player, options, "DLC StoryEvent 1") and has(state, player, options, "Displaced Presence")) or (has(state, player, options, "DLC StoryEvent 1") and has(state, player, options, "Displaced Presence")) or (has(state, player, options, "DLC StoryEvent 1") and has(state, player, options, "Displaced Presence") and has(state, player, options, "Skin Knitter")), False)
	connect_region("Hidden Realms", "The Masquerade Ball", region_map, None, lambda state: (has_blast(state, player, options) and has(state, player, options, "Skin Knitter") and has(state, player, options, "Displaced Presence")) or (has(state, player, options, "Skin Knitter") and has(state, player, options, "Displaced Presence")), False)
	connect_region("Ephemeral Station", "Intention Capital", region_map, None, lambda state: (has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation")) or (has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence")) or (has_blast(state, player, options) and has(state, player, options, "FearKey") and has(state, player, options, "Stone of Creation") and has(state, player, options, "Stone of Intention")) or (has_blast(state, player, options) and has(state, player, options, "FearKey") and has(state, player, options, "Displaced Presence") and has(state, player, options, "Stone of Intention")), False)
	connect_region("Ephemeral Station", "Hidden Realms", region_map, None, lambda state: has(state, player, options, "Displaced Presence") and has(state, player, options, "Stone of Creation") and has(state, player, options, "Stone of Intention"), False)
	connect_region("Hidden Bridge", "Hidden Realms", region_map, None, lambda state: has(state, player, options, "Displaced Presence"), False)
	connect_region("The Enduring Fortress", "Hidden Realms", region_map, None, lambda state: True, False)
	connect_region("The Privileged Keep", "Hidden Realms", region_map, None, lambda state: True, False)
	connect_region("The Pioneer Facility", "Hidden Realms", region_map, None, lambda state: True, False)
	connect_region("Masters' Auditorium", "Hidden Realms", region_map, None, lambda state: True, False)
	connect_region("The Masquerade Ball", "Hidden Realms", region_map, None, lambda state: has(state, player, options, "Displaced Presence"), False)
	connect_region("Exile of Contemplations", "Hidden Realms", region_map, None, lambda state: True, False)
	connect_region("Golden Fortress", "The Salt Is Hesitant", region_map, None, lambda state: has(state, player, options, "FinalBoss_Kill"), False)
	connect_region("The Salt Is Hesitant", "The Colossal Bridge", region_map, None, lambda state: has(state, player, options, "Stone of Intention"), False)
	connect_region("Menu", "Heart Shop", region_map, None, lambda state: has(state, player, options, "Heart Enhancer Permit"), False)
	connect_region("Menu", "Mana Shop", region_map, None, lambda state: has(state, player, options, "Freedom Enhancer Permit"), False)
	connect_region("Menu", "Health Flask Shop", region_map, None, lambda state: has(state, player, options, "Essence Enhancer Permit"), False)
	connect_region("Menu", "Mana Flask Shop", region_map, None, lambda state: has(state, player, options, "Infusion Enhancer Permit"), False)
	for location in overworld_chest:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False, True)
	for location in fearworld_chest:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False, True)
	for location in shop_levels:
		if location[1] in region_map:
			make_location(world, location[0], location[1], region_map, rule_map, False, True)
	make_event_location(world, "Event: Kill Eldar", "Event: Kill Eldar", "FinalBoss_Kill", None, "Golden Fortress", region_map, rule_map, False)
	make_event_location(world, "Event: Ture Ending", "Event: Ture Ending", "DLCF_FearEnded", None, "The Salt Is Hesitant", region_map, rule_map, False)
	
	
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