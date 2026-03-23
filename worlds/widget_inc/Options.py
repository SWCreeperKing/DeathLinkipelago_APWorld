from dataclasses import dataclass
from Options import *
from .Locations import *

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


class ScoutHintTierProducers(Range):
	"""
	Scout hint upto [1-13] Tier resource producers
	0 is off
	"""
	display_name = "Scout Hint Tier Producers"
	range_start = 0
	range_end = 12
	default = 3


@dataclass
class WidgetIncOptions(PerGameCommonOptions):
	production_multiplier: ProductionMultiplier
	hand_crafting_multiplier: HandCraftingMultiplier
	scout_hint_tier_producers: ScoutHintTierProducers


def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Widget Inc YAML ERROR ===\nWidget Inc: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')