import sqlite3
import json

conn = sqlite3.connect('movies.db')

crs = conn.cursor()

# school.name,school.city,school.state,school.zip,school.carnegie_size_setting,school.school_url,school.carnegie_basic,school.locale,school.region_id,school.ownership,school.carnegie_undergrad
crs.execute('''create table movies (
                 minimum_iva_rating text,
                 program_types text,
                 genres text,
                 providers text,
                 budget text,
                 status text,
                 season_id text,
                 people_id text,
                 release_types text
                 originating_networks text,
                 year_range_start text,
                 year_range_end text,
                 certifications text,
                 availability countries text,
                 title text,
                 includes text)''')

def insert_movies(movies):
  minimum_iva_rating = str(movies['movies.minimum_iva_rating]) if movies['movies.minimum_iva_rating']')
  program_types = str(movies['movies.program_types']) if movies['movies.program_types']')'
  carnegie_basic = str(school['school.carnegie_basic']) if school['school.carnegie_basic'] else 'null'
  carnegie_undergrad = str(school['school.carnegie_undergrad']) if school['school.carnegie_undergrad'] else 'null'
  ownership = str(school['school.ownership']) if school['school.ownership'] else 'null'
  url = '"' + school['school.school_url'] + '"' if school['school.school_url'] else 'null'
  query = 'insert into schools values(' + \
          '"' + school['school.name'] + '", ' + \
          '"' + school['school.city'] + '", ' + \
          '"' + school['school.state'] + '", ' + \
          url + ', ' + \
          str(school['school.region_id']) + ', ' + \
          locale + ', ' + \
          carnegie_size_setting + ', ' + \
          carnegie_basic + ', ' + \
          carnegie_undergrad + ', ' + \
          ownership + ")"
  print(query)
  crs.execute(query)


def process_file(file_name):
  with open(file_name) as f:
    data = json.load(f)
  for school in data['results']:
    insert_movies(movies)


for file in range(68):
  print('Reading file #' + str(file))
  file_name = 'schools/school-' + str(file) + '.json'
  process_file(file_name)

conn.commit()
conn.close()
