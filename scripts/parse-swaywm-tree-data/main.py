import os
from loader import load_idle_events, load_swaymsg_events


def main():
    home = os.getenv("HOME")
    base_dir = os.path.join(home, ".data", "swaywm")

    idle_dir = os.path.join(base_dir, "idle")
    idle_df = load_idle_events(idle_dir)
    print(idle_df)

    swaymsg_dir = os.path.join(base_dir, "events")
    msg_df = load_swaymsg_events(swaymsg_dir)
    print(msg_df)


if __name__ == "__main__":
    main()
