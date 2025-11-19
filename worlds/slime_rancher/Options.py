import logging
from typing import List, Union
from dataclasses import dataclass
from Options import Range, Toggle, DefaultOnToggle, PerGameCommonOptions, OptionSet, OptionError, Choice, Accessibility
from settings import Group, Bool
from random import Random

class EnableStylishDlcTreasurePods(Toggle):
	"""
	note: THIS WILL NOT GIVE YOU DLC
	YOU MUST __***OWN***__ THE DLC
	"""
	display_name = "Enable Stylish Dlc Treasure Pods"

@dataclass
class SlimeRancherOptions(PerGameCommonOptions):
	enable_stylish_dlc_treasure_pods: EnableStylishDlcTreasurePods