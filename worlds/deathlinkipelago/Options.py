import logging
from dataclasses import dataclass
from Options import Range, Toggle, PerGameCommonOptions, DefaultOnToggle


class CheckCount(Range):
    """
    How many death checks there will be
    max is 50

    extend_death_limit in the host yaml will remove the 50 check limit
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

class SecondsPerLifeCoin(Range):
    """How long in seconds can no death occur to gain a life coin? 0 = disabled, 7min default, 2hr max"""
    display_name = "Seconds Per Life Coin"
    default = 420
    range_start = 0
    range_end = 7200


class UseGlobalDeathCounter(Toggle):
    """Will store death counts in the global slot and sync with anyone else with this enabled (might be a bit strange with overriding)"""
    display_name = "Use Global Death Counter"


class ProgressiveItemsPerShop(Range):
    """How many items in the shop will be priority"""
    display_name = "Progressive Items Per Shop"
    default = 3
    range_start = 0
    range_end = 10

class SendDeathTrapsAfterGoal(Toggle):
    """Send deathlinks from traps after goal"""
    display_name = "Send Death Trap After Goal"

class SendScoutHints(DefaultOnToggle):
    """Sends scout hints about progressive items in the death shop"""
    display_name = "Send Scout Hints"

@dataclass
class DeathLinkipelagoOptions(PerGameCommonOptions):
    death_check_amount: CheckCount
    has_funny_button: EnableFunnyButton
    death_trap_percent: DeathTrapPercent
    progressive_items_per_shop: ProgressiveItemsPerShop
    send_traps_after_goal: SendDeathTrapsAfterGoal
    seconds_per_life_coin: SecondsPerLifeCoin
    use_global_counter: UseGlobalDeathCounter
    send_scout_hints: SendScoutHints


def check_options(world):
    if world.options.death_check_amount > 50 and not world.settings.extend_death_limit:
        logging.info(
            f"DeathLinkipelago: {world.player_name} has {world.options.death_check_amount} > 50. since the host has remove_death_limit false the check amount will default to 50")
        world.options.death_check_amount = CheckCount(50)

    if world.options.has_funny_button and not world.settings.allow_funny_button:
        logging.info(
            f"DeathLinkipelago: {world.player_name} wants the funny button, but won't get it due to the allow_funny_button host setting")
