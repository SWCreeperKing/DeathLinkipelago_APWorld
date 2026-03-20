import math
from .Locations import *

# File is Auto-generated, see: [https://github.com/SWCreeperKing/ApWorldFactories/tree/master/ApWorldFactories/Games]

def get_rule_map(player):
	return {
		"Tier 1 Mastery": lambda state: basic_widget(state, player),
		"Deconstruct": lambda state: basic_widget(state, player),
		"Frame Relocation": lambda state: has_frame(state, player, 'Deconstruct') and basic_widget(state, player),
		"Efficient Extraction": lambda state: has_frame(state, player, 'Iron Mine') and basic_widget(state, player),
		"Iron Smelter": lambda state: has_frame(state, player, 'Iron Mine'),
		"Furnace Optimizer": lambda state: has_frame(state, player, 'Iron Smelter') and basic_widget(state, player),
		"Superheated Crucible (Iron Ingot)": lambda state: has_frame(state, player, 'Iron Smelter') and basic_widget(state, player),
		"Widget Factory": lambda state: has_frame(state, player, 'Iron Smelter') and iron_ingot(state, player),
		"Optimized Materials": lambda state: has_frame(state, player, 'Widget Factory') and basic_widget(state, player),
		"Rapid Assembly": lambda state: has_frame(state, player, 'Widget Factory') and basic_widget(state, player),
		"Glitched Frame": lambda state: has_frame(state, player, 'Widget Factory') and basic_widget(state, player),
		"Fortress": lambda state: has_frame(state, player, 'Widget Factory') and basic_widget(state, player),
		"Dig Site": lambda state: has_frame(state, player, 'Widget Factory') and basic_widget(state, player),
		"Tier 2": lambda state: basic_widget(state, player),
		"Tier 2 Mastery": lambda state: spinning_widget(state, player),
		"Warehouse": lambda state: spinning_widget(state, player),
		"Sand Pit": lambda state: basic_widget(state, player),
		"Mechanized Shovels": lambda state: has_frame(state, player, 'Sand Pit') and spinning_widget(state, player),
		"Glass Kiln": lambda state: has_frame(state, player, 'Sand Pit') and basic_widget(state, player),
		"Kiln Governor": lambda state: has_frame(state, player, 'Glass Kiln') and spinning_widget(state, player),
		"Gyroscope Fabricator": lambda state: has_frame(state, player, 'Glass Kiln') and basic_widget(state, player),
		"Widget Spinner": lambda state: has_frame(state, player, 'Gyroscope Fabricator') and basic_widget(state, player),
		"Spin Stabilizer": lambda state: has_frame(state, player, 'Widget Spinner') and spinning_widget(state, player),
		"Gyroscopic Array": lambda state: has_frame(state, player, 'Widget Spinner') and spinning_widget(state, player),
		"Iron-rich Rocks": lambda state: has_frame(state, player, 'Iron Mine') and spinning_widget(state, player),
		"Efficient Loader Arms": lambda state: has_frame(state, player, 'Iron Smelter') and spinning_widget(state, player),
		"High Heat Density": lambda state: has_frame(state, player, 'Superheated Crucible (Iron Ingot)') and spinning_widget(state, player),
		"Widget Twins": lambda state: has_frame(state, player, 'Optimized Materials') and spinning_widget(state, player),
		"Warped Speed": lambda state: has_frame(state, player, 'Glitched Frame') and spinning_widget(state, player),
		"Tier 3": lambda state: spinning_widget(state, player),
		"Construction Overview": lambda state: capacitor_widget(state, player),
		"Pause Construction": lambda state: has_frame(state, player, 'Construction Overview') and capacitor_widget(state, player),
		"Cancel All Construction": lambda state: has_frame(state, player, 'Pause Construction') and capacitor_widget(state, player),
		"Tier 3 Mastery": lambda state: capacitor_widget(state, player),
		"Eminent Domain": lambda state: capacitor_widget(state, player),
		"Clone Layout": lambda state: has_frame(state, player, 'Eminent Domain') and capacitor_widget(state, player),
		"Area Move": lambda state: has_frame(state, player, 'Clone Layout') and capacitor_widget(state, player),
		"Oil Field": lambda state: spinning_widget(state, player),
		"Autopressurizer": lambda state: has_frame(state, player, 'Oil Field') and capacitor_widget(state, player),
		"Black Gold": lambda state: has_frame(state, player, 'Oil Field') and capacitor_widget(state, player),
		"Oil Power Plant": lambda state: has_frame(state, player, 'Oil Field') and spinning_widget(state, player),
		"Flame Stack": lambda state: has_frame(state, player, 'Oil Power Plant') and capacitor_widget(state, player),
		"Battery Assembler": lambda state: has_frame(state, player, 'Oil Power Plant') and spinning_widget(state, player),
		"Superjuiced Upcharger": lambda state: has_frame(state, player, 'Battery Assembler') and capacitor_widget(state, player),
		"Capacitor Bank": lambda state: has_frame(state, player, 'Battery Assembler') and spinning_widget(state, player),
		"Substable Wiring": lambda state: has_frame(state, player, 'Capacitor Bank') and capacitor_widget(state, player),
		"Supercharged Array": lambda state: has_frame(state, player, 'Capacitor Bank') and capacitor_widget(state, player),
		"Logistics Hub": lambda state: has_frame(state, player, 'Capacitor Bank') and capacitor_widget(state, player),
		"Coordinated Logistics": lambda state: has_frame(state, player, 'Logistics Hub') and capacitor_widget(state, player),
		"Napalm Charge": lambda state: has_frame(state, player, 'Logistics Hub') and oil(state, player) and spinning_widget(state, player),
		"Beach Harvest": lambda state: has_frame(state, player, 'Sand Pit') and capacitor_widget(state, player),
		"Molten Conveyor System": lambda state: has_frame(state, player, 'Kiln Governor') and capacitor_widget(state, player),
		"Superheated Crucible (Glass)": lambda state: has_frame(state, player, 'Glass Kiln') and capacitor_widget(state, player),
		"Glass Ball Bearings": lambda state: has_frame(state, player, 'Gyroscope Fabricator') and capacitor_widget(state, player),
		"Core Drilling": lambda state: has_frame(state, player, 'Efficient Extraction') and capacitor_widget(state, player),
		"Ultra-Fast Widget Synthesizer": lambda state: has_frame(state, player, 'Rapid Assembly') and capacitor_widget(state, player),
		"Careful Study": lambda state: has_frame(state, player, 'Dig Site') and capacitor_widget(state, player),
		"Tier 4": lambda state: capacitor_widget(state, player),
		"Eagle Eye": lambda state: computational_widget(state, player),
		"Discerning Vision": lambda state: has_frame(state, player, 'Eagle Eye') and computational_widget(state, player),
		"Tier 4 Mastery": lambda state: computational_widget(state, player),
		"Long Distance Upgrades": lambda state: computational_widget(state, player),
		"Upgrade Status": lambda state: has_frame(state, player, 'Long Distance Upgrades') and computational_widget(state, player),
		"Copper Mine": lambda state: capacitor_widget(state, player),
		"Turbo Drill Motors": lambda state: has_frame(state, player, 'Copper Mine') and computational_widget(state, player),
		"Copper Forge": lambda state: has_frame(state, player, 'Copper Mine') and capacitor_widget(state, player),
		"Forge Attendant": lambda state: has_frame(state, player, 'Copper Forge') and computational_widget(state, player),
		"Rapid Heat Induction Coils": lambda state: has_frame(state, player, 'Copper Forge') and computational_widget(state, player),
		"Plastic Extractor": lambda state: has_frame(state, player, 'Copper Forge') and capacitor_widget(state, player),
		"Enhanced Chemical Mixer": lambda state: has_frame(state, player, 'Plastic Extractor') and computational_widget(state, player),
		"Circuit Fab": lambda state: has_frame(state, player, 'Plastic Extractor') and capacitor_widget(state, player),
		"Computational Engine": lambda state: has_frame(state, player, 'Circuit Fab') and capacitor_widget(state, player),
		"Enhanced Logic Synthesizer": lambda state: has_frame(state, player, 'Computational Engine') and computational_widget(state, player),
		"Rapid Component Feeder": lambda state: has_frame(state, player, 'Computational Engine') and computational_widget(state, player),
		"Peat Oil Processing": lambda state: has_frame(state, player, 'Autopressurizer') and computational_widget(state, player),
		"Power Plant Logistics": lambda state: has_frame(state, player, 'Oil Power Plant') and computational_widget(state, player),
		"High Yield Compressor": lambda state: has_frame(state, player, 'Flame Stack') and computational_widget(state, player),
		"Depletion Recycler": lambda state: has_frame(state, player, 'Battery Assembler') and computational_widget(state, player),
		"Expanded Shelf Storage": lambda state: has_frame(state, player, 'Warehouse') and computational_widget(state, player),
		"Bucket Excavator": lambda state: has_frame(state, player, 'Mechanized Shovels') and computational_widget(state, player),
		"Glass Shard Recombinator": lambda state: has_frame(state, player, 'Glass Kiln') and computational_widget(state, player),
		"Direct Glass Insertion": lambda state: has_frame(state, player, 'Gyroscope Fabricator') and computational_widget(state, player),
		"Tuned Spinners": lambda state: has_frame(state, player, 'Gyroscopic Array') and computational_widget(state, player),
		"Glass Grinding Wheel": lambda state: has_frame(state, player, 'Gyroscopic Array') and computational_widget(state, player),
		"Industrial Capacity": lambda state: has_frame(state, player, 'Furnace Optimizer') and computational_widget(state, player),
		"Precision Widgeteering": lambda state: has_frame(state, player, 'Optimized Materials') and computational_widget(state, player),
		"Unnatural Duplication": lambda state: has_frame(state, player, 'Warped Speed') and computational_widget(state, player),
		"Tier 5": lambda state: computational_widget(state, player),
		"Tier 5 Mastery": lambda state: integrated_widget(state, player),
		"Tesla Coil": lambda state: computational_widget(state, player),
		"Rapid Charge Collector": lambda state: has_frame(state, player, 'Tesla Coil') and integrated_widget(state, player),
		"Core Foundry": lambda state: has_frame(state, player, 'Tesla Coil') and computational_widget(state, player),
		"Rudimentary Synapse Connector": lambda state: has_frame(state, player, 'Tesla Coil') and integrated_widget(state, player),
		"Integrator": lambda state: has_frame(state, player, 'Core Foundry') and computational_widget(state, player),
		"Synapse Fusion Unit": lambda state: has_frame(state, player, 'Integrator') and integrated_widget(state, player),
		"Rapid Coupler": lambda state: has_frame(state, player, 'Integrator') and integrated_widget(state, player),
		"Recycler": lambda state: has_frame(state, player, 'Integrator') and integrated_widget(state, player),
		"Rubble Grinder": lambda state: has_frame(state, player, 'Recycler') and integrated_widget(state, player),
		"Excavator": lambda state: has_frame(state, player, 'Recycler') and integrated_widget(state, player),
		"Giant Rock Crusher": lambda state: has_frame(state, player, 'Copper Mine') and integrated_widget(state, player),
		"Advanced Alloy Mixer": lambda state: has_frame(state, player, 'Copper Forge') and integrated_widget(state, player),
		"Slash And Burn": lambda state: has_frame(state, player, 'Rapid Heat Induction Coils') and integrated_widget(state, player),
		"Hyper-Speed Assembly Line": lambda state: has_frame(state, player, 'Circuit Fab') and integrated_widget(state, player),
		"Auxiliary Pump Stack": lambda state: has_frame(state, player, 'Black Gold') and integrated_widget(state, player),
		"Heat Recirculator": lambda state: has_frame(state, player, 'High Yield Compressor') and integrated_widget(state, player),
		"Hydrophobia": lambda state: has_frame(state, player, 'Battery Assembler') and integrated_widget(state, player),
		"Dedicated Battery Inserters": lambda state: has_frame(state, player, 'Substable Wiring') and integrated_widget(state, player),
		"Rapid Discharge Fabricator": lambda state: has_frame(state, player, 'Supercharged Array') and integrated_widget(state, player),
		"Optimized Supply Lines": lambda state: has_frame(state, player, 'Logistics Hub') and integrated_widget(state, player),
		"Perfectly Balanced Spinner": lambda state: has_frame(state, player, 'Glass Ball Bearings') and integrated_widget(state, player),
		"Gyroscope Sharing Plan": lambda state: has_frame(state, player, 'Spin Stabilizer') and integrated_widget(state, player),
		"Dig Deeper": lambda state: has_frame(state, player, 'Core Drilling') and integrated_widget(state, player),
		"Turbo Blast Furnace": lambda state: has_frame(state, player, 'Superheated Crucible (Iron Ingot)') and integrated_widget(state, player),
		"Omni-Assembler Core": lambda state: has_frame(state, player, 'Ultra-Fast Widget Synthesizer') and integrated_widget(state, player),
		"Tier 6": lambda state: integrated_widget(state, player),
		"Tier 6 Mastery": lambda state: mainframe_widget(state, player),
		"The Factory Must Grow": lambda state: mainframe_widget(state, player),
		"Silicon Extruder": lambda state: integrated_widget(state, player),
		"Swift Wafer Synthesizer": lambda state: has_frame(state, player, 'Silicon Extruder') and mainframe_widget(state, player),
		"Processor Lab": lambda state: has_frame(state, player, 'Silicon Extruder') and integrated_widget(state, player),
		"Extreme-UV Protocol": lambda state: has_frame(state, player, 'Processor Lab') and mainframe_widget(state, player),
		"Mainframe Assembler": lambda state: has_frame(state, player, 'Processor Lab') and integrated_widget(state, player),
		"Enhanced Data Synthesizer": lambda state: has_frame(state, player, 'Mainframe Assembler') and mainframe_widget(state, player),
		"Rapid Circuit Integrator": lambda state: has_frame(state, player, 'Mainframe Assembler') and mainframe_widget(state, player),
		"Indentured Servitude": lambda state: has_frame(state, player, 'Mainframe Assembler') and mainframe_widget(state, player),
		"Graveyard": lambda state: has_frame(state, player, 'Indentured Servitude') and mainframe_widget(state, player),
		"Chain Lightning": lambda state: has_frame(state, player, 'Tesla Coil') and mainframe_widget(state, player),
		"Efficient Neural Matrix": lambda state: has_frame(state, player, 'Core Foundry') and mainframe_widget(state, player),
		"Introvert": lambda state: has_frame(state, player, 'Core Foundry') and mainframe_widget(state, player),
		"Reclaim Sorting System": lambda state: has_frame(state, player, 'Rubble Grinder') and mainframe_widget(state, player),
		"Hyper-Speed Conveyor System": lambda state: has_frame(state, player, 'Turbo Drill Motors') and mainframe_widget(state, player),
		"Shortened Transfer Tube": lambda state: has_frame(state, player, 'Plastic Extractor') and mainframe_widget(state, player),
		"Advanced Refining Chamber": lambda state: has_frame(state, player, 'Enhanced Chemical Mixer') and mainframe_widget(state, player),
		"Precision Assembly Matrix": lambda state: has_frame(state, player, 'Circuit Fab') and mainframe_widget(state, player),
		"Agoraphobia": lambda state: has_frame(state, player, 'Circuit Fab') and mainframe_widget(state, player),
		"Standalone": lambda state: has_frame(state, player, 'Enhanced Logic Synthesizer') and mainframe_widget(state, player),
		"Accelerated Component Placement": lambda state: has_frame(state, player, 'Rapid Component Feeder') and mainframe_widget(state, player),
		"Exhaust Vent Recycler": lambda state: has_frame(state, player, 'Heat Recirculator') and mainframe_widget(state, player),
		"Rapid Heat Exchanger (Battery)": lambda state: has_frame(state, player, 'Superjuiced Upcharger') and mainframe_widget(state, player),
		"Energy Optimization Core": lambda state: has_frame(state, player, 'Substable Wiring') and mainframe_widget(state, player),
		"Warehouse Shelf Stacker": lambda state: has_frame(state, player, 'Expanded Shelf Storage') and mainframe_widget(state, player),
		"Grain Matrix Duplicator": lambda state: has_frame(state, player, 'Bucket Excavator') and mainframe_widget(state, player),
		"Rapid Heat Exchanger (Glass)": lambda state: has_frame(state, player, 'Superheated Crucible (Glass)') and mainframe_widget(state, player),
		"Counterspin Anchors": lambda state: has_frame(state, player, 'Tuned Spinners') and mainframe_widget(state, player),
		"Double-stacked Conveyors": lambda state: has_frame(state, player, 'Efficient Loader Arms') and mainframe_widget(state, player),
		"Productivity Optimization Node": lambda state: has_frame(state, player, 'Precision Widgeteering') and mainframe_widget(state, player),
		"Dutiful Archivist": lambda state: has_frame(state, player, 'Careful Study') and mainframe_widget(state, player),
		"Tier 7": lambda state: mainframe_widget(state, player),
		"Tier 7 Mastery": lambda state: cloud_widget(state, player) and fuel_rod(state, player),
		"Auto Upgrade": lambda state: cloud_widget(state, player) and fuel_rod(state, player),
		"Uranium Mine": lambda state: mainframe_widget(state, player),
		"Rapid Extraction Module": lambda state: has_frame(state, player, 'Uranium Mine') and cloud_widget(state, player) and fuel_rod(state, player),
		"Fuel Rod Assembler": lambda state: has_frame(state, player, 'Uranium Mine') and mainframe_widget(state, player),
		"Accelerated Molding Unit": lambda state: has_frame(state, player, 'Fuel Rod Assembler') and cloud_widget(state, player) and fuel_rod(state, player),
		"Nuclear Power Plant": lambda state: has_frame(state, player, 'Fuel Rod Assembler') and mainframe_widget(state, player),
		"Advanced Heat Exchanger": lambda state: has_frame(state, player, 'Nuclear Power Plant') and cloud_widget(state, player) and fuel_rod(state, player),
		"Cloud Digitizer": lambda state: has_frame(state, player, 'Nuclear Power Plant') and mainframe_widget(state, player),
		"Multi-Core Upload System": lambda state: has_frame(state, player, 'Cloud Digitizer') and cloud_widget(state, player) and fuel_rod(state, player),
		"Swift Transfer Protocol": lambda state: has_frame(state, player, 'Cloud Digitizer') and cloud_widget(state, player) and fuel_rod(state, player),
		"Monocrystalline": lambda state: has_frame(state, player, 'Silicon Extruder') and cloud_widget(state, player) and fuel_rod(state, player),
		"Microfine Engraving": lambda state: has_frame(state, player, 'Processor Lab') and cloud_widget(state, player),
		"Automated Chapel": lambda state: has_frame(state, player, 'Graveyard') and cloud_widget(state, player),
		"Multi-Bolt Capture Array": lambda state: has_frame(state, player, 'Rapid Charge Collector') and cloud_widget(state, player),
		"Lightning Interface": lambda state: has_frame(state, player, 'Rapid Coupler') and cloud_widget(state, player) and fuel_rod(state, player),
		"Extrovert": lambda state: has_frame(state, player, 'Rapid Coupler') and cloud_widget(state, player) and fuel_rod(state, player),
		"Autonomous Garbage Collectors": lambda state: has_frame(state, player, 'Reclaim Sorting System') and cloud_widget(state, player) and fuel_rod(state, player),
		"Autosifter": lambda state: has_frame(state, player, 'Excavator') and cloud_widget(state, player) and fuel_rod(state, player),
		"Dense Packing Grid": lambda state: has_frame(state, player, 'Forge Attendant') and cloud_widget(state, player) and fuel_rod(state, player),
		"Advanced Circuit Optimization": lambda state: has_frame(state, player, 'Enhanced Logic Synthesizer') and cloud_widget(state, player) and fuel_rod(state, player),
		"Pipe Repressurizer": lambda state: has_frame(state, player, 'Auxiliary Pump Stack') and cloud_widget(state, player),
		"Instantaneous Charge Module": lambda state: has_frame(state, player, 'Rapid Discharge Fabricator') and cloud_widget(state, player) and fuel_rod(state, player),
		"Lightspeed Rotation": lambda state: has_frame(state, player, 'Gyroscope Fabricator') and cloud_widget(state, player) and fuel_rod(state, player),
		"Calculated Material Distribution": lambda state: has_frame(state, player, 'Gyroscope Sharing Plan') and cloud_widget(state, player) and fuel_rod(state, player),
		"Uranium-powered Drills": lambda state: has_frame(state, player, 'Dig Deeper') and cloud_widget(state, player) and fuel_rod(state, player),
		"Infinite Widget Matrix": lambda state: has_frame(state, player, 'Omni-Assembler Core') and cloud_widget(state, player),
		"Tier 8": lambda state: cloud_widget(state, player),
		"Tier 8 Mastery": lambda state: quantum_widget(state, player),
		"Widget Minitizers": lambda state: cloud_widget(state, player),
		"Enhanced Particle Compressor": lambda state: has_frame(state, player, 'Widget Minitizers') and quantum_widget(state, player),
		"Quantum Shrink Matrix": lambda state: has_frame(state, player, 'Enhanced Particle Compressor') and quantum_widget(state, player),
		"Nanoscale Lab": lambda state: has_frame(state, player, 'Widget Minitizers') and cloud_widget(state, player),
		"Quantum Lithography": lambda state: has_frame(state, player, 'Nanoscale Lab') and quantum_widget(state, player),
		"Reactor Foundry": lambda state: has_frame(state, player, 'Nanoscale Lab') and cloud_widget(state, player),
		"Subatomic Power Booster": lambda state: has_frame(state, player, 'Reactor Foundry') and quantum_widget(state, player),
		"Quantum Tunneler": lambda state: has_frame(state, player, 'Reactor Foundry') and cloud_widget(state, player),
		"High-Efficiency Particle Matrix": lambda state: has_frame(state, player, 'Quantum Tunneler') and quantum_widget(state, player),
		"Rapid Particle Integrator": lambda state: has_frame(state, player, 'Quantum Tunneler') and quantum_widget(state, player),
		"City Builder": lambda state: has_frame(state, player, 'Rapid Particle Integrator') and quantum_widget(state, player),
		"Blitz Upgrade": lambda state: has_frame(state, player, 'Auto Upgrade') and quantum_widget(state, player),
		"Fallout": lambda state: has_frame(state, player, 'Uranium Mine') and quantum_widget(state, player),
		"Multi-Stage Refinement": lambda state: has_frame(state, player, 'Fuel Rod Assembler') and quantum_widget(state, player),
		"Green Energy": lambda state: has_frame(state, player, 'Fuel Rod Assembler') and quantum_widget(state, player),
		"Precision Control Rods": lambda state: has_frame(state, player, 'Advanced Heat Exchanger') and quantum_widget(state, player),
		"Rapid Crystal Formation Chamber": lambda state: has_frame(state, player, 'Swift Wafer Synthesizer') and quantum_widget(state, player),
		"Suburban Development": lambda state: has_frame(state, player, 'Processor Lab') and quantum_widget(state, player),
		"Binary Pairs": lambda state: has_frame(state, player, 'Enhanced Data Synthesizer') and quantum_widget(state, player),
		"Hyper-Speed Compiler": lambda state: has_frame(state, player, 'Rapid Circuit Integrator') and quantum_widget(state, player),
		"Efficient Value Extraction": lambda state: has_frame(state, player, 'Indentured Servitude') and quantum_widget(state, player),
		"Rapid Cognitive Assembler": lambda state: has_frame(state, player, 'Rudimentary Synapse Connector') and quantum_widget(state, player),
		"Quantum Logic Synthesizer": lambda state: has_frame(state, player, 'Synapse Fusion Unit') and quantum_widget(state, player),
		"Universal Recycling Schema": lambda state: has_frame(state, player, 'Autonomous Garbage Collectors') and quantum_widget(state, player),
		"High-Yield Extraction System": lambda state: has_frame(state, player, 'Hyper-Speed Conveyor System') and quantum_widget(state, player),
		"Quantum Heat Exchanger": lambda state: has_frame(state, player, 'Slash And Burn') and quantum_widget(state, player),
		"Yield Optimization Catalyst": lambda state: has_frame(state, player, 'Advanced Refining Chamber') and quantum_widget(state, player),
		"Turbo Soldering Station": lambda state: has_frame(state, player, 'Hyper-Speed Assembly Line') and quantum_widget(state, player),
		"Hyper-Speed Arithmetic Processor": lambda state: has_frame(state, player, 'Accelerated Component Placement') and quantum_widget(state, player),
		"Monopole Battery Tech": lambda state: has_frame(state, player, 'Depletion Recycler') and quantum_widget(state, player),
		"Nano-Capacitor Synthesizer": lambda state: has_frame(state, player, 'Energy Optimization Core') and quantum_widget(state, player),
		"Lost Package Tracker": lambda state: has_frame(state, player, 'Optimized Supply Lines') and quantum_widget(state, player),
		"Extradimensional Storage Lockers": lambda state: has_frame(state, player, 'Warehouse Shelf Stacker') and quantum_widget(state, player),
		"Unified Theory of Sand": lambda state: has_frame(state, player, 'Grain Matrix Duplicator') and quantum_widget(state, player),
		"Hyperfine Glass Distributor": lambda state: has_frame(state, player, 'Glass Shard Recombinator') and quantum_widget(state, player),
		"Spacetime Spin Matrix": lambda state: has_frame(state, player, 'Counterspin Anchors') and quantum_widget(state, player),
		"Hyper-Production Matrix": lambda state: has_frame(state, player, 'Precision Widgeteering') and quantum_widget(state, player),
		"Mitosis": lambda state: has_frame(state, player, 'Unnatural Duplication') and quantum_widget(state, player),
		"Boundless Patience": lambda state: has_frame(state, player, 'Dutiful Archivist') and quantum_widget(state, player),
		"Tier 9": lambda state: quantum_widget(state, player),
		"Tier 9 Mastery": lambda state: unshackled_widget(state, player),
		"New World Order": lambda state: unshackled_widget(state, player),
		"Helium Extractor": lambda state: quantum_widget(state, player),
		"Subatomic Yield Booster (Helium)": lambda state: has_frame(state, player, 'Helium Extractor') and unshackled_widget(state, player),
		"Conductor Foundry": lambda state: has_frame(state, player, 'Helium Extractor') and quantum_widget(state, player),
		"Lightning Flux Unit": lambda state: has_frame(state, player, 'Conductor Foundry') and unshackled_widget(state, player),
		"AI Laboratory": lambda state: has_frame(state, player, 'Conductor Foundry') and quantum_widget(state, player),
		"Quantum Neural Matrix": lambda state: has_frame(state, player, 'AI Laboratory') and unshackled_widget(state, player),
		"AI Delimiter": lambda state: has_frame(state, player, 'AI Laboratory') and quantum_widget(state, player),
		"Advanced Cognitive Network": lambda state: has_frame(state, player, 'AI Delimiter') and unshackled_widget(state, player),
		"Neural Accelerator": lambda state: has_frame(state, player, 'AI Delimiter') and unshackled_widget(state, player),
		"Direct Widget Insertion": lambda state: has_frame(state, player, 'Widget Minitizers') and unshackled_widget(state, player),
		"Superconducting Collider Matrix": lambda state: has_frame(state, player, 'Quantum Shrink Matrix') and unshackled_widget(state, player),
		"Precision Atom Placement": lambda state: has_frame(state, player, 'Nanoscale Lab') and unshackled_widget(state, player),
		"Relics of the Past": lambda state: has_frame(state, player, 'Nanoscale Lab') and unshackled_widget(state, player),
		"Rapid Core Integrator": lambda state: has_frame(state, player, 'Reactor Foundry') and unshackled_widget(state, player),
		"Accelerated Entanglement": lambda state: has_frame(state, player, 'Rapid Particle Integrator') and unshackled_widget(state, player),
		"Nuclear Bore Engine": lambda state: has_frame(state, player, 'Rapid Extraction Module') and unshackled_widget(state, player),
		"Direct Core Cooling": lambda state: has_frame(state, player, 'Nuclear Power Plant') and unshackled_widget(state, player),
		"Superconducting Fuel Chamber": lambda state: has_frame(state, player, 'Precision Control Rods') and unshackled_widget(state, player),
		"Datacenter Access": lambda state: has_frame(state, player, 'Multi-Core Upload System') and unshackled_widget(state, player),
		"Quantum Integration Matrix": lambda state: has_frame(state, player, 'Multi-Core Upload System') and unshackled_widget(state, player),
		"Rapid Cloud Integrator": lambda state: has_frame(state, player, 'Swift Transfer Protocol') and unshackled_widget(state, player),
		"Rapid Logic Preprocessor": lambda state: has_frame(state, player, 'Extreme-UV Protocol') and unshackled_widget(state, player),
		"Multi-Core Processor": lambda state: has_frame(state, player, 'Enhanced Data Synthesizer') and unshackled_widget(state, player),
		"Incinerator": lambda state: has_frame(state, player, 'Graveyard') and unshackled_widget(state, player),
		"Turbo Lightning Rods": lambda state: has_frame(state, player, 'Multi-Bolt Capture Array') and unshackled_widget(state, player),
		"Thought Integration Unit": lambda state: has_frame(state, player, 'Efficient Neural Matrix') and unshackled_widget(state, player),
		"Ultra-Quick Integrator": lambda state: has_frame(state, player, 'Lightning Interface') and unshackled_widget(state, player),
		"Automated Grading": lambda state: has_frame(state, player, 'Autosifter') and unshackled_widget(state, player),
		"Ore-to-Ingot Optimization System": lambda state: has_frame(state, player, 'Advanced Alloy Mixer') and unshackled_widget(state, player),
		"Quantum Circuitry Optimizer": lambda state: has_frame(state, player, 'Precision Assembly Matrix') and unshackled_widget(state, player),
		"Multi-Tasking Calculation Node": lambda state: has_frame(state, player, 'Advanced Circuit Optimization') and unshackled_widget(state, player),
		"Pressurized Storage Vats": lambda state: has_frame(state, player, 'Pipe Repressurizer') and unshackled_widget(state, player),
		"Ultra-Fast Circuit Integrator": lambda state: has_frame(state, player, 'Instantaneous Charge Module') and unshackled_widget(state, player),
		"Gyroscope Hyperprocessor": lambda state: has_frame(state, player, 'Lightspeed Rotation') and unshackled_widget(state, player),
		"Excess Spin Utilizer": lambda state: has_frame(state, player, 'Gyroscope Sharing Plan') and unshackled_widget(state, player),
		"Tier 10": lambda state: unshackled_widget(state, player),
		"Tier 10 Mastery": lambda state: ascended_widget(state, player),
		"Training Center": lambda state: unshackled_widget(state, player),
		"Advanced Cognitive Compiler": lambda state: has_frame(state, player, 'Training Center') and ascended_widget(state, player),
		"Data Transformer": lambda state: has_frame(state, player, 'Training Center') and unshackled_widget(state, player),
		"Expedite Ascension": lambda state: has_frame(state, player, 'Data Transformer') and unshackled_widget(state, player),
		"Ascension Facility": lambda state: has_frame(state, player, 'Data Transformer') and unshackled_widget(state, player),
		"Unleashed Thought Matrix": lambda state: has_frame(state, player, 'Ascension Facility') and ascended_widget(state, player),
		"Rapid Cognition Compiler": lambda state: has_frame(state, player, 'Ascension Facility') and ascended_widget(state, player),
		"Leveler": lambda state: has_frame(state, player, 'Ascension Facility') and ascended_widget(state, player),
		"Gaseous Bedrock": lambda state: has_frame(state, player, 'Helium Extractor') and ascended_widget(state, player),
		"Precision Gas Separator": lambda state: has_frame(state, player, 'Subatomic Yield Booster (Helium)') and ascended_widget(state, player),
		"Quantum Flux Matrix": lambda state: has_frame(state, player, 'Conductor Foundry') and ascended_widget(state, player),
		"Resource Management": lambda state: has_frame(state, player, 'Conductor Foundry') and ascended_widget(state, player),
		"Rapid AI Synthesizer": lambda state: has_frame(state, player, 'Quantum Neural Matrix') and ascended_widget(state, player),
		"Multi-Phase Logic Processor": lambda state: has_frame(state, player, 'Advanced Cognitive Network') and ascended_widget(state, player),
		"Upgraded AI Compiler": lambda state: has_frame(state, player, 'Neural Accelerator') and ascended_widget(state, player),
		"Subatomic Yield Booster (Widget Particle)": lambda state: has_frame(state, player, 'Superconducting Collider Matrix') and ascended_widget(state, player),
		"Industrial Espionage": lambda state: has_frame(state, player, 'Reactor Foundry') and ascended_widget(state, player),
		"Subatomic Yield Optimizer": lambda state: has_frame(state, player, 'High-Efficiency Particle Matrix') and ascended_widget(state, player),
		"Cowboy Coding": lambda state: has_frame(state, player, 'Quantum Tunneler') and ascended_widget(state, player),
		"Lightning Upgrade": lambda state: has_frame(state, player, 'Blitz Upgrade') and ascended_widget(state, player),
		"Rapid Rod Fabricator": lambda state: has_frame(state, player, 'Accelerated Molding Unit') and ascended_widget(state, player),
		"Quantum Efficiency Reactor": lambda state: has_frame(state, player, 'Superconducting Fuel Chamber') and ascended_widget(state, player),
		"Yield Maximization Reactor": lambda state: has_frame(state, player, 'Rapid Crystal Formation Chamber') and ascended_widget(state, player),
		"N-Step Branch Prediction": lambda state: has_frame(state, player, 'Microfine Engraving') and unshackled_widget(state, player),
		"Lightning Data Bus": lambda state: has_frame(state, player, 'Hyper-Speed Compiler') and ascended_widget(state, player),
		"High Intensity Furnace": lambda state: has_frame(state, player, 'Incinerator') and ascended_widget(state, player),
		"Remnants of Humanity": lambda state: has_frame(state, player, 'Efficient Value Extraction') and ascended_widget(state, player),
		"Yield Maximization Protocol": lambda state: has_frame(state, player, 'Quantum Logic Synthesizer') and ascended_widget(state, player),
		"Advanced Mining Protocol": lambda state: has_frame(state, player, 'High-Yield Extraction System') and ascended_widget(state, player),
		"Rapid Refinement Module": lambda state: has_frame(state, player, 'Yield Optimization Catalyst') and ascended_widget(state, player),
		"Ultra-Quick Logic Compiler": lambda state: has_frame(state, player, 'Hyper-Speed Arithmetic Processor') and ascended_widget(state, player),
		"High-Efficiency Capacitor Matrix": lambda state: has_frame(state, player, 'Energy Optimization Core') and ascended_widget(state, player),
		"Infinite Storage Glitch": lambda state: has_frame(state, player, 'Extradimensional Storage Lockers') and ascended_widget(state, player),
		"Tier 11": lambda state: ascended_widget(state, player),
		"Tier 11 Mastery": lambda state: sentient_widget(state, player),
		"Absolute Dominion": lambda state: sentient_widget(state, player),
		"Perpetual Motion Machine": lambda state: ascended_widget(state, player),
		"Physics Engine Decoder": lambda state: has_frame(state, player, 'Perpetual Motion Machine') and sentient_widget(state, player),
		"Sentience Facility": lambda state: has_frame(state, player, 'Perpetual Motion Machine') and ascended_widget(state, player),
		"Sentience Recombobulator": lambda state: has_frame(state, player, 'Sentience Facility') and sentient_widget(state, player),
		"Picoscale Lab": lambda state: has_frame(state, player, 'Sentience Facility') and ascended_widget(state, player),
		"Enhanced Production Algorithms": lambda state: has_frame(state, player, 'Picoscale Lab') and sentient_widget(state, player),
		"Sentience Aggregator": lambda state: has_frame(state, player, 'Picoscale Lab') and ascended_widget(state, player),
		"Processor Sharing System": lambda state: has_frame(state, player, 'Sentience Aggregator') and sentient_widget(state, player),
		"Thought Enhancer Matrix": lambda state: has_frame(state, player, 'Sentience Aggregator') and sentient_widget(state, player),
		"History Lesson": lambda state: has_frame(state, player, 'Training Center') and sentient_widget(state, player),
		"Rapid Spec Synthesizer": lambda state: has_frame(state, player, 'Advanced Cognitive Compiler') and sentient_widget(state, player),
		"Advanced Cognitive Release": lambda state: has_frame(state, player, 'Data Transformer') and sentient_widget(state, player),
		"Wild Mutation": lambda state: has_frame(state, player, 'Data Transformer') and sentient_widget(state, player),
		"Advanced Neural Compiler": lambda state: has_frame(state, player, 'Unleashed Thought Matrix') and sentient_widget(state, player),
		"Frictionless Neural Compiler": lambda state: has_frame(state, player, 'Rapid Cognition Compiler') and sentient_widget(state, player),
		"Enhanced Helium Synthesizer": lambda state: has_frame(state, player, 'Precision Gas Separator') and sentient_widget(state, player),
		"Hyper-Speed Magnet Chamber": lambda state: has_frame(state, player, 'Lightning Flux Unit') and sentient_widget(state, player),
		"Hello World": lambda state: has_frame(state, player, 'AI Laboratory') and sentient_widget(state, player),
		"Optimized Neuron Compiler": lambda state: has_frame(state, player, 'Rapid AI Synthesizer') and sentient_widget(state, player),
		"Trinity": lambda state: has_frame(state, player, 'AI Delimiter') and sentient_widget(state, player),
		"Accelerated Thought Synthesizer": lambda state: has_frame(state, player, 'Upgraded AI Compiler') and sentient_widget(state, player),
		"Hyper-Accelerated Fabricator": lambda state: has_frame(state, player, 'Quantum Lithography') and sentient_widget(state, player),
		"Multi-Fuel Synthesizer": lambda state: has_frame(state, player, 'Subatomic Power Booster') and sentient_widget(state, player),
		"Stellar Quantum Weaver": lambda state: has_frame(state, player, 'Accelerated Entanglement') and sentient_widget(state, player),
		"Radiometric Ore Separator": lambda state: has_frame(state, player, 'Nuclear Bore Engine') and sentient_widget(state, player),
		"Isotope Yield Booster": lambda state: has_frame(state, player, 'Multi-Stage Refinement') and sentient_widget(state, player),
		"Data Yield Optimizer": lambda state: has_frame(state, player, 'Quantum Integration Matrix') and sentient_widget(state, player),
		"Hyper-Speed Data Link": lambda state: has_frame(state, player, 'Rapid Cloud Integrator') and sentient_widget(state, player),
		"Data Stream Optimizer": lambda state: has_frame(state, player, 'Multi-Core Processor') and sentient_widget(state, player),
		"High-Capacity Energy Condenser": lambda state: has_frame(state, player, 'Turbo Lightning Rods') and sentient_widget(state, player),
		"Swift Logic Gate Fabricator": lambda state: has_frame(state, player, 'Ultra-Quick Integrator') and sentient_widget(state, player),
		"Pristine Protection Protocol": lambda state: has_frame(state, player, 'Automated Grading') and sentient_widget(state, player),
		"Advanced Arithmetic Processor": lambda state: has_frame(state, player, 'Advanced Circuit Optimization') and sentient_widget(state, player),
		"Tier 12": lambda state: sentient_widget(state, player),
		"Tier 12 Mastery": lambda state: omega_widget(state, player),
		"Omega Processor Lab": lambda state: sentient_widget(state, player),
		"Omega Core Foundry": lambda state: has_frame(state, player, 'Omega Processor Lab') and sentient_widget(state, player),
		"Rocket Electronics Lab": lambda state: has_frame(state, player, 'Omega Core Foundry') and omega_widget(state, player),
		"Omega Widget Distiller": lambda state: has_frame(state, player, 'Omega Core Foundry') and sentient_widget(state, player),
		"Rocket Fuel Distiller": lambda state: has_frame(state, player, 'Omega Widget Distiller') and omega_widget(state, player),
		"Omega Casing Factory": lambda state: has_frame(state, player, 'Omega Widget Distiller') and sentient_widget(state, player),
		"Omega Shielding Plant": lambda state: has_frame(state, player, 'Omega Casing Factory') and sentient_widget(state, player),
		"Rocket Part Assembler": lambda state: has_frame(state, player, 'Omega Shielding Plant') and omega_widget(state, player),
		"Omega Project Assembler": lambda state: has_frame(state, player, 'Omega Shielding Plant') and sentient_widget(state, player),
		"Omega Launch Facility": lambda state: has_frame(state, player, 'Omega Project Assembler') and omega_widget(state, player),
		"Omega Limit Break": lambda state: has_frame(state, player, 'Physics Engine Decoder') and omega_widget(state, player),
		"Glitch in the System": lambda state: has_frame(state, player, 'Perpetual Motion Machine') and omega_widget(state, player),
		"Omega Thought Processor": lambda state: has_frame(state, player, 'Sentience Facility') and omega_widget(state, player),
		"Myriad Landscape": lambda state: has_frame(state, player, 'Sentience Facility') and omega_widget(state, player),
		"Omega Yield Enhancer": lambda state: has_frame(state, player, 'Picoscale Lab') and omega_widget(state, player),
		"Generational Uplift": lambda state: has_frame(state, player, 'Picoscale Lab') and omega_widget(state, player),
		"Omega Assembly Lab": lambda state: has_frame(state, player, 'Processor Sharing System') and omega_widget(state, player),
		"Stepping Stone To Greatness": lambda state: has_frame(state, player, 'Sentience Aggregator') and omega_widget(state, player),
		"Omega Sentience Circuitry": lambda state: has_frame(state, player, 'Thought Enhancer Matrix') and omega_widget(state, player),
		"Omega Training Compiler": lambda state: has_frame(state, player, 'Rapid Spec Synthesizer') and omega_widget(state, player),
		"Omega Matrix Integrator": lambda state: has_frame(state, player, 'Expedite Ascension') and omega_widget(state, player),
		"Omega Cognitive Engine": lambda state: has_frame(state, player, 'Advanced Neural Compiler') and omega_widget(state, player),
		"Beacon of Ascension": lambda state: has_frame(state, player, 'Ascension Facility') and omega_widget(state, player),
		"Omega Ascension Planner": lambda state: has_frame(state, player, 'Frictionless Neural Compiler') and omega_widget(state, player),
		"Omega Extraction Matrix": lambda state: has_frame(state, player, 'Enhanced Helium Synthesizer') and omega_widget(state, player),
		"Omega Magnetizer Unit": lambda state: has_frame(state, player, 'Quantum Flux Matrix') and omega_widget(state, player),
		"Omega Thought Conductor": lambda state: has_frame(state, player, 'Optimized Neuron Compiler') and omega_widget(state, player),
		"Omega Neural Matrix": lambda state: has_frame(state, player, 'Multi-Phase Logic Processor') and omega_widget(state, player),
		"Omega Etching System": lambda state: has_frame(state, player, 'Precision Atom Placement') and omega_widget(state, player),
		"Omega Containment Field": lambda state: has_frame(state, player, 'Rapid Core Integrator') and omega_widget(state, player),
		"Omega Entanglement Field": lambda state: has_frame(state, player, 'Subatomic Yield Optimizer') and omega_widget(state, player),
		"Omega Mining Protocol": lambda state: has_frame(state, player, 'Radiometric Ore Separator') and omega_widget(state, player),
		"Omega Cloud Synthesizer": lambda state: has_frame(state, player, 'Quantum Integration Matrix') and omega_widget(state, player),
		"Omega Accelerated Digitizer": lambda state: has_frame(state, player, 'Hyper-Speed Data Link') and omega_widget(state, player),
		"Omega Crystal Stabilizer": lambda state: has_frame(state, player, 'Yield Maximization Reactor') and omega_widget(state, player),
		"Omega Logic Amplifier": lambda state: has_frame(state, player, 'Multi-Core Processor') and omega_widget(state, player),
		"Omega Circuit Weaver": lambda state: has_frame(state, player, 'Lightning Data Bus') and omega_widget(state, player),
		"Omega Assembly Core": lambda state: has_frame(state, player, 'Quantum Logic Synthesizer') and omega_widget(state, player),
	}

