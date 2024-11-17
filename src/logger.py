import logging
import os
import datetime

# Set default log file folder
logs_path = os.getcwd() + "/logs"

print(logs_path)

# Create logs folder if directory not exist
if not os.path.exists(logs_path):
    os.mkdir(logs_path)

# Logger settings
logger = logging.getLogger("soyo_bot")
logger.setLevel(logging.DEBUG)

handler_base_filename = logs_path + "/{:%Y-%m-%d}".format(datetime.datetime.now())
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