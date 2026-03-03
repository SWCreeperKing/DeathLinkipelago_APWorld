from dataclasses import dataclass
from Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

class Bacteria(DefaultOnToggle):
	"""
	Allow the disease as an item in the multiworld
	"""
	display_name = "Bacteria"


class Virus(Toggle):
	"""
	Allow the disease as an item in the multiworld
	"""
	display_name = "Virus"


class Fungus(Toggle):
	"""
	Allow the disease as an item in the multiworld
	"""
	display_name = "Fungus"


class Parasite(Toggle):
	"""
	Allow the disease as an item in the multiworld
	"""
	display_name = "Parasite"


class Prion(Toggle):
	"""
	Allow the disease as an item in the multiworld
	"""
	display_name = "Prion"


class NanoVirus(Toggle):
	"""
	Allow the disease as an item in the multiworld
	"""
	display_name = "Nano Virus"


class BioWeapon(Toggle):
	"""
	Allow the disease as an item in the multiworld
	"""
	display_name = "Bio Weapon"


class NormalDifficulty(Toggle):
	"""
	Allow the difficulty as an item in the multiworld
	"""
	display_name = "Normal Difficulty"


@dataclass
class PlagueIncOptions(PerGameCommonOptions):
	bacteria: Bacteria
	virus: Virus
	fungus: Fungus
	parasite: Parasite
	prion: Prion
	nano_virus: NanoVirus
	bio_weapon: BioWeapon
	normal_difficulty: NormalDifficulty


def check_options(world):
	options = world.options
	random = world.random
	settings = world.settings
	difs = [item for item in [options.normal_difficulty] if item]
	diseases = [item for item in [options.bacteria, options.virus, options.fungus, options.parasite, options.prion, options.nano_virus, options.bio_weapon] if item]
	dif_count = len(difs)
	disease_count = len(diseases)
	if dif_count < 1:
		raise_yaml_error(world.player, "You must have at least 1 difficulty enabled")
	else:
		world.starting_diff = random.choice(difs).display_name.replace(" Difficulty", "")
	if disease_count < 1:
		raise_yaml_error(world.player, "You must have at least 1 disease enabled")
	else:
		world.starting_disease = random.choice(diseases).display_name
	world.victories_needed = dif_count * disease_count

def raise_yaml_error(player_name, error):
	raise OptionError(f'\n\n=== Plague Inc YAML ERROR ===\nPlague Inc: {player_name} {error}, PLEASE FIX YOUR YAML\n\n')