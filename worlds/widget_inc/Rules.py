import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/Widgitpelago/blob/master/Widgitpelago/Archipelago/ApShenanigans.cs]

def get_rule_map(player):
	return {
		"Tier 1": lambda state: has_tier(state, player, 0),
		"Tier 1 Mastery": lambda state: basic_widget(state, player) and has_tier(state, player, 1),
		"Deconstruct": lambda state: basic_widget(state, player) and has_tier(state, player, 1),
		"Frame Relocation": lambda state: has_frame(state, player, 'Deconstruct') and basic_widget(state, player) and has_tier(state, player, 1),
		"Iron Mine": lambda state: has_tier(state, player, 1),
		"Efficient Extraction": lambda state: has_frame(state, player, 'Iron Mine') and basic_widget(state, player) and has_tier(state, player, 1),
		"Iron Smelter": lambda state: has_frame(state, player, 'Iron Mine') and has_tier(state, player, 1),
		"Furnace Optimizer": lambda state: has_frame(state, player, 'Iron Smelter') and basic_widget(state, player) and has_tier(state, player, 1),
		"Superheated Crucible (Iron Ingot)": lambda state: has_frame(state, player, 'Iron Smelter') and basic_widget(state, player) and has_tier(state, player, 1),
		"Widget Factory": lambda state: has_frame(state, player, 'Iron Smelter') and iron_ingot(state, player) and has_tier(state, player, 1),
		"Optimized Materials": lambda state: has_frame(state, player, 'Widget Factory') and basic_widget(state, player) and has_tier(state, player, 1),
		"Rapid Assembly": lambda state: has_frame(state, player, 'Widget Factory') and basic_widget(state, player) and has_tier(state, player, 1),
		"Glitched Frame": lambda state: has_frame(state, player, 'Widget Factory') and basic_widget(state, player) and has_tier(state, player, 1),
		"Fortress": lambda state: has_frame(state, player, 'Widget Factory') and basic_widget(state, player) and has_tier(state, player, 1),
		"Dig Site": lambda state: has_frame(state, player, 'Widget Factory') and basic_widget(state, player) and has_tier(state, player, 1),
		"Tier 2": lambda state: basic_widget(state, player) and has_tier(state, player, 1),
		"Tier 2 Mastery": lambda state: spinning_widget(state, player) and has_tier(state, player, 2),
		"Warehouse": lambda state: spinning_widget(state, player) and has_tier(state, player, 2),
		"Sand Pit": lambda state: basic_widget(state, player) and has_tier(state, player, 2),
		"Mechanized Shovels": lambda state: has_frame(state, player, 'Sand Pit') and spinning_widget(state, player) and has_tier(state, player, 2),
		"Glass Kiln": lambda state: has_frame(state, player, 'Sand Pit') and basic_widget(state, player) and has_tier(state, player, 2),
		"Kiln Governor": lambda state: has_frame(state, player, 'Glass Kiln') and spinning_widget(state, player) and has_tier(state, player, 2),
		"Gyroscope Fabricator": lambda state: has_frame(state, player, 'Glass Kiln') and basic_widget(state, player) and has_tier(state, player, 2),
		"Widget Spinner": lambda state: has_frame(state, player, 'Gyroscope Fabricator') and basic_widget(state, player) and has_tier(state, player, 2),
		"Spin Stabilizer": lambda state: has_frame(state, player, 'Widget Spinner') and spinning_widget(state, player) and has_tier(state, player, 2),
		"Gyroscopic Array": lambda state: has_frame(state, player, 'Widget Spinner') and spinning_widget(state, player) and has_tier(state, player, 2),
		"Iron-rich Rocks": lambda state: has_frame(state, player, 'Iron Mine') and spinning_widget(state, player) and has_tier(state, player, 2),
		"Efficient Loader Arms": lambda state: has_frame(state, player, 'Iron Smelter') and spinning_widget(state, player) and has_tier(state, player, 2),
		"High Heat Density": lambda state: has_frame(state, player, 'Iron Smelter') and spinning_widget(state, player) and has_tier(state, player, 2),
		"Widget Twins": lambda state: has_frame(state, player, 'Optimized Materials') and spinning_widget(state, player) and has_tier(state, player, 2),
		"Warped Speed": lambda state: has_frame(state, player, 'Glitched Frame') and spinning_widget(state, player) and has_tier(state, player, 2),
		"Tier 3": lambda state: spinning_widget(state, player) and has_tier(state, player, 2),
		"Construction Overview": lambda state: capacitor_widget(state, player) and has_tier(state, player, 3),
		"Pause Construction": lambda state: has_frame(state, player, 'Construction Overview') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Cancel All Construction": lambda state: has_frame(state, player, 'Pause Construction') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Tier 3 Mastery": lambda state: capacitor_widget(state, player) and has_tier(state, player, 3),
		"Eminent Domain": lambda state: capacitor_widget(state, player) and has_tier(state, player, 3),
		"Clone Layout": lambda state: has_frame(state, player, 'Eminent Domain') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Area Move": lambda state: has_frame(state, player, 'Clone Layout') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Oil Field": lambda state: spinning_widget(state, player) and has_tier(state, player, 3),
		"Autopressurizer": lambda state: has_frame(state, player, 'Oil Field') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Black Gold": lambda state: has_frame(state, player, 'Oil Field') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Oil Power Plant": lambda state: has_frame(state, player, 'Oil Field') and spinning_widget(state, player) and has_tier(state, player, 3),
		"Flame Stack": lambda state: has_frame(state, player, 'Oil Power Plant') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Battery Assembler": lambda state: has_frame(state, player, 'Oil Power Plant') and spinning_widget(state, player) and has_tier(state, player, 3),
		"Superjuiced Upcharger": lambda state: has_frame(state, player, 'Battery Assembler') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Capacitor Bank": lambda state: has_frame(state, player, 'Battery Assembler') and spinning_widget(state, player) and has_tier(state, player, 3),
		"Substable Wiring": lambda state: has_frame(state, player, 'Capacitor Bank') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Supercharged Array": lambda state: has_frame(state, player, 'Capacitor Bank') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Logistics Hub": lambda state: has_frame(state, player, 'Capacitor Bank') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Coordinated Logistics": lambda state: has_frame(state, player, 'Logistics Hub') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Napalm Charge": lambda state: has_frame(state, player, 'Logistics Hub') and oil(state, player) and has_tier(state, player, 3),
		"Beach Harvest": lambda state: has_frame(state, player, 'Sand Pit') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Molten Conveyor System": lambda state: has_frame(state, player, 'Kiln Governor') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Superheated Crucible (Glass)": lambda state: has_frame(state, player, 'Glass Kiln') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Glass Ball Bearings": lambda state: has_frame(state, player, 'Gyroscope Fabricator') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Core Drilling": lambda state: has_frame(state, player, 'Efficient Extraction') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Ultra-Fast Widget Synthesizer": lambda state: has_frame(state, player, 'Rapid Assembly') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Careful Study": lambda state: has_frame(state, player, 'Dig Site') and capacitor_widget(state, player) and has_tier(state, player, 3),
		"Tier 4": lambda state: capacitor_widget(state, player) and has_tier(state, player, 3),
		"Eagle Eye": lambda state: computational_widget(state, player) and has_tier(state, player, 4),
		"Discerning Vision": lambda state: has_frame(state, player, 'Eagle Eye') and computational_widget(state, player) and has_tier(state, player, 4),
		"Tier 4 Mastery": lambda state: computational_widget(state, player) and has_tier(state, player, 4),
		"Long Distance Upgrades": lambda state: computational_widget(state, player) and has_tier(state, player, 4),
		"Upgrade Status": lambda state: has_frame(state, player, 'Long Distance Upgrades') and computational_widget(state, player) and has_tier(state, player, 4),
		"Copper Mine": lambda state: capacitor_widget(state, player) and has_tier(state, player, 4),
		"Turbo Drill Motors": lambda state: has_frame(state, player, 'Copper Mine') and computational_widget(state, player) and has_tier(state, player, 4),
		"Copper Forge": lambda state: has_frame(state, player, 'Copper Mine') and capacitor_widget(state, player) and has_tier(state, player, 4),
		"Forge Attendant": lambda state: has_frame(state, player, 'Copper Forge') and computational_widget(state, player) and has_tier(state, player, 4),
		"Rapid Heat Induction Coils": lambda state: has_frame(state, player, 'Copper Forge') and computational_widget(state, player) and has_tier(state, player, 4),
		"Plastic Extractor": lambda state: has_frame(state, player, 'Copper Forge') and capacitor_widget(state, player) and has_tier(state, player, 4),
		"Enhanced Chemical Mixer": lambda state: has_frame(state, player, 'Plastic Extractor') and computational_widget(state, player) and has_tier(state, player, 4),
		"Circuit Fab": lambda state: has_frame(state, player, 'Plastic Extractor') and capacitor_widget(state, player) and has_tier(state, player, 4),
		"Computational Engine": lambda state: has_frame(state, player, 'Circuit Fab') and capacitor_widget(state, player) and has_tier(state, player, 4),
		"Enhanced Logic Synthesizer": lambda state: has_frame(state, player, 'Computational Engine') and computational_widget(state, player) and has_tier(state, player, 4),
		"Rapid Component Feeder": lambda state: has_frame(state, player, 'Computational Engine') and computational_widget(state, player) and has_tier(state, player, 4),
		"Peat Oil Processing": lambda state: has_frame(state, player, 'Autopressurizer') and computational_widget(state, player) and has_tier(state, player, 4),
		"Power Plant Logistics": lambda state: has_frame(state, player, 'Oil Power Plant') and computational_widget(state, player) and has_tier(state, player, 4),
		"High Yield Compressor": lambda state: has_frame(state, player, 'Flame Stack') and computational_widget(state, player) and has_tier(state, player, 4),
		"Depletion Recycler": lambda state: has_frame(state, player, 'Battery Assembler') and computational_widget(state, player) and has_tier(state, player, 4),
		"Expanded Shelf Storage": lambda state: has_frame(state, player, 'Warehouse') and computational_widget(state, player) and has_tier(state, player, 4),
		"Bucket Excavator": lambda state: has_frame(state, player, 'Mechanized Shovels') and computational_widget(state, player) and has_tier(state, player, 4),
		"Glass Shard Recombinator": lambda state: has_frame(state, player, 'Glass Kiln') and computational_widget(state, player) and has_tier(state, player, 4),
		"Direct Glass Insertion": lambda state: has_frame(state, player, 'Gyroscope Fabricator') and computational_widget(state, player) and has_tier(state, player, 4),
		"Tuned Spinners": lambda state: has_frame(state, player, 'Gyroscopic Array') and computational_widget(state, player) and has_tier(state, player, 4),
		"Glass Grinding Wheel": lambda state: has_frame(state, player, 'Gyroscopic Array') and computational_widget(state, player) and has_tier(state, player, 4),
		"Industrial Capacity": lambda state: has_frame(state, player, 'Furnace Optimizer') and computational_widget(state, player) and has_tier(state, player, 4),
		"Precision Widgeteering": lambda state: has_frame(state, player, 'Optimized Materials') and computational_widget(state, player) and has_tier(state, player, 4),
		"Unnatural Duplication": lambda state: has_frame(state, player, 'Warped Speed') and computational_widget(state, player) and has_tier(state, player, 4),
		"Tier 5": lambda state: computational_widget(state, player) and has_tier(state, player, 4),
		"Tier 5 Mastery": lambda state: integrated_widget(state, player) and has_tier(state, player, 5),
		"Tesla Coil": lambda state: computational_widget(state, player) and has_tier(state, player, 5),
		"Rapid Charge Collector": lambda state: has_frame(state, player, 'Tesla Coil') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Core Foundry": lambda state: has_frame(state, player, 'Tesla Coil') and computational_widget(state, player) and has_tier(state, player, 5),
		"Rudimentary Synapse Connector": lambda state: has_frame(state, player, 'Tesla Coil') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Integrator": lambda state: has_frame(state, player, 'Core Foundry') and computational_widget(state, player) and has_tier(state, player, 5),
		"Synapse Fusion Unit": lambda state: has_frame(state, player, 'Integrator') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Rapid Coupler": lambda state: has_frame(state, player, 'Integrator') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Recycler": lambda state: has_frame(state, player, 'Integrator') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Rubble Grinder": lambda state: has_frame(state, player, 'Recycler') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Excavator": lambda state: has_frame(state, player, 'Recycler') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Giant Rock Crusher": lambda state: has_frame(state, player, 'Copper Mine') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Advanced Alloy Mixer": lambda state: has_frame(state, player, 'Copper Forge') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Slash And Burn": lambda state: has_frame(state, player, 'Rapid Heat Induction Coils') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Hyper-Speed Assembly Line": lambda state: has_frame(state, player, 'Circuit Fab') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Auxiliary Pump Stack": lambda state: has_frame(state, player, 'Black Gold') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Heat Recirculator": lambda state: has_frame(state, player, 'High Yield Compressor') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Hydrophobia": lambda state: has_frame(state, player, 'Battery Assembler') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Dedicated Battery Inserters": lambda state: has_frame(state, player, 'Substable Wiring') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Rapid Discharge Fabricator": lambda state: has_frame(state, player, 'Supercharged Array') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Optimized Supply Lines": lambda state: has_frame(state, player, 'Logistics Hub') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Perfectly Balanced Spinner": lambda state: has_frame(state, player, 'Glass Ball Bearings') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Gyroscope Sharing Plan": lambda state: has_frame(state, player, 'Spin Stabilizer') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Dig Deeper": lambda state: has_frame(state, player, 'Core Drilling') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Turbo Blast Furnace": lambda state: has_frame(state, player, 'Superheated Crucible (Iron Ingot)') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Omni-Assembler Core": lambda state: has_frame(state, player, 'Ultra-Fast Widget Synthesizer') and integrated_widget(state, player) and has_tier(state, player, 5),
		"Tier 6": lambda state: integrated_widget(state, player) and has_tier(state, player, 5),
		"Tier 6 Mastery": lambda state: mainframe_widget(state, player) and has_tier(state, player, 6),
		"The Factory Must Grow": lambda state: mainframe_widget(state, player) and has_tier(state, player, 6),
		"Silicon Extruder": lambda state: integrated_widget(state, player) and has_tier(state, player, 6),
		"Swift Wafer Synthesizer": lambda state: has_frame(state, player, 'Silicon Extruder') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Processor Lab": lambda state: has_frame(state, player, 'Silicon Extruder') and integrated_widget(state, player) and has_tier(state, player, 6),
		"Extreme-UV Protocol": lambda state: has_frame(state, player, 'Processor Lab') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Mainframe Assembler": lambda state: has_frame(state, player, 'Processor Lab') and integrated_widget(state, player) and has_tier(state, player, 6),
		"Enhanced Data Synthesizer": lambda state: has_frame(state, player, 'Mainframe Assembler') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Rapid Circuit Integrator": lambda state: has_frame(state, player, 'Mainframe Assembler') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Indentured Servitude": lambda state: has_frame(state, player, 'Mainframe Assembler') and integrated_widget(state, player) and has_tier(state, player, 6),
		"Graveyard": lambda state: has_frame(state, player, 'Indentured Servitude') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Chain Lightning": lambda state: has_frame(state, player, 'Tesla Coil') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Efficient Neural Matrix": lambda state: has_frame(state, player, 'Core Foundry') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Introvert": lambda state: has_frame(state, player, 'Core Foundry') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Reclaim Sorting System": lambda state: has_frame(state, player, 'Rubble Grinder') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Hyper-Speed Conveyor System": lambda state: has_frame(state, player, 'Turbo Drill Motors') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Shortened Transfer Tube": lambda state: has_frame(state, player, 'Plastic Extractor') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Advanced Refining Chamber": lambda state: has_frame(state, player, 'Enhanced Chemical Mixer') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Precision Assembly Matrix": lambda state: has_frame(state, player, 'Circuit Fab') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Agoraphobia": lambda state: has_frame(state, player, 'Circuit Fab') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Standalone": lambda state: has_frame(state, player, 'Enhanced Logic Synthesizer') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Accelerated Component Placement": lambda state: has_frame(state, player, 'Rapid Component Feeder') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Exhaust Vent Recycler": lambda state: has_frame(state, player, 'Heat Recirculator') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Rapid Heat Exchanger (Battery)": lambda state: has_frame(state, player, 'Superjuiced Upcharger') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Energy Optimization Core": lambda state: has_frame(state, player, 'Substable Wiring') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Warehouse Shelf Stacker": lambda state: has_frame(state, player, 'Expanded Shelf Storage') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Grain Matrix Duplicator": lambda state: has_frame(state, player, 'Bucket Excavator') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Rapid Heat Exchanger (Glass)": lambda state: has_frame(state, player, 'Superheated Crucible (Glass)') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Counterspin Anchors": lambda state: has_frame(state, player, 'Tuned Spinners') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Double-stacked Conveyors": lambda state: has_frame(state, player, 'Efficient Loader Arms') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Productivity Optimization Node": lambda state: has_frame(state, player, 'Precision Widgeteering') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Dutiful Archivist": lambda state: has_frame(state, player, 'Careful Study') and mainframe_widget(state, player) and has_tier(state, player, 6),
		"Tier 7": lambda state: mainframe_widget(state, player) and has_tier(state, player, 6),
		"Tier 7 Mastery": lambda state: cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Auto Upgrade": lambda state: cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Uranium Mine": lambda state: mainframe_widget(state, player) and has_tier(state, player, 7),
		"Rapid Extraction Module": lambda state: has_frame(state, player, 'Uranium Mine') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Fuel Rod Assembler": lambda state: has_frame(state, player, 'Uranium Mine') and mainframe_widget(state, player) and has_tier(state, player, 7),
		"Accelerated Molding Unit": lambda state: has_frame(state, player, 'Fuel Rod Assembler') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Nuclear Power Plant": lambda state: has_frame(state, player, 'Fuel Rod Assembler') and mainframe_widget(state, player) and has_tier(state, player, 7),
		"Advanced Heat Exchanger": lambda state: has_frame(state, player, 'Nuclear Power Plant') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Cloud Digitizer": lambda state: has_frame(state, player, 'Nuclear Power Plant') and mainframe_widget(state, player) and has_tier(state, player, 7),
		"Multi-Core Upload System": lambda state: has_frame(state, player, 'Cloud Digitizer') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Swift Transfer Protocol": lambda state: has_frame(state, player, 'Cloud Digitizer') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Monocrystalline": lambda state: has_frame(state, player, 'Silicon Extruder') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Microfine Engraving": lambda state: has_frame(state, player, 'Processor Lab') and cloud_widget(state, player) and has_tier(state, player, 7),
		"Automated Chapel": lambda state: has_frame(state, player, 'Graveyard') and cloud_widget(state, player) and has_tier(state, player, 7),
		"Multi-Bolt Capture Array": lambda state: has_frame(state, player, 'Rapid Charge Collector') and cloud_widget(state, player) and has_tier(state, player, 7),
		"Lightning Interface": lambda state: has_frame(state, player, 'Rapid Coupler') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Extrovert": lambda state: has_frame(state, player, 'Rapid Coupler') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Autonomous Garbage Collectors": lambda state: has_frame(state, player, 'Reclaim Sorting System') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Autosifter": lambda state: has_frame(state, player, 'Excavator') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Dense Packing Grid": lambda state: has_frame(state, player, 'Forge Attendant') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Advanced Circuit Optimization": lambda state: has_frame(state, player, 'Enhanced Logic Synthesizer') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Pipe Repressurizer": lambda state: has_frame(state, player, 'Auxiliary Pump Stack') and cloud_widget(state, player) and has_tier(state, player, 7),
		"Instantaneous Charge Module": lambda state: has_frame(state, player, 'Rapid Discharge Fabricator') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Lightspeed Rotation": lambda state: has_frame(state, player, 'Gyroscope Fabricator') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Calculated Material Distribution": lambda state: has_frame(state, player, 'Gyroscope Sharing Plan') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Uranium-powered Drills": lambda state: has_frame(state, player, 'Dig Deeper') and cloud_widget(state, player) and fuel_rod(state, player) and has_tier(state, player, 7),
		"Infinite Widget Matrix": lambda state: has_frame(state, player, 'Omni-Assembler Core') and cloud_widget(state, player) and has_tier(state, player, 7),
		"Tier 8": lambda state: cloud_widget(state, player) and has_tier(state, player, 7),
		"Tier 8 Mastery": lambda state: quantum_widget(state, player) and has_tier(state, player, 8),
		"Widget Minitizers": lambda state: cloud_widget(state, player) and has_tier(state, player, 8),
		"Enhanced Particle Compressor": lambda state: has_frame(state, player, 'Widget Minitizers') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Quantum Shrink Matrix": lambda state: has_frame(state, player, 'Enhanced Particle Compressor') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Nanoscale Lab": lambda state: has_frame(state, player, 'Widget Minitizers') and cloud_widget(state, player) and has_tier(state, player, 8),
		"Quantum Lithography": lambda state: has_frame(state, player, 'Nanoscale Lab') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Reactor Foundry": lambda state: has_frame(state, player, 'Nanoscale Lab') and cloud_widget(state, player) and has_tier(state, player, 8),
		"Subatomic Power Booster": lambda state: has_frame(state, player, 'Reactor Foundry') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Quantum Tunneler": lambda state: has_frame(state, player, 'Reactor Foundry') and cloud_widget(state, player) and has_tier(state, player, 8),
		"High-Efficiency Particle Matrix": lambda state: has_frame(state, player, 'Quantum Tunneler') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Rapid Particle Integrator": lambda state: has_frame(state, player, 'Quantum Tunneler') and quantum_widget(state, player) and has_tier(state, player, 8),
		"City Builder": lambda state: has_frame(state, player, 'Rapid Particle Integrator') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Blitz Upgrade": lambda state: has_frame(state, player, 'Auto Upgrade') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Fallout": lambda state: has_frame(state, player, 'Uranium Mine') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Multi-Stage Refinement": lambda state: has_frame(state, player, 'Fuel Rod Assembler') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Green Energy": lambda state: has_frame(state, player, 'Fuel Rod Assembler') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Precision Control Rods": lambda state: has_frame(state, player, 'Advanced Heat Exchanger') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Rapid Crystal Formation Chamber": lambda state: has_frame(state, player, 'Swift Wafer Synthesizer') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Suburban Development": lambda state: has_frame(state, player, 'Processor Lab') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Binary Pairs": lambda state: has_frame(state, player, 'Enhanced Data Synthesizer') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Hyper-Speed Compiler": lambda state: has_frame(state, player, 'Rapid Circuit Integrator') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Efficient Value Extraction": lambda state: has_frame(state, player, 'Indentured Servitude') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Rapid Cognitive Assembler": lambda state: has_frame(state, player, 'Rudimentary Synapse Connector') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Quantum Logic Synthesizer": lambda state: has_frame(state, player, 'Synapse Fusion Unit') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Universal Recycling Schema": lambda state: has_frame(state, player, 'Autonomous Garbage Collectors') and quantum_widget(state, player) and has_tier(state, player, 8),
		"High-Yield Extraction System": lambda state: has_frame(state, player, 'Hyper-Speed Conveyor System') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Quantum Heat Exchanger": lambda state: has_frame(state, player, 'Slash And Burn') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Yield Optimization Catalyst": lambda state: has_frame(state, player, 'Advanced Refining Chamber') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Turbo Soldering Station": lambda state: has_frame(state, player, 'Hyper-Speed Assembly Line') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Hyper-Speed Arithmetic Processor": lambda state: has_frame(state, player, 'Accelerated Component Placement') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Monopole Battery Tech": lambda state: has_frame(state, player, 'Depletion Recycler') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Nano-Capacitor Synthesizer": lambda state: has_frame(state, player, 'Energy Optimization Core') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Lost Package Tracker": lambda state: has_frame(state, player, 'Optimized Supply Lines') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Extradimensional Storage Lockers": lambda state: has_frame(state, player, 'Warehouse Shelf Stacker') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Unified Theory of Sand": lambda state: has_frame(state, player, 'Grain Matrix Duplicator') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Hyperfine Glass Distributor": lambda state: has_frame(state, player, 'Glass Shard Recombinator') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Spacetime Spin Matrix": lambda state: has_frame(state, player, 'Counterspin Anchors') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Hyper-Production Matrix": lambda state: has_frame(state, player, 'Precision Widgeteering') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Mitosis": lambda state: has_frame(state, player, 'Unnatural Duplication') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Boundless Patience": lambda state: has_frame(state, player, 'Dutiful Archivist') and quantum_widget(state, player) and has_tier(state, player, 8),
		"Tier 9": lambda state: quantum_widget(state, player) and has_tier(state, player, 8),
		"Tier 9 Mastery": lambda state: unshackled_widget(state, player) and has_tier(state, player, 9),
		"New World Order": lambda state: unshackled_widget(state, player) and has_tier(state, player, 9),
		"Helium Extractor": lambda state: quantum_widget(state, player) and has_tier(state, player, 9),
		"Subatomic Yield Booster (Helium)": lambda state: has_frame(state, player, 'Helium Extractor') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Conductor Foundry": lambda state: has_frame(state, player, 'Helium Extractor') and quantum_widget(state, player) and has_tier(state, player, 9),
		"Lightning Flux Unit": lambda state: has_frame(state, player, 'Conductor Foundry') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"AI Laboratory": lambda state: has_frame(state, player, 'Conductor Foundry') and quantum_widget(state, player) and has_tier(state, player, 9),
		"Quantum Neural Matrix": lambda state: has_frame(state, player, 'AI Laboratory') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"AI Delimiter": lambda state: has_frame(state, player, 'AI Laboratory') and quantum_widget(state, player) and has_tier(state, player, 9),
		"Advanced Cognitive Network": lambda state: has_frame(state, player, 'AI Delimiter') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Neural Accelerator": lambda state: has_frame(state, player, 'AI Delimiter') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Direct Widget Insertion": lambda state: has_frame(state, player, 'Widget Minitizers') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Superconducting Collider Matrix": lambda state: has_frame(state, player, 'Quantum Shrink Matrix') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Precision Atom Placement": lambda state: has_frame(state, player, 'Nanoscale Lab') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Relics of the Past": lambda state: has_frame(state, player, 'Nanoscale Lab') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Rapid Core Integrator": lambda state: has_frame(state, player, 'Reactor Foundry') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Accelerated Entanglement": lambda state: has_frame(state, player, 'Rapid Particle Integrator') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Nuclear Bore Engine": lambda state: has_frame(state, player, 'Rapid Extraction Module') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Direct Core Cooling": lambda state: has_frame(state, player, 'Nuclear Power Plant') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Superconducting Fuel Chamber": lambda state: has_frame(state, player, 'Precision Control Rods') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Datacenter Access": lambda state: has_frame(state, player, 'Multi-Core Upload System') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Quantum Integration Matrix": lambda state: has_frame(state, player, 'Multi-Core Upload System') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Rapid Cloud Integrator": lambda state: has_frame(state, player, 'Swift Transfer Protocol') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Rapid Logic Preprocessor": lambda state: has_frame(state, player, 'Extreme-UV Protocol') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Multi-Core Processor": lambda state: has_frame(state, player, 'Enhanced Data Synthesizer') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Incinerator": lambda state: has_frame(state, player, 'Graveyard') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Turbo Lightning Rods": lambda state: has_frame(state, player, 'Multi-Bolt Capture Array') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Thought Integration Unit": lambda state: has_frame(state, player, 'Efficient Neural Matrix') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Ultra-Quick Integrator": lambda state: has_frame(state, player, 'Lightning Interface') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Automated Grading": lambda state: has_frame(state, player, 'Autosifter') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Ore-to-Ingot Optimization System": lambda state: has_frame(state, player, 'Advanced Alloy Mixer') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Quantum Circuitry Optimizer": lambda state: has_frame(state, player, 'Precision Assembly Matrix') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Multi-Tasking Calculation Node": lambda state: has_frame(state, player, 'Advanced Circuit Optimization') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Pressurized Storage Vats": lambda state: has_frame(state, player, 'Pipe Repressurizer') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Ultra-Fast Circuit Integrator": lambda state: has_frame(state, player, 'Instantaneous Charge Module') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Gyroscope Hyperprocessor": lambda state: has_frame(state, player, 'Lightspeed Rotation') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Excess Spin Utilizer": lambda state: has_frame(state, player, 'Gyroscope Sharing Plan') and unshackled_widget(state, player) and has_tier(state, player, 9),
		"Tier 10": lambda state: unshackled_widget(state, player) and has_tier(state, player, 9),
		"Tier 10 Mastery": lambda state: ascended_widget(state, player) and has_tier(state, player, 10),
		"Training Center": lambda state: unshackled_widget(state, player) and has_tier(state, player, 10),
		"Advanced Cognitive Compiler": lambda state: has_frame(state, player, 'Training Center') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Data Transformer": lambda state: has_frame(state, player, 'Training Center') and unshackled_widget(state, player) and has_tier(state, player, 10),
		"Expedite Ascension": lambda state: has_frame(state, player, 'Data Transformer') and unshackled_widget(state, player) and has_tier(state, player, 10),
		"Ascension Facility": lambda state: has_frame(state, player, 'Data Transformer') and unshackled_widget(state, player) and has_tier(state, player, 10),
		"Unleashed Thought Matrix": lambda state: has_frame(state, player, 'Ascension Facility') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Rapid Cognition Compiler": lambda state: has_frame(state, player, 'Ascension Facility') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Leveler": lambda state: has_frame(state, player, 'Ascension Facility') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Gaseous Bedrock": lambda state: has_frame(state, player, 'Helium Extractor') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Precision Gas Separator": lambda state: has_frame(state, player, 'Subatomic Yield Booster (Helium)') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Quantum Flux Matrix": lambda state: has_frame(state, player, 'Conductor Foundry') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Resource Management": lambda state: has_frame(state, player, 'Conductor Foundry') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Rapid AI Synthesizer": lambda state: has_frame(state, player, 'Quantum Neural Matrix') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Multi-Phase Logic Processor": lambda state: has_frame(state, player, 'Advanced Cognitive Network') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Upgraded AI Compiler": lambda state: has_frame(state, player, 'Neural Accelerator') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Subatomic Yield Booster (Widget Particle)": lambda state: has_frame(state, player, 'Superconducting Collider Matrix') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Industrial Espionage": lambda state: has_frame(state, player, 'Reactor Foundry') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Subatomic Yield Optimizer": lambda state: has_frame(state, player, 'High-Efficiency Particle Matrix') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Cowboy Coding": lambda state: has_frame(state, player, 'Quantum Tunneler') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Lightning Upgrade": lambda state: has_frame(state, player, 'Blitz Upgrade') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Rapid Rod Fabricator": lambda state: has_frame(state, player, 'Accelerated Molding Unit') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Quantum Efficiency Reactor": lambda state: has_frame(state, player, 'Superconducting Fuel Chamber') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Yield Maximization Reactor": lambda state: has_frame(state, player, 'Rapid Crystal Formation Chamber') and ascended_widget(state, player) and has_tier(state, player, 10),
		"N-Step Branch Prediction": lambda state: has_frame(state, player, 'Microfine Engraving') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Lightning Data Bus": lambda state: has_frame(state, player, 'Hyper-Speed Compiler') and ascended_widget(state, player) and has_tier(state, player, 10),
		"High Intensity Furnace": lambda state: has_frame(state, player, 'Incinerator') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Remnants of Humanity": lambda state: has_frame(state, player, 'Efficient Value Extraction') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Yield Maximization Protocol": lambda state: has_frame(state, player, 'Quantum Logic Synthesizer') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Advanced Mining Protocol": lambda state: has_frame(state, player, 'High-Yield Extraction System') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Rapid Refinement Module": lambda state: has_frame(state, player, 'Yield Optimization Catalyst') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Ultra-Quick Logic Compiler": lambda state: has_frame(state, player, 'Hyper-Speed Arithmetic Processor') and ascended_widget(state, player) and has_tier(state, player, 10),
		"High-Efficiency Capacitor Matrix": lambda state: has_frame(state, player, 'Energy Optimization Core') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Infinite Storage Glitch": lambda state: has_frame(state, player, 'Extradimensional Storage Lockers') and ascended_widget(state, player) and has_tier(state, player, 10),
		"Tier 11": lambda state: ascended_widget(state, player) and has_tier(state, player, 10),
		"Tier 11 Mastery": lambda state: sentient_widget(state, player) and has_tier(state, player, 11),
		"Absolute Dominion": lambda state: sentient_widget(state, player) and has_tier(state, player, 11),
		"Perpetual Motion Machine": lambda state: ascended_widget(state, player) and has_tier(state, player, 11),
		"Physics Engine Decoder": lambda state: has_frame(state, player, 'Perpetual Motion Machine') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Sentience Facility": lambda state: has_frame(state, player, 'Perpetual Motion Machine') and ascended_widget(state, player) and has_tier(state, player, 11),
		"Sentience Recombobulator": lambda state: has_frame(state, player, 'Sentience Facility') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Picoscale Lab": lambda state: has_frame(state, player, 'Sentience Facility') and ascended_widget(state, player) and has_tier(state, player, 11),
		"Enhanced Production Algorithms": lambda state: has_frame(state, player, 'Picoscale Lab') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Sentience Aggregator": lambda state: has_frame(state, player, 'Picoscale Lab') and ascended_widget(state, player) and has_tier(state, player, 11),
		"Processor Sharing System": lambda state: has_frame(state, player, 'Sentience Aggregator') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Thought Enhancer Matrix": lambda state: has_frame(state, player, 'Sentience Aggregator') and sentient_widget(state, player) and has_tier(state, player, 11),
		"History Lesson": lambda state: has_frame(state, player, 'Training Center') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Rapid Spec Synthesizer": lambda state: has_frame(state, player, 'Advanced Cognitive Compiler') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Advanced Cognitive Release": lambda state: has_frame(state, player, 'Data Transformer') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Wild Mutation": lambda state: has_frame(state, player, 'Data Transformer') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Advanced Neural Compiler": lambda state: has_frame(state, player, 'Unleashed Thought Matrix') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Frictionless Neural Compiler": lambda state: has_frame(state, player, 'Rapid Cognition Compiler') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Enhanced Helium Synthesizer": lambda state: has_frame(state, player, 'Precision Gas Separator') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Hyper-Speed Magnet Chamber": lambda state: has_frame(state, player, 'Lightning Flux Unit') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Hello World": lambda state: has_frame(state, player, 'AI Laboratory') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Optimized Neuron Compiler": lambda state: has_frame(state, player, 'Rapid AI Synthesizer') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Trinity": lambda state: has_frame(state, player, 'AI Delimiter') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Accelerated Thought Synthesizer": lambda state: has_frame(state, player, 'Upgraded AI Compiler') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Hyper-Accelerated Fabricator": lambda state: has_frame(state, player, 'Quantum Lithography') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Multi-Fuel Synthesizer": lambda state: has_frame(state, player, 'Subatomic Power Booster') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Stellar Quantum Weaver": lambda state: has_frame(state, player, 'Accelerated Entanglement') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Radiometric Ore Separator": lambda state: has_frame(state, player, 'Nuclear Bore Engine') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Isotope Yield Booster": lambda state: has_frame(state, player, 'Multi-Stage Refinement') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Data Yield Optimizer": lambda state: has_frame(state, player, 'Quantum Integration Matrix') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Hyper-Speed Data Link": lambda state: has_frame(state, player, 'Rapid Cloud Integrator') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Data Stream Optimizer": lambda state: has_frame(state, player, 'Multi-Core Processor') and sentient_widget(state, player) and has_tier(state, player, 11),
		"High-Capacity Energy Condenser": lambda state: has_frame(state, player, 'Turbo Lightning Rods') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Swift Logic Gate Fabricator": lambda state: has_frame(state, player, 'Ultra-Quick Integrator') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Pristine Protection Protocol": lambda state: has_frame(state, player, 'Automated Grading') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Advanced Arithmetic Processor": lambda state: has_frame(state, player, 'Advanced Circuit Optimization') and sentient_widget(state, player) and has_tier(state, player, 11),
		"Tier 12": lambda state: sentient_widget(state, player) and has_tier(state, player, 11),
		"Tier 12 Mastery": lambda state: omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Processor Lab": lambda state: sentient_widget(state, player) and has_tier(state, player, 12),
		"Omega Core Foundry": lambda state: has_frame(state, player, 'Omega Processor Lab') and sentient_widget(state, player) and has_tier(state, player, 12),
		"Rocket Electronics Lab": lambda state: has_frame(state, player, 'Omega Core Foundry') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Widget Distiller": lambda state: has_frame(state, player, 'Omega Core Foundry') and sentient_widget(state, player) and has_tier(state, player, 12),
		"Rocket Fuel Distiller": lambda state: has_frame(state, player, 'Omega Widget Distiller') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Casing Factory": lambda state: has_frame(state, player, 'Omega Widget Distiller') and sentient_widget(state, player) and has_tier(state, player, 12),
		"Omega Shielding Plant": lambda state: has_frame(state, player, 'Omega Casing Factory') and sentient_widget(state, player) and has_tier(state, player, 12),
		"Rocket Part Assembler": lambda state: has_frame(state, player, 'Omega Shielding Plant') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Project Assembler": lambda state: has_frame(state, player, 'Omega Shielding Plant') and sentient_widget(state, player) and has_tier(state, player, 12),
		"Omega Launch Facility": lambda state: has_frame(state, player, 'Omega Project Assembler') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Limit Break": lambda state: has_frame(state, player, 'Physics Engine Decoder') and omega_widget(state, player) and has_tier(state, player, 12),
		"Glitch in the System": lambda state: has_frame(state, player, 'Perpetual Motion Machine') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Thought Processor": lambda state: has_frame(state, player, 'Sentience Facility') and omega_widget(state, player) and has_tier(state, player, 12),
		"Myriad Landscape": lambda state: has_frame(state, player, 'Sentience Facility') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Yield Enhancer": lambda state: has_frame(state, player, 'Picoscale Lab') and omega_widget(state, player) and has_tier(state, player, 12),
		"Generational Uplift": lambda state: has_frame(state, player, 'Picoscale Lab') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Assembly Lab": lambda state: has_frame(state, player, 'Processor Sharing System') and omega_widget(state, player) and has_tier(state, player, 12),
		"Stepping Stone To Greatness": lambda state: has_frame(state, player, 'Sentience Aggregator') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Sentience Circuitry": lambda state: has_frame(state, player, 'Thought Enhancer Matrix') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Training Compiler": lambda state: has_frame(state, player, 'Rapid Spec Synthesizer') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Matrix Integrator": lambda state: has_frame(state, player, 'Expedite Ascension') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Cognitive Engine": lambda state: has_frame(state, player, 'Advanced Neural Compiler') and omega_widget(state, player) and has_tier(state, player, 12),
		"Beacon of Ascension": lambda state: has_frame(state, player, 'Ascension Facility') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Ascension Planner": lambda state: has_frame(state, player, 'Frictionless Neural Compiler') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Extraction Matrix": lambda state: has_frame(state, player, 'Enhanced Helium Synthesizer') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Magnetizer Unit": lambda state: has_frame(state, player, 'Quantum Flux Matrix') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Thought Conductor": lambda state: has_frame(state, player, 'Optimized Neuron Compiler') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Neural Matrix": lambda state: has_frame(state, player, 'Multi-Phase Logic Processor') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Etching System": lambda state: has_frame(state, player, 'Precision Atom Placement') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Containment Field": lambda state: has_frame(state, player, 'Rapid Core Integrator') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Entanglement Field": lambda state: has_frame(state, player, 'Subatomic Yield Optimizer') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Mining Protocol": lambda state: has_frame(state, player, 'Radiometric Ore Separator') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Cloud Synthesizer": lambda state: has_frame(state, player, 'Quantum Integration Matrix') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Accelerated Digitizer": lambda state: has_frame(state, player, 'Hyper-Speed Data Link') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Crystal Stabilizer": lambda state: has_frame(state, player, 'Yield Maximization Reactor') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Logic Amplifier": lambda state: has_frame(state, player, 'Multi-Core Processor') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Circuit Weaver": lambda state: has_frame(state, player, 'Lightning Data Bus') and omega_widget(state, player) and has_tier(state, player, 12),
		"Omega Assembly Core": lambda state: has_frame(state, player, 'Quantum Logic Synthesizer') and omega_widget(state, player) and has_tier(state, player, 12),
	}

