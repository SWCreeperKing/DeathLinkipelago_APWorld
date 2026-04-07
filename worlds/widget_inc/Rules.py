import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player, options):
	return {
		"Tier 1 Mastery": lambda state: basic_widget(state, player, options),
		"Deconstruct": lambda state: basic_widget(state, player, options),
		"Frame Relocation": lambda state: has_frame(state, player, options, 'Deconstruct') and basic_widget(state, player, options),
		"Efficient Extraction": lambda state: has_frame(state, player, options, 'Iron Mine') and basic_widget(state, player, options),
		"Iron Smelter": lambda state: has_frame(state, player, options, 'Iron Mine'),
		"Furnace Optimizer": lambda state: has_frame(state, player, options, 'Iron Smelter') and basic_widget(state, player, options),
		"Superheated Crucible (Iron Ingot)": lambda state: has_frame(state, player, options, 'Iron Smelter') and basic_widget(state, player, options),
		"Widget Factory": lambda state: has_frame(state, player, options, 'Iron Smelter') and iron_ingot(state, player, options),
		"Optimized Materials": lambda state: has_frame(state, player, options, 'Widget Factory') and basic_widget(state, player, options),
		"Rapid Assembly": lambda state: has_frame(state, player, options, 'Widget Factory') and basic_widget(state, player, options),
		"Glitched Frame": lambda state: has_frame(state, player, options, 'Widget Factory') and basic_widget(state, player, options),
		"Fortress": lambda state: has_frame(state, player, options, 'Widget Factory') and basic_widget(state, player, options),
		"Dig Site": lambda state: has_frame(state, player, options, 'Widget Factory') and basic_widget(state, player, options),
		"Tier 2": lambda state: basic_widget(state, player, options),
		"Tier 2 Mastery": lambda state: spinning_widget(state, player, options),
		"Warehouse": lambda state: spinning_widget(state, player, options),
		"Sand Pit": lambda state: basic_widget(state, player, options),
		"Mechanized Shovels": lambda state: has_frame(state, player, options, 'Sand Pit') and spinning_widget(state, player, options),
		"Glass Kiln": lambda state: has_frame(state, player, options, 'Sand Pit') and basic_widget(state, player, options),
		"Kiln Governor": lambda state: has_frame(state, player, options, 'Glass Kiln') and spinning_widget(state, player, options),
		"Gyroscope Fabricator": lambda state: has_frame(state, player, options, 'Glass Kiln') and basic_widget(state, player, options),
		"Widget Spinner": lambda state: has_frame(state, player, options, 'Gyroscope Fabricator') and basic_widget(state, player, options),
		"Spin Stabilizer": lambda state: has_frame(state, player, options, 'Widget Spinner') and spinning_widget(state, player, options),
		"Gyroscopic Array": lambda state: has_frame(state, player, options, 'Widget Spinner') and spinning_widget(state, player, options),
		"Iron-rich Rocks": lambda state: has_frame(state, player, options, 'Iron Mine') and spinning_widget(state, player, options),
		"Efficient Loader Arms": lambda state: has_frame(state, player, options, 'Iron Smelter') and spinning_widget(state, player, options),
		"High Heat Density": lambda state: has_frame(state, player, options, 'Superheated Crucible (Iron Ingot)') and spinning_widget(state, player, options),
		"Widget Twins": lambda state: has_frame(state, player, options, 'Optimized Materials') and spinning_widget(state, player, options),
		"Warped Speed": lambda state: has_frame(state, player, options, 'Glitched Frame') and spinning_widget(state, player, options),
		"Tier 3": lambda state: spinning_widget(state, player, options),
		"Construction Overview": lambda state: capacitor_widget(state, player, options),
		"Pause Construction": lambda state: has_frame(state, player, options, 'Construction Overview') and capacitor_widget(state, player, options),
		"Cancel All Construction": lambda state: has_frame(state, player, options, 'Pause Construction') and capacitor_widget(state, player, options),
		"Tier 3 Mastery": lambda state: capacitor_widget(state, player, options),
		"Eminent Domain": lambda state: capacitor_widget(state, player, options),
		"Clone Layout": lambda state: has_frame(state, player, options, 'Eminent Domain') and capacitor_widget(state, player, options),
		"Area Move": lambda state: has_frame(state, player, options, 'Clone Layout') and capacitor_widget(state, player, options),
		"Oil Field": lambda state: spinning_widget(state, player, options),
		"Autopressurizer": lambda state: has_frame(state, player, options, 'Oil Field') and capacitor_widget(state, player, options),
		"Black Gold": lambda state: has_frame(state, player, options, 'Oil Field') and capacitor_widget(state, player, options),
		"Oil Power Plant": lambda state: has_frame(state, player, options, 'Oil Field') and spinning_widget(state, player, options),
		"Flame Stack": lambda state: has_frame(state, player, options, 'Oil Power Plant') and capacitor_widget(state, player, options),
		"Battery Assembler": lambda state: has_frame(state, player, options, 'Oil Power Plant') and spinning_widget(state, player, options),
		"Superjuiced Upcharger": lambda state: has_frame(state, player, options, 'Battery Assembler') and capacitor_widget(state, player, options),
		"Capacitor Bank": lambda state: has_frame(state, player, options, 'Battery Assembler') and spinning_widget(state, player, options),
		"Substable Wiring": lambda state: has_frame(state, player, options, 'Capacitor Bank') and capacitor_widget(state, player, options),
		"Supercharged Array": lambda state: has_frame(state, player, options, 'Capacitor Bank') and capacitor_widget(state, player, options),
		"Logistics Hub": lambda state: has_frame(state, player, options, 'Capacitor Bank') and capacitor_widget(state, player, options),
		"Coordinated Logistics": lambda state: has_frame(state, player, options, 'Logistics Hub') and capacitor_widget(state, player, options),
		"Napalm Charge": lambda state: has_frame(state, player, options, 'Logistics Hub') and oil(state, player, options) and spinning_widget(state, player, options),
		"Beach Harvest": lambda state: has_frame(state, player, options, 'Sand Pit') and capacitor_widget(state, player, options),
		"Molten Conveyor System": lambda state: has_frame(state, player, options, 'Kiln Governor') and capacitor_widget(state, player, options),
		"Superheated Crucible (Glass)": lambda state: has_frame(state, player, options, 'Glass Kiln') and capacitor_widget(state, player, options),
		"Glass Ball Bearings": lambda state: has_frame(state, player, options, 'Gyroscope Fabricator') and capacitor_widget(state, player, options),
		"Core Drilling": lambda state: has_frame(state, player, options, 'Efficient Extraction') and capacitor_widget(state, player, options),
		"Ultra-Fast Widget Synthesizer": lambda state: has_frame(state, player, options, 'Rapid Assembly') and capacitor_widget(state, player, options),
		"Careful Study": lambda state: has_frame(state, player, options, 'Dig Site') and capacitor_widget(state, player, options),
		"Tier 4": lambda state: capacitor_widget(state, player, options),
		"Eagle Eye": lambda state: computational_widget(state, player, options),
		"Discerning Vision": lambda state: has_frame(state, player, options, 'Eagle Eye') and computational_widget(state, player, options),
		"Tier 4 Mastery": lambda state: computational_widget(state, player, options),
		"Long Distance Upgrades": lambda state: computational_widget(state, player, options),
		"Upgrade Status": lambda state: has_frame(state, player, options, 'Long Distance Upgrades') and computational_widget(state, player, options),
		"Copper Mine": lambda state: capacitor_widget(state, player, options),
		"Turbo Drill Motors": lambda state: has_frame(state, player, options, 'Copper Mine') and computational_widget(state, player, options),
		"Copper Forge": lambda state: has_frame(state, player, options, 'Copper Mine') and capacitor_widget(state, player, options),
		"Forge Attendant": lambda state: has_frame(state, player, options, 'Copper Forge') and computational_widget(state, player, options),
		"Rapid Heat Induction Coils": lambda state: has_frame(state, player, options, 'Copper Forge') and computational_widget(state, player, options),
		"Plastic Extractor": lambda state: has_frame(state, player, options, 'Copper Forge') and capacitor_widget(state, player, options),
		"Enhanced Chemical Mixer": lambda state: has_frame(state, player, options, 'Plastic Extractor') and computational_widget(state, player, options),
		"Circuit Fab": lambda state: has_frame(state, player, options, 'Plastic Extractor') and capacitor_widget(state, player, options),
		"Computational Engine": lambda state: has_frame(state, player, options, 'Circuit Fab') and capacitor_widget(state, player, options),
		"Enhanced Logic Synthesizer": lambda state: has_frame(state, player, options, 'Computational Engine') and computational_widget(state, player, options),
		"Rapid Component Feeder": lambda state: has_frame(state, player, options, 'Computational Engine') and computational_widget(state, player, options),
		"Peat Oil Processing": lambda state: has_frame(state, player, options, 'Autopressurizer') and computational_widget(state, player, options),
		"Power Plant Logistics": lambda state: has_frame(state, player, options, 'Oil Power Plant') and computational_widget(state, player, options),
		"High Yield Compressor": lambda state: has_frame(state, player, options, 'Flame Stack') and computational_widget(state, player, options),
		"Depletion Recycler": lambda state: has_frame(state, player, options, 'Battery Assembler') and computational_widget(state, player, options),
		"Expanded Shelf Storage": lambda state: has_frame(state, player, options, 'Warehouse') and computational_widget(state, player, options),
		"Bucket Excavator": lambda state: has_frame(state, player, options, 'Mechanized Shovels') and computational_widget(state, player, options),
		"Glass Shard Recombinator": lambda state: has_frame(state, player, options, 'Glass Kiln') and computational_widget(state, player, options),
		"Direct Glass Insertion": lambda state: has_frame(state, player, options, 'Gyroscope Fabricator') and computational_widget(state, player, options),
		"Tuned Spinners": lambda state: has_frame(state, player, options, 'Gyroscopic Array') and computational_widget(state, player, options),
		"Glass Grinding Wheel": lambda state: has_frame(state, player, options, 'Gyroscopic Array') and computational_widget(state, player, options),
		"Industrial Capacity": lambda state: has_frame(state, player, options, 'Furnace Optimizer') and computational_widget(state, player, options),
		"Precision Widgeteering": lambda state: has_frame(state, player, options, 'Optimized Materials') and computational_widget(state, player, options),
		"Unnatural Duplication": lambda state: has_frame(state, player, options, 'Warped Speed') and computational_widget(state, player, options),
		"Tier 5": lambda state: computational_widget(state, player, options),
		"Tier 5 Mastery": lambda state: integrated_widget(state, player, options),
		"Tesla Coil": lambda state: computational_widget(state, player, options),
		"Rapid Charge Collector": lambda state: has_frame(state, player, options, 'Tesla Coil') and integrated_widget(state, player, options),
		"Core Foundry": lambda state: has_frame(state, player, options, 'Tesla Coil') and computational_widget(state, player, options),
		"Rudimentary Synapse Connector": lambda state: has_frame(state, player, options, 'Tesla Coil') and integrated_widget(state, player, options),
		"Integrator": lambda state: has_frame(state, player, options, 'Core Foundry') and computational_widget(state, player, options),
		"Synapse Fusion Unit": lambda state: has_frame(state, player, options, 'Integrator') and integrated_widget(state, player, options),
		"Rapid Coupler": lambda state: has_frame(state, player, options, 'Integrator') and integrated_widget(state, player, options),
		"Recycler": lambda state: has_frame(state, player, options, 'Integrator') and integrated_widget(state, player, options),
		"Rubble Grinder": lambda state: has_frame(state, player, options, 'Recycler') and integrated_widget(state, player, options),
		"Excavator": lambda state: has_frame(state, player, options, 'Recycler') and integrated_widget(state, player, options),
		"Giant Rock Crusher": lambda state: has_frame(state, player, options, 'Copper Mine') and integrated_widget(state, player, options),
		"Advanced Alloy Mixer": lambda state: has_frame(state, player, options, 'Copper Forge') and integrated_widget(state, player, options),
		"Slash And Burn": lambda state: has_frame(state, player, options, 'Rapid Heat Induction Coils') and integrated_widget(state, player, options),
		"Hyper-Speed Assembly Line": lambda state: has_frame(state, player, options, 'Circuit Fab') and integrated_widget(state, player, options),
		"Auxiliary Pump Stack": lambda state: has_frame(state, player, options, 'Black Gold') and integrated_widget(state, player, options),
		"Heat Recirculator": lambda state: has_frame(state, player, options, 'High Yield Compressor') and integrated_widget(state, player, options),
		"Hydrophobia": lambda state: has_frame(state, player, options, 'Battery Assembler') and integrated_widget(state, player, options),
		"Dedicated Battery Inserters": lambda state: has_frame(state, player, options, 'Substable Wiring') and integrated_widget(state, player, options),
		"Rapid Discharge Fabricator": lambda state: has_frame(state, player, options, 'Supercharged Array') and integrated_widget(state, player, options),
		"Optimized Supply Lines": lambda state: has_frame(state, player, options, 'Logistics Hub') and integrated_widget(state, player, options),
		"Perfectly Balanced Spinner": lambda state: has_frame(state, player, options, 'Glass Ball Bearings') and integrated_widget(state, player, options),
		"Gyroscope Sharing Plan": lambda state: has_frame(state, player, options, 'Spin Stabilizer') and integrated_widget(state, player, options),
		"Dig Deeper": lambda state: has_frame(state, player, options, 'Core Drilling') and integrated_widget(state, player, options),
		"Turbo Blast Furnace": lambda state: has_frame(state, player, options, 'Superheated Crucible (Iron Ingot)') and integrated_widget(state, player, options),
		"Omni-Assembler Core": lambda state: has_frame(state, player, options, 'Ultra-Fast Widget Synthesizer') and integrated_widget(state, player, options),
		"Tier 6": lambda state: integrated_widget(state, player, options),
		"Tier 6 Mastery": lambda state: mainframe_widget(state, player, options),
		"The Factory Must Grow": lambda state: mainframe_widget(state, player, options),
		"Silicon Extruder": lambda state: integrated_widget(state, player, options),
		"Swift Wafer Synthesizer": lambda state: has_frame(state, player, options, 'Silicon Extruder') and mainframe_widget(state, player, options),
		"Processor Lab": lambda state: has_frame(state, player, options, 'Silicon Extruder') and integrated_widget(state, player, options),
		"Extreme-UV Protocol": lambda state: has_frame(state, player, options, 'Processor Lab') and mainframe_widget(state, player, options),
		"Mainframe Assembler": lambda state: has_frame(state, player, options, 'Processor Lab') and integrated_widget(state, player, options),
		"Enhanced Data Synthesizer": lambda state: has_frame(state, player, options, 'Mainframe Assembler') and mainframe_widget(state, player, options),
		"Rapid Circuit Integrator": lambda state: has_frame(state, player, options, 'Mainframe Assembler') and mainframe_widget(state, player, options),
		"Indentured Servitude": lambda state: has_frame(state, player, options, 'Mainframe Assembler') and mainframe_widget(state, player, options),
		"Graveyard": lambda state: has_frame(state, player, options, 'Indentured Servitude') and mainframe_widget(state, player, options),
		"Chain Lightning": lambda state: has_frame(state, player, options, 'Tesla Coil') and mainframe_widget(state, player, options),
		"Efficient Neural Matrix": lambda state: has_frame(state, player, options, 'Core Foundry') and mainframe_widget(state, player, options),
		"Introvert": lambda state: has_frame(state, player, options, 'Core Foundry') and mainframe_widget(state, player, options),
		"Reclaim Sorting System": lambda state: has_frame(state, player, options, 'Rubble Grinder') and mainframe_widget(state, player, options),
		"Hyper-Speed Conveyor System": lambda state: has_frame(state, player, options, 'Turbo Drill Motors') and mainframe_widget(state, player, options),
		"Shortened Transfer Tube": lambda state: has_frame(state, player, options, 'Plastic Extractor') and mainframe_widget(state, player, options),
		"Advanced Refining Chamber": lambda state: has_frame(state, player, options, 'Enhanced Chemical Mixer') and mainframe_widget(state, player, options),
		"Precision Assembly Matrix": lambda state: has_frame(state, player, options, 'Circuit Fab') and mainframe_widget(state, player, options),
		"Agoraphobia": lambda state: has_frame(state, player, options, 'Circuit Fab') and mainframe_widget(state, player, options),
		"Standalone": lambda state: has_frame(state, player, options, 'Enhanced Logic Synthesizer') and mainframe_widget(state, player, options),
		"Accelerated Component Placement": lambda state: has_frame(state, player, options, 'Rapid Component Feeder') and mainframe_widget(state, player, options),
		"Exhaust Vent Recycler": lambda state: has_frame(state, player, options, 'Heat Recirculator') and mainframe_widget(state, player, options),
		"Rapid Heat Exchanger (Battery)": lambda state: has_frame(state, player, options, 'Superjuiced Upcharger') and mainframe_widget(state, player, options),
		"Energy Optimization Core": lambda state: has_frame(state, player, options, 'Substable Wiring') and mainframe_widget(state, player, options),
		"Warehouse Shelf Stacker": lambda state: has_frame(state, player, options, 'Expanded Shelf Storage') and mainframe_widget(state, player, options),
		"Grain Matrix Duplicator": lambda state: has_frame(state, player, options, 'Bucket Excavator') and mainframe_widget(state, player, options),
		"Rapid Heat Exchanger (Glass)": lambda state: has_frame(state, player, options, 'Superheated Crucible (Glass)') and mainframe_widget(state, player, options),
		"Counterspin Anchors": lambda state: has_frame(state, player, options, 'Tuned Spinners') and mainframe_widget(state, player, options),
		"Double-stacked Conveyors": lambda state: has_frame(state, player, options, 'Efficient Loader Arms') and mainframe_widget(state, player, options),
		"Productivity Optimization Node": lambda state: has_frame(state, player, options, 'Precision Widgeteering') and mainframe_widget(state, player, options),
		"Dutiful Archivist": lambda state: has_frame(state, player, options, 'Careful Study') and mainframe_widget(state, player, options),
		"Tier 7": lambda state: mainframe_widget(state, player, options),
		"Tier 7 Mastery": lambda state: cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Auto Upgrade": lambda state: cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Uranium Mine": lambda state: mainframe_widget(state, player, options),
		"Rapid Extraction Module": lambda state: has_frame(state, player, options, 'Uranium Mine') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Fuel Rod Assembler": lambda state: has_frame(state, player, options, 'Uranium Mine') and mainframe_widget(state, player, options),
		"Accelerated Molding Unit": lambda state: has_frame(state, player, options, 'Fuel Rod Assembler') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Nuclear Power Plant": lambda state: has_frame(state, player, options, 'Fuel Rod Assembler') and mainframe_widget(state, player, options),
		"Advanced Heat Exchanger": lambda state: has_frame(state, player, options, 'Nuclear Power Plant') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Cloud Digitizer": lambda state: has_frame(state, player, options, 'Nuclear Power Plant') and mainframe_widget(state, player, options),
		"Multi-Core Upload System": lambda state: has_frame(state, player, options, 'Cloud Digitizer') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Swift Transfer Protocol": lambda state: has_frame(state, player, options, 'Cloud Digitizer') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Monocrystalline": lambda state: has_frame(state, player, options, 'Silicon Extruder') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Microfine Engraving": lambda state: has_frame(state, player, options, 'Processor Lab') and cloud_widget(state, player, options),
		"Automated Chapel": lambda state: has_frame(state, player, options, 'Graveyard') and cloud_widget(state, player, options),
		"Multi-Bolt Capture Array": lambda state: has_frame(state, player, options, 'Rapid Charge Collector') and cloud_widget(state, player, options),
		"Lightning Interface": lambda state: has_frame(state, player, options, 'Rapid Coupler') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Extrovert": lambda state: has_frame(state, player, options, 'Rapid Coupler') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Autonomous Garbage Collectors": lambda state: has_frame(state, player, options, 'Reclaim Sorting System') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Autosifter": lambda state: has_frame(state, player, options, 'Excavator') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Dense Packing Grid": lambda state: has_frame(state, player, options, 'Forge Attendant') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Advanced Circuit Optimization": lambda state: has_frame(state, player, options, 'Enhanced Logic Synthesizer') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Pipe Repressurizer": lambda state: has_frame(state, player, options, 'Auxiliary Pump Stack') and cloud_widget(state, player, options),
		"Instantaneous Charge Module": lambda state: has_frame(state, player, options, 'Rapid Discharge Fabricator') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Lightspeed Rotation": lambda state: has_frame(state, player, options, 'Gyroscope Fabricator') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Calculated Material Distribution": lambda state: has_frame(state, player, options, 'Gyroscope Sharing Plan') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Uranium-powered Drills": lambda state: has_frame(state, player, options, 'Dig Deeper') and cloud_widget(state, player, options) and fuel_rod(state, player, options),
		"Infinite Widget Matrix": lambda state: has_frame(state, player, options, 'Omni-Assembler Core') and cloud_widget(state, player, options),
		"Tier 8": lambda state: cloud_widget(state, player, options),
		"Tier 8 Mastery": lambda state: quantum_widget(state, player, options),
		"Widget Minitizers": lambda state: cloud_widget(state, player, options),
		"Enhanced Particle Compressor": lambda state: has_frame(state, player, options, 'Widget Minitizers') and quantum_widget(state, player, options),
		"Quantum Shrink Matrix": lambda state: has_frame(state, player, options, 'Enhanced Particle Compressor') and quantum_widget(state, player, options),
		"Nanoscale Lab": lambda state: has_frame(state, player, options, 'Widget Minitizers') and cloud_widget(state, player, options),
		"Quantum Lithography": lambda state: has_frame(state, player, options, 'Nanoscale Lab') and quantum_widget(state, player, options),
		"Reactor Foundry": lambda state: has_frame(state, player, options, 'Nanoscale Lab') and cloud_widget(state, player, options),
		"Subatomic Power Booster": lambda state: has_frame(state, player, options, 'Reactor Foundry') and quantum_widget(state, player, options),
		"Quantum Tunneler": lambda state: has_frame(state, player, options, 'Reactor Foundry') and cloud_widget(state, player, options),
		"High-Efficiency Particle Matrix": lambda state: has_frame(state, player, options, 'Quantum Tunneler') and quantum_widget(state, player, options),
		"Rapid Particle Integrator": lambda state: has_frame(state, player, options, 'Quantum Tunneler') and quantum_widget(state, player, options),
		"City Builder": lambda state: has_frame(state, player, options, 'Rapid Particle Integrator') and quantum_widget(state, player, options),
		"Blitz Upgrade": lambda state: has_frame(state, player, options, 'Auto Upgrade') and quantum_widget(state, player, options),
		"Fallout": lambda state: has_frame(state, player, options, 'Uranium Mine') and quantum_widget(state, player, options),
		"Multi-Stage Refinement": lambda state: has_frame(state, player, options, 'Fuel Rod Assembler') and quantum_widget(state, player, options),
		"Green Energy": lambda state: has_frame(state, player, options, 'Fuel Rod Assembler') and quantum_widget(state, player, options),
		"Precision Control Rods": lambda state: has_frame(state, player, options, 'Advanced Heat Exchanger') and quantum_widget(state, player, options),
		"Rapid Crystal Formation Chamber": lambda state: has_frame(state, player, options, 'Swift Wafer Synthesizer') and quantum_widget(state, player, options),
		"Suburban Development": lambda state: has_frame(state, player, options, 'Processor Lab') and quantum_widget(state, player, options),
		"Binary Pairs": lambda state: has_frame(state, player, options, 'Enhanced Data Synthesizer') and quantum_widget(state, player, options),
		"Hyper-Speed Compiler": lambda state: has_frame(state, player, options, 'Rapid Circuit Integrator') and quantum_widget(state, player, options),
		"Efficient Value Extraction": lambda state: has_frame(state, player, options, 'Indentured Servitude') and quantum_widget(state, player, options),
		"Rapid Cognitive Assembler": lambda state: has_frame(state, player, options, 'Rudimentary Synapse Connector') and quantum_widget(state, player, options),
		"Quantum Logic Synthesizer": lambda state: has_frame(state, player, options, 'Synapse Fusion Unit') and quantum_widget(state, player, options),
		"Universal Recycling Schema": lambda state: has_frame(state, player, options, 'Autonomous Garbage Collectors') and quantum_widget(state, player, options),
		"High-Yield Extraction System": lambda state: has_frame(state, player, options, 'Hyper-Speed Conveyor System') and quantum_widget(state, player, options),
		"Quantum Heat Exchanger": lambda state: has_frame(state, player, options, 'Slash And Burn') and quantum_widget(state, player, options),
		"Yield Optimization Catalyst": lambda state: has_frame(state, player, options, 'Advanced Refining Chamber') and quantum_widget(state, player, options),
		"Turbo Soldering Station": lambda state: has_frame(state, player, options, 'Hyper-Speed Assembly Line') and quantum_widget(state, player, options),
		"Hyper-Speed Arithmetic Processor": lambda state: has_frame(state, player, options, 'Accelerated Component Placement') and quantum_widget(state, player, options),
		"Monopole Battery Tech": lambda state: has_frame(state, player, options, 'Depletion Recycler') and quantum_widget(state, player, options),
		"Nano-Capacitor Synthesizer": lambda state: has_frame(state, player, options, 'Energy Optimization Core') and quantum_widget(state, player, options),
		"Lost Package Tracker": lambda state: has_frame(state, player, options, 'Optimized Supply Lines') and quantum_widget(state, player, options),
		"Extradimensional Storage Lockers": lambda state: has_frame(state, player, options, 'Warehouse Shelf Stacker') and quantum_widget(state, player, options),
		"Unified Theory of Sand": lambda state: has_frame(state, player, options, 'Grain Matrix Duplicator') and quantum_widget(state, player, options),
		"Hyperfine Glass Distributor": lambda state: has_frame(state, player, options, 'Glass Shard Recombinator') and quantum_widget(state, player, options),
		"Spacetime Spin Matrix": lambda state: has_frame(state, player, options, 'Counterspin Anchors') and quantum_widget(state, player, options),
		"Hyper-Production Matrix": lambda state: has_frame(state, player, options, 'Precision Widgeteering') and quantum_widget(state, player, options),
		"Mitosis": lambda state: has_frame(state, player, options, 'Unnatural Duplication') and quantum_widget(state, player, options),
		"Boundless Patience": lambda state: has_frame(state, player, options, 'Dutiful Archivist') and quantum_widget(state, player, options),
		"Tier 9": lambda state: quantum_widget(state, player, options),
		"Tier 9 Mastery": lambda state: unshackled_widget(state, player, options),
		"New World Order": lambda state: unshackled_widget(state, player, options),
		"Helium Extractor": lambda state: quantum_widget(state, player, options),
		"Subatomic Yield Booster (Helium)": lambda state: has_frame(state, player, options, 'Helium Extractor') and unshackled_widget(state, player, options),
		"Conductor Foundry": lambda state: has_frame(state, player, options, 'Helium Extractor') and quantum_widget(state, player, options),
		"Lightning Flux Unit": lambda state: has_frame(state, player, options, 'Conductor Foundry') and unshackled_widget(state, player, options),
		"AI Laboratory": lambda state: has_frame(state, player, options, 'Conductor Foundry') and quantum_widget(state, player, options),
		"Quantum Neural Matrix": lambda state: has_frame(state, player, options, 'AI Laboratory') and unshackled_widget(state, player, options),
		"AI Delimiter": lambda state: has_frame(state, player, options, 'AI Laboratory') and quantum_widget(state, player, options),
		"Advanced Cognitive Network": lambda state: has_frame(state, player, options, 'AI Delimiter') and unshackled_widget(state, player, options),
		"Neural Accelerator": lambda state: has_frame(state, player, options, 'AI Delimiter') and unshackled_widget(state, player, options),
		"Direct Widget Insertion": lambda state: has_frame(state, player, options, 'Widget Minitizers') and unshackled_widget(state, player, options),
		"Superconducting Collider Matrix": lambda state: has_frame(state, player, options, 'Quantum Shrink Matrix') and unshackled_widget(state, player, options),
		"Precision Atom Placement": lambda state: has_frame(state, player, options, 'Nanoscale Lab') and unshackled_widget(state, player, options),
		"Relics of the Past": lambda state: has_frame(state, player, options, 'Nanoscale Lab') and unshackled_widget(state, player, options),
		"Rapid Core Integrator": lambda state: has_frame(state, player, options, 'Reactor Foundry') and unshackled_widget(state, player, options),
		"Accelerated Entanglement": lambda state: has_frame(state, player, options, 'Rapid Particle Integrator') and unshackled_widget(state, player, options),
		"Nuclear Bore Engine": lambda state: has_frame(state, player, options, 'Rapid Extraction Module') and unshackled_widget(state, player, options),
		"Direct Core Cooling": lambda state: has_frame(state, player, options, 'Nuclear Power Plant') and unshackled_widget(state, player, options),
		"Superconducting Fuel Chamber": lambda state: has_frame(state, player, options, 'Precision Control Rods') and unshackled_widget(state, player, options),
		"Datacenter Access": lambda state: has_frame(state, player, options, 'Multi-Core Upload System') and unshackled_widget(state, player, options),
		"Quantum Integration Matrix": lambda state: has_frame(state, player, options, 'Multi-Core Upload System') and unshackled_widget(state, player, options),
		"Rapid Cloud Integrator": lambda state: has_frame(state, player, options, 'Swift Transfer Protocol') and unshackled_widget(state, player, options),
		"Rapid Logic Preprocessor": lambda state: has_frame(state, player, options, 'Extreme-UV Protocol') and unshackled_widget(state, player, options),
		"Multi-Core Processor": lambda state: has_frame(state, player, options, 'Enhanced Data Synthesizer') and unshackled_widget(state, player, options),
		"Incinerator": lambda state: has_frame(state, player, options, 'Graveyard') and unshackled_widget(state, player, options),
		"Turbo Lightning Rods": lambda state: has_frame(state, player, options, 'Multi-Bolt Capture Array') and unshackled_widget(state, player, options),
		"Thought Integration Unit": lambda state: has_frame(state, player, options, 'Efficient Neural Matrix') and unshackled_widget(state, player, options),
		"Ultra-Quick Integrator": lambda state: has_frame(state, player, options, 'Lightning Interface') and unshackled_widget(state, player, options),
		"Automated Grading": lambda state: has_frame(state, player, options, 'Autosifter') and unshackled_widget(state, player, options),
		"Ore-to-Ingot Optimization System": lambda state: has_frame(state, player, options, 'Advanced Alloy Mixer') and unshackled_widget(state, player, options),
		"Quantum Circuitry Optimizer": lambda state: has_frame(state, player, options, 'Precision Assembly Matrix') and unshackled_widget(state, player, options),
		"Multi-Tasking Calculation Node": lambda state: has_frame(state, player, options, 'Advanced Circuit Optimization') and unshackled_widget(state, player, options),
		"Pressurized Storage Vats": lambda state: has_frame(state, player, options, 'Pipe Repressurizer') and unshackled_widget(state, player, options),
		"Ultra-Fast Circuit Integrator": lambda state: has_frame(state, player, options, 'Instantaneous Charge Module') and unshackled_widget(state, player, options),
		"Gyroscope Hyperprocessor": lambda state: has_frame(state, player, options, 'Lightspeed Rotation') and unshackled_widget(state, player, options),
		"Excess Spin Utilizer": lambda state: has_frame(state, player, options, 'Gyroscope Sharing Plan') and unshackled_widget(state, player, options),
		"Tier 10": lambda state: unshackled_widget(state, player, options),
		"Tier 10 Mastery": lambda state: ascended_widget(state, player, options),
		"Training Center": lambda state: unshackled_widget(state, player, options),
		"Advanced Cognitive Compiler": lambda state: has_frame(state, player, options, 'Training Center') and ascended_widget(state, player, options),
		"Data Transformer": lambda state: has_frame(state, player, options, 'Training Center') and unshackled_widget(state, player, options),
		"Expedite Ascension": lambda state: has_frame(state, player, options, 'Data Transformer') and unshackled_widget(state, player, options),
		"Ascension Facility": lambda state: has_frame(state, player, options, 'Data Transformer') and unshackled_widget(state, player, options),
		"Unleashed Thought Matrix": lambda state: has_frame(state, player, options, 'Ascension Facility') and ascended_widget(state, player, options),
		"Rapid Cognition Compiler": lambda state: has_frame(state, player, options, 'Ascension Facility') and ascended_widget(state, player, options),
		"Leveler": lambda state: has_frame(state, player, options, 'Ascension Facility') and ascended_widget(state, player, options),
		"Gaseous Bedrock": lambda state: has_frame(state, player, options, 'Helium Extractor') and ascended_widget(state, player, options),
		"Precision Gas Separator": lambda state: has_frame(state, player, options, 'Subatomic Yield Booster (Helium)') and ascended_widget(state, player, options),
		"Quantum Flux Matrix": lambda state: has_frame(state, player, options, 'Conductor Foundry') and ascended_widget(state, player, options),
		"Resource Management": lambda state: has_frame(state, player, options, 'Conductor Foundry') and ascended_widget(state, player, options),
		"Rapid AI Synthesizer": lambda state: has_frame(state, player, options, 'Quantum Neural Matrix') and ascended_widget(state, player, options),
		"Multi-Phase Logic Processor": lambda state: has_frame(state, player, options, 'Advanced Cognitive Network') and ascended_widget(state, player, options),
		"Upgraded AI Compiler": lambda state: has_frame(state, player, options, 'Neural Accelerator') and ascended_widget(state, player, options),
		"Subatomic Yield Booster (Widget Particle)": lambda state: has_frame(state, player, options, 'Superconducting Collider Matrix') and ascended_widget(state, player, options),
		"Industrial Espionage": lambda state: has_frame(state, player, options, 'Reactor Foundry') and ascended_widget(state, player, options),
		"Subatomic Yield Optimizer": lambda state: has_frame(state, player, options, 'High-Efficiency Particle Matrix') and ascended_widget(state, player, options),
		"Cowboy Coding": lambda state: has_frame(state, player, options, 'Quantum Tunneler') and ascended_widget(state, player, options),
		"Lightning Upgrade": lambda state: has_frame(state, player, options, 'Blitz Upgrade') and ascended_widget(state, player, options),
		"Rapid Rod Fabricator": lambda state: has_frame(state, player, options, 'Accelerated Molding Unit') and ascended_widget(state, player, options),
		"Quantum Efficiency Reactor": lambda state: has_frame(state, player, options, 'Superconducting Fuel Chamber') and ascended_widget(state, player, options),
		"Yield Maximization Reactor": lambda state: has_frame(state, player, options, 'Rapid Crystal Formation Chamber') and ascended_widget(state, player, options),
		"N-Step Branch Prediction": lambda state: has_frame(state, player, options, 'Microfine Engraving') and unshackled_widget(state, player, options),
		"Lightning Data Bus": lambda state: has_frame(state, player, options, 'Hyper-Speed Compiler') and ascended_widget(state, player, options),
		"High Intensity Furnace": lambda state: has_frame(state, player, options, 'Incinerator') and ascended_widget(state, player, options),
		"Remnants of Humanity": lambda state: has_frame(state, player, options, 'Efficient Value Extraction') and ascended_widget(state, player, options),
		"Yield Maximization Protocol": lambda state: has_frame(state, player, options, 'Quantum Logic Synthesizer') and ascended_widget(state, player, options),
		"Advanced Mining Protocol": lambda state: has_frame(state, player, options, 'High-Yield Extraction System') and ascended_widget(state, player, options),
		"Rapid Refinement Module": lambda state: has_frame(state, player, options, 'Yield Optimization Catalyst') and ascended_widget(state, player, options),
		"Ultra-Quick Logic Compiler": lambda state: has_frame(state, player, options, 'Hyper-Speed Arithmetic Processor') and ascended_widget(state, player, options),
		"High-Efficiency Capacitor Matrix": lambda state: has_frame(state, player, options, 'Energy Optimization Core') and ascended_widget(state, player, options),
		"Infinite Storage Glitch": lambda state: has_frame(state, player, options, 'Extradimensional Storage Lockers') and ascended_widget(state, player, options),
		"Tier 11": lambda state: ascended_widget(state, player, options),
		"Tier 11 Mastery": lambda state: sentient_widget(state, player, options),
		"Absolute Dominion": lambda state: sentient_widget(state, player, options),
		"Perpetual Motion Machine": lambda state: ascended_widget(state, player, options),
		"Physics Engine Decoder": lambda state: has_frame(state, player, options, 'Perpetual Motion Machine') and sentient_widget(state, player, options),
		"Sentience Facility": lambda state: has_frame(state, player, options, 'Perpetual Motion Machine') and ascended_widget(state, player, options),
		"Sentience Recombobulator": lambda state: has_frame(state, player, options, 'Sentience Facility') and sentient_widget(state, player, options),
		"Picoscale Lab": lambda state: has_frame(state, player, options, 'Sentience Facility') and ascended_widget(state, player, options),
		"Enhanced Production Algorithms": lambda state: has_frame(state, player, options, 'Picoscale Lab') and sentient_widget(state, player, options),
		"Sentience Aggregator": lambda state: has_frame(state, player, options, 'Picoscale Lab') and ascended_widget(state, player, options),
		"Processor Sharing System": lambda state: has_frame(state, player, options, 'Sentience Aggregator') and sentient_widget(state, player, options),
		"Thought Enhancer Matrix": lambda state: has_frame(state, player, options, 'Sentience Aggregator') and sentient_widget(state, player, options),
		"History Lesson": lambda state: has_frame(state, player, options, 'Training Center') and sentient_widget(state, player, options),
		"Rapid Spec Synthesizer": lambda state: has_frame(state, player, options, 'Advanced Cognitive Compiler') and sentient_widget(state, player, options),
		"Advanced Cognitive Release": lambda state: has_frame(state, player, options, 'Data Transformer') and sentient_widget(state, player, options),
		"Wild Mutation": lambda state: has_frame(state, player, options, 'Data Transformer') and sentient_widget(state, player, options),
		"Advanced Neural Compiler": lambda state: has_frame(state, player, options, 'Unleashed Thought Matrix') and sentient_widget(state, player, options),
		"Frictionless Neural Compiler": lambda state: has_frame(state, player, options, 'Rapid Cognition Compiler') and sentient_widget(state, player, options),
		"Enhanced Helium Synthesizer": lambda state: has_frame(state, player, options, 'Precision Gas Separator') and sentient_widget(state, player, options),
		"Hyper-Speed Magnet Chamber": lambda state: has_frame(state, player, options, 'Lightning Flux Unit') and sentient_widget(state, player, options),
		"Hello World": lambda state: has_frame(state, player, options, 'AI Laboratory') and sentient_widget(state, player, options),
		"Optimized Neuron Compiler": lambda state: has_frame(state, player, options, 'Rapid AI Synthesizer') and sentient_widget(state, player, options),
		"Trinity": lambda state: has_frame(state, player, options, 'AI Delimiter') and sentient_widget(state, player, options),
		"Accelerated Thought Synthesizer": lambda state: has_frame(state, player, options, 'Upgraded AI Compiler') and sentient_widget(state, player, options),
		"Hyper-Accelerated Fabricator": lambda state: has_frame(state, player, options, 'Quantum Lithography') and sentient_widget(state, player, options),
		"Multi-Fuel Synthesizer": lambda state: has_frame(state, player, options, 'Subatomic Power Booster') and sentient_widget(state, player, options),
		"Stellar Quantum Weaver": lambda state: has_frame(state, player, options, 'Accelerated Entanglement') and sentient_widget(state, player, options),
		"Radiometric Ore Separator": lambda state: has_frame(state, player, options, 'Nuclear Bore Engine') and sentient_widget(state, player, options),
		"Isotope Yield Booster": lambda state: has_frame(state, player, options, 'Multi-Stage Refinement') and sentient_widget(state, player, options),
		"Data Yield Optimizer": lambda state: has_frame(state, player, options, 'Quantum Integration Matrix') and sentient_widget(state, player, options),
		"Hyper-Speed Data Link": lambda state: has_frame(state, player, options, 'Rapid Cloud Integrator') and sentient_widget(state, player, options),
		"Data Stream Optimizer": lambda state: has_frame(state, player, options, 'Multi-Core Processor') and sentient_widget(state, player, options),
		"High-Capacity Energy Condenser": lambda state: has_frame(state, player, options, 'Turbo Lightning Rods') and sentient_widget(state, player, options),
		"Swift Logic Gate Fabricator": lambda state: has_frame(state, player, options, 'Ultra-Quick Integrator') and sentient_widget(state, player, options),
		"Pristine Protection Protocol": lambda state: has_frame(state, player, options, 'Automated Grading') and sentient_widget(state, player, options),
		"Advanced Arithmetic Processor": lambda state: has_frame(state, player, options, 'Advanced Circuit Optimization') and sentient_widget(state, player, options),
		"Tier 12": lambda state: sentient_widget(state, player, options),
		"Tier 12 Mastery": lambda state: omega_widget(state, player, options),
		"Omega Processor Lab": lambda state: sentient_widget(state, player, options),
		"Omega Core Foundry": lambda state: has_frame(state, player, options, 'Omega Processor Lab') and sentient_widget(state, player, options),
		"Rocket Electronics Lab": lambda state: has_frame(state, player, options, 'Omega Core Foundry') and omega_widget(state, player, options),
		"Omega Widget Distiller": lambda state: has_frame(state, player, options, 'Omega Core Foundry') and sentient_widget(state, player, options),
		"Rocket Fuel Distiller": lambda state: has_frame(state, player, options, 'Omega Widget Distiller') and omega_widget(state, player, options),
		"Omega Casing Factory": lambda state: has_frame(state, player, options, 'Omega Widget Distiller') and sentient_widget(state, player, options),
		"Omega Shielding Plant": lambda state: has_frame(state, player, options, 'Omega Casing Factory') and sentient_widget(state, player, options),
		"Rocket Part Assembler": lambda state: has_frame(state, player, options, 'Omega Shielding Plant') and omega_widget(state, player, options),
		"Omega Project Assembler": lambda state: has_frame(state, player, options, 'Omega Shielding Plant') and sentient_widget(state, player, options),
		"Omega Launch Facility": lambda state: has_frame(state, player, options, 'Omega Project Assembler') and omega_widget(state, player, options),
		"Omega Limit Break": lambda state: has_frame(state, player, options, 'Physics Engine Decoder') and omega_widget(state, player, options),
		"Glitch in the System": lambda state: has_frame(state, player, options, 'Perpetual Motion Machine') and omega_widget(state, player, options),
		"Omega Thought Processor": lambda state: has_frame(state, player, options, 'Sentience Facility') and omega_widget(state, player, options),
		"Myriad Landscape": lambda state: has_frame(state, player, options, 'Sentience Facility') and omega_widget(state, player, options),
		"Omega Yield Enhancer": lambda state: has_frame(state, player, options, 'Picoscale Lab') and omega_widget(state, player, options),
		"Generational Uplift": lambda state: has_frame(state, player, options, 'Picoscale Lab') and omega_widget(state, player, options),
		"Omega Assembly Lab": lambda state: has_frame(state, player, options, 'Processor Sharing System') and omega_widget(state, player, options),
		"Stepping Stone To Greatness": lambda state: has_frame(state, player, options, 'Sentience Aggregator') and omega_widget(state, player, options),
		"Omega Sentience Circuitry": lambda state: has_frame(state, player, options, 'Thought Enhancer Matrix') and omega_widget(state, player, options),
		"Omega Training Compiler": lambda state: has_frame(state, player, options, 'Rapid Spec Synthesizer') and omega_widget(state, player, options),
		"Omega Matrix Integrator": lambda state: has_frame(state, player, options, 'Expedite Ascension') and omega_widget(state, player, options),
		"Omega Cognitive Engine": lambda state: has_frame(state, player, options, 'Advanced Neural Compiler') and omega_widget(state, player, options),
		"Beacon of Ascension": lambda state: has_frame(state, player, options, 'Ascension Facility') and omega_widget(state, player, options),
		"Omega Ascension Planner": lambda state: has_frame(state, player, options, 'Frictionless Neural Compiler') and omega_widget(state, player, options),
		"Omega Extraction Matrix": lambda state: has_frame(state, player, options, 'Enhanced Helium Synthesizer') and omega_widget(state, player, options),
		"Omega Magnetizer Unit": lambda state: has_frame(state, player, options, 'Quantum Flux Matrix') and omega_widget(state, player, options),
		"Omega Thought Conductor": lambda state: has_frame(state, player, options, 'Optimized Neuron Compiler') and omega_widget(state, player, options),
		"Omega Neural Matrix": lambda state: has_frame(state, player, options, 'Multi-Phase Logic Processor') and omega_widget(state, player, options),
		"Omega Etching System": lambda state: has_frame(state, player, options, 'Precision Atom Placement') and omega_widget(state, player, options),
		"Omega Containment Field": lambda state: has_frame(state, player, options, 'Rapid Core Integrator') and omega_widget(state, player, options),
		"Omega Entanglement Field": lambda state: has_frame(state, player, options, 'Subatomic Yield Optimizer') and omega_widget(state, player, options),
		"Omega Mining Protocol": lambda state: has_frame(state, player, options, 'Radiometric Ore Separator') and omega_widget(state, player, options),
		"Omega Cloud Synthesizer": lambda state: has_frame(state, player, options, 'Quantum Integration Matrix') and omega_widget(state, player, options),
		"Omega Accelerated Digitizer": lambda state: has_frame(state, player, options, 'Hyper-Speed Data Link') and omega_widget(state, player, options),
		"Omega Crystal Stabilizer": lambda state: has_frame(state, player, options, 'Yield Maximization Reactor') and omega_widget(state, player, options),
		"Omega Logic Amplifier": lambda state: has_frame(state, player, options, 'Multi-Core Processor') and omega_widget(state, player, options),
		"Omega Circuit Weaver": lambda state: has_frame(state, player, options, 'Lightning Data Bus') and omega_widget(state, player, options),
		"Omega Assembly Core": lambda state: has_frame(state, player, options, 'Quantum Logic Synthesizer') and omega_widget(state, player, options),
	}

