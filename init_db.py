import sqlite3


def init_db():
    """
     init_db database initialization
     """
    connection = sqlite3.connect('./database/contacts.db')

    with open('migrations/schema.sql') as file:
        connection.executescript(file.read())
    connection.commit()

    cursor = connection.execute('SELECT COUNT(*) FROM migrations;')

    count = cursor.fetchone()[0]
    if int(count) == 0:
        with open('migrations/001.sql') as file:
            connection.executescript(file.read())
        connection.commit()
        # Внесли в базу информацию о том, что миграция 001 была исполнена,
        # чтобы информация в базе данных не дублировалась при старте
        connection.execute('INSERT INTO migrations (seq) VALUES (?)',
                           ('001',))
        connection.commit()
    connection.close()
