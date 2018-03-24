"""
Instructions
If you don't already have it, install the SQLite Browser from http://sqlitebrowser.org/.

Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Emmanuel', 37);
INSERT INTO Ages (name, age) VALUES ('Hugh', 17);
INSERT INTO Ages (name, age) VALUES ('Ossian', 16);
INSERT INTO Ages (name, age) VALUES ('Hajirah', 33);
INSERT INTO Ages (name, age) VALUES ('Ellisa', 15);
INSERT INTO Ages (name, age) VALUES ('Sanaa', 18);
Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X
Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.
Note: This assignment must be done using SQLite - in particular, the SELECT query above will not work in any other database. So you cannot use MySQL or Oracle for this assignment.



"""


import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
   ('Emmanuel', 37))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Hugh', 17))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
   ('Ossian', 16))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
   ('Hajirah', 33))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
('Ellisa', 15))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
('Sanaa', 18))


conn.commit()


cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for row in cur:
    print(row)



conn.close()