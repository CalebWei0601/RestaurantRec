from sentence_transformers import SentenceTransformer, util
import torch
import json
import pickle as pk
from model_class import model
import gzip

# We use the SBERT algorithm to embed each review into a vector space, and for each user query, return the closest embedding
# from the corpus.  For more information, check sbert.net

# Load list of reviews
with open('RestaurantRec/data/reviews.json') as res_data:
    file_contents = res_data.read()

restaurants = json.loads(file_contents)

# Merge all comments into a single list for processing
merged_reviews = []

# Keep track of which reviews belong to which restaurant
restaurant_mapping = {}

for restaurant, reviews in restaurants.items():
    merged_reviews.extend(reviews)
    restaurant_mapping.update({review: restaurant for review in reviews})

# Load list of places to retrive names of restaurants
with open('RestaurantRec/data/restaurants_indiv_info.json') as res_data:
    file_contents = res_data.read()

info = json.loads(file_contents)
print(type(info))
places = {id: info[id]['result']['name'] for id in info if 'result' in info[id]}

# Initialize model
SBERT_mod = model(SentenceTransformer('multi-qa-MiniLM-L6-cos-v1'), merged_reviews, restaurant_mapping, places)

with gzip.open('RestaurantRec/SBERT/model.pkl', 'wb') as file:
    pk.dump(SBERT_mod, file)

