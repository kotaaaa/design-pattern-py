import configparser


class Database:
    def __init__(self):
        pass

    def get_proprties(dbname):
        prop = configparser.ConfigParser()
        filename = dbname + ".txt"
        try:
            prop.read(filename)
        except Exception:
            print("Warning: " + filename + " is not found.")
        return prop
