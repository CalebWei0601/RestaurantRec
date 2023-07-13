import pickle as pk
import gzip

query = 'We are looking for some good sushi, preferably served on belts'

with gzip.open('RestaurantRec/SBERT/model.pkl', 'rb') as file:
    Recommender = pk.load(file)

prediction = Recommender.predict(query)
print(prediction)