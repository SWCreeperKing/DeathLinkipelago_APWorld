from dataclasses import dataclass
from Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class CDsRequiredToGoal(Range):
	"""
	The amount of CDs required to goal
	"""
	display_name = "CDs Required To Goal"
	range_start = 5
	range_end = 40
	default = 25


@dataclass
class ConbunnCardboardOptions(PerGameCommonOptions):
	cds_required_to_goal: CDsRequiredToGoal


def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings
	if options.accessibility == Accessibility.option_minimal:
	    print("Conbunn Cardboard doesn't support accessibility minimal, defaulting accessibility to full")
	    options.accessibility = Accessibility(Accessibility.option_full)

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Conbunn Cardboard YAML ERROR ===\nConbunn Cardboard: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')