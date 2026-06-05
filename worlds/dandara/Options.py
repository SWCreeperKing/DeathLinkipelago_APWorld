from dataclasses import dataclass
from Options import *
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class GoalType(Choice):
	"""
	Which Boss to defeat as goal
	"""
	display_name = "Goal Type"
	option_final_boss = 0
	option_true_ending = 1
	default = 0


@dataclass
class DandaraOptions(PerGameCommonOptions):
	goal_type: GoalType

	def get_options_map(self, option):
		match option:
			case "goal_type":
				return self.goal_type
		

def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Dandara YAML ERROR ===\nDandara: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')