from dataclasses import dataclass
from Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class GoalType(Choice):
	"""
	What criteria to goal
	notes = read all notes
	7Zee = buy all 7Zee ranks
	credits = get credits
	"""
	display_name = "Goal Type"
	option_notes = 0
	option_7Zee = 1
	option_credits = 2


class StartWithDryReef(DefaultOnToggle):
	"""
	Start with the Dry Reef unlocked
	"""
	display_name = "Start With Dry Reef"


class EnableStylishDlcTreasurePods(Toggle):
	"""
	note: THIS WILL NOT GIVE YOU DLC
	YOU MUST __***OWN***__ THE DLC
	"""
	display_name = "Enable Stylish Dlc Treasure Pods"


class TreasureCrackerChecks(Range):
	"""
	which levels of the treasure cracker is considered as checks
	default: level 1
	level 1 requires crafting 1 gadget
	level 2 requires crafting 20 gadgets
	level 3 requires crafting 50 gadgets
	"""
	display_name = "Treasure Cracker Checks"
	range_start = 0
	range_end = 3
	default = 1


class Include7z(Toggle):
	"""
	Include unlockables behind 7z as checks
	estimated to appear in sphere 2 and above
	"""
	display_name = "Include 7z"


class FixMarketRates(DefaultOnToggle):
	"""
	Overrides the default market behavior:
	instead of https://slimerancher.fandom.com/wiki/Plort_Market_(Slime_Rancher)
	it will make all plort prices 150% base value, base value listed in the above link
	"""
	display_name = "Fix Market Rates"


class StartWithDrone(DefaultOnToggle):
	"""
	Start with a Drone
	"""
	display_name = "Start With Drone"


class TrapPercent(Range):
	"""
	what percent of filler should be replaced with traps
	"""
	display_name = "Trap Percent"
	range_start = 0
	range_end = 100
	default = 15


@dataclass
class SlimeRancherOptions(PerGameCommonOptions):
	goal_type: GoalType
	start_with_dry_reef: StartWithDryReef
	enable_stylish_dlc_treasure_pods: EnableStylishDlcTreasurePods
	treasure_cracker_checks: TreasureCrackerChecks
	include_7z: Include7z
	fix_market_rates: FixMarketRates
	start_with_drone: StartWithDrone
	trap_percent: TrapPercent


def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings
	if options.goal_type == 1 and not options.include_7z:
	    raise_yaml_error(world.player, "7Zee goal type requires you to include 7Zee locations")

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Slime Rancher YAML ERROR ===\nSlime Rancher: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')