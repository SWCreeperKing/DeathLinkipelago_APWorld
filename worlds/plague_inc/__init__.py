from worlds.AutoWorld import World
from .Locations import *
from .Rules import *
from .Options import *
from .Items import *
from .Regions import *
from .Settings import *
from typing import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class PlagueInc(World):
	"""
	Plague Inc
	"""
	game = "Plague Inc"
	options_dataclass = PlagueIncOptions
	options: PlagueIncOptions
	settings: ClassVar[PlagueIncSettings]
	location_name_to_id = {value: location_dict.index(value) + 1 for value in location_dict}
	item_name_to_id = {value: raw_items.index(value) + 1 for value in raw_items}
	topology_present = True
	ut_can_gen_without_yaml = True
	gen_puml = False

	def __init__(self, multiworld: "MultiWorld", player: int):
		super().__init__(multiworld, player)
		self.location_count = 0
		self.starting_diff = ""
		self.starting_disease = ""
		self.victories_needed = 0

	def generate_early(self):
		options = self.options
		if hasattr(self.multiworld, "re_gen_passthrough"):
			if "Plague Inc" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["Plague Inc"]
			if "bacteria" in passthrough:
				self.options.bacteria = Bacteria(passthrough["bacteria"])
			
			if "virus" in passthrough:
				self.options.virus = Virus(passthrough["virus"])
			
			if "fungus" in passthrough:
				self.options.fungus = Fungus(passthrough["fungus"])
			
			if "parasite" in passthrough:
				self.options.parasite = Parasite(passthrough["parasite"])
			
			if "prion" in passthrough:
				self.options.prion = Prion(passthrough["prion"])
			
			if "nano_virus" in passthrough:
				self.options.nano_virus = NanoVirus(passthrough["nano_virus"])
			
			if "bio_weapon" in passthrough:
				self.options.bio_weapon = BioWeapon(passthrough["bio_weapon"])
			
			if "normal_difficulty" in passthrough:
				self.options.normal_difficulty = NormalDifficulty(passthrough["normal_difficulty"])
			
			if "victories_needed" in passthrough:
				victories_needed = passthrough["victories_needed"]
			
		check_options(self)
		self.multiworld.push_precollected(self.create_item(self.starting_diff))
		self.multiworld.push_precollected(self.create_item(self.starting_disease))
		for always_avail_tech in always_tech:
			self.multiworld.push_precollected(self.create_item(always_avail_tech))

	def create_regions(self):
		gen_create_regions(self)

	def create_item(self, name: str):
		return Item(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self):
		gen_create_items(self)

	def set_rules(self):
		player = self.player
		self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", player, self.victories_needed)

	def fill_slot_data(self):
		slot_data = {
			"bacteria": bool(self.options.bacteria),
			"virus": bool(self.options.virus),
			"fungus": bool(self.options.fungus),
			"parasite": bool(self.options.parasite),
			"prion": bool(self.options.prion),
			"nano_virus": bool(self.options.nano_virus),
			"bio_weapon": bool(self.options.bio_weapon),
			"normal_difficulty": bool(self.options.normal_difficulty),
			"victories_needed": int(self.victories_needed)
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