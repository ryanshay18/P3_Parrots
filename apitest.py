import requests

url = "https://universities-and-colleges.p.rapidapi.com/universities-by-id"

querystring = {"id": "<REQUIRED>"}

headers = {
    'x-rapidapi-key': "7a79b8a230mshff68040a0bd2bf0p1174f8jsnf85b178f3369",
    'x-rapidapi-host': "universities-and-colleges.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

