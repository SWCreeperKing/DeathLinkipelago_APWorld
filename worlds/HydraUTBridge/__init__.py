import json

from NetUtils import NetworkItem
from worlds.LauncherComponents import Component, components, Type
from worlds.powerwashsimulator import raw_location_dict


def run_tracker():
    try:
        import logging
        from worlds.tracker.TrackerCore import TrackerCore
        from worlds.AutoWorld import AutoWorldRegister
        from worlds.tracker import DeferredEntranceMode
        from BaseClasses import LocationProgressType
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
        tracker_core.run_generator(None, None)

        print("slot_data")
        slot_data = json.loads(input())

        connected_cls = AutoWorldRegister.world_types.get(game)
        tracker_core.set_slot_params(game, 1, slot_name, 1)
        tracker_core.initalize_tracker_core(connected_cls, slot_data)

        print("missing_locations")
        tracker_core.set_missing_locations(set(parse_ids(input())))

        deferred_callback = getattr(tracker_core.get_current_world(), "reconnect_found_entrances", None)

        if hasattr(tracker_core.get_current_world(), "found_entrances_datastorage_key"):
            data_keys = getattr(tracker_core.get_current_world(), "found_entrances_datastorage_key", None)
            print(f"sending_data_store_keys {json.dumps(data_keys)}")

        print("start")
        while True:
            nxt = input()
            if nxt == "stop": return

            if nxt.startswith("entrance "):
                entrances_got = json.loads(nxt.replace("entrance ", "", 1))
                for entrance_got in entrances_got:
                    entrance_got = entrance_got.replace("{player}", slot_name, 1)
                    deferred_callback(entrance_got, True)
                continue

            if nxt.startswith("next_items "):
                command_raw = nxt.replace("next_items ", "", 1).split('|')
                current = parse_ids(command_raw[0])
                next_items = parse_ids(command_raw[1])

                tracker_core.set_items_received([make_network_item(item) for item in current])
                current_count = len(tracker_core.updateTracker().in_logic_locations)

                item_counts = {}
                for item in next_items:
                    tracker_core.set_items_received([make_network_item(item) for item in [*current, item]])
                    count = len(tracker_core.updateTracker().in_logic_locations) - current_count
                    if count <= 0: continue

                    item_counts[item] = count

                print(f"counts {json.dumps(item_counts)}")
                continue

            split = nxt.split('|')
            tracker_core.set_items_received([make_network_item(item) for item in parse_ids(split[1])])

            world = tracker_core.get_current_world()

            def build_location(loc_name):
                loc_obj = world.get_location(loc_name)
                return {
                    "id": world.location_name_to_id[loc_name],
                    "is_excluded": loc_obj.progress_type == LocationProgressType.EXCLUDED
                }

            state = tracker_core.updateTracker()
            current_circle = {
                "circle": split[0],
                "location_list": [build_location(loc_name) for loc_name in state.in_logic_locations],
                "glitched_list": [world.location_name_to_id[loc_name] for loc_name in state.in_logic_locations],
                "entrances": [entrance.name for entrance in state.unconnected_entrances],
            }

            print(f"Circle {json.dumps(current_circle)}")
    except Exception as err:
        print(f"ERROR: {err}")


def parse_ids(locs: str):
    if locs == "": return [];
    return [int(item.strip()) for item in locs.split(',')]


components.append(Component("HydraUTBridge", None, func=run_tracker, component_type=Type.CLIENT))
