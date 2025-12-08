import logging
from typing import List, Union
from dataclasses import dataclass
from Options import Range, Toggle, DefaultOnToggle, PerGameCommonOptions, OptionSet, OptionError, Choice, Accessibility
from settings import Group, Bool
from random import Random

class StartWithDryReef(DefaultOnToggle):
	"""
	Start with the Dry Reef unlocked
	"""
	display_name = "Start With Dry Reef"

class EnableStylishDlcTreasurePods(Toggle):
	"""
	note: THIS WILL NOT GIVE YOU DLC
	YOU MUST __***OWN***__ THE DLC
	"""
	display_name = "Enable Stylish Dlc Treasure Pods"

class TreasureCrackerChecks(Range):
	"""
	which levels of the treasure cracker is considered as checks
	default: level 1
	level 1 requires crafting 1 gadget
	level 2 requires crafting 20 gadgets
	level 3 requires crafting 50 gadgets
	"""
	display_name = "Treasure Cracker Checks"
	range_start = 0
	range_end = 3
	default = 1

class Include7z(Toggle):
	"""
	Include unlockables behind 7z as checks
	estimated to appear in sphere 2 and above
	"""
	display_name = "Include 7z"

class FixMarketRates(DefaultOnToggle):
	"""
	Overrides the default market behavior:
	instead of https://slimerancher.fandom.com/wiki/Plort_Market_(Slime_Rancher)
	it will make all plort prices 150% base value, base value listed in the above link
	"""
	display_name = "Fix Market Rates"

@dataclass
class SlimeRancherOptions(PerGameCommonOptions):
	start_with_dry_reef: StartWithDryReef
	enable_stylish_dlc_treasure_pods: EnableStylishDlcTreasurePods
	treasure_cracker_checks: TreasureCrackerChecks
	include_7z: Include7z
	fix_market_rates: FixMarketRates