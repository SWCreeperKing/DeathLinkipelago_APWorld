from worlds.AutoWorld import World
from .Locations import *
from .Rules import *
from .Options import *
from .Items import *
from .Regions import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/Werepelago/blob/master/Werepelago/Archipelago/ApShenanigans.cs]

class TheWereCleaner(World):
	"""
	The WereCleaner
	"""
	game = "The WereCleaner"
	options_dataclass = TheWereCleanerOptions
	options: TheWereCleanerOptions
	location_name_to_id = {value: location_dict.index(value) + 1 for value in location_dict}
	item_name_to_id = {value: raw_items.index(value) + 1 for value in raw_items}
	topology_present = True
	ut_can_gen_without_yaml = True
	gen_puml = False

	def __init__(self, multiworld: "MultiWorld", player: int):
		super().__init__(multiworld, player)
		self.location_count = 0
		self.starting_stage = ""

	def generate_early(self):
		check_options(self)
		if hasattr(self.multiworld, "re_gen_passthrough"):
			if "The WereCleaner" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["The WereCleaner"]

	def create_regions(self):
		gen_create_regions(self)

	def create_item(self, name: str):
		return Item(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self):
		gen_create_items(self)

	def set_rules(self):
		self.multiworld.completion_condition[self.player] = lambda state: state.has("Nights Survived", self.player, 7)

	def fill_slot_data(self):
		slot_data = {
			"Kyle": str("Best Boi")
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