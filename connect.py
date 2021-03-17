# TODO: Добавить запись логов

import sqlite3

from sqlite3 import Error
from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")


def createConnection():
    connection = None
    db_file = config.get("DataBase", "filename")

    try:
        connection = sqlite3.connect(db_file)
        print("Подключение к БД SQLite прошло успешно!")
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    return connection

def executeQuery(connection, query, value=()):
    cursor = connection.cursor()
    try:
        cursor.execute(query, value)
        connection.commit()
        print("Запрос успешно выполнен!")
    except Error as e:
        print(f"Произошла ошибка '{e}'")

def createTable():
    connection = createConnection()
    table = config.get("DataBase", "table")
    return executeQuery(connection, table)

def insertData(data):
    connection = createConnection()

    if data['info'] == "": data['info'] = None

    account = config.get("DataBase", "account")
    values = (
        data['name'], data['url'],
        data['login'], data['password'],
        data['info']
    )

    executeQuery(connection, account, values)