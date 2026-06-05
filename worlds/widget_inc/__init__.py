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
			if "Widget Inc" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["Widget Inc"]
			if "production_multiplier" in passthrough:
				options.production_multiplier = ProductionMultiplier(passthrough["production_multiplier"])
			
			if "hand_crafting_multiplier" in passthrough:
				options.hand_crafting_multiplier = HandCraftingMultiplier(passthrough["hand_crafting_multiplier"])
			
			if "scout_hint_tier_producers" in passthrough:
				options.scout_hint_tier_producers = ScoutHintTierProducers(passthrough["scout_hint_tier_producers"])
			
		check_options(self)
		self.multiworld.push_precollected(self.create_item("Widget Factory"))
		if options.scout_hint_tier_producers > 0:
			options.start_hints = StartHints([*options.start_hints, "Iron Mine", "Iron Smelter", "Widget Factory"])
		if options.scout_hint_tier_producers > 1:
			options.start_hints = StartHints([*options.start_hints, "Sand Pit", "Glass Kiln", "Gyroscope Fabricator", "Widget Spinner"])
		if options.scout_hint_tier_producers > 2:
			options.start_hints = StartHints([*options.start_hints, "Oil Field", "Oil Power Plant", "Battery Assembler", "Capacitor Bank"])
		if options.scout_hint_tier_producers > 3:
			options.start_hints = StartHints([*options.start_hints, "Copper Mine", "Copper Forge", "Plastic Extractor", "Circuit Fab", "Computational Engine"])
		if options.scout_hint_tier_producers > 4:
			options.start_hints = StartHints([*options.start_hints, "Tesla Coil", "Core Foundry", "Integrator"])
		if options.scout_hint_tier_producers > 5:
			options.start_hints = StartHints([*options.start_hints, "Silicon Extruder", "Processor Lab", "Mainframe Assembler"])
		if options.scout_hint_tier_producers > 6:
			options.start_hints = StartHints([*options.start_hints, "Uranium Mine", "Fuel Rod Assembler", "Cloud Digitizer"])
		if options.scout_hint_tier_producers > 7:
			options.start_hints = StartHints([*options.start_hints, "Widget Minitizers", "Nanoscale Lab", "Reactor Foundry", "Quantum Tunneler"])
		if options.scout_hint_tier_producers > 8:
			options.start_hints = StartHints([*options.start_hints, "Helium Extractor", "Conductor Foundry", "AI Laboratory", "AI Delimiter"])
		if options.scout_hint_tier_producers > 9:
			options.start_hints = StartHints([*options.start_hints, "Training Center", "Data Transformer", "Ascension Facility"])
		if options.scout_hint_tier_producers > 10:
			options.start_hints = StartHints([*options.start_hints, "Sentience Facility", "Picoscale Lab", "Sentience Aggregator"])
		if options.scout_hint_tier_producers > 11:
			options.start_hints = StartHints([*options.start_hints, "Omega Processor Lab", "Omega Core Foundry", "Rocket Electronics Lab", "Omega Widget Distiller", "Rocket Fuel Distiller", "Omega Casing Factory", "Omega Shielding Plant", "Rocket Part Assembler", "Omega Project Assembler", "Omega Launch Facility"])

	def create_regions(self):
		gen_create_regions(self)

	def create_item(self, name: str):
		return Item(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self):
		gen_create_items(self)

	def set_rules(self):
		player = self.player
		options = self.options
		player = self.player
		self.multiworld.completion_condition[self.player] = lambda state: rocket_segment(state, player, options)

	def fill_slot_data(self):
		characters = [char for char in f"{self.multiworld.seed}{self.player_name}"]
		self.random.shuffle(characters)
		shuffled = f"ap_uuid_{''.join(characters).replace(" ", "_")}"
		slot_data = {
			"production_multiplier": int(self.options.production_multiplier),
			"hand_crafting_multiplier": int(self.options.hand_crafting_multiplier),
			"scout_hint_tier_producers": int(self.options.scout_hint_tier_producers),
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