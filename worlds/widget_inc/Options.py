from dataclasses import dataclass
from Options import Range, Toggle, DefaultOnToggle, PerGameCommonOptions, OptionSet, OptionError, Choice, Accessibility

# File is Auto-generated, see: [https://github.com/SWCreeperKing/Widgitpelago/blob/master/Widgitpelago/Archipelago/ApShenanigans.cs]

class ProductionMultiplier(Range):
	"""
	Gives a production multiplier
	"""
	display_name = "Production Multiplier"
	range_start = 1
	range_end = 10
	default = 4


class HandCraftingMultiplier(Range):
	"""
	Gives a multiplier to hand crafting
	"""
	display_name = "Hand Crafting Multiplier"
	range_start = 1
	range_end = 10
	default = 2


@dataclass
class WidgetIncOptions(PerGameCommonOptions):
	production_multiplier: ProductionMultiplier
	hand_crafting_multiplier: HandCraftingMultiplier


def check_options(world):
	pass

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Widget Inc YAML ERROR ===\nWidget Inc: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')