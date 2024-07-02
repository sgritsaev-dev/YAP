import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS toppings(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream_toppings(    
id INTEGER NOT NULL,
ice_cream INTEGER NOT NULL,
topping INTEGER NOT NULL,
id PRIMARY KEY,
FOREIGN KEY(ice_cream) REFERENCES ice_cream(id),
FOREIGN KEY(topping) REFERENCES toppings(id));
''')

con.close()