def has_amount(state, player, item, amount) -> bool:
	return state.has(item, player, amount)

def has(state, player, item) -> bool:
	return has_amount(state, player, item, 1)

def has_any(state, player, items) -> bool:
	return any(has(state, player, item) for item in items)

def has_all(state, player, items) -> bool:
	return all(has(state, player, item) for item in items)

def has_tier(state, player, tier) -> bool:
	return has_amount(state, player, 'Progressive Tier', tier)

def has_frame(state, player, frame) -> bool:
	return has(state, player, frame)

def iron_ore(state, player) -> bool:
	return has_frame(state, player, 'Iron Mine')

def sand(state, player) -> bool:
	return has_frame(state, player, 'Sand Pit')

def oil(state, player) -> bool:
	return has_frame(state, player, 'Oil Field')

def copper_ore(state, player) -> bool:
	return has_frame(state, player, 'Copper Mine')

def iron_ingot(state, player) -> bool:
	return has_frame(state, player, "Iron Smelter") and iron_ore(state, player)

def basic_widget(state, player) -> bool:
	return has_frame(state, player, "Widget Factory") and iron_ingot(state, player)

def glass(state, player) -> bool:
	return has_frame(state, player, "Glass Kiln") and sand(state, player)

def gyroscope(state, player) -> bool:
	return has_frame(state, player, "Gyroscope Fabricator") and glass(state, player) and basic_widget(state, player)

