import http.client

conn = http.client.HTTPSConnection("university-college-list-and-rankings.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88",
    'x-rapidapi-host': "university-college-list-and-rankings.p.rapidapi.com"
}

conn.request("GET", "/api/top-universities/europe", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))