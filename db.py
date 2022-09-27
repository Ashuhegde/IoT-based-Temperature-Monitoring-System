import sqlite3
conn = sqlite3.connect('data.db')
conn.execute("CREATE TABLE sensors(id INTEGER PRIMARY KEY AUTOINCREMENT,temp TEXT,humi TEXT)")
conn.execute("INSERT INTO sensors(temp,humi) VALUES(25,48)")
conn.commit()