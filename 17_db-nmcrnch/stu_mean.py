#
#
#
#

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
db.text_factory = str         #change data from fethall() from unicode to utf

#=======================================================================

command = "DROP TABLE peeps_avg"
c.execute(command)
command = "CREATE TABLE peeps_avg (name TEXT, id INTEGER, average INTEGER)"
c.execute(command)

data = []

command = "SELECT peeps.name, peeps.id FROM peeps"
c.execute(command)

for peep in c.fetchall():
    individual_data = []
    command = "SELECT courses.mark FROM courses WHERE courses.id = " + str(peep[1])
    c.execute(command)
    sum = 0
    num = 0
    for mark in c.fetchall():
        sum += mark[0]
        num += 1
    sum /= num
    individual_data.append(peep[0])
    individual_data.append(peep[1])
    individual_data.append(sum)
    data.append(individual_data)

c.executemany("INSERT INTO peeps_avg VALUES (?, ?, ?)", data)

command = "SELECT * FROM peeps_avg"
c.execute(command)
print(c.fetchall())

db.commit()
db.close()
