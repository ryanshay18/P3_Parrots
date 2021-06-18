import requests
import json

from quiz import questions

"""
Entertainment API
 Implementation - 
    Can query entertainment things
"""

url = "https://ivaee-internet-video-archive-entertainment-v1.p.rapidapi.com/entertainment/search/"

querystring = {
    # "ProgramTypes": "Season",
    #            "Providers": "Netflix",
    #            "Genres": "Drama",
    "OfferTypes": "Free"
}
# Providers: "Netflix", "Hulu", "AmazonPrimeVideo", "HBO", "iTunes"
# Genres: "Horror", "Comedy", "Action", "Drama", "Romance"
# OfferTypes: "Buy", "Rent", "Subscription", "Free"
# ProgramTypes: "Movie", "Show", "Season", "Episode", "Game"


               # "OriginatingNetworks": "Netflix",
               # "Tags": "movie",
               # "AvailabilityCountries": "US",
               # "ReleaseCountries": "US",
               # "PersonNames": "Anne Hathaway",
               # "Take": "1"}

headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88",
    'x-rapidapi-host': "ivaee-internet-video-archive-entertainment-v1.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

# "0": "Genres"

def query_movies(answers):
  print('querying movies now')
  answers_json = json.loads(answers)
  print(answers_json)
  query = {}

  for i in range(len(questions)):
    answer_index = answers_json[str(i)]
    print(answer_index)
    field = questions[i].field
    answer = questions[i].find_answer(int(answer_index))
    print(field + ' = ' + answer.text)
    query[field] = answer.text

  print(query)

  response = requests.request("GET", url, headers=headers, params=query)

  response_json = json.loads(response.text)

  print(response_json['Hits'])

  result = response_json['Hits']

  return result
