import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY,
title TEXT,
description TEXT,
wrapper_id INTEGER,
FOREIGN KEY(wrapper_id) REFERENCES wrappers(id));

CREATE TABLE IF NOT EXISTS wrappers(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL);
''')
con.close()

import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

results = cur.execute('''
SELECT ice_cream.title,
       wrappers.title
FROM ice_cream,
     wrappers
WHERE wrappers.title LIKE 'Б%'
    AND 
    ice_cream.wrapper_id = wrappers.id;
''')

for result in results:
    print(result)

con.close()
