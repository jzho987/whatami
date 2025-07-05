import json
import polars as pl
import os


def process_swaymsg_events(event):
    if "container" not in event:
        print("event does not contain container", event)
        return None

    container = event["container"]
    if "app_id" not in container:
        print("container does not contain app id", event)
        return None

    app = container["app_id"]
    timestamp = event["timestamp"]

    return app, timestamp


def process_idle_events(event):
    if "type" not in event:
        print("event does not contain type", event)
        return None

    if "timestamp" not in event:
        print("event does not contain timestamp", event)
        return None

    etype = event["type"]
    timestamp = event["timestamp"]

    return etype, timestamp


def main():
    home = os.getenv("HOME")
    data_dir = os.path.join(home, ".data", "swaywm")
    files = os.listdir(data_dir)

    events = []
    for file in files:
        full_path = os.path.join(data_dir, file)
        with open(full_path) as f:
            for line in f.readlines():
                try:
                    e = json.loads(line)
                except:
                    continue
                events.append(e)

    events_dict = {
        "app": [],
        "action": [],
        "time": [],
    }
    for event in events:
        app, timestamp, etype = None, None, None
        if "change" in event and event["change"] != "focus":
            app, timestamp = process_swaymsg_events(event)
            etype = "focus"
        elif "type" in event:
            etype, timestamp = process_swaymsg_events(event)
        else:
            continue

        events_dict["app"].append(app)
        events_dict["action"].append(etype)
        events_dict["time"].append(timestamp)

    events_df = pl.from_dict(events_dict)
    print(events_df)


if __name__ == "__main__":
    main()
