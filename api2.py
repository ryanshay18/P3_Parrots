import requests

url = "https://universities-and-colleges.p.rapidapi.com/universities"

querystring = {"page":"5","includeUniversityDetails":"false","countryCode":"US","limit":"50"}

headers = {
    'x-rapidapi-key': "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88",
    'x-rapidapi-host': "universities-and-colleges.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)