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

class Include7zUpgrades(Toggle):
	"""
	Include the upgrades locked behind 7z as checks?
	estimated to appear in sphere 2 and above
	"""
	display_name = "Include 7z Upgrades"

@dataclass
class SlimeRancherOptions(PerGameCommonOptions):
	start_with_dry_reef: StartWithDryReef
	enable_stylish_dlc_treasure_pods: EnableStylishDlcTreasurePods
	include_7z_upgrades: Include7zUpgrades