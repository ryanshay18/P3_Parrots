import sqlite3
import json

import movies

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
  minimum_iva_rating = str(movies['movies.minimum_iva_rating']) if movies['movies.minimum_iva_rating'] else 'null'
  program_types = str(movies['movies.program_types']) if movies['movies.program_types'] else 'null'
  genres = str(movies['genres']) if movies['genres'] else 'null'
  providers = str(movies['movies.providers']) if movies['movies.budget'] else 'null'
  budget = str(movies['movies.budget']) if movies['movies.budget'] else 'null'
  status = str(movies['movies.status']) if movies['movies.status'] else 'null'
  season_id = '"' + movies['movies.season_id'] + '"' if movies['school.season_id'] else 'null'
  people_id = str(movies['movies.people_id']) if movies['movies.people_id'] else 'null'
  release_types = str(movies['movies.release_types']) if movies['movies.release_types'] else 'null'
  originating_networks = str(movies['movies.originating_networks']) if movies['movies.originating_networks'] else 'null'
  year_range_start = str(movies['movies.year_range_start']) if movies['movies.year_range_start'] else 'null'
  certifications = str(movies['movies.certifications']) if movies['movies.certifications'] else 'null'
  availability_countries = str(movies['movies.availability countries']) if movies['movies.availability countries'] else 'null'
  title = str(movies['movies.title']) if movies['movies.title'] else 'null'

query = 'insert into movies values(' + \
          '"' + movies['title'] + '", ' + \
          '"' + movies['movies.providers'] + '", ' + \
          '"' + movies['movies.genres'] + ")"
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