def has_tier(state, player, tier) -> bool:
	return state.has("Progressive Tier", player, tier)

def has_frame(state, player, frame) -> bool:
	return state.has(frame, player, 1)

def iron_ore(state, player) -> bool:
	return has_frame(state, player, 'Iron Mine')

def sand(state, player) -> bool:
	return has_frame(state, player, 'Sand Pit')

def oil(state, player) -> bool:
	return has_frame(state, player, 'Oil Field')

def copper_ore(state, player) -> bool:
	return has_frame(state, player, 'Copper Mine')

def iron_ingot(state, player) -> bool:
	return iron_ore(state, player)

def basic_widget(state, player) -> bool:
	return iron_ingot(state, player)

def glass(state, player) -> bool:
	return sand(state, player)

def gyroscope(state, player) -> bool:
	return glass(state, player) and basic_widget(state, player)

def power(state, player) -> bool:
	return oil(state, player)

def spinning_widget(state, player) -> bool:
	return gyroscope(state, player) and basic_widget(state, player)

def battery(state, player) -> bool:
	return iron_ingot(state, player) and basic_widget(state, player) and power(state, player)

def capacitor_widget(state, player) -> bool:
	return spinning_widget(state, player) and battery(state, player)

def copper_ingot(state, player) -> bool:
	return copper_ore(state, player)