def get_yaml_option(state, player, options, option) -> bool:
	return options.get_options_map(option).value

def has_amount(state, player, options, item, amount) -> bool:
	return state.has(item, player, amount)

def has(state, player, options, item) -> bool:
	return has_amount(state, player, options, item, 1)

def has_any(state, player, options, items) -> bool:
	return any(has(state, player, options, item) for item in items)

def has_all(state, player, options, items) -> bool:
	return all(has(state, player, options, item) for item in items)

def has_tier(state, player, options, tier) -> bool:
	return has_amount(state, player, options, 'Progressive Tier', tier)

def has_frame(state, player, options, frame) -> bool:
	return has(state, player, options, frame)

def iron_ore(state, player, options) -> bool:
	return has_frame(state, player, options, 'Iron Mine')

def sand(state, player, options) -> bool:
	return has_frame(state, player, options, 'Sand Pit')

def oil(state, player, options) -> bool:
	return has_frame(state, player, options, 'Oil Field')

def copper_ore(state, player, options) -> bool:
	return has_frame(state, player, options, 'Copper Mine')

def iron_ingot(state, player, options) -> bool:
	return has_frame(state, player, options, "Iron Smelter") and iron_ore(state, player, options)

def basic_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Widget Factory") and iron_ingot(state, player, options)

