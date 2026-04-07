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
		"The Ranch": Region("The Ranch", world.player, world.multiworld),
		"The Grotto": Region("The Grotto", world.player, world.multiworld),
		"The Overgrowth": Region("The Overgrowth", world.player, world.multiworld),
		"The Lab": Region("The Lab", world.player, world.multiworld),
		"The Docks": Region("The Docks", world.player, world.multiworld),
		"Ogden's Retreat": Region("Ogden's Retreat", world.player, world.multiworld),
		"Mochi's Manor": Region("Mochi's Manor", world.player, world.multiworld),
		"Viktor's Workshop": Region("Viktor's Workshop", world.player, world.multiworld),
		"Dry Reef - Main": Region("Dry Reef - Main", world.player, world.multiworld),
		"Dry Reef - Beach": Region("Dry Reef - Beach", world.player, world.multiworld),
		"Dry Reef - Ring Island": Region("Dry Reef - Ring Island", world.player, world.multiworld),
		"The Slime Sea - Between Grotto and Dry Reef Island 2": Region("The Slime Sea - Between Grotto and Dry Reef Island 2", world.player, world.multiworld),
		"Dry Reef - Offshoot": Region("Dry Reef - Offshoot", world.player, world.multiworld),
		"The Slime Sea - Between Grotto and Dry Reef Island 1": Region("The Slime Sea - Between Grotto and Dry Reef Island 1", world.player, world.multiworld),
		"The Slime Sea - Mustache Shrine": Region("The Slime Sea - Mustache Shrine", world.player, world.multiworld),
		"Moss Blanket - Hunter's Domain": Region("Moss Blanket - Hunter's Domain", world.player, world.multiworld),
		"The Slime Sea - Off Moss Blanket": Region("The Slime Sea - Off Moss Blanket", world.player, world.multiworld),
		"Indigo Quarry - Before First Bridge": Region("Indigo Quarry - Before First Bridge", world.player, world.multiworld),
		"Indigo Quarry - After The Bridge": Region("Indigo Quarry - After The Bridge", world.player, world.multiworld),
		"Indigo Quarry - Ancient Ruins Transition Overlap": Region("Indigo Quarry - Ancient Ruins Transition Overlap", world.player, world.multiworld),
		"Ancient Ruins Transition": Region("Ancient Ruins Transition", world.player, world.multiworld),
		"Indigo Quarry - Ash Isles": Region("Indigo Quarry - Ash Isles", world.player, world.multiworld),
		"Moss Blanket - Main": Region("Moss Blanket - Main", world.player, world.multiworld),
		"Moss Blanket - Mushroom Island": Region("Moss Blanket - Mushroom Island", world.player, world.multiworld),
		"Ancient Ruins - Main": Region("Ancient Ruins - Main", world.player, world.multiworld),
		"Ancient Ruins - Teleporter Room": Region("Ancient Ruins - Teleporter Room", world.player, world.multiworld),
		"Glass Desert - First Half": Region("Glass Desert - First Half", world.player, world.multiworld),
		"Glass Desert - Second Half": Region("Glass Desert - Second Half", world.player, world.multiworld),
		"The Wilds": Region("The Wilds", world.player, world.multiworld),
		"Nimble Valley": Region("Nimble Valley", world.player, world.multiworld),
		"The Slimeulation": Region("The Slimeulation", world.player, world.multiworld)
	}
	
	region_map["Menu"].connect(region_map["Upgrades"], rule = lambda state: True)
	region_map["Menu"].connect(region_map["The Ranch"], rule = lambda state: True)
	region_map["The Ranch"].connect(region_map["The Grotto"], rule = lambda state: ( has_region(state, player, options, "The Grotto") ))
	region_map["The Ranch"].connect(region_map["The Overgrowth"], rule = lambda state: ( has_region(state, player, options, "The Overgrowth") ))
	region_map["The Ranch"].connect(region_map["The Lab"], rule = lambda state: ( has_region(state, player, options, "The Lab") ))
	region_map["The Overgrowth"].connect(region_map["The Docks"], rule = lambda state: ( has_region(state, player, options, "The Docks") ))
	region_map["The Ranch"].connect(region_map["The Docks"], rule = lambda state: ( has_region(state, player, options, "The Docks") ))
	region_map["The Overgrowth"].connect(region_map["Ogden's Retreat"], rule = lambda state: ( has_region(state, player, options, "Ogden's Retreat") ))
	region_map["The Grotto"].connect(region_map["Mochi's Manor"], rule = lambda state: ( has_region(state, player, options, "Mochi's Manor") ))
	region_map["The Lab"].connect(region_map["Viktor's Workshop"], rule = lambda state: ( has_region(state, player, options, "Viktor's Workshop") ))
	region_map["The Ranch"].connect(region_map["Dry Reef - Main"], rule = lambda state: ( has_region(state, player, options, "Dry Reef") ))
	region_map["The Overgrowth"].connect(region_map["Dry Reef - Beach"], rule = lambda state: ( has_region(state, player, options, "Dry Reef") ))
	region_map["Dry Reef - Main"].connect(region_map["Dry Reef - Beach"], rule = lambda state: ( has_region(state, player, options, "Dry Reef") ))
	region_map["Dry Reef - Beach"].connect(region_map["Dry Reef - Ring Island"], rule = lambda state: ( has_region(state, player, options, "Dry Reef") ))
	region_map["The Slime Sea - Between Grotto and Dry Reef Island 2"].connect(region_map["Dry Reef - Offshoot"], rule = lambda state: ( has_region(state, player, options, "Dry Reef") ))
	region_map["The Grotto"].connect(region_map["The Slime Sea - Between Grotto and Dry Reef Island 1"], rule = lambda state: ( get_yaml_option(state, player, options, 'precise_movement') and get_yaml_option(state, player, options, 'obscure_locations') ))
	region_map["The Slime Sea - Between Grotto and Dry Reef Island 2"].connect(region_map["The Slime Sea - Between Grotto and Dry Reef Island 1"], rule = lambda state: True)
	region_map["The Slime Sea - Between Grotto and Dry Reef Island 1"].connect(region_map["The Slime Sea - Between Grotto and Dry Reef Island 2"], rule = lambda state: True)
	region_map["Dry Reef - Offshoot"].connect(region_map["The Slime Sea - Between Grotto and Dry Reef Island 2"], rule = lambda state: True)
	region_map["Moss Blanket - Hunter's Domain"].connect(region_map["The Slime Sea - Off Moss Blanket"], rule = lambda state: ( has_region(state, player, options, "Moss Blanket") ) or ( has_region(state, player, options, "Moss Blanket") and get_yaml_option(state, player, options, 'obscure_locations') ))
	region_map["Dry Reef - Main"].connect(region_map["Indigo Quarry - Before First Bridge"], rule = lambda state: ( has_region(state, player, options, "Indigo Quarry") ))
	region_map["Indigo Quarry - After The Bridge"].connect(region_map["Indigo Quarry - Before First Bridge"], rule = lambda state: ( has_region(state, player, options, "Indigo Quarry") ))
	region_map["Indigo Quarry - Before First Bridge"].connect(region_map["Indigo Quarry - After The Bridge"], rule = lambda state: ( has_region(state, player, options, "Indigo Quarry") ))
	region_map["Indigo Quarry - Ancient Ruins Transition Overlap"].connect(region_map["Indigo Quarry - After The Bridge"], rule = lambda state: ( has_region(state, player, options, "Indigo Quarry") ))
	region_map["Indigo Quarry - After The Bridge"].connect(region_map["Indigo Quarry - Ancient Ruins Transition Overlap"], rule = lambda state: ( has_region(state, player, options, "Indigo Quarry") and has_region(state, player, options, "Ancient Ruins Transition") ))
	region_map["Ancient Ruins Transition"].connect(region_map["Indigo Quarry - Ancient Ruins Transition Overlap"], rule = lambda state: ( has_region(state, player, options, "Indigo Quarry") and has_region(state, player, options, "Ancient Ruins Transition") ))
	region_map["Indigo Quarry - After The Bridge"].connect(region_map["Indigo Quarry - Ash Isles"], rule = lambda state: ( has_region(state, player, options, "Indigo Quarry") ))
	region_map["Dry Reef - Main"].connect(region_map["Moss Blanket - Main"], rule = lambda state: ( has_region(state, player, options, "Moss Blanket") ) or ( has_region(state, player, options, "Moss Blanket") and get_yaml_option(state, player, options, 'easy_skips') ))
	region_map["Moss Blanket - Main"].connect(region_map["Moss Blanket - Mushroom Island"], rule = lambda state: ( has_region(state, player, options, "Moss Blanket") ) or ( has_region(state, player, options, "Moss Blanket") and get_yaml_option(state, player, options, 'precise_movement') and get_yaml_option(state, player, options, 'obscure_locations') ))
	region_map["Moss Blanket - Main"].connect(region_map["Moss Blanket - Hunter's Domain"], rule = lambda state: ( has_region(state, player, options, "Moss Blanket") and get_yaml_option(state, player, options, 'precise_movement') and get_yaml_option(state, player, options, 'dangerous_skips') ) or ( has_region(state, player, options, "Moss Blanket") ))
	region_map["Moss Blanket - Main"].connect(region_map["Ancient Ruins Transition"], rule = lambda state: ( has_region(state, player, options, "Ancient Ruins Transition") ))
	region_map["Indigo Quarry - Ancient Ruins Transition Overlap"].connect(region_map["Ancient Ruins Transition"], rule = lambda state: ( has_region(state, player, options, "Ancient Ruins Transition") ))
	region_map["Ancient Ruins Transition"].connect(region_map["Ancient Ruins - Main"], rule = lambda state: ( has_region(state, player, options, "Ancient Ruins") and has(state, player, options, 'Tabby Plort') and has(state, player, options, 'Rock Plort') and has(state, player, options, 'Phosphor Plort') and has(state, player, options, 'Boom Plort') and has(state, player, options, 'Rad Plort') and has(state, player, options, 'Honey Plort') ))
	region_map["Ancient Ruins - Main"].connect(region_map["Ancient Ruins - Teleporter Room"], rule = lambda state: ( has_region(state, player, options, "Ancient Ruins") ))
	region_map["Ancient Ruins - Teleporter Room"].connect(region_map["Glass Desert - First Half"], rule = lambda state: ( has_region(state, player, options, "Glass Desert") and has(state, player, options, 'Quantum Plort') ))
	region_map["Glass Desert - First Half"].connect(region_map["Glass Desert - Second Half"], rule = lambda state: ( has_region(state, player, options, "Glass Desert") ) or ( has_region(state, player, options, "Glass Desert") and get_yaml_option(state, player, options, 'precise_movement') and get_yaml_option(state, player, options, 'obscure_locations') ) or ( has_region(state, player, options, "Glass Desert") and get_yaml_option(state, player, options, 'obscure_locations') ))
	region_map["Ogden's Retreat"].connect(region_map["The Wilds"], rule = lambda state: ( has_region(state, player, options, "The Wilds") ))
	region_map["Mochi's Manor"].connect(region_map["Nimble Valley"], rule = lambda state: ( has_region(state, player, options, "Nimble Valley") ))
	region_map["Viktor's Workshop"].connect(region_map["The Slimeulation"], rule = lambda state: ( has_region(state, player, options, "The Slimeulations") ))
	if ( options.precise_movement ):
		region_map["Dry Reef - Main"].connect(region_map["Dry Reef - Offshoot"], rule = lambda state: ( has_region(state, player, options, "Dry Reef") and get_yaml_option(state, player, options, 'precise_movement') ))
	
	if ( options.obscure_locations ):
		region_map["Dry Reef - Main"].connect(region_map["The Slime Sea - Mustache Shrine"], rule = lambda state: ( get_yaml_option(state, player, options, 'obscure_locations') ))
	
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
	
	make_location(world, "Buy Personal Upgrade (Dash Boots lv.1)", region_map["Upgrades"], rule_map)
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
		make_event_location(world, "Read: The Overgrowth - Artificial Moss Blanket", "The Overgrowth - Artificial Moss Blanket", "Note Read", None, region_map["The Overgrowth"], rule_map)
		make_event_location(world, "Read: The Docks - Our Greater Purpose", "The Docks - Our Greater Purpose", "Note Read", None, region_map["The Docks"], rule_map)
		make_event_location(world, "Read: Dry Reef -  Hobson's Greetings", "Dry Reef -  Hobson's Greetings", "Note Read", None, region_map["Dry Reef - Main"], rule_map)
		make_event_location(world, "Read: Dry Reef - Indigo Quarry Entrance", "Dry Reef - Indigo Quarry Entrance", "Note Read", None, region_map["Dry Reef - Main"], rule_map)
		make_event_location(world, "Read: Dry Reef - Great Big Tree", "Dry Reef - Great Big Tree", "Note Read", None, region_map["Dry Reef - Main"], rule_map)
		make_event_location(world, "Read: Dry Reef - Ruminating on the Beach", "Dry Reef - Ruminating on the Beach", "Note Read", None, region_map["Dry Reef - Beach"], rule_map)
		make_event_location(world, "Read: Indigo Quarry - I Liked Her Laugh", "Indigo Quarry - I Liked Her Laugh", "Note Read", None, region_map["Indigo Quarry - Before First Bridge"], rule_map)
		make_event_location(world, "Read: Indigo Quarry - Crystal Wind Chime", "Indigo Quarry - Crystal Wind Chime", "Note Read", None, region_map["Indigo Quarry - Before First Bridge"], rule_map)
		make_event_location(world, "Read: Dry Reef - A Darn Good Boot", "Dry Reef - A Darn Good Boot", "Note Read", None, region_map["Dry Reef - Main"], rule_map)
		make_event_location(world, "Read: Indigo Quarry - Peeping Puddle Slimes", "Indigo Quarry - Peeping Puddle Slimes", "Note Read", None, region_map["Indigo Quarry - Before First Bridge"], rule_map)
		make_event_location(world, "Read: Ash Isles - Looking to the Stars", "Ash Isles - Looking to the Stars", "Note Read", None, region_map["Indigo Quarry - Ash Isles"], rule_map)
		make_event_location(world, "Read: Ring Island - Naturally Curious", "Ring Island - Naturally Curious", "Note Read", None, region_map["Dry Reef - Ring Island"], rule_map)
		make_event_location(world, "Read: Moss Blanket - New Ancient Jungle", "Moss Blanket - New Ancient Jungle", "Note Read", None, region_map["Moss Blanket - Main"], rule_map)
		make_event_location(world, "Read: Moss Blanket - MOSS BLANKET STUCK", "Moss Blanket - MOSS BLANKET STUCK", "Note Read", None, region_map["Moss Blanket - Main"], rule_map)
		make_event_location(world, "Read: The Grotto - The Limitless Black of Space", "The Grotto - The Limitless Black of Space", "Note Read", None, region_map["The Grotto"], rule_map)
		make_event_location(world, "Read: Moss Blanket - Can't Recommend Love Enough", "Moss Blanket - Can't Recommend Love Enough", "Note Read", None, region_map["Moss Blanket - Mushroom Island"], rule_map)
		make_event_location(world, "Read: Moss Blanket - Peepers Peeled!", "Moss Blanket - Peepers Peeled!", "Note Read", None, region_map["Moss Blanket - Hunter's Domain"], rule_map)
		make_event_location(world, "Read: Ancient Ruins - The Purpose of the Ruins", "Ancient Ruins - The Purpose of the Ruins", "Note Read", None, region_map["Ancient Ruins - Main"], rule_map)
		make_event_location(world, "Read: Ancient Ruins - You Gotta Choose a Path", "Ancient Ruins - You Gotta Choose a Path", "Note Read", None, region_map["Ancient Ruins - Main"], rule_map)
		make_event_location(world, "Read: Ancient Ruins - Ice-Cold Lemonade", "Ancient Ruins - Ice-Cold Lemonade", "Note Read", None, region_map["Ancient Ruins - Main"], rule_map)
		make_event_location(world, "Read: Ancient Ruins - Truly Untamed Country", "Ancient Ruins - Truly Untamed Country", "Note Read", None, region_map["Ancient Ruins - Teleporter Room"], rule_map)
		make_event_location(world, "Read: The Lab - The Wonders of Plort Technology", "The Lab - The Wonders of Plort Technology", "Note Read", None, region_map["The Lab"], rule_map)
		make_event_location(world, "Read: Glass Desert - You'll Risk Burning Your Tuchus!", "Glass Desert - You'll Risk Burning Your Tuchus!", "Note Read", None, region_map["Glass Desert - First Half"], rule_map)
		make_event_location(world, "Read: Glass Desert - Two Overlapping Times", "Glass Desert - Two Overlapping Times", "Note Read", None, region_map["Glass Desert - Second Half"], rule_map)
		make_event_location(world, "Read: Glass Desert - Two Doors", "Glass Desert - Two Doors", "Note Read", None, region_map["Glass Desert - Second Half"], rule_map)
		make_event_location(world, "Read: Glass Desert - She Stole a Piece of My Heart", "Glass Desert - She Stole a Piece of My Heart", "Note Read", None, region_map["Glass Desert - Second Half"], rule_map)
		make_event_location(world, "Read: Glass Desert - Sold the Ranch", "Glass Desert - Sold the Ranch", "Note Read", None, region_map["Glass Desert - Second Half"], rule_map)
		make_event_location(world, "Read: Glass Desert - I Wasn't Ready", "Glass Desert - I Wasn't Ready", "Note Read", None, region_map["Glass Desert - Second Half"], rule_map)
		make_event_location(world, "Read: Glass Desert - Life Waiting to Flow", "Glass Desert - Life Waiting to Flow", "Note Read", None, region_map["Glass Desert - First Half"], rule_map)
		make_event_location(world, "Read: Glass Desert - The Sand Sea", "Glass Desert - The Sand Sea", "Note Read", None, region_map["Glass Desert - Second Half"], rule_map)
		
	
	if world.options.enable_stylish_dlc_treasure_pods:
		for location in dlc_interactables:
			make_location(world, location[0], region_map[location[1]], rule_map)
	
	if world.options.include_7z:
		for location in corporate_locations:
			make_location(world, location[0], region_map[location[1]], rule_map)
	
	if world.options.include_7z and world.options.goal_type == 1:
		for location in corporate_locations:
			make_event_location(world, f"Bought: {location[0]}", location[0], "7Zee Bought", None, region_map[location[1]], rule_map)
	
	make_event_location(world, "Pink Slime (The Ranch)", "''", "Pink Plort", None, region_map["The Ranch"], rule_map)
	make_event_location(world, "Pink Slime (Dry Reef - Main)", "''", "Pink Plort", None, region_map["Dry Reef - Main"], rule_map)
	make_event_location(world, "Pink Slime (Dry Reef - Beach)", "''", "Pink Plort", None, region_map["Dry Reef - Beach"], rule_map)
	make_event_location(world, "Pink Slime (Dry Reef - Ring Island)", "''", "Pink Plort", None, region_map["Dry Reef - Ring Island"], rule_map)
	make_event_location(world, "Pink Slime (The Slime Sea - Between Grotto and Dry Reef Island 2)", "''", "Pink Plort", None, region_map["The Slime Sea - Between Grotto and Dry Reef Island 2"], rule_map)
	make_event_location(world, "Pink Slime (Indigo Quarry - Before First Bridge)", "''", "Pink Plort", None, region_map["Indigo Quarry - Before First Bridge"], rule_map)
	make_event_location(world, "Pink Slime (Indigo Quarry - After The Bridge)", "''", "Pink Plort", None, region_map["Indigo Quarry - After The Bridge"], rule_map)
	make_event_location(world, "Pink Slime (Indigo Quarry - Ash Isles)", "''", "Pink Plort", None, region_map["Indigo Quarry - Ash Isles"], rule_map)
	make_event_location(world, "Pink Slime (Indigo Quarry - Ancient Ruins Transition Overlap)", "''", "Pink Plort", None, region_map["Indigo Quarry - Ancient Ruins Transition Overlap"], rule_map)
	make_event_location(world, "Pink Slime (Moss Blanket - Main)", "''", "Pink Plort", None, region_map["Moss Blanket - Main"], rule_map)
	make_event_location(world, "Pink Slime (Moss Blanket - Mushroom Island)", "''", "Pink Plort", None, region_map["Moss Blanket - Mushroom Island"], rule_map)
	make_event_location(world, "Pink Slime (Ancient Ruins - Main)", "''", "Pink Plort", None, region_map["Ancient Ruins - Main"], rule_map)
	make_event_location(world, "Pink Slime (Glass Desert - First Half)", "''", "Pink Plort", None, region_map["Glass Desert - First Half"], rule_map)
	make_event_location(world, "Pink Slime (Glass Desert - Second Half)", "''", "Pink Plort", None, region_map["Glass Desert - Second Half"], rule_map)
	make_event_location(world, "Pink Slime (The Wilds)", "''", "Pink Plort", None, region_map["The Wilds"], rule_map)
	make_event_location(world, "Tabby Slime (Dry Reef - Main)", "''", "Tabby Plort", None, region_map["Dry Reef - Main"], rule_map)
	make_event_location(world, "Tabby Slime (Dry Reef - Beach)", "''", "Tabby Plort", None, region_map["Dry Reef - Beach"], rule_map)
	make_event_location(world, "Tabby Slime (Dry Reef - Ring Island)", "''", "Tabby Plort", None, region_map["Dry Reef - Ring Island"], rule_map)
	make_event_location(world, "Tabby Slime (Moss Blanket - Main)", "''", "Tabby Plort", None, region_map["Moss Blanket - Main"], rule_map)
	make_event_location(world, "Tabby Slime (Moss Blanket - Mushroom Island)", "''", "Tabby Plort", None, region_map["Moss Blanket - Mushroom Island"], rule_map)
	make_event_location(world, "Tabby Slime (Ancient Ruins - Main)", "''", "Tabby Plort", None, region_map["Ancient Ruins - Main"], rule_map)
	make_event_location(world, "Tabby Slime (Glass Desert - First Half)", "''", "Tabby Plort", None, region_map["Glass Desert - First Half"], rule_map)
	make_event_location(world, "Tabby Slime (Glass Desert - Second Half)", "''", "Tabby Plort", None, region_map["Glass Desert - Second Half"], rule_map)
	make_event_location(world, "Tabby Slime (The Wilds)", "''", "Tabby Plort", None, region_map["The Wilds"], rule_map)
	make_event_location(world, "Tabby Slime (Dry Reef - Offshoot)", "''", "Tabby Plort", None, region_map["Dry Reef - Offshoot"], rule_map)
	make_event_location(world, "Rock Slime (Dry Reef - Main)", "''", "Rock Plort", None, region_map["Dry Reef - Main"], rule_map)
	make_event_location(world, "Rock Slime (Dry Reef - Beach)", "''", "Rock Plort", None, region_map["Dry Reef - Beach"], rule_map)
	make_event_location(world, "Rock Slime (Dry Reef - Ring Island)", "''", "Rock Plort", None, region_map["Dry Reef - Ring Island"], rule_map)
	make_event_location(world, "Rock Slime (Indigo Quarry - Before First Bridge)", "''", "Rock Plort", None, region_map["Indigo Quarry - Before First Bridge"], rule_map)
	make_event_location(world, "Rock Slime (Indigo Quarry - After The Bridge)", "''", "Rock Plort", None, region_map["Indigo Quarry - After The Bridge"], rule_map)
	make_event_location(world, "Rock Slime (Indigo Quarry - Ash Isles)", "''", "Rock Plort", None, region_map["Indigo Quarry - Ash Isles"], rule_map)
	make_event_location(world, "Rock Slime (Indigo Quarry - Ancient Ruins Transition Overlap)", "''", "Rock Plort", None, region_map["Indigo Quarry - Ancient Ruins Transition Overlap"], rule_map)
	make_event_location(world, "Rock Slime (Ancient Ruins - Main)", "''", "Rock Plort", None, region_map["Ancient Ruins - Main"], rule_map)
	make_event_location(world, "Rock Slime (Glass Desert - First Half)", "''", "Rock Plort", None, region_map["Glass Desert - First Half"], rule_map)
	make_event_location(world, "Rock Slime (Glass Desert - Second Half)", "''", "Rock Plort", None, region_map["Glass Desert - Second Half"], rule_map)
	make_event_location(world, "Rock Slime (The Wilds)", "''", "Rock Plort", None, region_map["The Wilds"], rule_map)
	make_event_location(world, "Rock Slime (Dry Reef - Offshoot)", "''", "Rock Plort", None, region_map["Dry Reef - Offshoot"], rule_map)
	make_event_location(world, "Phosphor Slime (Dry Reef - Main)", "''", "Phosphor Plort", None, region_map["Dry Reef - Main"], rule_map)
	make_event_location(world, "Phosphor Slime (Dry Reef - Beach)", "''", "Phosphor Plort", None, region_map["Dry Reef - Beach"], rule_map)
	make_event_location(world, "Phosphor Slime (Dry Reef - Ring Island)", "''", "Phosphor Plort", None, region_map["Dry Reef - Ring Island"], rule_map)
	make_event_location(world, "Phosphor Slime (The Slime Sea - Between Grotto and Dry Reef Island 2)", "''", "Phosphor Plort", None, region_map["The Slime Sea - Between Grotto and Dry Reef Island 2"], rule_map)
	make_event_location(world, "Phosphor Slime (Indigo Quarry - Before First Bridge)", "''", "Phosphor Plort", None, region_map["Indigo Quarry - Before First Bridge"], rule_map)
	make_event_location(world, "Phosphor Slime (Indigo Quarry - After The Bridge)", "''", "Phosphor Plort", None, region_map["Indigo Quarry - After The Bridge"], rule_map)
	make_event_location(world, "Phosphor Slime (Indigo Quarry - Ash Isles)", "''", "Phosphor Plort", None, region_map["Indigo Quarry - Ash Isles"], rule_map)
	make_event_location(world, "Phosphor Slime (Indigo Quarry - Ancient Ruins Transition Overlap)", "''", "Phosphor Plort", None, region_map["Indigo Quarry - Ancient Ruins Transition Overlap"], rule_map)
	make_event_location(world, "Phosphor Slime (Moss Blanket - Main)", "''", "Phosphor Plort", None, region_map["Moss Blanket - Main"], rule_map)
	make_event_location(world, "Phosphor Slime (Moss Blanket - Mushroom Island)", "''", "Phosphor Plort", None, region_map["Moss Blanket - Mushroom Island"], rule_map)
	make_event_location(world, "Phosphor Slime (Ancient Ruins - Main)", "''", "Phosphor Plort", None, region_map["Ancient Ruins - Main"], rule_map)
	make_event_location(world, "Phosphor Slime (Glass Desert - First Half)", "''", "Phosphor Plort", None, region_map["Glass Desert - First Half"], rule_map)
	make_event_location(world, "Phosphor Slime (Glass Desert - Second Half)", "''", "Phosphor Plort", None, region_map["Glass Desert - Second Half"], rule_map)
	make_event_location(world, "Phosphor Slime (The Wilds)", "''", "Phosphor Plort", None, region_map["The Wilds"], rule_map)
	make_event_location(world, "Boom Slime (Indigo Quarry - Before First Bridge)", "''", "Boom Plort", None, region_map["Indigo Quarry - Before First Bridge"], rule_map)
	make_event_location(world, "Boom Slime (Indigo Quarry - After The Bridge)", "''", "Boom Plort", None, region_map["Indigo Quarry - After The Bridge"], rule_map)
	make_event_location(world, "Boom Slime (Indigo Quarry - Ash Isles)", "''", "Boom Plort", None, region_map["Indigo Quarry - Ash Isles"], rule_map)
	make_event_location(world, "Boom Slime (Indigo Quarry - Ancient Ruins Transition Overlap)", "''", "Boom Plort", None, region_map["Indigo Quarry - Ancient Ruins Transition Overlap"], rule_map)
	make_event_location(world, "Boom Slime (Moss Blanket - Main)", "''", "Boom Plort", None, region_map["Moss Blanket - Main"], rule_map)
	make_event_location(world, "Boom Slime (Ancient Ruins - Main)", "''", "Boom Plort", None, region_map["Ancient Ruins - Main"], rule_map)
	make_event_location(world, "Boom Slime (The Wilds)", "''", "Boom Plort", None, region_map["The Wilds"], rule_map)
	make_event_location(world, "Rad Slime (Indigo Quarry - Before First Bridge)", "''", "Rad Plort", None, region_map["Indigo Quarry - Before First Bridge"], rule_map)
	make_event_location(world, "Rad Slime (Indigo Quarry - After The Bridge)", "''", "Rad Plort", None, region_map["Indigo Quarry - After The Bridge"], rule_map)
	make_event_location(world, "Rad Slime (The Wilds)", "''", "Rad Plort", None, region_map["The Wilds"], rule_map)
	make_event_location(world, "Crystal Slime (Indigo Quarry - Before First Bridge)", "''", "Crystal Plort", None, region_map["Indigo Quarry - Before First Bridge"], rule_map)
	make_event_location(world, "Crystal Slime (Indigo Quarry - Ash Isles)", "''", "Crystal Plort", None, region_map["Indigo Quarry - Ash Isles"], rule_map)
	make_event_location(world, "Honey Slime (Moss Blanket - Main)", "''", "Honey Plort", None, region_map["Moss Blanket - Main"], rule_map)
	make_event_location(world, "Hunter Slime (Moss Blanket - Mushroom Island)", "''", "Hunter Plort", None, region_map["Moss Blanket - Mushroom Island"], rule_map)
	make_event_location(world, "Hunter Slime (Moss Blanket - Main)", "''", "Hunter Plort", None, region_map["Moss Blanket - Main"], rule_map)
	make_event_location(world, "Hunter Slime (The Wilds)", "''", "Hunter Plort", None, region_map["The Wilds"], rule_map)
	make_event_location(world, "Quantum Slime (Ancient Ruins - Main)", "''", "Quantum Plort", None, region_map["Ancient Ruins - Main"], rule_map)
	make_event_location(world, "Dervish Slime (Glass Desert - Second Half)", "''", "Dervish Plort", None, region_map["Glass Desert - Second Half"], rule_map)
	make_event_location(world, "Dervish Slime (Glass Desert - First Half)", "''", "Dervish Plort", None, region_map["Glass Desert - First Half"], rule_map)
	make_event_location(world, "Tangle Slime (Glass Desert - Second Half)", "''", "Tangle Plort", None, region_map["Glass Desert - Second Half"], rule_map)
	make_event_location(world, "Tangle Slime (Glass Desert - First Half)", "''", "Tangle Plort", None, region_map["Glass Desert - First Half"], rule_map)
	make_event_location(world, "Mosaic Slime (Glass Desert - Second Half)", "''", "Mosaic Plort", None, region_map["Glass Desert - Second Half"], rule_map)
	make_event_location(world, "Mosaic Slime (Glass Desert - First Half)", "''", "Mosaic Plort", None, region_map["Glass Desert - First Half"], rule_map)
	make_event_location(world, "Gold Slime (Dry Reef - Main)", "''", "Gold Plort", None, region_map["Dry Reef - Main"], rule_map)
	make_event_location(world, "Gold Slime (Dry Reef - Beach)", "''", "Gold Plort", None, region_map["Dry Reef - Beach"], rule_map)
	make_event_location(world, "Gold Slime (Dry Reef - Ring Island)", "''", "Gold Plort", None, region_map["Dry Reef - Ring Island"], rule_map)
	make_event_location(world, "Gold Slime (Dry Reef - Offshoot)", "''", "Gold Plort", None, region_map["Dry Reef - Offshoot"], rule_map)
	make_event_location(world, "Gold Slime (The Slime Sea - Between Grotto and Dry Reef Island 1)", "''", "Gold Plort", None, region_map["The Slime Sea - Between Grotto and Dry Reef Island 1"], rule_map)
	make_event_location(world, "Gold Slime (The Slime Sea - Between Grotto and Dry Reef Island 2)", "''", "Gold Plort", None, region_map["The Slime Sea - Between Grotto and Dry Reef Island 2"], rule_map)
	make_event_location(world, "Gold Slime (The Slime Sea - Mustache Shrine)", "''", "Gold Plort", None, region_map["The Slime Sea - Mustache Shrine"], rule_map)
	make_event_location(world, "Gold Slime (The Slime Sea - Off Moss Blanket)", "''", "Gold Plort", None, region_map["The Slime Sea - Off Moss Blanket"], rule_map)
	make_event_location(world, "Gold Slime (Indigo Quarry - Before First Bridge)", "''", "Gold Plort", None, region_map["Indigo Quarry - Before First Bridge"], rule_map)
	make_event_location(world, "Gold Slime (Indigo Quarry - After The Bridge)", "''", "Gold Plort", None, region_map["Indigo Quarry - After The Bridge"], rule_map)
	make_event_location(world, "Gold Slime (Indigo Quarry - Ash Isles)", "''", "Gold Plort", None, region_map["Indigo Quarry - Ash Isles"], rule_map)
	make_event_location(world, "Gold Slime (Indigo Quarry - Ancient Ruins Transition Overlap)", "''", "Gold Plort", None, region_map["Indigo Quarry - Ancient Ruins Transition Overlap"], rule_map)
	make_event_location(world, "Gold Slime (Moss Blanket - Main)", "''", "Gold Plort", None, region_map["Moss Blanket - Main"], rule_map)
	make_event_location(world, "Gold Slime (Moss Blanket - Mushroom Island)", "''", "Gold Plort", None, region_map["Moss Blanket - Mushroom Island"], rule_map)
	make_event_location(world, "Gold Slime (Moss Blanket - Hunter's Domain)", "''", "Gold Plort", None, region_map["Moss Blanket - Hunter's Domain"], rule_map)
	make_event_location(world, "Gold Slime (Ancient Ruins - Main)", "''", "Gold Plort", None, region_map["Ancient Ruins - Main"], rule_map)
	make_event_location(world, "Gold Slime (Glass Desert - First Half)", "''", "Gold Plort", None, region_map["Glass Desert - First Half"], rule_map)
	make_event_location(world, "Gold Slime (Glass Desert - Second Half)", "''", "Gold Plort", None, region_map["Glass Desert - Second Half"], rule_map)
	make_event_location(world, "Gold Slime (The Wilds)", "''", "Gold Plort", None, region_map["The Wilds"], rule_map)
	make_event_location(world, "Saber Slime (The Wilds)", "''", "Saber Plort", None, region_map["The Wilds"], rule_map)
	
	
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