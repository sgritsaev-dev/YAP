import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

results = cur.execute('''
SELECT ice_cream.title,
       wrappers.title
FROM ice_cream
JOIN wrappers ON wrappers.id = ice_cream.wrapper_id
WHERE wrappers.title LIKE '%праздн%';
''')

for result in results:
    print(result)

con.close()