def plastic(state, player) -> bool:
	return oil(state, player)

def circuit_board(state, player) -> bool:
	return copper_ingot(state, player) and plastic(state, player)

def computational_widget(state, player) -> bool:
	return circuit_board(state, player) and capacitor_widget(state, player) and spinning_widget(state, player)

def bottled_lightning(state, player) -> bool:
	return glass(state, player) and power(state, player)

def thinking_core(state, player) -> bool:
	return capacitor_widget(state, player) and computational_widget(state, player)

def integrated_widget(state, player) -> bool:
	return bottled_lightning(state, player) and capacitor_widget(state, player) and thinking_core(state, player)

def silicon(state, player) -> bool:
	return sand(state, player) and power(state, player)

def microprocessors(state, player) -> bool:
	return silicon(state, player) and circuit_board(state, player) and thinking_core(state, player)

def mainframe_widget(state, player) -> bool:
	return microprocessors(state, player) and integrated_widget(state, player)

def uranium(state, player) -> bool:
	return power(state, player)

def fuel_rod(state, player) -> bool:
	return iron_ingot(state, player) and uranium(state, player) and power(state, player) and gyroscope(state, player)

def cloud_widget(state, player) -> bool:
	return mainframe_widget(state, player) and power(state, player)

def widget_particle(state, player) -> bool:
	return basic_widget(state, player) and power(state, player)

