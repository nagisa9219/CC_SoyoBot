import logging
import os
import datetime

if not os.path.exists(f"{os.getcwd()}/src/logs"):
    os.mkdir(f"{os.getcwd()}/src/logs")

logger = logging.getLogger("soyo_bot")
logger.setLevel(logging.DEBUG)

handler_base_filename = f"{os.getcwd()}/src/logs/" + "{:%Y-%m-%d}".format(datetime.datetime.now())
handler_file_path = f"{handler_base_filename}.log"
counter = 1
while os.path.exists(handler_file_path):
    handler_file_path = f"{handler_base_filename}-{counter}.log"
    counter += 1

file_handler = logging.FileHandler(filename=handler_file_path, encoding="utf-8", mode="w")
console_handler = logging.StreamHandler()

handler_format = logging.Formatter("[%(name)s] [%(asctime)s] [%(levelname)s] %(message)s")
file_handler.setFormatter(handler_format)
console_handler.setFormatter(handler_format)

logger.addHandler(file_handler)
logger.addHandler(console_handler)