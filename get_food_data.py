import requests
import json
import sys
import argparse
from food_cache import FoodCache
from urls import (
    get_autocomplete_url,
    get_fooddata_url,
    FOODDATA_BASE_URL
)

def get_food_data(search_term):
    """
    Searches for a food term using the MyFoodData API, retrieves the food data for the first search result,
    and caches the result for future use.

    Args:
        search_term: The food item to search for.

    Returns:
        A dictionary containing the food data if successful, or None if an error occurs or no results are found.
    """
    cache = FoodCache()
    autocomplete_url = get_autocomplete_url(search_term)
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'dnt': '1',
        'origin': 'https://tools.myfooddata.com',
        'priority': 'u=1, i',
        'referer': 'https://tools.myfooddata.com/',
        'sec-ch-ua': '"Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    try:
        # Request autocomplete suggestions for the search term
        print(f"Requesting autocomplete for: {autocomplete_url}")
        autocomplete_response = requests.get(autocomplete_url, headers=headers)
        autocomplete_response.raise_for_status()  # Raise an exception for bad status codes

        response_data = autocomplete_response.json()
        print(f"Autocomplete suggestions: {json.dumps(response_data, indent=2)}")

        # Check if any hits were found
        if not response_data.get('hits'):
            print(f"No hits found in response for '{search_term}'.")
            return None

        # Extract the food ID from the first hit
        first_hit = response_data['hits'][0]
        if not first_hit.get('document'):
            print(f"No document found in first hit for '{search_term}'.")
            return None

        food_id = str(first_hit['document']['fdc_id'])
        print(f"Found food ID: {food_id}")

        # Check if the food data is already cached
        cached_data = cache.get_cached_data(food_id)
        if cached_data:
            return cached_data

        # Construct the URL to request food data
        fooddata_url = get_fooddata_url(food_id)
        print(f"Requesting food data from: {fooddata_url}")
        
        # Request food data
        fooddata_response = requests.get(fooddata_url, headers=headers)
        print(f"Response status code: {fooddata_response.status_code}")
        
        fooddata_response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the JSON response
        food_data = fooddata_response.json()
        # If the response is a list, take the first item
        if isinstance(food_data, list) and len(food_data) > 0:
            food_data = food_data[0]
        
        # Save the food data to the cache
        cache.save_to_cache(food_id, food_data)
        
        return food_data

    except requests.exceptions.RequestException as e:
        # Handle any errors during the request
        print(f"Error during request: {e}")
        return None
    except json.JSONDecodeError as e:
        # Handle errors in decoding the JSON response
        print(f"Error decoding JSON response: {e}")
        return None
    except KeyError as e:
        # Handle errors in accessing expected keys in the response data
        print(f"Error accessing response data: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Get nutritional data for a food item')
    parser.add_argument('food', help='The food item to search for')
    parser.add_argument('--raw', action='store_true', 
                       help='Print raw JSON output without formatting')
    
    args = parser.parse_args()
    
    food_data = get_food_data(args.food)

    if food_data:
        if args.raw:
            print(json.dumps(food_data))
        else:
            print("\nFood Data:")
            print(json.dumps(food_data, indent=2))
    else:
        print("Could not retrieve food data.")
        sys.exit(1)

if __name__ == "__main__":
    main()