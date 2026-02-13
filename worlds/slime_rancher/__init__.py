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
	item_name_groups = {
		"unlocks": region_unlocks
	}
	ut_can_gen_without_yaml = True
	gen_puml = False

	def __init__(self, multiworld: "MultiWorld", player: int):
		super().__init__(multiworld, player)
		self.location_count = 0

	def generate_early(self):
		check_options(self)
		if hasattr(self.multiworld, "re_gen_passthrough"):
			if "Slime Rancher" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["Slime Rancher"]
			if "goal_type" in passthrough:
				self.options.goal_type = GoalType(passthrough["goal_type"])
			
			if "start_with_dry_reef" in passthrough:
				self.options.start_with_dry_reef = StartWithDryReef(passthrough["start_with_dry_reef"])
			
			if "enable_stylish_dlc_treasure_pods" in passthrough:
				self.options.enable_stylish_dlc_treasure_pods = EnableStylishDlcTreasurePods(passthrough["enable_stylish_dlc_treasure_pods"])
			
			if "treasure_cracker_checks" in passthrough:
				self.options.treasure_cracker_checks = TreasureCrackerChecks(passthrough["treasure_cracker_checks"])
			
			if "include_7z" in passthrough:
				self.options.include_7z = Include7z(passthrough["include_7z"])
			
			if "fix_market_rates" in passthrough:
				self.options.fix_market_rates = FixMarketRates(passthrough["fix_market_rates"])
			
			if "start_with_drone" in passthrough:
				self.options.start_with_drone = StartWithDrone(passthrough["start_with_drone"])
			
			if "trap_percent" in passthrough:
				self.options.trap_percent = TrapPercent(passthrough["trap_percent"])
			
		if self.options.start_with_dry_reef:
		    self.multiworld.push_precollected(self.create_item("Region Unlock: Dry Reef"))
		if self.options.start_with_drone:
		    self.multiworld.push_precollected(self.create_item("Drone"))

	def create_regions(self):
		gen_create_regions(self)

	def create_item(self, name: str):
		return Item(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self):
		gen_create_items(self)

	def set_rules(self):
		player = self.player
		if self.options.goal_type == 0:
		    self.multiworld.completion_condition[self.player] = lambda state: state.has("Note Read", player, 28)
		elif self.options.goal_type == 1:
		    self.multiworld.completion_condition[self.player] = lambda state: state.has("7Zee Bought", player, len(corporate_locations))
		elif self.options.goal_type == 2:
		    self.multiworld.completion_condition[self.player] = lambda state: state.has_all(region_unlocks[3:], player)

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