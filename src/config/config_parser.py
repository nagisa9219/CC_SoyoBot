import os
import json
from src.logger import logger

config_path = os.getcwd()
config_default = {
    "credentials": {
        "token": ""
    },
    "permissions": {
        "owner_id": "auto"
    },
    "cogs": {
        "enabled_cogs": [
            "vc_logging",
            "random_pick"
        ]
    }
}

def config_create(src_path: str) -> int:
    if os.path.isfile(f"{src_path}/config/config.json"):
        logger.error("Action aborted because config.json exists.")
        return 0
    else:
        with open(f"{src_path}/config/config.json", "w", encoding="utf-8") as config:
            json.dump(config_default, config, ensure_ascii=False)
        logger.info("Created config.json.")
        return 1

def config_load(src_path: str) -> dict:
    with open(f"{src_path}/config/config.json") as rconfig:
        config = json.load(rconfig)
    return config