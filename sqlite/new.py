import sqlite3


con = sqlite3.connect("db_video.sqlite")

cur = con.cursor()

query = '''
SELECT title,
       release_year
FROM video_products;
'''

print(*cur.execute(query))
con.commit()
con.close()