def power(state, player) -> bool:
	return has_frame(state, player, "Oil Power Plant") and oil(state, player)

def spinning_widget(state, player) -> bool:
	return has_frame(state, player, "Widget Spinner") and gyroscope(state, player) and basic_widget(state, player)

def battery(state, player) -> bool:
	return has_frame(state, player, "Battery Assembler") and iron_ingot(state, player) and basic_widget(state, player) and power(state, player)

def capacitor_widget(state, player) -> bool:
	return has_frame(state, player, "Capacitor Bank") and spinning_widget(state, player) and battery(state, player)

def copper_ingot(state, player) -> bool:
	return has_frame(state, player, "Copper Forge") and copper_ore(state, player)

def plastic(state, player) -> bool:
	return has_frame(state, player, "Plastic Extractor") and oil(state, player)

def circuit_board(state, player) -> bool:
	return has_frame(state, player, "Circuit Fab") and copper_ingot(state, player) and plastic(state, player)

def computational_widget(state, player) -> bool:
	return has_frame(state, player, "Computational Engine") and circuit_board(state, player) and capacitor_widget(state, player) and spinning_widget(state, player)

def bottled_lightning(state, player) -> bool:
	return has_frame(state, player, "Tesla Coil") and glass(state, player) and power(state, player)

def thinking_core(state, player) -> bool:
	return has_frame(state, player, "Core Foundry") and capacitor_widget(state, player) and computational_widget(state, player)