def glass(state, player, options) -> bool:
	return has_frame(state, player, options, "Glass Kiln") and sand(state, player, options)

def gyroscope(state, player, options) -> bool:
	return has_frame(state, player, options, "Gyroscope Fabricator") and glass(state, player, options) and basic_widget(state, player, options)

def power(state, player, options) -> bool:
	return has_frame(state, player, options, "Oil Power Plant") and oil(state, player, options)

def spinning_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Widget Spinner") and gyroscope(state, player, options) and basic_widget(state, player, options)

def battery(state, player, options) -> bool:
	return has_frame(state, player, options, "Battery Assembler") and iron_ingot(state, player, options) and basic_widget(state, player, options) and power(state, player, options)

def capacitor_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Capacitor Bank") and spinning_widget(state, player, options) and battery(state, player, options)

def copper_ingot(state, player, options) -> bool:
	return has_frame(state, player, options, "Copper Forge") and copper_ore(state, player, options)

def plastic(state, player, options) -> bool:
	return has_frame(state, player, options, "Plastic Extractor") and oil(state, player, options)

def circuit_board(state, player, options) -> bool:
	return has_frame(state, player, options, "Circuit Fab") and copper_ingot(state, player, options) and plastic(state, player, options)

def computational_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Computational Engine") and circuit_board(state, player, options) and capacitor_widget(state, player, options) and spinning_widget(state, player, options)

