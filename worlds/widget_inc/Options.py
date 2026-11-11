from dataclasses import dataclass
from Options import *
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

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
	scout_hint_tier_producers: ScoutHintTierProducers

	def get_options_map(self, option):
		match option:
			case "scout_hint_tier_producers":
				return self.scout_hint_tier_producers
		

def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Widget Inc YAML ERROR ===\nWidget Inc: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')