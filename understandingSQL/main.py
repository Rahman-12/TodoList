msg = """create table if not exists todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT)"""


import sqlite3
connection = sqlite3.connect("äll_tods.db") 
cursor = connection.cursor()
cursor.execute(msg)
cursor.execute("insert into todo (task) values (?)",("sleep early",)  )
data = cursor.execute("select * from todo")
print(data.fetchall())
connection.commit()
connection.close()




