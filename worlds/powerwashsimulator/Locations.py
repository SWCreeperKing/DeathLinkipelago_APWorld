land_vehicles = [
    "Van",
    "Vintage Car",
    "Grandpa Miller's Car",
    "Fire Truck",
    "Dirt Bike",
    "Penny Farthing",
    "Recreation Vehicle",
    "Golf Cart",
    "Motorbike and Sidecar",
    "SUV",
    "Drill",
    "Monster Truck",
]

water_vehicles = [
    "Frolic Boat",
    "Fishing Boat",
]

air_vehicles = [
    "Fire Helicopter",
    "Private Jet",
    "Stunt Plane",
    "Recreational Vehicle (Again)",
]

places = [
    "Back Garden",
    "Bungalow",
    "Playground",
    "Detached House",
    "Shoe House",
    "Fire Station",
    "Skatepark",
    "Forest Cottage",
    "Mayor's Mansion",
    "Carousel",
    "Tree House",
    "Temple",
    "Washroom",
    "Helter Skelter",
    "Ferris Wheel",
    "Subway Platform",
    "Fortune Teller's Wagon",
    "Ancient Statue",
    "Ancient Monument",
    "Lost City Palace",
]

raw_location_dict = land_vehicles + water_vehicles + air_vehicles + places

# work smarter, not harder
addendums = [f"{num * 2}0%" for num in range(1, 6)]
locations_percentages = {location: [f"{location} {addendum}" for addendum in addendums] for location in raw_location_dict}
location_dict = [location for _, percentages in locations_percentages.items() for location in percentages]
