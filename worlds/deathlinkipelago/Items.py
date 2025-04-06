import math

from BaseClasses import Item, ItemClassification, Optional
from typing import NamedTuple, Dict

class DeathLinkipelagoItem(Item):
    game = "DeathLinkipelago"


class DeathLinkipelagoItemData(NamedTuple):
    type: ItemClassification
    id_offset: Optional[int]


item_table: Dict[str, DeathLinkipelagoItemData] = {
    "Death Trap": DeathLinkipelagoItemData(ItemClassification.trap, 1),
    "Death Shield": DeathLinkipelagoItemData(ItemClassification.useful, 2),
    "Death Grass": DeathLinkipelagoItemData(ItemClassification.filler, 3),
    "The Urge to Die": DeathLinkipelagoItemData(ItemClassification.progression, 4),
}

def create_items(world):
    item_count = world.options.death_check_amount
    trap_amount = math.ceil(item_count / 2)
    for i in range(trap_amount):
        world.multiworld.itempool.append(world.create_item("Death Trap"))

    for i in range(item_count - trap_amount):
        world.multiworld.itempool.append(world.create_item("Death Shield"))