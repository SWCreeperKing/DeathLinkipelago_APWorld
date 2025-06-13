import logging
from typing import List
from dataclasses import dataclass
from Options import Range, Toggle, PerGameCommonOptions, DefaultOnToggle, OptionSet
from .Locations import land_vehicles, water_vehicles, air_vehicles, places


class StartWithVan(Toggle):
    """
    Start with Van as the random starting level
    """
    display_name = "Start With Van"


class LandVehicles(OptionSet):
    """
    Allowed Land Vehicles

    ["Van", "Vintage Car", "Grandpa Miller's Car", "Fire Truck", "Dirt Bike", "Golf Cart", "Motorbike and Sidecar", "SUV", "Penny Farthing", "Recreation Vehicle", "Drill", "Monster Truck"]
    """
    display_name = "Land Vehicles"
    valid_keys = frozenset(land_vehicles)
    default = frozenset(land_vehicles)


class WaterVehicles(OptionSet):
    """
    Allowed Water Vehicles

    ["Frolic Boat", "Fishing Boat"]
    """
    display_name = "Water Vehicles"
    valid_keys = frozenset(water_vehicles)
    default = frozenset(water_vehicles)


class AirVehicles(OptionSet):
    """
    Allowed Air Vehicles

    ["Fire Helicopter", "Private Jet", "Stunt Plane", "Recreational Vehicle (Again)"]
    """
    display_name = "Air Vehicles"
    valid_keys = frozenset(air_vehicles)
    default = frozenset(air_vehicles)


class Places(OptionSet):
    """
    Allowed Places

    ["Back Garden", "Bungalow", "Playground", "Detached House", "Shoe House", "Fire Station", "Skatepark", "Forest Cottage", "Mayor's Mansion", "Carousel", "Tree House", "Temple", "Washroom", "Helter Skelter", "Ferris Wheel", "Subway Platform", "Fortune Teller's Wagon", "Ancient Statue", "Ancient Monument", "Lost City Palace"]
    """
    display_name = "Places"
    valid_keys = frozenset(places)
    default = frozenset(places)


@dataclass
class PowerwashSimulatorOptions(PerGameCommonOptions):
    start_with_van: StartWithVan
    land_vehicles: LandVehicles
    water_vehicles: WaterVehicles
    air_vehicles: AirVehicles
    places: Places

    def get_locations(self) -> List[str]:
        return extract_location(self.land_vehicles) + extract_location(self.water_vehicles) + extract_location(
            self.air_vehicles) + extract_location(self.places)


def extract_location(option_set: OptionSet) -> List[str]:
    return [loc for loc in option_set]

def check_options(world):
    options: PowerwashSimulatorOptions = world.options
    full_list = options.get_locations()

    if len(full_list) > 0: return

    logging.error(f"Powerwash Simulator: {world.player_name} does not have any allowed locations")
