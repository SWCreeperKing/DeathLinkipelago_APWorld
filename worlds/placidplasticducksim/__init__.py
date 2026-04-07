import math
from typing import Dict, Any, Union, ClassVar, Final
from .Locations import locations, columns
from .Items import PPDSItem, item_table, create_items
from worlds.AutoWorld import World
from BaseClasses import Location, Region, LocationProgressType
from settings import Group, Bool

class PlacidPlasticDuckSimulator(World):
    """A game about funny ducks in a pool"""
    game = "Placid Plastic Duck Simulator"
    location_name_to_id = {value: locations.index(value) + 1 for value in locations}
    item_name_to_id = {name: data.id_offset + 1 for name, data in item_table.items()}
    player_locations_to_fill: Dict[str, int] = {}

    def create_regions(self) -> None:
        self.player_locations_to_fill[self.player_name] = 0
        menu_region = Region("Menu", self.player, self.multiworld)
        last_region = menu_region

        for column in range(len(columns)):
            next_region = Region(f"Duck Column {column}", self.player, self.multiworld)
            self.multiworld.regions.append(next_region)

            if column > 0:
                last_region.connect(next_region, rule=lambda state, progression_req=column: \
                    state.has("Progressive Column Unlock", self.player, progression_req))
            else:
                last_region.connect(next_region)
            last_region = next_region

            for duck in columns[column]:
                self.player_locations_to_fill[self.player_name] += 1
                location = Location(self.player, duck, self.location_name_to_id[duck], last_region)
                last_region.locations.append(location)

        self.multiworld.regions.append(menu_region)

    def create_item(self, name: str) -> PPDSItem:
        return PPDSItem(name, item.type, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        create_items(self)

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Progressive Column Unlock", self.player, 9)
