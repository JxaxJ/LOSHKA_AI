import sqlite3
import os

print(os.listdir())
db = sqlite3.connect('DATA/data.db')
sql = db.cursor()

sql.execute(f'''CREATE TABLE IF NOT EXISTS generate_data(
    lenght INT,
    train_epoch INT
    )''')
db.commit()


def creating_colums(lenght, epoch):
    sql.execute(f'INSERT INTO generate_data VALUES ({lenght}, {epoch})')
    db.commit()


def save_data(lenght, epoch):
    sql.execute(f"SELECT lenght, train_epoch FROM generate_data")
    execute = sql.fetchall()

    if not execute:
        creating_colums(lenght, epoch)

    else:
        sql.execute(f'UPDATE generate_data SET lenght = {lenght}')
        sql.execute(f'UPDATE generate_data SET train_epoch = {epoch}')
        db.commit()
        print('update')


def get_lenght():
    try:
        sql.execute("SELECT lenght FROM generate_data")
        data = sql.fetchall()[0][0]
        print('Вызов get_lenght')
        return data

    except IndexError:
        creating_colums(200, 3)

def get_train_epoch():
    try:
        sql.execute("SELECT train_epoch FROM generate_data")
        data = sql.fetchall()[0][0]
        print(data)
        print('Вызов get_train_epoch')
        return data

    except IndexError:
        creating_colums(200, 3)

get_lenght()
