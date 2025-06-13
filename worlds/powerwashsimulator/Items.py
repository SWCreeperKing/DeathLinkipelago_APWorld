import math

from BaseClasses import Item, ItemClassification, Optional
from typing import NamedTuple, Dict

from .Locations import raw_location_dict
from .Options import PowerwashSimulatorOptions

class PowerwashSimulatorItem(Item):
    game = "Powerwash Simulator"

progression_items = [f"{location} Unlock" for location in raw_location_dict] + ["A Job Well Done"]
filler_items = ["Dirt", "Grime", "Satisfaction", "Water", "Sponge", "Bubblegum Flavored Soap"]

item_table: Dict[str, ItemClassification] = {
    **{item: ItemClassification.progression for item in progression_items},
    **{item: ItemClassification.filler for item in filler_items}
}

raw_items = progression_items + filler_items

def create_items(world):
    options: PowerwashSimulatorOptions = world.options

    for location in options.get_locations():
        world.multiworld.itempool.append(world.create_item("A Job Well Done"))
        world.location_counter -= 1

        if location == world.starting_location: continue
        world.multiworld.itempool.append(world.create_item(f"{location} Unlock"))
        world.location_counter -= 1

    while world.location_counter > 0:
        world.multiworld.itempool.append(world.create_item(world.random.choice(filler_items)))
        world.location_counter -= 1
