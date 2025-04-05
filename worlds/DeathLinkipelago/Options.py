from dataclasses import dataclass
from Options import Range, Choice, Toggle, PerGameCommonOptions, StartInventoryPool

class CheckCount(Range):
    """
    How many death checks there will be
    max is 50
    """
    display_name = "Death Check Count"
    default = 5
    range_start = 0
    range_end = 50

@dataclass
class DeathLinkipelagoOptions(PerGameCommonOptions):
    death_check_amount: CheckCount