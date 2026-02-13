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
		"The Ranch": Region("The Ranch", world.player, world.multiworld),
		"Upgrades": Region("Upgrades", world.player, world.multiworld),
		"The Lab": Region("The Lab", world.player, world.multiworld),
		"The Overgrowth": Region("The Overgrowth", world.player, world.multiworld),
		"The Grotto": Region("The Grotto", world.player, world.multiworld),
		"Dry Reef": Region("Dry Reef", world.player, world.multiworld),
		"Indigo Quarry": Region("Indigo Quarry", world.player, world.multiworld),
		"Moss Blanket": Region("Moss Blanket", world.player, world.multiworld),
		"Ancient Ruins Transition": Region("Ancient Ruins Transition", world.player, world.multiworld),
		"Ancient Ruins": Region("Ancient Ruins", world.player, world.multiworld),
		"Glass Desert": Region("Glass Desert", world.player, world.multiworld)
	}
	
	region_map["Menu"].connect(region_map["The Ranch"])
	region_map["Menu"].connect(region_map["Upgrades"])
	region_map["The Ranch"].connect(region_map["The Lab"], rule = lambda state: has_region(state, player, "The Lab"))
	region_map["The Ranch"].connect(region_map["The Overgrowth"], rule = lambda state: has_region(state, player, "The Overgrowth"))
	region_map["The Ranch"].connect(region_map["The Grotto"], rule = lambda state: has_region(state, player, "The Grotto"))
	region_map["The Ranch"].connect(region_map["Dry Reef"], rule = lambda state: has_region(state, player, "Dry Reef"))
	region_map["Dry Reef"].connect(region_map["Indigo Quarry"], rule = lambda state: has_region(state, player, "Indigo Quarry"))
	region_map["Dry Reef"].connect(region_map["Moss Blanket"], rule = lambda state: has_region(state, player, "Moss Blanket"))
	region_map["Indigo Quarry"].connect(region_map["Ancient Ruins Transition"], rule = lambda state: has_region(state, player, "Ancient Ruins Transition"))
	region_map["Moss Blanket"].connect(region_map["Ancient Ruins Transition"], rule = lambda state: has_region(state, player, "Ancient Ruins Transition"))
	region_map["Ancient Ruins Transition"].connect(region_map["Ancient Ruins"], rule = lambda state: can_access_to_ruins_from_trans(state, player))
	region_map["Ancient Ruins"].connect(region_map["Glass Desert"], rule = lambda state: has_region(state, player, "Glass Desert"))
	make_location(world, "Buy Personal Upgrade (Heart Module lv.1)", region_map["Upgrades"], rule_map)
	make_location(world, "Buy Personal Upgrade (Heart Module lv.2)", region_map["Upgrades"], rule_map)
	make_location(world, "Buy Personal Upgrade (Heart Module lv.3)", region_map["Upgrades"], rule_map)
	if world.options.include_7z:
		make_location(world, "Buy Personal Upgrade (Heart Module lv.4)", region_map["Upgrades"], rule_map)
	
	make_location(world, "Buy Personal Upgrade (Tank Booster lv.1)", region_map["Upgrades"], rule_map)
	make_location(world, "Buy Personal Upgrade (Tank Booster lv.2)", region_map["Upgrades"], rule_map)
	make_location(world, "Buy Personal Upgrade (Tank Booster lv.3)", region_map["Upgrades"], rule_map)
	if world.options.include_7z:
		make_location(world, "Buy Personal Upgrade (Tank Booster lv.4)", region_map["Upgrades"], rule_map)
	
	make_location(world, "Buy Personal Upgrade (Dash Boots lv. 1)", region_map["Upgrades"], rule_map)
	if world.options.include_7z:
		make_location(world, "Buy Personal Upgrade (Dash Boots lv.2)", region_map["Upgrades"], rule_map)
	
	make_location(world, "Buy Personal Upgrade (Power Core lv.1)", region_map["Upgrades"], rule_map)
	make_location(world, "Buy Personal Upgrade (Power Core lv.2)", region_map["Upgrades"], rule_map)
	make_location(world, "Buy Personal Upgrade (Power Core lv.3)", region_map["Upgrades"], rule_map)
	if "Buy Personal Upgrade (Treasure Cracker lv.1)" > f"Buy Personal Upgrade (Treasure Cracker lv.{world.options.treasure_cracker_checks})":
		make_location(world, "Buy Personal Upgrade (Treasure Cracker lv.1)", region_map["Upgrades"], rule_map)
	
	if "Buy Personal Upgrade (Treasure Cracker lv.2)" > f"Buy Personal Upgrade (Treasure Cracker lv.{world.options.treasure_cracker_checks})":
		make_location(world, "Buy Personal Upgrade (Treasure Cracker lv.2)", region_map["Upgrades"], rule_map)
	
	if "Buy Personal Upgrade (Treasure Cracker lv.3)" > f"Buy Personal Upgrade (Treasure Cracker lv.{world.options.treasure_cracker_checks})":
		make_location(world, "Buy Personal Upgrade (Treasure Cracker lv.3)", region_map["Upgrades"], rule_map)
	
	make_location(world, "Buy Personal Upgrade (Jetpack)", region_map["Upgrades"], rule_map)
	make_location(world, "Buy Personal Upgrade (Air Drive)", region_map["Upgrades"], rule_map)
	make_location(world, "Buy Personal Upgrade (Pulse Wave)", region_map["Upgrades"], rule_map)
	make_location(world, "Buy Personal Upgrade (Liquid Slot)", region_map["Upgrades"], rule_map)
	for location in interactables:
		make_location(world, location[0], region_map[location[1]], rule_map)
	if world.options.goal_type == 0:
		make_event_location(world, "Read: Hobson's Note - Outside Ranch", "Hobson's Note - Outside Ranch", "Note Read", None, region_map["Dry Reef"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Cliff Near Tabby Slimes", "Hobson's Note - Cliff Near Tabby Slimes", "Note Read", None, region_map["Dry Reef"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Cliff Near Ring Island", "Hobson's Note - Cliff Near Ring Island", "Note Read", None, region_map["Dry Reef"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Ancient Ruins Entrance", "Hobson's Note - Ancient Ruins Entrance", "Note Read", None, region_map["Ancient Ruins"], rule_map)
		make_event_location(world, "Read: Hobson's Note - The Grotto", "Hobson's Note - The Grotto", "Note Read", None, region_map["The Grotto"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Cliff Across Indigo Quarry", "Hobson's Note - Cliff Across Indigo Quarry", "Note Read", None, region_map["Dry Reef"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Cave to Indigo Quarry", "Hobson's Note - Cave to Indigo Quarry", "Note Read", None, region_map["Dry Reef"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Moss Blanket Main Area", "Hobson's Note - Moss Blanket Main Area", "Note Read", None, region_map["Moss Blanket"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Moss Blanket Ledge", "Hobson's Note - Moss Blanket Ledge", "Note Read", None, region_map["Moss Blanket"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Moss Blanket Mushroom Island", "Hobson's Note - Moss Blanket Mushroom Island", "Note Read", None, region_map["Moss Blanket"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Mushroom Feral Slime Area", "Hobson's Note - Mushroom Feral Slime Area", "Note Read", None, region_map["Moss Blanket"], rule_map)
		make_event_location(world, "Read: Hobson's Note - The Lab", "Hobson's Note - The Lab", "Note Read", None, region_map["The Lab"], rule_map)
		make_event_location(world, "Read: Hobson's Note - The Overgrowth", "Hobson's Note - The Overgrowth", "Note Read", None, region_map["The Overgrowth"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Crystal Slime Cave", "Hobson's Note - Crystal Slime Cave", "Note Read", None, region_map["Indigo Quarry"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Indigo Quarry Pond", "Hobson's Note - Indigo Quarry Pond", "Note Read", None, region_map["Indigo Quarry"], rule_map)
		make_event_location(world, "Read: Hobson's Note - The Docks", "Hobson's Note - The Docks", "Note Read", None, region_map["The Overgrowth"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Indigo Quarry Entry", "Hobson's Note - Indigo Quarry Entry", "Note Read", None, region_map["Indigo Quarry"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Ash Isle", "Hobson's Note - Ash Isle", "Note Read", None, region_map["Indigo Quarry"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Ring Island", "Hobson's Note - Ring Island", "Note Read", None, region_map["Dry Reef"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Ancient Bottom Floor Mushroom Cave", "Hobson's Note - Ancient Bottom Floor Mushroom Cave", "Note Read", None, region_map["Ancient Ruins"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Ancient Ruins Back Half Oasis", "Hobson's Note - Ancient Ruins Back Half Oasis", "Note Read", None, region_map["Ancient Ruins"], rule_map)
		make_event_location(world, "Read: Hobson's Note - End of Ancient Ruins", "Hobson's Note - End of Ancient Ruins", "Note Read", None, region_map["Ancient Ruins"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Entrance to Glass Desert", "Hobson's Note - Entrance to Glass Desert", "Note Read", None, region_map["Glass Desert"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Glass Desert Rock Slime Fountain", "Hobson's Note - Glass Desert Rock Slime Fountain", "Note Read", None, region_map["Glass Desert"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Glass Desert Northern Courtyard", "Hobson's Note - Glass Desert Northern Courtyard", "Note Read", None, region_map["Glass Desert"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Glass Desert Northern Ruins", "Hobson's Note - Glass Desert Northern Ruins", "Note Read", None, region_map["Glass Desert"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Glass Desert Slime Statue", "Hobson's Note - Glass Desert Slime Statue", "Note Read", None, region_map["Glass Desert"], rule_map)
		make_event_location(world, "Read: Hobson's Note - Doors Like These", "Hobson's Note - Doors Like These", "Note Read", None, region_map["Glass Desert"], rule_map)
		
	
	if world.options.enable_stylish_dlc_treasure_pods:
		for location in dlc_interactables:
			make_location(world, location[0], region_map[location[1]], rule_map)
	
	if world.options.include_7z:
		for location in corporate_locations:
			make_location(world, location[0], region_map[location[1]], rule_map)
	
	if world.options.include_7z and world.options.goal_type == 1:
		for location in corporate_locations:
			make_event_location(world, f"Bought: {location[0]}", location[0], "7Zee Bought", None, region_map[location[1]], rule_map)
	
	
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