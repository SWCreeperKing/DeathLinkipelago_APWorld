import math
from typing import Dict, Any, ClassVar, List
from worlds.AutoWorld import World
from BaseClasses import Location, Region, Item, ItemClassification
from .Items import raw_items, PowerwashSimulatorItem, item_table, create_items, unlock_items, filler_items
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
    player_item_steps: Dict[str, Dict[str, int]] = {}
    player_filler_locations: Dict[str, List[str]] = {}
    player_goal_levels: Dict[str, List[str]] = {}
    player_starting_location: Dict[str, str] = {}
    item_name_groups = {
        "unlocks": unlock_items
    }

    def generate_early(self) -> None:
        item_steps: Dict[str, int] = {}
        self.player_starting_location[self.player_name] = land_vehicles[0]
        option_locations = self.options.get_locations()
        check_options(self)

        option_location_count = len(option_locations)
        percentsanity = self.options.percentsanity

        item_steps["total"] = 0
        item_steps["percentsanity"] = (len(range(percentsanity, 100, percentsanity)) + 1) * option_location_count
        item_steps["objectsanity"] = sum(len(objectsanity_dict[loc]) for loc in option_locations)

        if self.options.has_percentsanity():
            item_steps["total"] += item_steps["percentsanity"]

        if self.options.has_objectsanity():
            item_steps["total"] += item_steps["objectsanity"]

        item_steps["unlocks"] = option_location_count - 1
        item_steps["raw mcguffins"] = option_location_count if self.options.goal_type == 0 else 0
        item_steps["progression before added"] = item_steps["unlocks"] + item_steps["raw mcguffins"]

        item_steps["added mcguffins"] = math.floor(
            (item_steps["total"] - item_steps[
                "progression before added"]) * .075) if self.options.goal_type == 0 else 0

        item_steps["total mcguffins"] = item_steps["raw mcguffins"] + item_steps["added mcguffins"]

        item_steps["total progression"] = item_steps["progression before added"] + item_steps[
            "added mcguffins"]

        item_steps["filler"] = math.floor(
            (item_steps["total"] - item_steps["total progression"]) * self.options.local_fill / 100.0)

        if self.options.goal_type == 1:
            amount_to_goal: int = self.options.amount_of_levels_to_goal
            levels = self.options.get_goal_levels()
            level_count = len(levels)
            if amount_to_goal == 0 or amount_to_goal == level_count:
                self.player_goal_levels[self.player_name] = levels
            elif 0 < amount_to_goal <= len(levels):
                self.player_goal_levels[self.player_name] = self.random.sample(levels, amount_to_goal)
            else:
                amount_to_goal = self.random.randint(1, min(7, level_count))
                self.player_goal_levels[self.player_name] = self.random.sample(levels, amount_to_goal)
            item_steps["goal level count"] = amount_to_goal
        else:
            self.player_goal_levels[self.player_name] = ["None"]

        self.player_item_steps[self.player_name] = item_steps


    def create_regions(self) -> None:
        self.player_filler_locations[self.player_name] = []
        option_locations = self.options.get_locations()
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        option_location_count = len(option_locations)
        percentsanity = self.options.percentsanity
        starting_location = self.player_starting_location[self.player_name]

        for location in option_locations:
            location_list: List[str] = []
            next_region = Region(f"Clean the {location}", self.player, self.multiworld)
            self.multiworld.regions.append(next_region)

            if self.options.has_percentsanity():
                for i in range(percentsanity, 100, percentsanity):
                    location_list.append(self.make_location(f"{location} {i}%", next_region).name)

                location_list.append(self.make_location(f"{location} 100%", next_region).name)

            if self.options.has_objectsanity():
                for part in objectsanity_dict[location]:
                    location_list.append(self.make_location(part, next_region).name)

            level_completion_loc = Location(self.player, f"Urge to clean the {location}", None, next_region)
            level_completion_loc.place_locked_item(
                Item(f"Cleaned the {location}", ItemClassification.progression, None, self.player))
            next_region.locations.append(level_completion_loc)

            if location == starting_location:
                menu_region.connect(next_region)
            else:
                menu_region.connect(next_region,
                                    rule=lambda state, location_lock=location: state.has(f"{location_lock} Unlock",
                                                                                         self.player))

            next_region.connect(menu_region)
            self.random.shuffle(location_list)
            location_list.pop()
            location_list.pop()
            for loc in location_list:
                self.player_filler_locations[self.player_name].append(loc)

        item_steps = self.player_item_steps[self.player_name]
        item_steps["mcguffin requirement"] = max(
            min(math.floor(item_steps["total"] * .05), item_steps["total"] - option_location_count * 2),
            len(option_locations))
        self.player_item_steps[self.player_name] = item_steps


    def create_item(self, name: str) -> PowerwashSimulatorItem:
        return PowerwashSimulatorItem(name, item_table[name], self.item_name_to_id[name], self.player)


    def create_items(self) -> None:
        create_items(self)


    def set_rules(self) -> None:
        if self.options.goal_type == 0:
            self.multiworld.completion_condition[self.player] = lambda state: state.has("A Job Well Done", self.player,
                                                                                        self.mcguffin_requirement)
        else:
            level_requirements = [f"Cleaned the {loc}" for loc in self.player_goal_levels[self.player_name]]
            level_amount_requirements = len(level_requirements)
            self.multiworld.completion_condition[self.player] = lambda state, reqs=level_requirements, amount=level_amount_requirements: len(
                [True for item in reqs if state.has(item, self.player)]) == amount


    def pre_fill(self) -> None:
        location_map: Dict[str, Location] = {loc.name: loc for loc in
                                             self.multiworld.get_locations(self.player)}

        for _ in range(self.player_item_steps[self.player_name]["filler"]):
            location_map[self.player_filler_locations[self.player_name].pop()].place_locked_item(
                self.create_item(self.random.choice(filler_items)))


    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "starting_location": str(self.player_starting_location[self.player_name]),
            "jobs_done": int(self.player_item_steps[self.player_name]["mcguffin requirement"]),
            "objectsanity": bool("Objectsanity" in self.options.sanities),
            "percentsanity": bool("Percentsanity" in self.options.sanities),
            "goal_levels": str(self.player_goal_levels[self.player_name]),
            "goal_level_amount": int(self.player_item_steps[self.player_name]["goal level count"])
        }

        return slot_data


    def make_location(self, location_name, region) -> Location:
        location = Location(self.player, location_name, self.location_name_to_id[location_name], region)
        region.locations.append(location)
        return location
