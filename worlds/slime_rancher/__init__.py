from worlds.AutoWorld import World
from .Locations import *
from .Rules import *
from .Options import *
from .Items import *
from .Regions import *
from .Settings import *
from typing import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class SlimeRancher(World):
	"""
	Slime Rancher
	"""
	game = "Slime Rancher"
	options_dataclass = SlimeRancherOptions
	options: SlimeRancherOptions
	settings: ClassVar[SlimeRancherSettings]
	location_name_to_id = {value: location_dict.index(value) + 1 for value in location_dict}
	item_name_to_id = {value: raw_items.index(value) + 1 for value in raw_items}
	topology_present = True
	ut_can_gen_without_yaml = True
	gen_puml = False
	item_name_groups = {
		"unlocks": region_unlocks
	}
	location_name_groups = {
		"The Ranch": ["The Overgrowth - Artificial Moss Blanket", "The Docks - Our Greater Purpose", "The Grotto - The Limitless Black of Space", "The Grotto - Overlooking the Slime Sea", "The Lab - The Wonders of Plort Technology", "The Lab - Tinkerer's Starting Cache"],
		"Dry Reef": ["Dry Reef - Hobson's Greetings", "Dry Reef - Indigo Quarry Entrance", "Dry Reef - Great Big Tree", "Dry Reef - Map Data Node", "Dry Reef - Hidden Treasure of the Pink Gordo", "Dry Reef - Nested in Crystal", "Dry Reef - Hidden Behind a Short Wall", "Dry Reef - Phosphor Gordo's Personal Pod", "Dry Reef - Cliff Tree Prize", "Dry Reef - Ruminating on the Beach", "Dry Reef - Hidden in the Shade", "Dry Reef - Outside Tabby Gordo's Home", "Dry Reef - A Darn Good Boot", "Dry Reef - Tiny Not-Huge Island", "Ring Island - King of the Hill", "Ring Island - Flower Viewing on a Cliff", "Ring Island - Naturally Curious", "Dry Reef - Hidden Away on an ARCH-ipelago", "Dry Reef - Carrot Chest", "Ring Island - Perilously Perched Pod", "Dry Reef - Overlooking the Tarr Hotspot", "Dry Reef - On the Middle Shelf", "Dry Reef - Hidden Crevice Under the Hidden Cliff", "Ring Island - On a Dirty Patch", "The Slime Sea - Floating Alone in the Sea", "Dry Reef - Stony Hen Hen Coop"],
		"Indigo Quarry": ["Indigo Quarry - I Liked Her Laugh", "Indigo Quarry - The Boom Zone", "Indigo Quarry - Map Data Node", "Indigo Quarry - Skate Fast Eat Grass", "Indigo Quarry - Crystal Wind Chime", "Indigo Quarry - Coral Tube Treasure", "Indigo Quarry - Puddle Lake", "Indigo Quarry - Peeping Puddle Slimes", "Indigo Quarry - Under a Hexium Crystal", "Ash Isles - Looking to the Stars", "Ash Isles - Blooming from Fire Flowers", "Indigo Quarry - Above the Smoke and Ashes", "Indigo Quarry - Personal Puddle Pod", "Indigo Quarry - Under Crumbled Scaffolding", "Indigo Quarry - Slightly Irradiated Reward", "Indigo Quarry - Treasure After the End", "Indigo Quarry - Follow the Ravine", "Ash Isles - Atop a Firey Perch", "Indigo Quarry - Hidden Behind Stalagtmites", "Indigo Quarry - On a Cliff Before Puddle Lake", "Indigo Quarry - Isolated from the Quarry", "Indigo Quarry - Crystal Cache behind Rickety Bridges", "Indigo Quarry - Across Hexium Crystal Formations", "Ash Isles - The Edge of the World"],
		"Moss Blanket": ["Moss Blanket - Fairy Circle Treasure", "Moss Blanket - Map Data Node", "Moss Blanket - New Ancient Jungle", "Moss Blanket - Overgrown Fungus Pod", "Moss Blanket - MOSS BLANKET STUCK", "Moss Blanket - Hidden Flowery Place", "Moss Blanket - The Cupboard under the Stairs", "Moss Blanket - Above the Hungry Hungry Largos", "Moss Blanket - Can't Recommend Love Enough", "Moss Blanket - Just Under a Ledge", "Moss Blanket - On a Lone Island", "Moss Blanket - At the Bottom of a Sheer Wall", "Moss Blanket - Briar Hen Pen", "Moss Blanket - Peepers Peeled!", "Moss Blanket - Tall Tree Treasure", "Moss Blanket - The Lost Archipelago", "Moss Blanket - Under The (Not) Sea", "Moss Blanket - The End Reward", "Moss Blanket - Lonely Rock Pile", "Moss Blanket - In the Roots of a Huge Tree", "Moss Blanket - Overlooking the Tiny Pond", "Moss Blanket - Sunken Treasure", "Moss Blanket - In the Rock Circle", "Moss Blanket - The 'Missed the Jump' Crevice"],
		"The Slime Sea": ["Slime Sea - In Between a Rock and an Island", "The Mustache Shrine - Mustache Stache Cache", "The Slime Sea - On the Giant Tree Stump"],
		"Ancient Ruins": ["Ancient Ruins Transition - Slime Buddy", "Ancient Ruins - The Purpose of the Ruins", "Ancient Ruins - You Gotta Choose a Path", "Ancient Ruins - Everything Quiet on the Western Front", "Ancient Ruins - Map Data Node", "Ancient Ruins - Hidden Nook", "Ancient Ruins - At the End of a Broken Pillar Path", "Ancient Ruins - Tree Memorial", "Ancient Ruins - The Hidden Turnabout", "Ancient Ruins - Caught Up in the Explosion", "Ancient Ruins - A Flowery Respite", "Ancient Ruins - Overlooking From a Flowery Ledge", "Ancient Ruins - Ice-Cold Lemonade", "Ancient Ruins - Above the Ancient Teleporter", "Ancient Ruins - In a Crumbled Pile", "Ancient Ruins - Truly Untamed Country", "Ancient Ruins - There's Slimes in the Walls", "Ancient Ruins - Collapsed Upper Staircase", "Ancient Ruins - The Room With No Door", "Ancient Ruins - Shrine Overlooking the Ancient Ruins", "Ancient Ruins - Hidden Nook on a High Up Platform", "Ancient Ruins - Just Around the Corner"],
		"Glass Desert": ["Glass Desert - Buried Among Rubble", "Glass Desert - Slime Statue Offering", "Glass Desert - At the Tippy Top of the Highest Mountain", "Glass Desert - Behind a False Wall", "Glass Desert - You'll Risk Burning Your Tuchus!", "Glass Desert - Atop the Pillar before a Chasm", "Glass Desert - Painted Hen Stowaway Crate", "Glass Desert - Map Data Node", "Glass Desert - The Side of the Central Ruin", "Glass Desert - In a High-up Nook", "Glass Desert - On a Private Island", "Glass Desert - Under the Private Island", "Glass Desert - Hiding Behind a Sheer Mountain", "Glass Desert - Down in a Hole", "Glass Desert - Two Overlapping Times", "Glass Desert - Overlooking Great Glass Pillars", "Glass Desert - Hover from One Tower to Another", "Glass Desert - Two Doors", "Glass Desert - She Stole a Piece of My Heart", "Glass Desert - Sold the Ranch", "Glass Desert - I Wasn't Ready", "Glass Desert - Stupidly High Up", "Glass Desert - Secret Crevice Above Death Pit", "Glass Desert - Situated on a Collapsed Bridge", "Glass Desert - Hidden in the Rafters", "Glass Desert - Life Waiting to Flow", "Glass Desert - In a Supporting Pillar", "Glass Desert - Jagged Rock Formation in a Plateu", "Glass Desert - Hidden at the Edge of the Sand Sea", "Glass Desert - At the Base of a Fire Glass Sculpture", "Glass Desert - Just Around the Brick Wall", "Glass Desert - The Sand Sea", "Glass Desert - The Highest Fountain"],
		"Viktor's Workshop": ["The Slimeulation - Under a Cliff Bordering The Simulated Sea", "The Slimeulation - Not Quite Rendered Arch", "The Slimeulation - Non-Rendered Cliff", "The Slimeulation - Platforming On Blocky Clouds", "The Slimeulation - Off The Rendered Path", "The Slimeulation - Just Around the Corner", "The Slimeulation - Right Across from the Exit", "The Slimeulation - On Top Of The Simulated Winding Path", "The Slimeulation - Blocky Crevice Beside Moss Entrance", "The Slimeulation - In Between Muhsrooms and Rivers", "The Slimeulation - Underwater in a Ravine", "The Slimeulation - Offshoot of a Hazardous Pathway", "The Slimeulation - Looking Over the Puddle Slimes"],
		"Ogden's Retreat": ["The Wilds - Coral Ring Island Exit", "The Wilds - Across From the Hunter's Sakura Tree", "The Wilds - Inside a Pink Tree Stump", "The Wilds - On a Cliff Dividing Two Entrances", "The Wilds - Hidden Bridge Behind a Triangular Staircase", "The Wilds - A Precarious Ledge By the Waterfall", "The Wilds - Double Waterfall Treasure", "The Wilds - An Outcropping Near the Beach"],
		"Mochi's Manor": ["Nimble Valley - Overlooking the Beginner Start", "Nimble Valley - In a Nook on Top of The Final Stretch Arch", "Nimble Valley - Floating Above the Second Stretch", "Nimble Valley - Bordering the Slime Sea", "Nimble Valley - Inside the Magneticore Pillar", "Nimble Valley - Floating Outcropping Above a Crevice", "Nimble Valley - Hidden in some Magneticore Ore"]
	}

	def __init__(self, multiworld: "MultiWorld", player: int):
		super().__init__(multiworld, player)
		self.location_count = 0

	def generate_early(self):
		check_options(self)
		options = self.options
		if hasattr(self.multiworld, "re_gen_passthrough"):
			if "Slime Rancher" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["Slime Rancher"]
			if "goal_type" in passthrough:
				options.goal_type = GoalType(passthrough["goal_type"])
			
			if "start_with_dry_reef" in passthrough:
				options.start_with_dry_reef = StartWithDryReef(passthrough["start_with_dry_reef"])
			
			if "enable_stylish_dlc_treasure_pods" in passthrough:
				options.enable_stylish_dlc_treasure_pods = EnableStylishDlcTreasurePods(passthrough["enable_stylish_dlc_treasure_pods"])
			
			if "treasure_cracker_checks" in passthrough:
				options.treasure_cracker_checks = TreasureCrackerChecks(passthrough["treasure_cracker_checks"])
			
			if "include_7z" in passthrough:
				options.include_7z = Include7z(passthrough["include_7z"])
			
			if "fix_market_rates" in passthrough:
				options.fix_market_rates = FixMarketRates(passthrough["fix_market_rates"])
			
			if "start_with_drone" in passthrough:
				options.start_with_drone = StartWithDrone(passthrough["start_with_drone"])
			
			if "trap_percent" in passthrough:
				options.trap_percent = TrapPercent(passthrough["trap_percent"])
			
			if "include_ogden" in passthrough:
				options.include_ogden = IncludeOgden(passthrough["include_ogden"])
			
			if "include_mochi" in passthrough:
				options.include_mochi = IncludeMochi(passthrough["include_mochi"])
			
			if "include_viktor" in passthrough:
				options.include_viktor = IncludeViktor(passthrough["include_viktor"])
			
			if "easy_skips" in passthrough:
				options.easy_skips = EasySkips(passthrough["easy_skips"])
			
			if "precise_movement" in passthrough:
				options.precise_movement = PreciseMovement(passthrough["precise_movement"])
			
			if "dangerous_skips" in passthrough:
				options.dangerous_skips = DangerousSkips(passthrough["dangerous_skips"])
			
			if "obscure_locations" in passthrough:
				options.obscure_locations = ObscureLocations(passthrough["obscure_locations"])
			
			if "largo_jumps" in passthrough:
				options.largo_jumps = LargoJumps(passthrough["largo_jumps"])
			
			if "jetpack_boosts" in passthrough:
				options.jetpack_boosts = JetpackBoosts(passthrough["jetpack_boosts"])
			
		if self.options.start_with_dry_reef:
		    self.multiworld.push_precollected(self.create_item("Region Unlock: Dry Reef"))
		if self.options.start_with_drone:
		    self.multiworld.push_precollected(self.create_item("Drone"))
		if not self.options.include_ogden:
		    self.multiworld.push_precollected(self.create_item("Region Unlock: Ogden's Retreat"))
		if not self.options.include_ogden:
		    self.multiworld.push_precollected(self.create_item("Region Unlock: The Wilds"))
		if not self.options.include_mochi:
		    self.multiworld.push_precollected(self.create_item("Region Unlock: Mochi's Manor"))
		if not self.options.include_mochi:
		    self.multiworld.push_precollected(self.create_item("Region Unlock: Nimble Valley"))
		if not self.options.include_viktor:
		    self.multiworld.push_precollected(self.create_item("Region Unlock: Viktor's Workshop"))
		if not self.options.include_viktor:
		    self.multiworld.push_precollected(self.create_item("Region Unlock: The Slimeulations"))

	def create_regions(self):
		gen_create_regions(self)

	def create_item(self, name: str):
		return Item(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self):
		gen_create_items(self)

	def set_rules(self):
		player = self.player
		options = self.options
		match self.options.goal_type:
			case 0:
				self.multiworld.completion_condition[self.player] = lambda state: state.has("Note Read", player, 28)
			case 1:
				self.multiworld.completion_condition[self.player] = lambda state: state.has("7Zee Bought", player, len(corporate_locations))
			case 2:
				self.multiworld.completion_condition[self.player] = lambda state: state.has_all(credits_unlocks, player)
		

	def fill_slot_data(self):
		characters = [char for char in f"{self.multiworld.seed}{self.player_name}"]
		self.random.shuffle(characters)
		shuffled = f"ap_uuid_{''.join(characters).replace(" ", "_")}"
		slot_data = {
			"goal_type": int(self.options.goal_type),
			"start_with_dry_reef": bool(self.options.start_with_dry_reef),
			"enable_stylish_dlc_treasure_pods": bool(self.options.enable_stylish_dlc_treasure_pods),
			"treasure_cracker_checks": int(self.options.treasure_cracker_checks),
			"include_7z": bool(self.options.include_7z),
			"fix_market_rates": bool(self.options.fix_market_rates),
			"start_with_drone": bool(self.options.start_with_drone),
			"trap_percent": int(self.options.trap_percent),
			"include_ogden": bool(self.options.include_ogden),
			"include_mochi": bool(self.options.include_mochi),
			"include_viktor": bool(self.options.include_viktor),
			"easy_skips": bool(self.options.easy_skips),
			"precise_movement": bool(self.options.precise_movement),
			"dangerous_skips": bool(self.options.dangerous_skips),
			"obscure_locations": bool(self.options.obscure_locations),
			"largo_jumps": bool(self.options.largo_jumps),
			"jetpack_boosts": bool(self.options.jetpack_boosts),
			"uuid": str(shuffled)
		}
		return slot_data

	def generate_output(self, output_directory: str):
		if self.gen_puml: 
		    from Utils import visualize_regions
		    state = self.multiworld.get_all_state(False)
		    state.update_reachable_regions(self.player)
		    visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml",
		                      show_entrance_names=True,
		                      regions_to_highlight=state.reachable_regions[self.player])