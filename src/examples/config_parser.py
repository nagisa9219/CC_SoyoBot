import configparser
import os

current_path = os.path.join(os.path.dirname(__file__))
config_path = os.path.abspath(current_path+os.path.sep+"../.."+os.path.sep+"config/config.ini")
config = configparser.ConfigParser()
config.read(config_path)

def main():
    config["Credentials"]["Token"]
    