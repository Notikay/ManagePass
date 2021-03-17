import os
import eel

from configparser import ConfigParser
from connect import createTable, insertData


@eel.expose
def getData(data):
    insertData(data)
    print(data)

def convert(tuple_):
    return tuple(int(i) for i in tuple_.split(","))

def main():
    config = ConfigParser()
    config.read("config.ini")

    db_file = config.get("DataBase", "filename")
    mode = config.get("Window", "mode")
    size = convert(config.get("Window", "size"))
    pos = convert(config.get("Window", "position"))

    if not os.path.exists(db_file):
        createTable()

    eel.init('web')
    eel.start('main.html',
              mode=mode,
              geometry={
                  'size': size,
                  'position': pos}
              )


if __name__ == "__main__":
    main()