import os
import json
import polars as pl


def load_swaymsg_events(
    swaymsg_dir: str,
) -> pl.DataFrame:
    files = os.listdir(swaymsg_dir)
    events = []
    for file in files:
        full_path = os.path.join(swaymsg_dir, file)
        with open(full_path) as f:
            lines = f.readlines()
        for line in lines:
            try:
                event = json.loads(line)
            except:
                continue
            events.append(event)

    app_ids = []
    timestamps = []
    containers = []
    for event in events:
        if "container" not in event:
            print("event does not contain container", event)
            continue
        container = event["container"]

        if "app_id" not in container:
            print("container does not contain app id", event)
            continue
        app = container["app_id"]
        timestamp = event["timestamp"]

        containers.append(container)
        app_ids.append(app)
        timestamps.append(timestamp)

    events_dicts = {
        "app_id": app_ids,
        "timestamp": timestamps,
        "container": containers,
    }
    df = pl.from_dict(events_dicts)

    return df


def load_idle_events(
    idle_dir: str,
) -> pl.DataFrame:
    files = os.listdir(idle_dir)
    events = []
    for file in files:
        full_path = os.path.join(idle_dir, file)
        with open(full_path) as f:
            lines = f.readlines()
        for line in lines:
            try:
                event = json.loads(line)
            except:
                continue
            events.append(event)

    types = []
    timestamps = []
    for event in events:
        if "type" not in event:
            print("event does not contain type", event)
            continue
        _type = event["type"]

        if "timestamp" not in event:
            print("event does not contain timestamp", event)
            continue
        timestamp = event["timestamp"]

        types.append(_type)
        timestamps.append(timestamp)

    events_dicts = {
        "type": types,
        "timestamp": timestamps,
    }
    df = pl.from_dict(events_dicts)

    return df