def bottled_lightning(state, player, options) -> bool:
	return has_frame(state, player, options, "Tesla Coil") and glass(state, player, options) and power(state, player, options)

def thinking_core(state, player, options) -> bool:
	return has_frame(state, player, options, "Core Foundry") and capacitor_widget(state, player, options) and computational_widget(state, player, options)

def integrated_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Integrator") and bottled_lightning(state, player, options) and capacitor_widget(state, player, options) and thinking_core(state, player, options)

def silicon(state, player, options) -> bool:
	return has_frame(state, player, options, "Silicon Extruder") and sand(state, player, options) and power(state, player, options)

def microprocessors(state, player, options) -> bool:
	return has_frame(state, player, options, "Processor Lab") and silicon(state, player, options) and circuit_board(state, player, options) and thinking_core(state, player, options)

def mainframe_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Mainframe Assembler") and microprocessors(state, player, options) and integrated_widget(state, player, options)

def uranium(state, player, options) -> bool:
	return has_frame(state, player, options, "Uranium Mine") and power(state, player, options)

def fuel_rod(state, player, options) -> bool:
	return has_frame(state, player, options, "Fuel Rod Assembler") and iron_ingot(state, player, options) and uranium(state, player, options) and power(state, player, options) and gyroscope(state, player, options)

