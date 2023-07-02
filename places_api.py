
import requests
import time
import json

# This file uses the Google places API to perform grid search to get a list of restaurants in Singapore
API_KEY = 'YOUR API KEY'
BASE_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# Singapore coordinates for grid search
lat_min = 1.22
lat_max = 1.47
lng_min = 103.60
lng_max = 104.03

# Keep track of and skip duplicate restaurants in grid search
visited = set()

# Define the search parameters
params = {
    'radius': 10000,  # Example search radius in meters
    'type': 'restaurant',  # Example search type
    'key': API_KEY
}

# Store all the results
results = []  

#Flag for whether to perform the grid search or not
search_flag = False

if search_flag:
    for lat in range(int(lat_min * 100), int(lat_max * 100), 3):
        for lng in range(int(lng_min * 100), int(lng_max * 100), 3):
            # Time lag to be nice to Google API
            time.sleep(2)

            # Set the location coordinates
            location = f"{lat/100:.5f},{lng/100:.5f}"
            params['location'] = location

            # This step is important because of the API documentation.  If the 
            # page token parameter is present, the API automatically ignores
            # all other parameters which means our grid search freezes and
            # Keeps performing the same search over and over again.
            if 'pagetoken' in params:
                params.pop('pagetoken')

            # Make the API request
            response = requests.get(BASE_URL, params=params)
            data = response.json()
            
            # Retrieve the results from the current page, skipping duplicates
            if 'results' in data:
                for result in data['results']:
                    place_id = result['place_id']
                    if place_id not in visited:
                        results.append(result)
                        visited.add(place_id)
            
            # Take care of next pages in each request
            while 'next_page_token' in data:
                # Set the next_page_token for the next iteration
                next_page_token = data['next_page_token']
                
                # Introduce a delay before making the next request
                time.sleep(2) 
                
                # Update the params dictionary with the next_page_token
                params['pagetoken'] = next_page_token
                response = requests.get(BASE_URL, params=params)
                data = response.json()
                
                # Retrieve the results from the current page
                if 'results' in data:
                    for result in data['results']:
                        place_id = result['place_id']
                        if place_id not in visited:
                            results.append(result)
                            visited.add(place_id)

    # filter out Malaysian restaurants
    results = [result for result in results if 'plus_code' in result and 'Singapore' in result['plus_code']['compound_code']]
    
    # save results to a json file
    with open('restaurants.json', 'w') as file:
        json.dump(results, file)