def integrated_widget(state, player) -> bool:
	return has_frame(state, player, "Integrator") and bottled_lightning(state, player) and capacitor_widget(state, player) and thinking_core(state, player)

def silicon(state, player) -> bool:
	return has_frame(state, player, "Silicon Extruder") and sand(state, player) and power(state, player)

def microprocessors(state, player) -> bool:
	return has_frame(state, player, "Processor Lab") and silicon(state, player) and circuit_board(state, player) and thinking_core(state, player)

def mainframe_widget(state, player) -> bool:
	return has_frame(state, player, "Mainframe Assembler") and microprocessors(state, player) and integrated_widget(state, player)

def uranium(state, player) -> bool:
	return has_frame(state, player, "Uranium Mine") and power(state, player)

def fuel_rod(state, player) -> bool:
	return has_frame(state, player, "Fuel Rod Assembler") and iron_ingot(state, player) and uranium(state, player) and power(state, player) and gyroscope(state, player)

def cloud_widget(state, player) -> bool:
	return has_frame(state, player, "Cloud Digitizer") and mainframe_widget(state, player) and power(state, player)

def widget_particle(state, player) -> bool:
	return has_frame(state, player, "Widget Minitizers") and basic_widget(state, player) and power(state, player)

def nanoprocessor(state, player) -> bool:
	return has_frame(state, player, "Nanoscale Lab") and microprocessors(state, player) and widget_particle(state, player)

