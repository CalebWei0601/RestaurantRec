from sentence_transformers import SentenceTransformer, util
import torch
import json

# We use the SBERT algorithm to embed each review into a vector space, and for each user query, return the closest embedding
# from the corpus.  For more information, check sbert.net
with open('data/reviews.json') as res_data:
    file_contents = res_data.read()

restaurants = json.loads(file_contents)

# Merge all comments into a single list for processing
merged_reviews = []
# Keep track of which reviews belong to which restaurant
restaurant_mapping = {}

for restaurant, reviews in restaurants.items():
    merged_reviews.extend(reviews)
    restaurant_mapping.update({review: restaurant for review in reviews})

# Initialize model
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

# Embed the corpus
corpus_embeddings = model.encode(merged_reviews, convert_to_tensor=True)