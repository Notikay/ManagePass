# TODO: Заменить текстовый файл на БД
# TODO: Переименовать функцию принятия данных

import eel


def main():

    @eel.expose
    def data(name, url, login, password, info):
        data_str = f"Имя: {name}; Ссылка: {url}; Логин: {login}; " \
                   f"Пароль: {password}; Доп. информация: {info}.\n"

        with open("db.txt", "a") as file:
            file.write(data_str)
        print(data_str)

    eel.init('web')
    eel.start('main.html',
              mode='chrome',
              geometry={'size': (375, 675), 'position': (300, 50)}
    )


if __name__ == "__main__":
    main()