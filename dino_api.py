# import requests

import requests

url = "https://alexnormand-dino-ipsum.p.rapidapi.com/"

querystring = {"format":"html","words":"30","paragraphs":"30"}

headers = {
    'x-rapidapi-key': "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88",
    'x-rapidapi-host': "alexnormand-dino-ipsum.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


""" try 2
import http.client

conn = http.client.HTTPSConnection("alexnormand-dino-ipsum.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88",
    'X=RapidAPI-Host': "alexnormand-dino-ipsum.p.rapidapi.com"
}

conn.request("GET","/?format=text&words=30&paragraphs=1", headers=headers)

response = conn.getresponse()
data = response.read()

print(data)

"""

""" try 1
words = 30
paragraphs = 1
formats = 'text'

response = requests.get(f"https://alexnormand-dino-ipsum.p.rapidapi.com/?"
                        f"format={formats}&words={words}&paragraphs={paragraphs}", headers={
    "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
    "X-RapidAPI-Key": "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88"})

print(response.text)
"""