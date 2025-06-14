from typing import Dict, Any
from worlds.AutoWorld import World
from BaseClasses import Location, Region
from .Items import raw_items, PowerwashSimulatorItem, item_table, create_items
from .Locations import location_dict, raw_location_dict, locations_percentages, land_vehicles
from .Options import PowerwashSimulatorOptions, check_options

uuid_offset = 0x3AF4F1BC
class PowerwashSimulator(World):
    """
    Powerwash Simulator
    """
    game = "Powerwash Simulator"
    options_dataclass = PowerwashSimulatorOptions
    options: PowerwashSimulatorOptions
    location_name_to_id = {value: location_dict.index(value) + uuid_offset for value in location_dict}
    item_name_to_id = {value: raw_items.index(value) + uuid_offset for value in raw_items}
    starting_location = land_vehicles[0]
    location_counter = 0

    def generate_early(self) -> None:
        check_options(self)

        option_locations = self.options.get_locations()
        if self.options.start_with_van and "Van" in option_locations: return
        self.starting_location = self.random.choice(option_locations)

    def create_regions(self) -> None:
        option_locations = self.options.get_locations()
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        for location in option_locations:
            next_region = Region(f"Clean the {location}", self.player, self.multiworld)
            self.multiworld.regions.append(next_region)

            for percent_location in locations_percentages[location]:
                self.location_counter += 1
                location_check = Location(self.player, percent_location, self.location_name_to_id[percent_location], next_region)
                next_region.locations.append(location_check)

            if location == self.starting_location:
                menu_region.connect(next_region)
            else:
                menu_region.connect(next_region, rule=lambda state, location_lock=location: state.has(f"{location_lock} Unlock", self.player))
            next_region.connect(menu_region)

    def create_item(self, name: str) -> PowerwashSimulatorItem:
        return PowerwashSimulatorItem(name, item_table[name], self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        create_items(self)

    def set_rules(self) -> None:
        location_count = len(self.options.get_locations())
        self.multiworld.completion_condition[self.player] = lambda state: state.has("A Job Well Done", self.player, location_count)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "starting_location": str(self.starting_location),
            "jobs_done": int(len(self.options.get_locations()))
        }

        return slot_data