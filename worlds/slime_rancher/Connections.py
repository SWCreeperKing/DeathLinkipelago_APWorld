zones = [
	"The Lab",
	"The Overgrowth",
	"The Grotto",
	"Dry Reef",
	"Indigo Quarry",
	"Moss Blanket",
	"Ancient Ruins Transition",
	"Ancient Ruins",
	"Glass Desert",
	# "The Slime Sea",
]

backwards_connections = {
	"The Lab": ["The Ranch"],
	"The Overgrowth": ["The Ranch"],
	"The Grotto": ["The Ranch"],
	"Dry Reef": ["The Ranch"],
	"Indigo Quarry": ["Dry Reef"],
	"Moss Blanket": ["Dry Reef"],
	"Ancient Ruins Transition": ["Indigo Quarry", "Moss Blanket"],
	"Ancient Ruins": ["Ancient Ruins Transition"],
	"Glass Desert": ["Ancient Ruins"],
}