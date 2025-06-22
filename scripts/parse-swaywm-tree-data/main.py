import json
import polars as pl
import os


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
        "time": [],
    }
    for event in events:
        if event["change"] != "focus":
            continue

        if "container" not in event:
            print("event does not contain container", event)

        container = event["container"]
        if "app_id" not in container:
            print("container does not contain app id", event)
            continue

        events_dict["app"].append(container["app_id"])
        events_dict["time"].append(event["timestamp"])

    events_df = pl.from_dict(events_dict)
    print(events_df)


if __name__ == "__main__":
    main()
