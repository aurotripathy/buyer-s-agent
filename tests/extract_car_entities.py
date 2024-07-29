import json
from car_entities import CarEntity
from pudb import set_trace
import random


def pick_random_element(elements):
    """
    Picks a random element from a list.
    
    Parameters:
    elements (list): A list of elements to pick from.
    
    Returns:
    element: A randomly chosen element from the list.
    """
    if not elements:
        raise ValueError("The list is empty. Please provide a list with at least one element.")
    return random.choice(elements)

# Example usage:
elements = ['apple', 'banana', 'cherry', 'date']
random_element = pick_random_element(elements)
print(f'Randomly selected element: {random_element}')


def read_and_process_json(file_path):
    results = []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)  # Load the JSON data from the file
            
            for item in data:  # Iterate through each item in the JSON array
                # Concatenate the list of strings in 'description' into a single string
                title = item['title']
                description = ' '.join(item['description'])
                price = item['price']  # Extract the price
                results.append((title, description, price))
                
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file content.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return results

if __name__ == "__main__":
    # file_path = input("Enter the path to the JSON file: ")
    file_path = '../data/craigslist_car.json'
    car_sale_listings = []
    car_entity = CarEntity()

    items = read_and_process_json(file_path)
    
    # set_trace()
    # if items is not None:
    #     count = 0
    #     for title, description, price in items:
    #         sale_listing = f"Title: {title}\n  Description: {description}\n  Price: {price}"
    #         print(sale_listing)
    #         entities = car_entity.get_car_entities(sale_listing)
    #         for entity in entities:
    #             print(f'label: {entity.label}, value: {entity.name}')
    #         print(f'------------------')
    #         count = count + 1
    #         if count == 2:
    #             break

    if items is not None:
        count = 5
        for i in range(count):
            title, description, price = pick_random_element(items)
            sale_listing = f"Title: {title}\n  Description: {description}\n  Price: {price}"
            print(sale_listing)
            entities = car_entity.get_car_entities(sale_listing)
            for entity in entities:
                print(f'label: {entity.label}, value: {entity.name}')
            print(f'------------------')



    print(f'Total number of item: {len(items)}')