def nanoprocessor(state, player) -> bool:
	return microprocessors(state, player) and widget_particle(state, player)

def portable_reactor(state, player) -> bool:
	return fuel_rod(state, player) and battery(state, player)

def quantum_widget(state, player) -> bool:
	return nanoprocessor(state, player) and portable_reactor(state, player) and cloud_widget(state, player)

def helium(state, player) -> bool:
	return power(state, player)

def superconductor(state, player) -> bool:
	return helium(state, player) and nanoprocessor(state, player) and iron_ingot(state, player)

def ai_core(state, player) -> bool:
	return superconductor(state, player) and silicon(state, player) and thinking_core(state, player)

def unshackled_widget(state, player) -> bool:
	return ai_core(state, player) and quantum_widget(state, player)

def ai_training_data(state, player) -> bool:
	return unshackled_widget(state, player)

def ascension_matrix(state, player) -> bool:
	return ai_training_data(state, player) and superconductor(state, player) and gyroscope(state, player)

def ascended_widget(state, player) -> bool:
	return ascension_matrix(state, player) and nanoprocessor(state, player) and unshackled_widget(state, player)

def sentience_core(state, player) -> bool:
	return ai_core(state, player) and ai_training_data(state, player) and power(state, player)

def picoprocessor(state, player) -> bool:
	return superconductor(state, player) and nanoprocessor(state, player) and ai_training_data(state, player)

