# TODO: Добавить запись логов
# TODO: Создать config-файл
# TODO: Изменить на один аргумент-кортеж в getData()

import eel
from connect import createTable, insertData

def main():

    @eel.expose
    def getData(name, url, login, password, info):
        insertData("db.sqlite", name, url, login, password, info)

        data_str = f"Имя: {name}; Ссылка: {url}; Логин: {login}; " \
                   f"Пароль: {password}; Доп. информация: {info}.\n"
        print(data_str)

    eel.init('web')
    eel.start('main.html',
              mode='chrome',
              geometry={'size': (375, 675), 'position': (300, 50)}
    )


if __name__ == "__main__":
    main() if createTable("db.sqlite") else exit()