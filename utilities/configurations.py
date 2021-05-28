import configparser
import os


# This method will return the path of the given file
def get_path(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    return file_path


# This method will parse properties file
def get_config():
    config = configparser.ConfigParser()
    config.read(get_path("properties.ini"))
    return config



