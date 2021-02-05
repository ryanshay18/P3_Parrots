import sqlite3

# https://collegescorecard.ed.gov/data/documentation/

conn = sqlite3.connect('schools.db')

# crs = conn.cursor()

# def construct_query(region, locale)

for row in conn.execute("select name, city, state, url, locale, carnegie_basic from schools where city = 'San Diego' and carnegie_basic = 30"):
  print(row)

