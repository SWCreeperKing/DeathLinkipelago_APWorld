from BaseClasses import ItemClassification
from .Locations import *
from .Options import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

always_tech = [
	"Air 1",
	"Bird 1",
	"Blood 1",
	"Insect 1",
	"Livestock 1",
	"Rodent 1",
	"Water 1"
]

tech_items = [
	"Bacterial Resilience 1",
	"Bacterial Resilience 2",
	"Bacterial Resilience 3",
	"Abscesses",
	"Air 2",
	"Anaemia",
	"Bird 2",
	"Blood 2",
	"Cold Resistance 1",
	"Cold Resistance 2",
	"Coma",
	"Coughing",
	"Cysts",
	"Diarrhoea",
	"Drug Resistance 1",
	"Drug Resistance 2",
	"Dysentery",
	"Environmental Hardening",
	"Extreme Bioaerosol",
	"Extreme Hematophagy",
	"Extreme Zoonosis",
	"Fever",
	"Genetic Hardening 1",
	"Genetic Hardening 2",
	"Genetic ReShuffle 1",
	"Genetic ReShuffle 2",
	"Genetic ReShuffle 3",
	"Haemophilia",
	"Heat Resistance 1",
	"Heat Resistance 2",
	"Hemorrhagic Shock",
	"Hyper sensitivity",
	"Immune Suppression",
	"Inflammation",
	"Insanity",
	"Insect 2",
	"Insomnia",
	"Internal Haemorrhaging",
	"Livestock 2",
	"Nausea",
	"Necrosis",
	"Paralysis",
	"Paranoia",
	"Pneumonia",
	"Pulmonary Fibrosis",
	"Pulmonary Oedema",
	"Rash",
	"Rodent 2",
	"Seizures",
	"Skin Lesions",
	"Sneezing",
	"Sweating",
	"Systemic Infection",
	"Total Organ Failure",
	"Tumours",
	"Vomiting",
	"Water 2",
	"Deactivate modified genes 1",
	"Deactivate modified genes 2",
	"Deactivate modified genes 3",
	"Gene Compression 1",
	"Gene Compression 2",
	"Gene Compression 3",
	"Neucleic Acid Neutralisation 1",
	"Neucleic Acid Neutralisation 2",
	"Neucleic Acid Neutralisation 3",
	"Unlock Annihilate gene",
	"Broadcast Interceptor overload",
	"Code fragment interception",
	"Code segment interception",
	"Drug immunity",
	"Encryption breached",
	"Kill Switch stasis",
	"Radical elements stabilised",
	"Replication Factory overload",
	"Symbiosis 1",
	"Symbiosis 2",
	"Symbiosis 3",
	"Neural Atrophy 1",
	"Neural Atrophy 2",
	"Neural Atrophy 3",
	"Viral Instability 1",
	"Viral Instability 2",
	"Viral Instability 3"
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