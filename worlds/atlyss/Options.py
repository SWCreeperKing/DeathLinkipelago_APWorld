from dataclasses import dataclass
from Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class Goal(Choice):
	"""
	What is required to complete the game.
	Slime Diva: Defeat the Slime Diva boss (level 10).
	Lord Zuulneruda: Defeat Lord Zuulneruda in the Catacombs (level 12).
	Colossus: Defeat the Colossus in Crescent Grove (level 20).
	Galius: Defeat Galius in Bularr Fortress (level 26) - DEFAULT.
	Lord Kaluuz: Defeat Lord Kaluuz in Catacombs Floor 3 (level 18).
	Valdur: Defeat Valdur the dragon (level 25+).
	All Bosses: Defeat all 6 major bosses.
	All Quests: Complete every quest in the game.
	Level 32: Reach the maximum level.
	"""
	display_name = "Goal"
	option_slime_diva = 0
	option_lord_zuulneruda = 1
	option_colossus = 2
	option_galius = 3
	option_lord_kaluuz = 4
	option_valdur = 5
	option_all_bosses = 6
	option_all_quests = 7
	option_level_32 = 8
	default = 0


class RandomPortals(Toggle):
	"""
	How area portals are unlocked.
	Off (default): Progressive Portals - find "Progressive Portal" items to unlock
	areas in a fixed sequence. Each portal found opens the next area in order.
	On: Random Portals - find individual portal items (e.g. "Outer Sanctum Portal",
	"Catacombs Portal") to unlock specific areas independently.
	"""
	display_name = "Random Portals"


class EquipmentProgression(Choice):
	"""
	How equipment is distributed.
	Gated (default): Equipment has level requirements. Higher tier gear only
	appears at locations accessible at appropriate levels. Tier 1 gear (lv 1-5)
	can appear anywhere; Tier 5 gear (lv 21-26) only at endgame locations.
	Random: Equipment can appear anywhere with no level gating. You may find
	endgame weapons in early spheres — chaotic but fun.
	"""
	display_name = "Equipment Progression"
	option_gated = 0
	option_random = 1
	default = 0


class ShopSanity(DefaultOnToggle):
	"""
	Whether shop items can contain Archipelago items from other worlds.
	When enabled, buying items from shops sends checks to other players.
	"""
	display_name = "Shop Sanity"


class MainClass(Choice):
	"""
	What you chose to be as your main class
	"""
	display_name = "Main Class"
	option_random = 0
	option_fighter = 1
	option_bandit = 2
	option_mystic = 3
	default = 0


class SecondaryClass(Choice):
	"""
	What you chose to be as your secondary class
	"""
	display_name = "Secondary Class"
	option_random = 0
	option_fighter = 1
	option_bandit = 2
	option_mystic = 3
	option_none = 4
	default = 0


@dataclass
class AtlyssOptions(PerGameCommonOptions):
	goal: Goal
	random_portals: RandomPortals
	equipment_progression: EquipmentProgression
	shop_sanity: ShopSanity
	main_class: MainClass
	secondary_class: SecondaryClass

	def is_class(self, class_name):
		class_name_lower = class_name.lower()
		if class_name_lower == 'any': return True
		return class_name_lower == self.main_class or class_name_lower == self.secondary_class

def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings
	classes = ['fighter', 'mystic', 'bandit']
	if options.main_class == 'random':
	    options.main_class = MainClass(random.choice(classes))
	
	if options.secondary_class == 'random':
	    options.secondary_class = SecondaryClass(random.choice([clas for clas in classes if clas != options.main_class]))
	    
	if options.main_class == options.secondary_class:
	    raise_yaml_error(world.player, "You cannot have the same class selected for main_class and secondary_class")

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Atlyss YAML ERROR ===\nAtlyss: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')