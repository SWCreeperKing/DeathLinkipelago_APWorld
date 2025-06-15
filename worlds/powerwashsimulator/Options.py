import logging
from typing import List, Union
from dataclasses import dataclass
from Options import Range, Toggle, PerGameCommonOptions, OptionSet, OptionError
from .Locations import raw_location_dict
from settings import Group, Bool


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

class Sanities(OptionSet):
    """
    Which sanities should be enabled?

    Percentsanity: every % total cleaned of a level is a check
    Objectsanity: each part of a cleanable object is a check
    """
    display_name = "Sanities"
    valid_keys = frozenset(["Percentsanity", "Objectsanity"])
    default = "Percentsanity"

class Percentsanity(Range):
    """
    What intervals of cleaned % to have checks at

    default 20: checks at 20%, 40%, 60%, 80%, and 100%
    host yaml setting `allow_percentsanity_below_7` (off by default) will allow % below 7%
    """
    default = 20
    range_end = 20
    range_start = 1

@dataclass
class PowerwashSimulatorOptions(PerGameCommonOptions):
    start_with_van: StartWithVan
    locations: Locations
    filler_to_mcguffin: FillerToMcGuffin
    sanities: Sanities
    percentsanity: Percentsanity

    def get_locations(self) -> List[str]:
        locations = [loc for loc in self.locations]

        if self.start_with_van and "Van" not in locations:
            locations.append("Van")

        return locations

class PowerwashSimulatorSettings(Group):
    class AllowPercentsanityBelow7(Bool):
        """Allow players to have the Percentsanity setting to be below 7%"""

    class AllowObjectsanity(Bool):
        """Allow players to enable Objectsanity"""

    allow_percentsanity_below_7: Union[AllowPercentsanityBelow7, bool] = False
    allow_objectsanity: Union[AllowObjectsanity, bool] = False

def check_options(world):
    options: PowerwashSimulatorOptions = world.options
    settings: PowerwashSimulatorSettings = world.settings

    if options.percentsanity < 7 and not settings.allow_percentsanity_below_7:
        logging.info(
            f"Powerwash Simulator: {world.player_name} has {settings.allow_percentsanity_below_7} < 7. since the host has allow_percentsanity_below_7 false percentsanity will be set to 7")
        options.percentsanity = Percentsanity(7)

    if "Objectsanity" in options.sanities and not settings.allow_objectsanity:
        RaiseYamlError(world.player_name, "Objectsanity can not be enabled unless the host setting 'allow_objectsanity' is also enabled")

    if len(options.get_locations()) > 0: return
    RaiseYamlError(world.player_name, "Does not have locations listed in their yaml")

def RaiseYamlError(player_name, error):
    raise OptionError(
        f"\n\n=== Powerwash Simulator YAML ERROR ===\nPowerwash Simulator: {player_name} {error}, PLEASE FIX YOUR YAML\n\n")