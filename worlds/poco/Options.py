from dataclasses import dataclass
from Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

@dataclass
class PocoOptions(PerGameCommonOptions):
	pass

def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Poco YAML ERROR ===\nPoco: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')