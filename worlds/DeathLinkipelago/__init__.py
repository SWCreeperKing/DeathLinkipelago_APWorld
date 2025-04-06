import logging
from typing import Dict, Any, Union, ClassVar
from .Options import DeathLinkipelagoOptions, check_options
from .Items import DeathLinkipelagoItem, item_table, create_items
from worlds.AutoWorld import World
from BaseClasses import Location, Region
from settings import Group, Bool

uuid_offset = 0x0AF5F0AC

class DeathLinkipelagoSettings(Group):
    class AllowFunnyButton(Bool):
        """Allow players to have the funny death button appear in the client"""

    class ExtendDeathLimit(Bool):
        """Extends the 50 deaths check limit to 999"""

    allow_funny_button: Union[AllowFunnyButton, bool] = False
    extend_death_limit: Union[ExtendDeathLimit, bool] = False


class DeathLinkipelago(World):
    """A Game about receiving death links"""
    game = "DeathLinkipelago"
    options_dataclass = DeathLinkipelagoOptions
    options: DeathLinkipelagoOptions
    settings: ClassVar[DeathLinkipelagoSettings]
    location_name_to_id = {f"DeathLinkipelago Death Check {id_offset + 1}": uuid_offset + id_offset for id_offset in range(999)}
    item_name_to_id = {name: uuid_offset + data.id_offset for name, data in item_table.items()}

    def generate_early(self) -> None:
        check_options(self)

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)

        for i in range(self.options.death_check_amount):
            location_name = f"DeathLinkipelago Death Check {i + 1}"
            location = Location(self.player, location_name, self.location_name_to_id[location_name], menu_region)
            menu_region.locations.append(location)

        self.multiworld.regions.append(menu_region)

    def create_item(self, name: str) -> DeathLinkipelagoItem:
        item = item_table[name]
        return DeathLinkipelagoItem(name, item.type, item.id_offset + uuid_offset, self.player)

    def create_items(self) -> None:
        self.push_precollected(self.create_item("The Urge to Die"))
        create_items(self)

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("The Urge to Die", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "death_check_amount": int(self.options.death_check_amount),
            "has_funny_button": bool(self.options.has_funny_button and self.settings.allow_funny_button)
        }

        return slot_data
