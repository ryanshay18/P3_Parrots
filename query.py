import sqlite3

# https://collegescorecard.ed.gov/data/documentation/

conn = sqlite3.connect('schools.db')

# crs = conn.cursor()

# def construct_query(region, locale)

for row in conn.execute("select name, city, state, url, locale, carnegie_basic from schools where city = 'Denver' and carnegie_basic = 11"):
  print(row)