def cloud_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Cloud Digitizer") and mainframe_widget(state, player, options) and power(state, player, options)

def widget_particle(state, player, options) -> bool:
	return has_frame(state, player, options, "Widget Minitizers") and basic_widget(state, player, options) and power(state, player, options)

def nanoprocessor(state, player, options) -> bool:
	return has_frame(state, player, options, "Nanoscale Lab") and microprocessors(state, player, options) and widget_particle(state, player, options)

def portable_reactor(state, player, options) -> bool:
	return has_frame(state, player, options, "Reactor Foundry") and fuel_rod(state, player, options) and battery(state, player, options)

def quantum_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Quantum Tunneler") and nanoprocessor(state, player, options) and portable_reactor(state, player, options) and cloud_widget(state, player, options)

def helium(state, player, options) -> bool:
	return has_frame(state, player, options, "Helium Extractor") and power(state, player, options)

def superconductor(state, player, options) -> bool:
	return has_frame(state, player, options, "Conductor Foundry") and helium(state, player, options) and nanoprocessor(state, player, options) and iron_ingot(state, player, options)

def ai_core(state, player, options) -> bool:
	return has_frame(state, player, options, "AI Laboratory") and superconductor(state, player, options) and silicon(state, player, options) and thinking_core(state, player, options)

