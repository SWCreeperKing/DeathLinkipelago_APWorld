from .Options import DeathLinkipelagoOptions
from .Items import DeathLinkipelagoItem, item_table, create_items
from worlds.AutoWorld import World
from BaseClasses import Location, Region

uuid_offset = 0x0AF5F0AC

class DeathLinkipelago(World):
    """A Game about receiving death links"""
    game = "DeathLinkipelago"
    options_dataclass = DeathLinkipelagoOptions
    options: DeathLinkipelagoOptions
    location_name_to_id = {f"DeathLinkipelago Death Check {id_offset + 1}": uuid_offset + id_offset for id_offset in range(50)}
    item_name_to_id = {name: uuid_offset + data.id_offset for name, data in item_table.items()}

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)

        for i in range(self.options.death_check_amount):
            location_name =  f"DeathLinkipelago Death Check {i + 1}"
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