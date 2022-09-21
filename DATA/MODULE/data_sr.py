import sqlite3

db = sqlite3.connect('../data.db')
sql = db.cursor()

sql.execute(f'''CREATE TABLE IF NOT EXISTS generate_data(
    lenght BIGINT
    )''')
db.commit()


def save_lenght(new_lenght):
    sql.execute(f"SELECT lenght FROM generate_data")
    data = sql.fetchall()

    if not data:
        sql.execute(f'INSERT INTO generate_data VALUES ({new_lenght})')
        db.commit()

    else:
        sql.execute(f'UPDATE generate_data SET lenght = {new_lenght}')
        db.commit()


def get_lenght():
    sql.execute("SELECT lenght FROM generate_data")
    try:
        data = sql.fetchall()[0][0]
        return data

    except IndexError:
        save_lenght(100)
        return 100