zones = [
	"The Lab",
	"The Overgrowth",
	"The Grotto",
	"Dry Reef",
	"Indigo Quarry",
	"Moss Blanket",
	"Ruins Transition",
	"Ruins",
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
	"Ruins Transition": ["Indigo Quarry", "Moss Blanket"],
	"Ruins": ["Ruins Transition"],
	"Glass Desert": ["Ruins"],
}