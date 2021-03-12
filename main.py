# TODO: Создать config-файл

import eel
from connect import createTable, insertData


def main():
    @eel.expose
    def getData(data):
        insertData("db.sqlite", data)
        print(data)

    eel.init('web')
    eel.start('main.html',
              mode='chrome',
              geometry={'size': (375, 675), 'position': (300, 50)}
              )


if __name__ == "__main__":
    main() if createTable("db.sqlite") else exit()