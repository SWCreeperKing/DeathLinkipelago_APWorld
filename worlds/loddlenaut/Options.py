from dataclasses import dataclass
from Options import *
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class Evolutionsanity(Toggle):
	"""
	Loddle Evolutions are checks
	"""
	display_name = "Evolutionsanity"


class Cooksanity(Toggle):
	"""
	Cooking Recipes are checks
	"""
	display_name = "Cooksanity"


@dataclass
class LoddlenautOptions(PerGameCommonOptions):
	evolutionsanity: Evolutionsanity
	cooksanity: Cooksanity

	def get_options_map(self, option):
		match option:
			case "evolutionsanity":
				return self.evolutionsanity
			case "cooksanity":
				return self.cooksanity
		

def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Loddlenaut YAML ERROR ===\nLoddlenaut: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')