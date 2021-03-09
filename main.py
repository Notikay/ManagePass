# TODO: Написать скрипт сохранения данных из полей в БД
import eel


def main():
    eel.init("web")
    eel.start("main.html", size=(375, 675))


if __name__ == '__main__':
    main()