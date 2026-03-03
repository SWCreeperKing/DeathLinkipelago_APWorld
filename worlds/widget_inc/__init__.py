from worlds.AutoWorld import World
from .Locations import *
from .Rules import *
from .Options import *
from .Items import *
from .Regions import *
from .Settings import *
from typing import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class WidgetInc(World):
	"""
	Widget Inc
	"""
	game = "Widget Inc"
	options_dataclass = WidgetIncOptions
	options: WidgetIncOptions
	settings: ClassVar[WidgetIncSettings]
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
			if "Widget Inc" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["Widget Inc"]
			if "production_multiplier" in passthrough:
				self.options.production_multiplier = ProductionMultiplier(passthrough["production_multiplier"])
			
			if "hand_crafting_multiplier" in passthrough:
				self.options.hand_crafting_multiplier = HandCraftingMultiplier(passthrough["hand_crafting_multiplier"])
			
			if "starting_tier_producers" in passthrough:
				self.options.starting_tier_producers = StartingTierProducers(passthrough["starting_tier_producers"])
			
		if options.starting_tier_producers == 1:
			self.multiworld.push_precollected(self.create_item("Iron Mine"))
			self.multiworld.push_precollected(self.create_item("Iron Smelter"))
			self.multiworld.push_precollected(self.create_item("Widget Factory"))
		else:
			self.multiworld.push_precollected(self.create_item("Widget Factory"))

	def create_regions(self):
		gen_create_regions(self)

	def create_item(self, name: str):
		return Item(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self):
		gen_create_items(self)

	def set_rules(self):
		player = self.player
		player = self.player
		self.multiworld.completion_condition[self.player] = lambda state: rocket_segment(state, player)

	def fill_slot_data(self):
		characters = [char for char in f"{self.multiworld.seed}{self.player_name}"]
		self.random.shuffle(characters)
		shuffled = f"ap_uuid_{''.join(characters).replace(" ", "_")}"
		slot_data = {
			"production_multiplier": int(self.options.production_multiplier),
			"hand_crafting_multiplier": int(self.options.hand_crafting_multiplier),
			"starting_tier_producers": int(self.options.starting_tier_producers),
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