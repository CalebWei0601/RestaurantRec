import json
import requests
import time
# This script searches each restaurant obtained from places_api.py individually
# to obtain the reviews that will later be used for modelling and predictions

# Load restaurants from Google Places API
with open('RestaurantRec/data/restaurants.json') as res_data:
    file_contents = res_data.read()

places = json.loads(file_contents)
places = [place for place in places if 'plus_code' in place and 'Singapore' in place['plus_code']['compound_code']]

results = {}
# Your API key here
API_KEY = 'YOUR API KEY'
BASE_URL = 'https://maps.googleapis.com/maps/api/place/details/json'

search_flag = False

params = {
    'key': API_KEY
}

if search_flag:
    for place in places:

        # Make specific place search request
        place_id = place['place_id']
        params['place_id'] = place_id

        response = requests.get(BASE_URL, params=params)

        # Store in json
        data = response.json()
        results[place_id] = data
        time.sleep(0.3)

    with open('RestaurantRec/data/restaurants_indiv_info.json', 'w') as file:
        json.dump(results, file)

