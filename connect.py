# TODO: Добавить запись логов
# TODO: Изменить на один аргумент-кортеж в insertData()

import sqlite3
from sqlite3 import Error


def createConnection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Подключение к SQLite БД прошло успешно!")
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    return connection

def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Запрос успешно выполнен!")
        return True
    except Error as e:
        print(f"Произошла ошибка '{e}'")
        return False

def createTable(path):
    connection = createConnection(path)
    table = """
        CREATE TABLE IF NOT EXISTS account_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            url TEXT NOT NULL,
            login TEXT NOT NULL,
            password TEXT NOT NULL,
            info TEXT
        );
    """
    return executeQuery(connection, table)

def insertData(path, name, url, login, password, info):
    connection = createConnection(path)
    account = f"""
        INSERT INTO
            account_data (name, url, login, password, info)
        VALUES
            ('{name}', '{url}', '{login}', '{password}', '{info}');
    """
    executeQuery(connection, account)