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
    "Progressive Death Shop": DeathLinkipelagoItemData(ItemClassification.progression, 5)
}

def create_items(world):
    item_count = world.options.death_check_amount
    if item_count == 0: return

    shop_items = max(0, math.ceil(item_count / 10) - 1)
    for i in range(shop_items):
        world.multiworld.itempool.append(world.create_item("Progressive Death Shop"))
        item_count -= 1

    trap_amount = math.ceil(item_count * (world.options.death_trap_percent / 100))
    for i in range(trap_amount):
        world.multiworld.itempool.append(world.create_item("Death Trap"))
        item_count -= 1

    for i in range(item_count):
        world.multiworld.itempool.append(world.create_item("Death Shield"))
        item_count -= 1