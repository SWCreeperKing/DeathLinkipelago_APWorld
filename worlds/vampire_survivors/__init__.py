import math
from typing import Dict, Any, ClassVar, List, Set
from Options import OptionError
from worlds.AutoWorld import World
from BaseClasses import Location, Region, Item, ItemClassification, LocationProgressType, MultiWorld
from .Options import VampireSurvivorsOptions, VampireSurvivorsSettings, check_options
from .Locations import location_dictionary, non_special_characters, secret_characters, megalo_characters, \
    unfair_characters, normal_stages, bonus_stages, challenge_stages
from .Items import raw_items, VampireSurvivorsItem, item_table, create_items, unlock_stage_items


class VampireSurvivors(World):
    """
    Vampire Survivors
    """
    game = "Vampire Survivors"
    options_dataclass = VampireSurvivorsOptions
    options: VampireSurvivorsOptions
    settings: ClassVar[VampireSurvivorsSettings]
    location_name_to_id = {value: location_dictionary.index(value) + 1 for value in location_dictionary}
    item_name_to_id = {value: raw_items.index(value) + 1 for value in raw_items}

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self.starting_character = ""
        self.starting_stage = ""
        self.check_count = 0
        self.stage_goal_amount = 0
        self.final_included_characters_list: List[str]
        self.final_included_stages_list: List[str]

    def generate_early(self) -> None:
        check_options(self)

        stages = self.final_included_stages_list
        characters = self.final_included_characters_list

        if len(stages) > 1:
            stages_to_choose_from = [stage for stage in stages if stage in normal_stages]

            if len(stages_to_choose_from) == 0:
                stages_to_choose_from = [stage for stage in stages if stage in bonus_stages]

            if len(stages_to_choose_from) == 0:
                stages_to_choose_from = [stage for stage in stages if stage in challenge_stages]

            if len(stages_to_choose_from) == 0:
                self.starting_stage = self.random.choice(stages)
            else:
                self.starting_stage = self.random.choice(stages_to_choose_from)
        else:
            self.starting_stage = stages[0]

        if len(characters) > 1:  # choose lesser powerful characters to start with
            characters_to_choose_from = [character for character in characters if character in non_special_characters]

            if self.options.allow_secret_characters and len(characters_to_choose_from) == 0:
                characters_to_choose_from = [character for character in characters if character in secret_characters]

            if self.options.allow_megalo_characters and len(characters_to_choose_from) == 0:
                characters_to_choose_from = [character for character in characters if character in megalo_characters]

            if self.options.allow_unfair_characters and self.settings.allow_unfair_characters and len(
                    characters_to_choose_from) == 0:
                characters_to_choose_from = [character for character in characters if character in unfair_characters]

            self.starting_character = self.random.choice(characters_to_choose_from)
        else:
            self.starting_character = characters[0]
        self.stage_goal_amount = len(stages) - 1

    def create_regions(self) -> None:
        stages = self.final_included_stages_list
        characters = self.final_included_characters_list
        chest_checks = self.options.chest_checks_per_stage

        menu_region = Region("Menu", self.player, self.multiworld)
        character_region = Region("Characters", self.player, self.multiworld)

        for stage in stages:
            stage_region = Region(stage, self.player, self.multiworld)

            self.make_location(f"{stage} Beaten", stage_region)

            for i in range(chest_checks):
                self.make_location(f"Open Chest #{i + 1} on {stage}", stage_region)

            if stage != self.starting_stage:
                stage_item_name = f"Stage Unlock: {stage}"
                menu_region.connect(stage_region, f"Menu FISH -> {stage}",
                                    lambda state, stage_item=stage_item_name: state.has(stage_item, self.player))
            else:
                menu_region.connect(stage_region)

            self.multiworld.regions.append(stage_region)

        for character in characters:
            character_location = self.make_location(f"Beat with {character}", character_region)

            if character == self.starting_character: continue

            character_item_name = f"Character Unlock: {character}"
            character_location.access_rule = lambda state, character_item=character_item_name: state.has(character_item,
                                                                                                         self.player)
        self.check_count += len(characters) + len(stages) * (chest_checks + 1)

        menu_region.connect(character_region)
        self.multiworld.regions.append(character_region)
        self.multiworld.regions.append(menu_region)

    def create_item(self, name: str) -> VampireSurvivorsItem:
        return VampireSurvivorsItem(name, item_table[name], self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        create_items(self)

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has_from_list_unique(unlock_stage_items,
                                                                                                     self.player,
                                                                                                     self.stage_goal_amount)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "egg_inclusion": int(self.options.egg_inclusion.value),
            "starting_character": str(self.starting_character),
            "starting_stage": str(self.starting_stage),
            "stages_to_beat": str(self.final_included_stages_list),
            "is_hyper_locked": bool(self.options.lock_hyper_behind_item),
            "is_hurry_locked": bool(self.options.lock_hurry_behind_item),
            "is_arcanas_locked": bool(self.options.lock_arcanas_behind_item),
            "chest_checks_per_stage": int(self.options.chest_checks_per_stage)
        }

        return slot_data

    def make_location(self, location_name, region) -> Location:
        location = Location(self.player, location_name, self.location_name_to_id[location_name], region)
        region.locations.append(location)
        return location
