import sqlite3
import csv
DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) 
c = db.cursor()
command = "DROP TABLE tpot;"
c.execute(command)
command = "CREATE TABLE tpot (name TEXT, userid INTEGER);"
c.execute(command)
command = 'INSERT INTO tpot VALUES ("Bob", 1)'
c.execute(command)
command = "SELECT * FROM tpot;"
output = c.execute(command)
print(output)
db.commit()
db.close()
