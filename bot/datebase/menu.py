import sqlite3

def SelectTable(dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM done_homework;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def selectFromNames(name,dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM done_homework WHERE name=?;"
        cursor.execute(sqlite_selection_query,(name,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по именам студентов.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")






def addNewHomework(record: list,dbpath):
    print()
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        insert_query = '''INSERT INTO done_homework (name,photo)
                          VALUES (?,?);'''
        cursor.executemany(insert_query,(record,))
        print('Домашнее задание добавлено')
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось записать информацию", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    print()









