msg = """create table if not exists todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT)"""


import sqlite3
def make_table():
    connection = sqlite3.connect("äll_tods.db") 
    cursor = connection.cursor()
    cursor.execute(msg)
    connection.commit()
    connection.close()



def insert_data(new_todo):
    connection = sqlite3.connect("äll_tods.db") 
    cursor = connection.cursor()
    cursor.execute("insert into todo (task) values (?)",(new_todo,)  )
    connection.commit()
    connection.close()


def collect_all_todos():
    connection = sqlite3.connect("äll_tods.db") 
    cursor = connection.cursor()
    data = cursor.execute("select * from todo")
    print(data.fetchall())
    connection.commit()
    connection.close()
    return data 




