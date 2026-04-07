import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player, options):
	return {
		"Dry Reef - Hidden Behind a Short Wall": lambda state: ( has_cracker(state, player, options, 1) ),
		"Dry Reef - Phosphor Gordo's Personal Pod": lambda state: ( has_cracker(state, player, options, 1) ),
		"Dry Reef - Cliff Tree Prize": lambda state: ( has_cracker(state, player, options, 1) and get_yaml_option(state, player, options, 'easy_skips') ) or ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) ),
		"Dry Reef - Hidden in the Shade": lambda state: ( has_cracker(state, player, options, 1) ),
		"Dry Reef - Outside Tabby Gordo's Home": lambda state: ( has_cracker(state, player, options, 1) ),
		"Indigo Quarry - The Boom Zone": lambda state: ( has_cracker(state, player, options, 1) ),
		"Indigo Quarry - Skate Fast Eat Grass": lambda state: ( has_cracker(state, player, options, 1) ),
		"Indigo Quarry - Crystal Wind Chime": lambda state: ( has_jetpack(state, player, options) ) or ( get_yaml_option(state, player, options, 'easy_skips') ),
		"Indigo Quarry - Coral Tube Treasure": lambda state: ( has_cracker(state, player, options, 1) ),
		"Dry Reef - A Darn Good Boot": lambda state: ( get_yaml_option(state, player, options, 'obscure_locations') ) or ( has_jetpack(state, player, options) ),
		"Dry Reef - Tiny Not-Huge Island": lambda state: ( has_jetpack(state, player, options) ),
		"Indigo Quarry - Under a Hexium Crystal": lambda state: ( has_cracker(state, player, options, 1) ),
		"Moss Blanket - Map Data Node": lambda state: ( get_yaml_option(state, player, options, 'easy_skips') ) or ( has_jetpack(state, player, options) ),
		"Ring Island - King of the Hill": lambda state: ( get_yaml_option(state, player, options, 'precise_movement') and get_yaml_option(state, player, options, 'obscure_locations') ) or ( has_jetpack(state, player, options) ),
		"Ring Island - Flower Viewing on a Cliff": lambda state: ( has_cracker(state, player, options, 1) and get_yaml_option(state, player, options, 'precise_movement') and get_yaml_option(state, player, options, 'obscure_locations') ) or ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) ),
		"Ring Island - Naturally Curious": lambda state: ( has_jetpack(state, player, options) ),
		"Moss Blanket - Overgrown Fungus Pod": lambda state: ( has_cracker(state, player, options, 1) and get_yaml_option(state, player, options, 'obscure_locations') ) or ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) ),
		"Moss Blanket - MOSS BLANKET STUCK": lambda state: ( get_yaml_option(state, player, options, 'largo_jumps') ) or ( has_jetpack(state, player, options) ),
		"Moss Blanket - Hidden Flowery Place": lambda state: ( has_cracker(state, player, options, 1) ),
		"Dry Reef - Hidden Away on an ARCH-ipelago": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"Dry Reef - Carrot Chest": lambda state: ( has_cracker(state, player, options, 2) ),
		"Ring Island - Perilously Perched Pod": lambda state: ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"Dry Reef - Overlooking the Tarr Hotspot": lambda state: ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'obscure_locations') ) or ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'jetpack_boosts') ) or ( has_cracker(state, player, options, 2) ),
		"Indigo Quarry - Above the Smoke and Ashes": lambda state: ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'easy_skips') ) or ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"Indigo Quarry - Personal Puddle Pod": lambda state: ( has_cracker(state, player, options, 2) ),
		"Indigo Quarry - Under Crumbled Scaffolding": lambda state: ( has_cracker(state, player, options, 2) ),
		"Indigo Quarry - Slightly Irradiated Reward": lambda state: ( has_cracker(state, player, options, 2) ),
		"Indigo Quarry - Treasure After the End": lambda state: ( has_cracker(state, player, options, 2) ),
		"Ash Isles - Atop a Firey Perch": lambda state: ( has_cracker(state, player, options, 2) ),
		"The Grotto - Overlooking the Slime Sea": lambda state: ( has_cracker(state, player, options, 2) ),
		"Dry Reef - On the Middle Shelf": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ) or ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'precise_movement') ),
		"Moss Blanket - The Cupboard under the Stairs": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ) or ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'largo_jumps') ) or ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'obscure_locations') ),
		"Moss Blanket - Above the Hungry Hungry Largos": lambda state: ( has_cracker(state, player, options, 1) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) ),
		"Moss Blanket - Just Under a Ledge": lambda state: ( has_cracker(state, player, options, 2) ),
		"Moss Blanket - On a Lone Island": lambda state: ( has_jetpack(state, player, options) ) or ( get_yaml_option(state, player, options, 'precise_movement') and get_yaml_option(state, player, options, 'dangerous_skips') ),
		"Moss Blanket - At the Bottom of a Sheer Wall": lambda state: ( has_cracker(state, player, options, 2) ),
		"Moss Blanket - Briar Hen Pen": lambda state: ( has_cracker(state, player, options, 1) ),
		"Moss Blanket - Tall Tree Treasure": lambda state: ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) ),
		"Moss Blanket - The Lost Archipelago": lambda state: ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) ),
		"Moss Blanket - Under The (Not) Sea": lambda state: ( has_cracker(state, player, options, 2) ),
		"Ancient Ruins Transition - Slime Buddy": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"Ancient Ruins - Hidden Nook": lambda state: ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'largo_jumps') ) or ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) and get_yaml_option(state, player, options, 'jetpack_boosts') ) or ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"Ancient Ruins - At the End of a Broken Pillar Path": lambda state: ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"Ancient Ruins - Tree Memorial": lambda state: ( has_cracker(state, player, options, 1) ),
		"Ancient Ruins - The Hidden Turnabout": lambda state: ( has_cracker(state, player, options, 2) ),
		"Ancient Ruins - Caught Up in the Explosion": lambda state: ( has_cracker(state, player, options, 2) ),
		"Ancient Ruins - A Flowery Respite": lambda state: ( has_cracker(state, player, options, 1) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) ),
		"Ancient Ruins - Overlooking From a Flowery Ledge": lambda state: ( has_cracker(state, player, options, 2) ),
		"Ancient Ruins - In a Crumbled Pile": lambda state: ( has_cracker(state, player, options, 2) ),
		"Dry Reef - Hidden Crevice Under the Hidden Cliff": lambda state: ( has_cracker(state, player, options, 3) ),
		"Indigo Quarry - Hidden Behind Stalagtmites": lambda state: ( has_cracker(state, player, options, 3) ),
		"Indigo Quarry - On a Cliff Before Puddle Lake": lambda state: ( has_cracker(state, player, options, 3) and get_yaml_option(state, player, options, 'easy_skips') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Indigo Quarry - Isolated from the Quarry": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Indigo Quarry - Crystal Cache behind Rickety Bridges": lambda state: ( has_cracker(state, player, options, 3) and get_yaml_option(state, player, options, 'precise_movement') and get_yaml_option(state, player, options, 'dangerous_skips') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Indigo Quarry - Across Hexium Crystal Formations": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Ring Island - On a Dirty Patch": lambda state: ( has_cracker(state, player, options, 3) ),
		"The Lab - Tinkerer's Starting Cache": lambda state: ( has_cracker(state, player, options, 1) ),
		"Ash Isles - The Edge of the World": lambda state: ( has_cracker(state, player, options, 3) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"The Slime Sea - Floating Alone in the Sea": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) and has_energy(state, player, options, 3) ),
		"The Mustache Shrine - Mustache Stache Cache": lambda state: ( has_cracker(state, player, options, 3) ),
		"Moss Blanket - Lonely Rock Pile": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) and get_yaml_option(state, player, options, 'precise_movement') and get_yaml_option(state, player, options, 'dangerous_skips') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2) ),
		"Moss Blanket - In the Roots of a Huge Tree": lambda state: ( has_cracker(state, player, options, 3) ),
		"Moss Blanket - Overlooking the Tiny Pond": lambda state: ( has_cracker(state, player, options, 3) and get_yaml_option(state, player, options, 'obscure_locations') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Moss Blanket - Sunken Treasure": lambda state: ( has_cracker(state, player, options, 3) ),
		"Moss Blanket - In the Rock Circle": lambda state: ( has_cracker(state, player, options, 3) and get_yaml_option(state, player, options, 'dangerous_skips') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"The Slime Sea - On the Giant Tree Stump": lambda state: ( has_cracker(state, player, options, 3) ),
		"Moss Blanket - The 'Missed the Jump' Crevice": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Ancient Ruins - There's Slimes in the Walls": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Ancient Ruins - Collapsed Upper Staircase": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Ancient Ruins - The Room With No Door": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ) or ( has_cracker(state, player, options, 3) and get_yaml_option(state, player, options, 'precise_movement') ),
		"Ancient Ruins - Shrine Overlooking the Ancient Ruins": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and get_yaml_option(state, player, options, 'jetpack_boosts') ) or ( has_cracker(state, player, options, 3) and get_yaml_option(state, player, options, 'obscure_locations') and get_yaml_option(state, player, options, 'largo_jumps') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Ancient Ruins - Hidden Nook on a High Up Platform": lambda state: ( has_cracker(state, player, options, 3) ),
		"Ancient Ruins - Just Around the Corner": lambda state: ( has_cracker(state, player, options, 3) and get_yaml_option(state, player, options, 'precise_movement') and get_yaml_option(state, player, options, 'obscure_locations') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Glass Desert - Buried Among Rubble": lambda state: ( has_cracker(state, player, options, 2) ),
		"Glass Desert - Slime Statue Offering": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2) ),
		"Glass Desert - At the Tippy Top of the Highest Mountain": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 3) ),
		"Glass Desert - Behind a False Wall": lambda state: ( has_cracker(state, player, options, 2) ),
		"Glass Desert - Atop the Pillar before a Chasm": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"Glass Desert - The Side of the Central Ruin": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) ),
		"Glass Desert - In a High-up Nook": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and get_yaml_option(state, player, options, 'precise_movement') ),
		"Glass Desert - On a Private Island": lambda state: ( has_jetpack(state, player, options) ),
		"Glass Desert - Under the Private Island": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Glass Desert - Hiding Behind a Sheer Mountain": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Glass Desert - Down in a Hole": lambda state: ( has_cracker(state, player, options, 2) ),
		"Glass Desert - Hover from One Tower to Another": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) ),
		"Glass Desert - Stupidly High Up": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) ),
		"Glass Desert - Secret Crevice Above Death Pit": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) ),
		"Glass Desert - Situated on a Collapsed Bridge": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) ),
		"Glass Desert - Hidden in the Rafters": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"Glass Desert - In a Supporting Pillar": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"Glass Desert - Jagged Rock Formation in a Plateu": lambda state: ( has_jetpack(state, player, options) ),
		"Glass Desert - Hidden at the Edge of the Sand Sea": lambda state: ( has_cracker(state, player, options, 3) ),
		"Glass Desert - At the Base of a Fire Glass Sculpture": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2) ),
		"Glass Desert - Just Around the Brick Wall": lambda state: ( has_cracker(state, player, options, 2) and get_yaml_option(state, player, options, 'precise_movement') ) or ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"Glass Desert - The Sand Sea": lambda state: ( has_jetpack(state, player, options) ),
		"Glass Desert - The Highest Fountain": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"The Slimeulation - Under a Cliff Bordering The Simulated Sea": lambda state: ( has_cracker(state, player, options, 2) ),
		"The Slimeulation - Not Quite Rendered Arch": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"The Slimeulation - Non-Rendered Cliff": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"The Slimeulation - Platforming On Blocky Clouds": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"The Slimeulation - Off The Rendered Path": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"The Slimeulation - Just Around the Corner": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"The Slimeulation - Right Across from the Exit": lambda state: ( has_jetpack(state, player, options) ),
		"The Slimeulation - On Top Of The Simulated Winding Path": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"The Slimeulation - Blocky Crevice Beside Moss Entrance": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"The Slimeulation - In Between Muhsrooms and Rivers": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"The Slimeulation - Underwater in a Ravine": lambda state: ( has_cracker(state, player, options, 2) ),
		"The Slimeulation - Offshoot of a Hazardous Pathway": lambda state: ( has_cracker(state, player, options, 2) ),
		"The Slimeulation - Looking Over the Puddle Slimes": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"The Wilds - Across From the Hunter's Sakura Tree": lambda state: ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) ),
		"The Wilds - Inside a Pink Tree Stump": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) ),
		"The Wilds - On a Cliff Dividing Two Entrances": lambda state: ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) ),
		"The Wilds - Hidden Bridge Behind a Triangular Staircase": lambda state: ( has_cracker(state, player, options, 2) ),
		"The Wilds - A Precarious Ledge By the Waterfall": lambda state: ( has_cracker(state, player, options, 1) ),
		"The Wilds - Double Waterfall Treasure": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) ),
		"The Wilds - An Outcropping Near the Beach": lambda state: ( has_cracker(state, player, options, 1) ),
		"Nimble Valley - Overlooking the Beginner Start": lambda state: ( has_jetpack(state, player, options) ),
		"Nimble Valley - In a Nook on Top of The Final Stretch Arch": lambda state: ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) ),
		"Nimble Valley - Floating Above the Second Stretch": lambda state: ( has_cracker(state, player, options, 3) and has_jetpack(state, player, options) and has_energy(state, player, options, 2) ),
		"Nimble Valley - Bordering the Slime Sea": lambda state: ( has_cracker(state, player, options, 1) and has_jetpack(state, player, options) ),
		"Nimble Valley - Inside the Magneticore Pillar": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) ),
		"Nimble Valley - Floating Outcropping Above a Crevice": lambda state: ( has_cracker(state, player, options, 2) and has_jetpack(state, player, options) and has_energy(state, player, options, 1) ),
		"Nimble Valley - Hidden in some Magneticore Ore": lambda state: ( has_cracker(state, player, options, 3) ),
		"Buy Personal Upgrade (Heart Module lv.2)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Heart Module lv.3)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Heart Module lv.4)": lambda state: can_access_7zee(state, player, options),
		"Buy Personal Upgrade (Tank Booster lv.2)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Tank Booster lv.3)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Tank Booster lv.4)": lambda state: can_access_7zee(state, player, options),
		"Buy Personal Upgrade (Dash Boots lv.2)": lambda state: can_access_7zee(state, player, options),
		"Buy Personal Upgrade (Power Core lv.2)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Power Core lv.3)": lambda state: can_access_dry_reef(state, player, options),
		"Buy Personal Upgrade (Treasure Cracker lv.1)": lambda state: can_access_lab(state, player, options),
		"Buy Personal Upgrade (Treasure Cracker lv.2)": lambda state: can_access_lab(state, player, options),
		"Buy Personal Upgrade (Treasure Cracker lv.3)": lambda state: can_access_lab(state, player, options),
		"Buy Personal Upgrade (Air Drive)": lambda state: can_access_dry_reef(state, player, options),
	}