def sentient_widget(state, player) -> bool:
	return sentience_core(state, player) and picoprocessor(state, player) and ascended_widget(state, player)

def processor_amalgamation(state, player) -> bool:
	return microprocessors(state, player) and circuit_board(state, player) and nanoprocessor(state, player) and picoprocessor(state, player)

def core_amalgamation(state, player) -> bool:
	return thinking_core(state, player) and ai_core(state, player) and sentience_core(state, player)

def widget_amalgamation(state, player) -> bool:
	return basic_widget(state, player) and spinning_widget(state, player) and capacitor_widget(state, player) and computational_widget(state, player) and integrated_widget(state, player) and mainframe_widget(state, player) and cloud_widget(state, player) and quantum_widget(state, player) and unshackled_widget(state, player) and ascended_widget(state, player) and sentient_widget(state, player)

def omega_project_casing(state, player) -> bool:
	return iron_ingot(state, player) and copper_ingot(state, player) and superconductor(state, player) and sentient_widget(state, player)

def omega_project_shielding(state, player) -> bool:
	return plastic(state, player) and bottled_lightning(state, player) and portable_reactor(state, player) and sentient_widget(state, player)

def omega_widget(state, player) -> bool:
	return widget_amalgamation(state, player) and core_amalgamation(state, player) and processor_amalgamation(state, player) and omega_project_casing(state, player) and omega_project_shielding(state, player)

def rocket_electronics(state, player) -> bool:
	return processor_amalgamation(state, player) and core_amalgamation(state, player)

def rocket_fuel(state, player) -> bool:
	return oil(state, player) and fuel_rod(state, player) and power(state, player)

def rocket_hull(state, player) -> bool:
	return omega_project_casing(state, player) and omega_project_shielding(state, player)

def rocket_segment(state, player) -> bool:
	return omega_widget(state, player) and rocket_hull(state, player) and rocket_electronics(state, player) and rocket_fuel(state, player)