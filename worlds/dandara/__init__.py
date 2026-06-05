from worlds.AutoWorld import World
from .Locations import *
from .Rules import *
from .Options import *
from .Items import *
from .Regions import *
from .Settings import *
from typing import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class Dandara(World):
	"""
	Dandara
	"""
	game = "Dandara"
	options_dataclass = DandaraOptions
	options: DandaraOptions
	settings: ClassVar[DandaraSettings]
	topology_present = True
	ut_can_gen_without_yaml = True
	gen_puml = False
	location_name_to_id = {value: location_dict.index(value) + 1 for value in location_dict}
	item_name_to_id = {value: raw_items.index(value) + 1 for value in raw_items}

	def __init__(self, multiworld: "MultiWorld", player: int):
		super().__init__(multiworld, player)
		self.location_count = 0

	def generate_early(self):
		options = self.options
		if hasattr(self.multiworld, "re_gen_passthrough"):
			if "Dandara" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["Dandara"]
			if "goal_type" in passthrough:
				options.goal_type = GoalType(passthrough["goal_type"])
			
		check_options(self)

	def create_regions(self):
		gen_create_regions(self)

	def create_item(self, name: str):
		return Item(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self):
		gen_create_items(self)

	def set_rules(self):
		player = self.player
		options = self.options
		match options.goal_type:
			case 0:
				self.multiworld.completion_condition[self.player] = lambda state: has(state, player, options, "FinalBoss_Kill")
			case 1:
				self.multiworld.completion_condition[self.player] = lambda state: has(state, player, options, "DLCF_FearEnded")
		

	def generate_output(self, output_directory: str):
		if self.gen_puml: 
		    from Utils import visualize_regions
		    state = self.multiworld.get_all_state(False)
		    state.update_reachable_regions(self.player)
		    visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml",
		                      show_entrance_names=True,
		                      regions_to_highlight=state.reachable_regions[self.player])