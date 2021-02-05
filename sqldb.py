import sqlite3

conn = sqlite3.connect('schools.db')

crs = conn.cursor()

crs.execute('''create table schools (
                 name text, 
                 region_id integer, 
                 state text)''')

crs.execute("insert into schools values('my school', 11, 'CA')")


conn.commit()
conn.close()


print(conn)