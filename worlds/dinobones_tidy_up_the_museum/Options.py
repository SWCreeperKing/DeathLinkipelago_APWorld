from dataclasses import dataclass
from Options import *
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class LocalFill(Range):
	"""
	% of filler to be made local
	"""
	display_name = "Local Fill"
	range_start = 55
	range_end = 100
	default = 80


@dataclass
class DinoBonesTidyUptheMuseumOptions(PerGameCommonOptions):
	local_fill: LocalFill

	def get_options_map(self, option):
		match option:
			case "local_fill":
				return self.local_fill
		

def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== DinoBones Tidy Up the Museum YAML ERROR ===\nDinoBones Tidy Up the Museum: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')