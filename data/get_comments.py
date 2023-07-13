import json
import re
# This file extracts the cleaned reviews for each restaurant before further analysis and modelling, wiwth place_id as keys
with open('RestaurantRec/data/restaurants_indiv_info.json') as res_data:
    file_contents = res_data.read()

restaurants = json.loads(file_contents)

restaurants = [restaurants[res]['result'] for res in restaurants if 'result' in restaurants[res]]

reviews = {}

for res in restaurants:
    if 'reviews' in res:
        for review in res['reviews']:
                # we only take reviews that came with more than a 3 star rating as we don't want negative reviews
                if review['text'] != '' and review['rating'] >= 3:
                    # Strip newline characters
                    stripped_text = review['text'].replace('\n', '')
                    # This step removes all mandarin unicode characters from the comments
                    strencode = stripped_text.encode('ascii', 'ignore')
                    strdecode = strencode.decode()
                    # add to dictionary where key is the restaurant
                    reviews[res['place_id']] = reviews.get(res['place_id'], []) + [strdecode]

# Save to json file
with open('RestaurantRec/data/reviews.json', 'w') as file:
        json.dump(reviews, file)