def unshackled_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "AI Delimiter") and ai_core(state, player, options) and quantum_widget(state, player, options)

def ai_training_data(state, player, options) -> bool:
	return has_frame(state, player, options, "Training Center") and unshackled_widget(state, player, options)

def ascension_matrix(state, player, options) -> bool:
	return has_frame(state, player, options, "Data Transformer") and ai_training_data(state, player, options) and superconductor(state, player, options) and gyroscope(state, player, options)

def ascended_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Ascension Facility") and ascension_matrix(state, player, options) and nanoprocessor(state, player, options) and unshackled_widget(state, player, options)

def sentience_core(state, player, options) -> bool:
	return has_frame(state, player, options, "Sentience Facility") and ai_core(state, player, options) and ai_training_data(state, player, options) and power(state, player, options)

def picoprocessor(state, player, options) -> bool:
	return has_frame(state, player, options, "Picoscale Lab") and superconductor(state, player, options) and nanoprocessor(state, player, options) and ai_training_data(state, player, options)

def sentient_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Sentience Aggregator") and sentience_core(state, player, options) and picoprocessor(state, player, options) and ascended_widget(state, player, options)

def processor_amalgamation(state, player, options) -> bool:
	return has_frame(state, player, options, "Omega Processor Lab") and microprocessors(state, player, options) and circuit_board(state, player, options) and nanoprocessor(state, player, options) and picoprocessor(state, player, options)

