import requests

url = "https://university-college-list-and-rankings.p.rapidapi.com/api/top-universities/us"

headers = {
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "university-college-list-and-rankings.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)