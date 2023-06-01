import sqlite3

con = sqlite3.connect("chinook.db")

c = con.cursor()

artists = c.execute("SELECT name FROM artists")

for row in artists:
    print(row)

con.commit()

con.close()