def portable_reactor(state, player) -> bool:
	return has_frame(state, player, "Reactor Foundry") and fuel_rod(state, player) and battery(state, player)

def quantum_widget(state, player) -> bool:
	return has_frame(state, player, "Quantum Tunneler") and nanoprocessor(state, player) and portable_reactor(state, player) and cloud_widget(state, player)

def helium(state, player) -> bool:
	return has_frame(state, player, "Helium Extractor") and power(state, player)

def superconductor(state, player) -> bool:
	return has_frame(state, player, "Conductor Foundry") and helium(state, player) and nanoprocessor(state, player) and iron_ingot(state, player)

def ai_core(state, player) -> bool:
	return has_frame(state, player, "AI Laboratory") and superconductor(state, player) and silicon(state, player) and thinking_core(state, player)

def unshackled_widget(state, player) -> bool:
	return has_frame(state, player, "AI Delimiter") and ai_core(state, player) and quantum_widget(state, player)

def ai_training_data(state, player) -> bool:
	return has_frame(state, player, "Training Center") and unshackled_widget(state, player)

def ascension_matrix(state, player) -> bool:
	return has_frame(state, player, "Data Transformer") and ai_training_data(state, player) and superconductor(state, player) and gyroscope(state, player)

def ascended_widget(state, player) -> bool:
	return has_frame(state, player, "Ascension Facility") and ascension_matrix(state, player) and nanoprocessor(state, player) and unshackled_widget(state, player)

