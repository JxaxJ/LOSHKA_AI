import sqlite3


db = sqlite3.connect('DATA/data.db')
sql = db.cursor()

sql.execute(f'''CREATE TABLE IF NOT EXISTS generate_data(
    lenght INT,
    train_epoch INT,
    theme TEXT
    )''')
db.commit()


def creating_colums(lenght, epoch, theme):
    sql.execute(f'INSERT INTO generate_data VALUES ({lenght}, {epoch}, "{theme}")')
    db.commit()


def save_data(lenght, epoch, theme):
    sql.execute(f"SELECT lenght, train_epoch, theme FROM generate_data")
    execute = sql.fetchall()

    if not execute:
        creating_colums(lenght, epoch, theme)

    else:
        sql.execute(f'UPDATE generate_data SET lenght = {lenght}')
        sql.execute(f'UPDATE generate_data SET train_epoch = {epoch}')
        sql.execute(f'UPDATE generate_data SET theme = "{theme}"')
        db.commit()


def get_lenght():
    try:
        sql.execute("SELECT lenght FROM generate_data")
        lenght = sql.fetchall()[0][0]
        return lenght

    except IndexError:
        creating_colums(100, 3, 'light')


def get_train_epoch():
    try:
        sql.execute("SELECT train_epoch FROM generate_data")
        train_epoch = sql.fetchall()[0][0]
        return train_epoch

    except IndexError:
        creating_colums(100, 3, 'light')


def set_theme():
    try:
        sql.execute('SELECT theme FROM generate_data')
        theme = sql.fetchall()[0][0]
        return theme

    except IndexError:
        creating_colums(100, 3, 'light')