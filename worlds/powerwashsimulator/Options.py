import logging
from typing import List
from dataclasses import dataclass
from Options import Range, Toggle, PerGameCommonOptions, DefaultOnToggle, OptionSet, OptionList
from .Locations import raw_location_dict


class StartWithVan(Toggle):
    """
    Start with Van as the random starting level
    """
    display_name = "Start With Van"


class Locations(OptionSet):
    """
    Allowed Locations

    [
        "Van", "Vintage Car", "Grandpa Miller's Car", "Fire Truck", "Dirt Bike", "Golf Cart", "Motorbike and Sidecar", "SUV", "Penny Farthing", "Recreation Vehicle", "Drill", "Monster Truck",
        "Frolic Boat", "Fishing Boat",
        "Fire Helicopter", "Private Jet", "Stunt Plane", "Recreational Vehicle (Again)",
        "Back Garden", "Bungalow", "Playground", "Detached House", "Shoe House", "Fire Station", "Skatepark", "Forest Cottage", "Mayor's Mansion", "Carousel", "Tree House", "Temple", "Washroom", "Helter Skelter", "Ferris Wheel", "Subway Platform", "Fortune Teller's Wagon", "Ancient Statue", "Ancient Monument", "Lost City Palace"
    ]
    """
    display_name = "Locations"
    valid_keys = frozenset(raw_location_dict)
    default = frozenset(raw_location_dict)

class FillerToMcGuffin(Range):
    """
    How much filler in % to set to McGuffins (A Job Well Done)
    """
    display_name = "Filler To McGuffin"
    range_start = 0
    range_end = 100
    default = 10

@dataclass
class PowerwashSimulatorOptions(PerGameCommonOptions):
    start_with_van: StartWithVan
    locations: Locations
    filler_to_mcguffin: FillerToMcGuffin

    def get_locations(self) -> List[str]:
        return [loc for loc in self.locations]

def check_options(world):
    options: PowerwashSimulatorOptions = world.options

    if options.start_with_van and "Van" not in options:
        logging.warning(f"Powerwash Simulator: {world.player_name} Has 'start_with_van' on but doesn't have 'Van' as an option in their locations, a random location will be picked")

    if len(options.get_locations()) > 0: return
    logging.error(
        f"Powerwash Simulator: {world.player_name} Does not have locations listed in their yaml, PLEASE FIX YOUR YAML")