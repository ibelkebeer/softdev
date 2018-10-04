import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitates db ops

command = "DROP TABLE peeps;"
c.execute(command)
command = "DROP TABLE courses;"
c.execute(command)
command = "DROP TABLE occupations;"
c.execute(command)


#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

data = []
individual_rows = []

with open('data/peeps.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		individual_rows.append(row['name'])
		individual_rows.append(row['age'])
		individual_rows.append(row['id'])
		data.append(individual_rows)
		individual_rows = []

command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGERY PRIMARY KEY)"    #build SQL stmt, save as string
c.execute(command)    #run SQL statement
c.executemany('INSERT INTO peeps VALUES (?, ?, ?)', data)

data = []
individual_rows = []

with open('data/courses.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		individual_rows.append(row['code'])
		individual_rows.append(row['mark'])
		individual_rows.append(row['id'])
		data.append(individual_rows)
		individual_rows = []

command = "CREATE TABLE courses (name TEXT, mark INTEGER, id INTEGERY)"          #build SQL stmt, save as string
c.execute(command)    #run SQL statement
c.executemany('INSERT INTO courses VALUES (?, ?, ?)', data)

data = []
individual_rows = []

with open('data/occupations.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		individual_rows.append(row['Job Class'])
		individual_rows.append(row['Percentage'])
		data.append(individual_rows)
		individual_rows = []

command = "CREATE TABLE occupations (name TEXT, percent INTEGER)"          #build SQL stmt, save as string
c.execute(command)    #run SQL statement
c.executemany('INSERT INTO occupations VALUES (?, ?)', data)
#==========================================================

c.execute("SELECT * FROM occupations")
rows = c.fetchall()
for row in rows:
    print(row)

db.commit() #save changes
db.close()  #close database
