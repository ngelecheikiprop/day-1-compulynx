'using config parser module in python'

import configparser
config = configparser.ConfigParser()
config.read("config.ini")
print((config.get("Database", "host")))