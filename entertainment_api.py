import requests

"""
Entertainment API
 Implementation - 
    Can query entertainment things
"""

url = "https://ivaee-internet-video-archive-entertainment-v1.p.rapidapi.com/entertainment/search/"

querystring = {"ProgramTypes": "Movie",
               "OriginatingNetworks": "Netflix",
               "Tags": "movie",
               "AvailabilityCountries": "US",
               "ReleaseCountries": "US",
               "PersonNames": "Anne Hathaway",
               "Take": "1"}

headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88",
    'x-rapidapi-host': "ivaee-internet-video-archive-entertainment-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
