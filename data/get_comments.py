import json
# This file extracts the reviews for each restaurant before further analysis and modelling, wiwth place_id as keys
with open('data/restaurants_indiv_info.json') as res_data:
    file_contents = res_data.read()

restaurants = json.loads(file_contents)
restaurants = [res['result'] for res in restaurants]

reviews = {}

for res in restaurants:
    if 'reviews' in res:
        for review in res['reviews']:
                if review['text'] != '' and review['rating'] >= 3:
                    reviews[res['place_id']] = reviews.get(res['place_id'], []) + [(review['text'])]

# Save to json file
with open('data/reviews.json', 'w') as file:
        json.dump(reviews, file)
