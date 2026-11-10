from dataclasses import dataclass
from Options import *
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

@dataclass
class ThiefSimulator1Options(PerGameCommonOptions):
	pass

def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Thief Simulator 1 YAML ERROR ===\nThief Simulator 1: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')