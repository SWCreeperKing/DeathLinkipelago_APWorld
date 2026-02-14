from worlds.AutoWorld import World
from .Locations import *
from .Rules import *
from .Options import *
from .Items import *
from .Regions import *
from .Settings import *
from typing import *

# File is Auto-generated, see: [No Link Given]

class ConbunnCardboard(World):
	"""
	Conbunn Cardboard
	"""
	game = "Conbunn Cardboard"
	options_dataclass = ConbunnCardboardOptions
	options: ConbunnCardboardOptions
	settings: ClassVar[ConbunnCardboardSettings]
	location_name_to_id = {value: location_dict.index(value) + 1 for value in location_dict}
	item_name_to_id = {value: raw_items.index(value) + 1 for value in raw_items}
	topology_present = True
	ut_can_gen_without_yaml = True
	gen_puml = False

	def __init__(self, multiworld: "MultiWorld", player: int):
		super().__init__(multiworld, player)
		self.location_count = 0

	def generate_early(self):
		check_options(self)
		options = self.options
		if hasattr(self.multiworld, "re_gen_passthrough"):
			if "Conbunn Cardboard" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["Conbunn Cardboard"]
			if "cds_required_to_goal" in passthrough:
				self.options.cds_required_to_goal = CDsRequiredToGoal(passthrough["cds_required_to_goal"])
			

	def create_regions(self):
		gen_create_regions(self)

	def create_item(self, name: str):
		return Item(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self):
		gen_create_items(self)

	def set_rules(self):
		player = self.player
		self.multiworld.completion_condition[self.player] = lambda state: state.has("CD", player, self.options.cds_required_to_goal)

	def fill_slot_data(self):
		characters = [char for char in f"{self.multiworld.seed}{self.player_name}"]
		self.random.shuffle(characters)
		shuffled = f"ap_uuid_{''.join(characters).replace(" ", "_")}"
		slot_data = {
			"cds_required_to_goal": int(self.options.cds_required_to_goal),
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