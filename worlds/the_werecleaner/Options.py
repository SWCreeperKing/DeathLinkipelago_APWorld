from dataclasses import dataclass
from Options import Range, Toggle, DefaultOnToggle, PerGameCommonOptions, OptionSet, OptionError, Choice, Accessibility

# File is Auto-generated, see: [https://github.com/SWCreeperKing/Werepelago/blob/master/Werepelago/Archipelago/ApShenanigans.cs]

@dataclass
class TheWereCleanerOptions(PerGameCommonOptions):
	pass

def check_options(world):
	pass

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== The WereCleaner YAML ERROR ===\nThe WereCleaner: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')