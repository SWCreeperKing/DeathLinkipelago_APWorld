import math
from typing import Dict, Any, ClassVar, List, Set
from Options import OptionError
from worlds.AutoWorld import World
from BaseClasses import Location, Region, Item, ItemClassification, LocationProgressType, MultiWorld
from .Locations import location_dict, interactables, dlc_interactables, upgrades
from .Connections import zones, backwards_connections
from .Rules import get_rule_map
from .Options import SlimeRancherOptions, EnableStylishDlcTreasurePods, StartWithDryReef, Include7zUpgrades
from .Items import raw_items, region_unlocks, create_items, SlimeRancherItem, item_table

class SlimeRancher(World):
	"""
	Slime Rancher
	"""
	game = "Slime Rancher"
	options_dataclass = SlimeRancherOptions
	options: SlimeRancherOptions
	location_name_to_id = {value: location_dict.index(value) + 1 for value in location_dict}
	item_name_to_id = {value: raw_items.index(value) + 1 for value in raw_items}

	item_name_groups = {
		"unlocks": region_unlocks
	}

	topology_present = True
	ut_can_gen_without_yaml = True
	gen_puml = False

	def __init__(self, multiworld: "MultiWorld", player: int):
		super().__init__(multiworld, player)
		self.location_count = 0

	def generate_early(self) -> None:
		if hasattr(self.multiworld, "re_gen_passthrough"):
			if "Slime Rancher" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["Slime Rancher"]
			self.options.enable_stylish_dlc_treasure_pods = EnableStylishDlcTreasurePods(passthrough["enable_dlc"])
			self.options.start_with_dry_reef = StartWithDryReef(passthrough("start_with_dry_reef"))
			self.options.include_7z_upgrades = Include7zUpgrades(passthrough["include_7z_upgrades"])

		if self.options.start_with_dry_reef:
			self.multiworld.push_precollected(self.create_item(f"Region Unlock: Dry Reef"))

	def create_regions(self) -> None:
		menu_region = Region("Menu", self.player, self.multiworld)
		ranch_region = Region("The Ranch", self.player, self.multiworld)
		upgrade_region = Region("Personal Upgrades", self.player, self.multiworld)

		menu_region.connect(ranch_region, "Menu -> The Ranch")
		ranch_region.connect(upgrade_region, "The Ranch -> Personal Upgrades")
		region_map: Dict[str, Region] = {
			"Menu": menu_region,
			"The Ranch": ranch_region,
			"Upgrades": upgrade_region
		}

		for zone in zones:
			zone_region = region_map[zone] = Region(zone, self.player, self.multiworld)

			for back_connection in backwards_connections[zone]:
				back_region = region_map[back_connection]
				back_region.connect(zone_region, f"{back_connection} -> {zone}",
					lambda state, region_unlock=zone: state.has(f"Region Unlock: {region_unlock}", self.player))

			region_map[zone] = zone_region

		rule_map = get_rule_map(self.player, self.options)

		for upgrade in upgrades:
			location = self.make_location(upgrade, upgrade_region)

			if upgrade not in rule_map: continue
			location.access_rule = rule_map[upgrade]

		for location_data in interactables:
			location_name = location_data[0]
			location_region = region_map[location_data[1]]
			location = self.make_location(location_name, location_region)

			if "Hobson's Note" in location_name:
				event_location = Location(self.player, f"Read: {location_name}", None, location_region)
				event_location.place_locked_item(Item("Note Read", ItemClassification.progression, None, self.player))
				location_region.locations.append(event_location)

				if location_name in rule_map:
					event_location.access_rule = rule_map[location_name]

			if location_name not in rule_map: continue
			location.access_rule = rule_map[location_name]

		if self.options.enable_stylish_dlc_treasure_pods:
			for location_data in dlc_interactables:
				location_name = location_data[0]
				location_region = region_map[location_data[1]]
				location = self.make_location(location_name, location_region)

				if location_name not in rule_map: continue
				location.access_rule = rule_map[location_name]

		for region in region_map.values():
			self.multiworld.regions.append(region)

	def create_item(self, name: str) -> SlimeRancherItem:
		return SlimeRancherItem(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self) -> None:
		create_items(self)

	def set_rules(self) -> None:
		self.multiworld.completion_condition[self.player] = lambda state: state.has("Note Read", self.player, 28)

	def fill_slot_data(self) -> Dict[str, Any]:
		characters = [char for char in f"{self.random.choice(zones)}{self.multiworld.seed}{self.player_name}"]
		self.random.shuffle(characters)
		shuffled = ''.join(characters).replace(" ", "_")
		slot_data: Dict[str, Any] = {
			"start_with_dry_reef": bool(self.options.start_with_dry_reef),
			"enable_dlc": bool(self.options.enable_stylish_dlc_treasure_pods),
			"include_7z_upgrades": bool(self.options.include_7z_upgrades),
			"uuid": str(f"ap_uuid_{shuffled}")
		}

		return slot_data

	def generate_output(self, output_directory: str) -> None:
		if not self.gen_puml: return
		from Utils import visualize_regions
		state = self.multiworld.get_all_state(False)
		state.update_reachable_regions(self.player)
		visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml",
			show_entrance_names=True,
			regions_to_highlight=state.reachable_regions[self.player])

	def make_location(self, location_name, region) -> Location:
		location = Location(self.player, location_name, self.location_name_to_id[location_name], region)
		region.locations.append(location)
		self.location_count += 1
		return location
