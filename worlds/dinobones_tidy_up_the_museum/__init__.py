from worlds.AutoWorld import *
from .Locations import *
from .Rules import *
from .Options import *
from .Items import *
from .Regions import *
from .Settings import *
from typing import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class DinoBonesTidyUptheMuseum(World):
	"""
	DinoBones Tidy Up the Museum
	"""
	class DinoBonesTidyUptheMuseumWeb(WebWorld):
		tutorials = []


	game = "DinoBones Tidy Up the Museum"
	options_dataclass = DinoBonesTidyUptheMuseumOptions
	options: DinoBonesTidyUptheMuseumOptions
	settings: ClassVar[DinoBonesTidyUptheMuseumSettings]
	topology_present = True
	ut_can_gen_without_yaml = True
	gen_puml = False
	location_name_to_id = {value: location_dict.index(value) + 1 for value in location_dict}
	item_name_to_id = {value: raw_items.index(value) + 1 for value in raw_items}
	enable_local_fill = True
	item_name_groups = {
		"crates": crates
	}

	def __init__(self, multiworld: "MultiWorld", player: int):
		super().__init__(multiworld, player)
		self.location_count = 0
		self.local_location_count = 0
		self.local_fill_loc = []

	def generate_early(self):
		options = self.options
		if hasattr(self.multiworld, "re_gen_passthrough"):
			if "DinoBones Tidy Up the Museum" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["DinoBones Tidy Up the Museum"]
		else: check_options(self)

	def create_regions(self):
		gen_create_regions(self)

	def create_item(self, name: str):
		return Item(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self):
		gen_create_items(self)

	def set_rules(self):
		player = self.player
		options = self.options
		self.multiworld.completion_condition[self.player] = lambda state: has_crate(state, player, options, 1) and has_crate(state, player, options, 2) and has_crate(state, player, options, 3) and has_crate(state, player, options, 4) and has_crate(state, player, options, 5) and has_crate(state, player, options, 6) and has_crate(state, player, options, 7) and has_crate(state, player, options, 8) and has_crate(state, player, options, 9) and has_crate(state, player, options, 10) and has_crate(state, player, options, 11) and has_crate(state, player, options, 12) and has_crate(state, player, options, 13) and has_crate(state, player, options, 14) and has_crate(state, player, options, 15) and has_crate(state, player, options, 16) and has_crate(state, player, options, 17) and has_crate(state, player, options, 18) and has_crate(state, player, options, 19) and has_crate(state, player, options, 20) and has_crate(state, player, options, 21) and has_crate(state, player, options, 22) and has_crate(state, player, options, 23) and has_crate(state, player, options, 24) and has_crate(state, player, options, 25) and has_crate(state, player, options, 26) and has_crate(state, player, options, 27) and has_crate(state, player, options, 28)

	def pre_fill(self):
		player = self.player
		options = self.options
		self.random.shuffle(self.local_fill_loc)
		for _ in range(self.local_location_count):
		    if len(self.local_fill_loc) == 0:
		        raise OptionError(
		            "ㄟ( ▔, ▔ )ㄏ blame other games for touching my speget (aka. other worlds are stealing DinoBones Tidy Up the Museum's prefill locations)\nbug the developers of the other worlds because they shouldn't be interfering with other worlds like this")
		    
		    location = self.local_fill_loc.pop()
		    try:
		        location.place_locked_item(self.create_item(self.get_filler_item_name()))
		    except:
		        pass

	def fill_slot_data(self):
		characters = [char for char in f"{self.multiworld.seed}{self.player_name}"]
		self.random.shuffle(characters)
		shuffled = f"ap_uuid_{''.join(characters).replace(" ", "_")}"
		slot_data = {
			"uuid": str(shuffled)
		}
		return slot_data

	def get_filler_item_name(self):
		return "Dust"

	def generate_output(self, output_directory: str):
		if self.gen_puml: 
		    from Utils import visualize_regions
		    state = self.multiworld.get_all_state(False)
		    state.update_reachable_regions(self.player)
		    visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml",
		                      show_entrance_names=True,
		                      regions_to_highlight=state.reachable_regions[self.player])