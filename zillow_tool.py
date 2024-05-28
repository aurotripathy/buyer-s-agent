from crewai_tools import BaseTool
import requests

class ZillowTool(BaseTool):
    name: str = "zillowtool"
    description: str = "Given the name of a city it gets the houses for sale."

    def _run(self, city: str) -> list:
        
        url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

        # querystring = {"location":"milpitas, ca","status_type":"ForSale","home_type":"Houses","daysOn":"1","soldInLast":"1"}
        querystring = {"location":city, "status_type":"ForSale","home_type":"Houses",}

        headers = {
            "x-rapidapi-key": "3d7570d0cdmsh1b768c6b3451450p18beaejsn02d747f4dcf4",
            "x-rapidapi-host": "zillow-com1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        json_response = response.json()
        properties = json_response['props']
        price_address_list = []
        for property in properties:
            print(f"{property['price']}, {property['address']}")
            price_address_list.append((property['price'], property['address']))

        return price_address_list
