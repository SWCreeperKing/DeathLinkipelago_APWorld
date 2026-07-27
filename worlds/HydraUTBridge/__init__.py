import json

from NetUtils import NetworkItem
from worlds.LauncherComponents import Component, components, Type

def run_tracker():
    try:
        import logging
        from worlds.tracker.TrackerCore import TrackerCore
        from worlds.AutoWorld import AutoWorldRegister
        from worlds.tracker import DeferredEntranceMode
        item_cache = {}
        
        def make_network_item(item_id) -> NetworkItem:
            if item_id in item_cache:
                return item_cache[item_id]
            item = NetworkItem(item_id, -1, -1, 0)
            item_cache[item_id] = item
            return item

        print("READY")

        print("slot_name")
        slot_name = input()

        print("game")
        game = input()

        logger = logging.getLogger("Client")
        tracker_core = TrackerCore(logger, False, False)
        tracker_core.enforce_deferred_connections = DeferredEntranceMode.disabled

        tracker_core.run_generator(None, None)

        print("slot_data")
        slot_data = json.loads(input())

        connected_cls = AutoWorldRegister.world_types.get(game)
        tracker_core.set_slot_params(game, 1, slot_name, 1)
        tracker_core.initalize_tracker_core(connected_cls, slot_data)

        print("missing_locations")
        tracker_core.set_missing_locations(set(parse_ids(input())))

        print("start")
        while True:
            nxt = input()
            if nxt == "stop": return

            if nxt.startswith("next_items "):
                command_raw = nxt.replace("next_items ", "").split('|')
                current = parse_ids(command_raw[0])
                next_items = parse_ids(command_raw[1])

                tracker_core.set_items_received([make_network_item(item) for item in current])
                current_count = len(tracker_core.updateTracker().in_logic_locations)

                item_counts = ""
                for item in next_items:
                    tracker_core.set_items_received([make_network_item(item) for item in [*current, item]])
                    count = len(tracker_core.updateTracker().in_logic_locations) - current_count
                    if count <= 0: continue

                    item_counts += f"{item}={count} "

                print(f"counts {item_counts}")
                continue

            split = nxt.split('|')
            tracker_core.set_items_received([make_network_item(item) for item in parse_ids(split[1])])

            print(f"Circle {split[0]}|{[tracker_core.get_current_world().location_name_to_id[loc_name] for loc_name in
                                        tracker_core.updateTracker().in_logic_locations]}")
    except Exception as err:
        print(f"ERROR: {err}")


def parse_ids(locs: str):
    if locs == "": return [];
    return [int(item.strip()) for item in locs.split(',')]


components.append(Component("HydraUTBridge", None, func=run_tracker, component_type=Type.CLIENT))
