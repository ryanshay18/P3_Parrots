import requests

url = "https://university-college-list-and-rankings.p.rapidapi.com/api/top-universities/us"

headers = {
    'x-rapidapi-key': "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88",
    'x-rapidapi-host': "university-college-list-and-rankings.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
