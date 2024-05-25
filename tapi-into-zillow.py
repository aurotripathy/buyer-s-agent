"""
Tap into zillow with rapidapi
"""
import requests

url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

# querystring = {"location":"milpitas, ca","status_type":"ForSale","home_type":"Houses","daysOn":"1","soldInLast":"1"}
querystring = {"location":"milpitas, ca","status_type":"ForSale","home_type":"Houses",}

headers = {
	"x-rapidapi-key": "3d7570d0cdmsh1b768c6b3451450p18beaejsn02d747f4dcf4",
	"x-rapidapi-host": "zillow-com1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
json_response = response.json()
properties = json_response['props']
for property in properties:
    print(f"{property['price']}, {property['address']}")
print(f'full response:\n {response.json()}')

