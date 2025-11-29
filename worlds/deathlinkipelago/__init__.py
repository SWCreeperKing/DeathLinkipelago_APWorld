import math
from typing import Dict, Any, Union, ClassVar, Final
from .Options import DeathLinkipelagoOptions, check_options
from .Items import DeathLinkipelagoItem, item_table, create_items
from worlds.AutoWorld import World
from BaseClasses import Location, Region, LocationProgressType
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
    shop_locations = {f"Death Shop {id_offset + 1}": uuid_offset + id_offset + 1 for id_offset in range(999)}
    location_name_to_id = {"Starting Check": uuid_offset, **shop_locations}
    item_name_to_id = {name: uuid_offset + data.id_offset for name, data in item_table.items()}
    topology_present = True

    def generate_early(self) -> None:
        check_options(self)

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        last_region = Region("Starting Region", self.player, self.multiworld)

        shops = math.ceil(self.options.death_check_amount / 10)

        last_region.locations.append(Location(self.player, "Starting Check", self.location_name_to_id["Starting Check"], last_region))
        menu_region.connect(last_region)
        self.multiworld.regions.append(menu_region)
        self.multiworld.regions.append(last_region)

        for shop in range(shops):
            next_region = Region(f"Shop {shop + 1}", self.player, self.multiworld)
            self.multiworld.regions.append(next_region)

            if shop > 0:
                last_region.connect(next_region, rule=lambda state, progression_req=shop: \
                        state.has("Progressive Death Shop", self.player, progression_req))
            else:
                last_region.connect(next_region)
            last_region = next_region

            for i in range(min(10, self.options.death_check_amount - shop * 10)):
                location_name = f"Death Shop {i + shop * 10 + 1}"
                location = Location(self.player, location_name, self.location_name_to_id[location_name], last_region)

                if i < self.options.progressive_items_per_shop and shop < shops - 1:
                    location.progress_type = LocationProgressType.PRIORITY

                last_region.locations.append(location)

    def create_item(self, name: str) -> DeathLinkipelagoItem:
        item = item_table[name]
        return DeathLinkipelagoItem(name, item.type, item.id_offset + uuid_offset, self.player)

    def create_items(self) -> None:
        create_items(self)

    def set_rules(self) -> None:
        if self.options.death_check_amount <= 10:
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Death Grass", self.player)
        else:
            self.multiworld.completion_condition[self.player] = \
                lambda state: state.has("Progressive Death Shop", self.player,
                                        math.ceil(self.options.death_check_amount / 10) - 1) and state.has("Death Grass", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "seconds_per_life_coin": int(self.options.seconds_per_life_coin),
            "death_check_amount": int(self.options.death_check_amount),
            "send_traps_after_goal": bool(self.options.send_traps_after_goal),
            "has_funny_button": (bool(self.options.has_funny_button) and bool(self.settings.allow_funny_button)),
            "use_global_counter": bool(self.options.use_global_counter),
            "send_scout_hints": bool(self.options.send_scout_hints),
            "compatibility_version": "v.0.13.0"
        }

        return slot_data
