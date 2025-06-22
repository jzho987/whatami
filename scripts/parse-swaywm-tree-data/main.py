import json


def main():
    with open("./data/data.json") as f:
        json.load(f.read())


if __name__ == "__main__":
    main()
