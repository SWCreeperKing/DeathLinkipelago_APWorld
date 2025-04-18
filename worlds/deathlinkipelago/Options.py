import logging
from dataclasses import dataclass
from Options import Range, Toggle, PerGameCommonOptions


class CheckCount(Range):
    """
    How many death checks there will be
    max is 50

    remove_death_limit in the host yaml will remove the 50 check limit
    """
    display_name = "Death Check Count"
    default = 5
    range_start = 0
    range_end = 999


class EnableFunnyButton(Toggle):
    """If host setting allow_funny_button enabled, then this will allow use of the funny death button"""
    display_name = "Death Button"


class DeathTrapPercent(Range):
    """Percent of items are Death Traps"""
    display_name = "Death Trap Percentage"
    default = 50
    range_start = 0
    range_end = 100


class ProgressiveItemsPerShop(Range):
    """How many items in the shop will be priority"""
    display_name = "Progressive Items Per Shop"
    default = 3
    range_start = 0
    range_end = 10

class SendDeathTrapsAfterGoal(Toggle):
    display_name = "Send Death Trap After Goal"

@dataclass
class DeathLinkipelagoOptions(PerGameCommonOptions):
    death_check_amount: CheckCount
    has_funny_button: EnableFunnyButton
    death_trap_percent: DeathTrapPercent
    progressive_items_per_shop: ProgressiveItemsPerShop
    send_traps_after_goal: SendDeathTrapsAfterGoal


def check_options(world):
    if world.options.death_check_amount > 50 and not world.settings.extend_death_limit:
        logging.info(
            f"DeathLinkipelago: {world.player_name} has {world.options.death_check_amount} > 50. since the host has remove_death_limit false the check amount will default to 50")
        world.options.death_check_amount = CheckCount(50)

    if world.options.has_funny_button and not world.settings.allow_funny_button:
        logging.info(
            f"DeathLinkipelago: {world.player_name} wants the funny button, but won't get it due to the allow_funny_button host setting")