def sentience_core(state, player) -> bool:
	return has_frame(state, player, "Sentience Facility") and ai_core(state, player) and ai_training_data(state, player) and power(state, player)

def picoprocessor(state, player) -> bool:
	return has_frame(state, player, "Picoscale Lab") and superconductor(state, player) and nanoprocessor(state, player) and ai_training_data(state, player)

def sentient_widget(state, player) -> bool:
	return has_frame(state, player, "Sentience Aggregator") and sentience_core(state, player) and picoprocessor(state, player) and ascended_widget(state, player)

def processor_amalgamation(state, player) -> bool:
	return has_frame(state, player, "Omega Processor Lab") and microprocessors(state, player) and circuit_board(state, player) and nanoprocessor(state, player) and picoprocessor(state, player)

def core_amalgamation(state, player) -> bool:
	return has_frame(state, player, "Omega Core Foundry") and thinking_core(state, player) and ai_core(state, player) and sentience_core(state, player)

def widget_amalgamation(state, player) -> bool:
	return has_frame(state, player, "Omega Widget Distiller") and basic_widget(state, player) and spinning_widget(state, player) and capacitor_widget(state, player) and computational_widget(state, player) and integrated_widget(state, player) and mainframe_widget(state, player) and cloud_widget(state, player) and quantum_widget(state, player) and unshackled_widget(state, player) and ascended_widget(state, player) and sentient_widget(state, player)

