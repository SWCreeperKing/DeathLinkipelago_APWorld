from dataclasses import dataclass
from Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

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


class StartingTierProducers(Range):
	"""
	Starts with upto X Tier producers
	"""
	display_name = "Starting Tier Producers"
	range_start = 0
	range_end = 3
	default = 1


@dataclass
class WidgetIncOptions(PerGameCommonOptions):
	production_multiplier: ProductionMultiplier
	hand_crafting_multiplier: HandCraftingMultiplier
	starting_tier_producers: StartingTierProducers


def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Widget Inc YAML ERROR ===\nWidget Inc: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')