def core_amalgamation(state, player, options) -> bool:
	return has_frame(state, player, options, "Omega Core Foundry") and thinking_core(state, player, options) and ai_core(state, player, options) and sentience_core(state, player, options)

def widget_amalgamation(state, player, options) -> bool:
	return has_frame(state, player, options, "Omega Widget Distiller") and basic_widget(state, player, options) and spinning_widget(state, player, options) and capacitor_widget(state, player, options) and computational_widget(state, player, options) and integrated_widget(state, player, options) and mainframe_widget(state, player, options) and cloud_widget(state, player, options) and quantum_widget(state, player, options) and unshackled_widget(state, player, options) and ascended_widget(state, player, options) and sentient_widget(state, player, options)

def omega_project_casing(state, player, options) -> bool:
	return has_frame(state, player, options, "Omega Casing Factory") and iron_ingot(state, player, options) and copper_ingot(state, player, options) and superconductor(state, player, options) and sentient_widget(state, player, options)

def omega_project_shielding(state, player, options) -> bool:
	return has_frame(state, player, options, "Omega Shielding Plant") and plastic(state, player, options) and bottled_lightning(state, player, options) and portable_reactor(state, player, options) and sentient_widget(state, player, options)

def omega_widget(state, player, options) -> bool:
	return has_frame(state, player, options, "Omega Project Assembler") and widget_amalgamation(state, player, options) and core_amalgamation(state, player, options) and processor_amalgamation(state, player, options) and omega_project_casing(state, player, options) and omega_project_shielding(state, player, options)

def rocket_electronics(state, player, options) -> bool:
	return has_frame(state, player, options, "Rocket Electronics Lab") and processor_amalgamation(state, player, options) and core_amalgamation(state, player, options)

def rocket_fuel(state, player, options) -> bool:
	return has_frame(state, player, options, "Rocket Fuel Distiller") and oil(state, player, options) and fuel_rod(state, player, options) and power(state, player, options)

def rocket_hull(state, player, options) -> bool:
	return has_frame(state, player, options, "Rocket Part Assembler") and omega_project_casing(state, player, options) and omega_project_shielding(state, player, options)

def rocket_segment(state, player, options) -> bool:
	return has_frame(state, player, options, "Omega Launch Facility") and omega_widget(state, player, options) and rocket_hull(state, player, options) and rocket_electronics(state, player, options) and rocket_fuel(state, player, options)