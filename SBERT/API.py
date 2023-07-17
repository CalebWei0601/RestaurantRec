import pickle as pk
import gzip
from sentence_transformers import util

with gzip.open('RestaurantRec/SBERT/model.pkl', 'rb') as file:
    Recommender = pk.load(file)