def get_yaml_option(state, player, options, option) -> bool:
	return options.get_options_map(option).value

def has_amount(state, player, options, item, amount) -> bool:
	return state.has(item, player, amount)

def has(state, player, options, item) -> bool:
	return has_amount(state, player, options, item, 1)

def has_any(state, player, options, items) -> bool:
	return any(has(state, player, options, item) for item in items)

def has_all(state, player, options, items) -> bool:
	return all(has(state, player, options, item) for item in items)

def has_cracker(state, player, options, level) -> bool:
	return has_amount(state, player, options, 'Progressive Treasure Cracker', level)

def has_energy(state, player, options, amount) -> bool:
	return has_amount(state, player, options, 'Progressive Max Energy', amount)

def has_jetpack(state, player, options) -> bool:
	return has(state, player, options, 'Progressive Jetpack')

def has_region(state, player, options, region) -> bool:
	return has(state, player, options, f"Region Unlock: {region}")

def can_access_dry_reef(state, player, options) -> bool:
	return has_region(state, player, options, 'Dry Reef')

def can_access_to_ruins_from_trans(state, player, options) -> bool:
	return has_region(state, player, options, 'Indigo Quarry') and has_region(state, player, options, 'Moss Blanket') and has_region(state, player, options, 'Ancient Ruins')

def can_access_7zee(state, player, options) -> bool:
	return can_access_dry_reef(state, player, options) and can_access_to_ruins_from_trans(state, player, options)

def can_access_lab(state, player, options) -> bool:
	return can_access_dry_reef(state, player, options) and has_region(state, player, options, 'Indigo Quarry') and has_region(state, player, options, 'The Lab')