from worlds.AutoWorld import World
from .Locations import *
from .Rules import *
from .Options import *
from .Items import *
from .Regions import *
from .Settings import *
from typing import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class Atlyss(World):
	"""
	Atlyss
	"""
	game = "Atlyss"
	options_dataclass = AtlyssOptions
	options: AtlyssOptions
	settings: ClassVar[AtlyssSettings]
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
			if "Atlyss" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["Atlyss"]
			if "goal" in passthrough:
				options.goal = Goal(passthrough["goal"])
			
			if "random_portals" in passthrough:
				options.random_portals = RandomPortals(passthrough["random_portals"])
			
			if "shop_sanity" in passthrough:
				options.shop_sanity = ShopSanity(passthrough["shop_sanity"])
			
			if "main_class" in passthrough:
				options.main_class = MainClass(passthrough["main_class"])
			
			if "secondary_class" in passthrough:
				options.secondary_class = SecondaryClass(passthrough["secondary_class"])
			

	def create_regions(self):
		gen_create_regions(self)

	def create_item(self, name: str):
		return Item(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self):
		gen_create_items(self)

	def set_rules(self):
		player = self.player
		options = self.options
		match options.goal:
			case 0:
				self.multiworld.completion_condition[self.player] = lambda state: can_beat_enemy(state, player, options, 'Slime Diva')
			case 1:
				self.multiworld.completion_condition[self.player] = lambda state: can_beat_enemy(state, player, options, 'Lord Zuulneruda')
			case 2:
				self.multiworld.completion_condition[self.player] = lambda state: can_beat_enemy(state, player, options, 'Colossus')
			case 3:
				self.multiworld.completion_condition[self.player] = lambda state: can_beat_enemy(state, player, options, 'Galius')
			case 4:
				self.multiworld.completion_condition[self.player] = lambda state: can_beat_enemy(state, player, options, 'Lord Kaluuz')
			case 5:
				self.multiworld.completion_condition[self.player] = lambda state: can_beat_enemy(state, player, options, 'Valdur')
			case 6:
				self.multiworld.completion_condition[self.player] = lambda state: can_beat_enemy(state, player, options, "Slime Diva") and can_beat_enemy(state, player, options, "Lord Zuulneruda") and can_beat_enemy(state, player, options, "Lord Kaluuz") and can_beat_enemy(state, player, options, "Colossus") and can_beat_enemy(state, player, options, "Valdur") and can_beat_enemy(state, player, options, "Galius")
			case 7:
				self.multiworld.completion_condition[self.player] = lambda state: has_quest(state, player, options, "The Glyphik Booklet") and has_quest(state, player, options, "Cleaning Terrace") and has_quest(state, player, options, "Ancient Beings") and has_quest(state, player, options, "Wicked Wizboars") and has_quest(state, player, options, "Spiraling In The Grove") and has_quest(state, player, options, "Hell In The Grove") and has_quest(state, player, options, "Nulversa Magica") and has_quest(state, player, options, "Night Spirits") and has_quest(state, player, options, "Ridding Slimes") and has_quest(state, player, options, "Huntin' Hogs") and has_quest(state, player, options, "Purging the Grove") and has_quest(state, player, options, "Cleansing the Grove") and has_quest(state, player, options, "Nulversa Viscera") and has_quest(state, player, options, "Call of Fury") and has_quest(state, player, options, "Mastery of Strength") and has_quest(state, player, options, "Beckoning Foes") and has_quest(state, player, options, "Summore' Spectral Powder!") and has_quest(state, player, options, "Makin' More Mekspears") and has_quest(state, player, options, "Makin' More Wizwands") and has_quest(state, player, options, "Makin' More Vile Blades") and has_quest(state, player, options, "Summore' Golem Chestpieces") and has_quest(state, player, options, "Makin' More Ragespears") and has_quest(state, player, options, "Summore' Monolith Chestpieces") and has_quest(state, player, options, "Nulversa, Greenversa!") and has_quest(state, player, options, "Summore' Firebreath Blades") and has_quest(state, player, options, "Makin' More Follycannons") and has_quest(state, player, options, "Focusin' in") and has_quest(state, player, options, "Mastery of Dexterity") and has_quest(state, player, options, "Whatta' Rush!") and has_quest(state, player, options, "Purging the Undead") and has_quest(state, player, options, "Rattlecage Rage") and has_quest(state, player, options, "Consumed Madness") and has_quest(state, player, options, "Eradicating the Undead") and has_quest(state, player, options, "Reviling more Rageboars") and has_quest(state, player, options, "Facing Foes") and has_quest(state, player, options, "The Gall of Galius") and has_quest(state, player, options, "Up and Over It") and has_quest(state, player, options, "Sapphite Ingots")
			case 8:
				self.multiworld.completion_condition[self.player] = lambda state: can_grind_level(state, player, options, 32)
		

	def fill_slot_data(self):
		slot_data = {
			"goal": int(self.options.goal),
			"random_portals": bool(self.options.random_portals),
			"shop_sanity": bool(self.options.shop_sanity),
			"main_class": int(self.options.main_class),
			"secondary_class": int(self.options.secondary_class)
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