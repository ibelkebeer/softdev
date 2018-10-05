#
#
#
#

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#=======================================================================

command = "DROP TABLE peeps_avg"
c.execute(command)
command = "CREATE TABLE peeps_avg (name TEXT, id INTEGER PRIMARY KEY, average INTEGER)"
c.execute(command)

data = []
individual_data = []

command = "SELECT peeps.name, peeps.id FROM peeps, courses WHERE peeps.id = courses.id"
c.execute(command)

for peep in c.fetchall():
    command = "SELECT courses.mark FROM courses WHERE courses.id = "+str(peep[1])
    c.execute(command)
    sum = 0
    num = 0
    for mark in c.fetchall():
        sum += mark[0]
        num += 1
    print(sum)
    print(num)
    sum /= num
    peep[2] = sum
    
c.executemany("INSERT INTO peeps_avg VALUES (?, ?, ?)", (c.fetchall()))


db.commit()
db.close()