def omega_project_casing(state, player) -> bool:
	return has_frame(state, player, "Omega Casing Factory") and iron_ingot(state, player) and copper_ingot(state, player) and superconductor(state, player) and sentient_widget(state, player)

def omega_project_shielding(state, player) -> bool:
	return has_frame(state, player, "Omega Shielding Plant") and plastic(state, player) and bottled_lightning(state, player) and portable_reactor(state, player) and sentient_widget(state, player)

def omega_widget(state, player) -> bool:
	return has_frame(state, player, "Omega Project Assembler") and widget_amalgamation(state, player) and core_amalgamation(state, player) and processor_amalgamation(state, player) and omega_project_casing(state, player) and omega_project_shielding(state, player)

def rocket_electronics(state, player) -> bool:
	return has_frame(state, player, "Rocket Electronics Lab") and processor_amalgamation(state, player) and core_amalgamation(state, player)

def rocket_fuel(state, player) -> bool:
	return has_frame(state, player, "Rocket Fuel Distiller") and oil(state, player) and fuel_rod(state, player) and power(state, player)

def rocket_hull(state, player) -> bool:
	return has_frame(state, player, "Rocket Part Assembler") and omega_project_casing(state, player) and omega_project_shielding(state, player)

def rocket_segment(state, player) -> bool:
	return has_frame(state, player, "Omega Launch Facility") and omega_widget(state, player) and rocket_hull(state, player) and rocket_electronics(state, player) and rocket_fuel(state, player)