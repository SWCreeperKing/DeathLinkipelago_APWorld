from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

always_tech = [
	"Bird 1",
	"Rodent 1",
	"Livestock 1",
	"Air 1",
	"Water 1",
	"Insect 1",
	"Blood 1"
]

tech_items = [
	"Nausea",
	"Coughing",
	"Rash",
	"Insomnia",
	"Cysts",
	"Anaemia",
	"Vomiting",
	"Pneumonia",
	"Sneezing",
	"Sweating",
	"Paranoia",
	"Hyper sensitivity",
	"Abscesses",
	"Haemophilia",
	"Pulmonary Oedema",
	"Fever",
	"Inflammation",
	"Tumours",
	"Diarrhoea",
	"Pulmonary Fibrosis",
	"Immune Suppression",
	"Skin Lesions",
	"Seizures",
	"Paralysis",
	"Systemic Infection",
	"Internal Haemorrhaging",
	"Dysentery",
	"Insanity",
	"Necrosis",
	"Hemorrhagic Shock",
	"Coma",
	"Total Organ Failure",
	"Bird 2",
	"Rodent 2",
	"Livestock 2",
	"Extreme Zoonosis",
	"Air 2",
	"Water 2",
	"Extreme Bioaerosol",
	"Insect 2",
	"Blood 2",
	"Extreme Hematophagy",
	"Cold Resistance 1",
	"Cold Resistance 2",
	"Heat Resistance 1",
	"Heat Resistance 2",
	"Environmental Hardening",
	"Bacterial Resilience 1",
	"Bacterial Resilience 2",
	"Bacterial Resilience 3",
	"Drug Resistance 1",
	"Drug Resistance 2",
	"Genetic Hardening 1",
	"Genetic Hardening 2",
	"Genetic ReShuffle 1",
	"Genetic ReShuffle 2",
	"Genetic ReShuffle 3"
]

difficulties = [
	"Normal"
]

diseases = [
	"Bacteria",
	"Virus",
	"Fungus",
	"Parasite",
	"Prion",
	"Nano Virus",
	"Bio Weapon"
]

item_table = {
	**{item: ItemClassification.progression for item in always_tech},
	**{item: ItemClassification.progression for item in tech_items},
	**{item: ItemClassification.progression for item in difficulties},
	**{item: ItemClassification.progression for item in diseases},
	"A Sickly Sensation": ItemClassification.filler
}

raw_items = [item for item, classification in item_table.items()]

def gen_create_items(world):
	pool = world.multiworld.itempool
	options = world.options
	for item in tech_items:
		world.location_count -= 1
		pool.append(world.create_item(item))
	if options.normal_difficulty and world.starting_diff != "Normal":
		world.location_count -= 1
		pool.append(world.create_item("Normal"))
	if options.bacteria and world.starting_disease != "Bacteria":
		world.location_count -= 1
		pool.append(world.create_item("Bacteria"))
	if options.virus and world.starting_disease != "Virus":
		world.location_count -= 1
		pool.append(world.create_item("Virus"))
	if options.fungus and world.starting_disease != "Fungus":
		world.location_count -= 1
		pool.append(world.create_item("Fungus"))
	if options.parasite and world.starting_disease != "Parasite":
		world.location_count -= 1
		pool.append(world.create_item("Parasite"))
	if options.prion and world.starting_disease != "Prion":
		world.location_count -= 1
		pool.append(world.create_item("Prion"))
	if options.nano_virus and world.starting_disease != "Nano Virus":
		world.location_count -= 1
		pool.append(world.create_item("Nano Virus"))
	if options.bio_weapon and world.starting_disease != "Bio Weapon":
		world.location_count -= 1
		pool.append(world.create_item("Bio Weapon"))
	for _ in range(world.location_count):
		pool.append(world.create_item("A Sickly Sensation"))