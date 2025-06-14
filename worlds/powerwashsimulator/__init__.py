import math
from typing import Dict, Any, Union, ClassVar
from worlds.AutoWorld import World
from BaseClasses import Location, Region
from .Items import raw_items, PowerwashSimulatorItem, item_table, create_items
from .Locations import location_dict, raw_location_dict, locations_percentages, land_vehicles, objectsanity_dict
from .Options import PowerwashSimulatorOptions, PowerwashSimulatorSettings, check_options

uuid_offset = 0x3AF4F1BC

class PowerwashSimulator(World):
    """
    Powerwash Simulator
    """
    game = "Powerwash Simulator"
    options_dataclass = PowerwashSimulatorOptions
    options: PowerwashSimulatorOptions
    settings: ClassVar[PowerwashSimulatorSettings]
    location_name_to_id = {value: location_dict.index(value) + uuid_offset for value in location_dict}
    item_name_to_id = {value: raw_items.index(value) + uuid_offset for value in raw_items}
    starting_location = land_vehicles[0]
    location_counter:int = 0
    mcguffin_requirement = 0

    def generate_early(self) -> None:
        check_options(self)

        option_locations = self.options.get_locations()
        if self.options.start_with_van and "Van" in option_locations: return
        self.starting_location = self.random.choice(option_locations)

    def create_regions(self) -> None:
        option_locations = self.options.get_locations()
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        percentsanity = self.options.percentsanity

        for location in option_locations:
            next_region = Region(f"Clean the {location}", self.player, self.multiworld)
            self.multiworld.regions.append(next_region)

            if "Percentsanity" in self.options.sanities:
                for i in range(percentsanity, 100, percentsanity):
                    self.location_counter += 1
                    percent_location = f"{location} {i}%"
                    percentsanity_location = Location(self.player, percent_location, self.location_name_to_id[percent_location], next_region)
                    next_region.locations.append(percentsanity_location)

                percent_location = f"{location} 100%"
                percentsanity_location = Location(self.player, percent_location, self.location_name_to_id[percent_location], next_region)
                next_region.locations.append(percentsanity_location)
                self.location_counter += 1

            if "Objectsanity" in self.options.sanities:
                for part in objectsanity_dict[location]:
                    self.location_counter += 1
                    objectsanity_location = Location(self.player, part, self.location_name_to_id[part], next_region)
                    next_region.locations.append(objectsanity_location)

            if location == self.starting_location:
                menu_region.connect(next_region)
            else:
                menu_region.connect(next_region, rule=lambda state, location_lock=location: state.has(f"{location_lock} Unlock", self.player))
            next_region.connect(menu_region)

        self.mcguffin_requirement = max(min(math.floor(self.location_counter * .1), self.location_counter - len(option_locations) * 2), len(option_locations))

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
            "jobs_done": int(self.mcguffin_requirement),
            "objectsanity": bool("Objectsanity" in self.options.sanities),
            "percentsanity": bool("Percentsanity" in self.options.sanities),
        }

        return slot_data