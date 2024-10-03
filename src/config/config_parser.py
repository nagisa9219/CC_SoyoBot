import os, json

def config_load() -> dict:
    with open(f"{os.getcwd()}/src/config/config.json") as rconfig:
        config = json.load(rconfig)
    return config